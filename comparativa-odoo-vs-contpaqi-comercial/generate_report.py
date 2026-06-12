#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolida los JSON de results/ en un report.md comparativo.
Estructura JSON: plana (campos al top level) con array `uncertain`.
Omite valores con [uncertain], los campos listados en `uncertain`, y vacios.
"""
import json
import re
import glob
import os
import yaml

BASE = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE, "results")
FIELDS_PATH = os.path.join(BASE, "fields.yaml")
OUTLINE_PATH = os.path.join(BASE, "outline.yaml")
REPORT_PATH = os.path.join(BASE, "report.md")

# Campos seleccionados por el usuario para el indice (TOC)
TOC_FIELDS = ["license_price", "license_model", "edition_required_for_mx_localization"]

# Etiquetas legibles para categorias
CATEGORY_LABELS = {
    "informacion_basica": "Información básica",
    "costo_tco": "Costo / TCO",
    "despliegue": "Despliegue",
    "funcionalidad_comercial": "Funcionalidad comercial",
    "cumplimiento_fiscal_mx": "Cumplimiento fiscal MX",
    "contabilidad": "Contabilidad",
    "escalabilidad_modulos": "Escalabilidad / módulos",
    "soporte_ecosistema": "Soporte y ecosistema",
    "integraciones": "Integraciones",
    "estrategico": "Estratégico",
    "usabilidad": "Usabilidad",
}

# Etiquetas en espanol para los nombres de campo
FIELD_LABELS = {
    "developer": "Desarrollador",
    "country_of_origin": "País de origen",
    "current_version": "Versión actual",
    "license_model": "Modelo de licencia",
    "license_price": "Precio de licencia",
    "licensing_scheme": "Esquema de licenciamiento",
    "implementation_cost": "Costo de implementación",
    "included_users": "Usuarios incluidos",
    "additional_user_and_rfc_cost": "Costo por usuario/RFC adicional",
    "maintenance_renewal_cost": "Costo de mantenimiento/renovación",
    "hidden_costs": "Costos ocultos",
    "tco_1_3_years": "TCO a 1-3 años",
    "hosting": "Despliegue / hosting",
    "hardware_requirements": "Requisitos de hardware",
    "operating_system": "Sistema operativo",
    "mobile_app_availability": "App móvil",
    "sales": "Ventas",
    "purchasing": "Compras",
    "inventory_warehouses": "Inventarios / almacenes",
    "point_of_sale": "Punto de venta",
    "crm": "CRM",
    "price_lists": "Listas de precios",
    "document_bulk_load": "Carga masiva de documentos",
    "xml_volume_multibranch_capacity": "Capacidad volumen XML / multisucursal",
    "cfdi_40": "CFDI 4.0",
    "edition_required_for_mx_localization": "Edición requerida para localización MX",
    "timbrado_stamping": "Timbrado",
    "complementos": "Complementos",
    "addendas": "Addendas",
    "pac_provider_flexibility": "Flexibilidad de PAC",
    "sat_connection": "Conexión SAT",
    "accounting_integration": "Integración contable",
    "accounting_handoff_to_contpaqi_contabilidad": "Hand-off a CONTPAQi Contabilidad",
    "available_modules": "Módulos disponibles",
    "extensibility": "Extensibilidad",
    "sdk_api_integration_tier_gating": "SDK / API (gating por tier)",
    "app_marketplace": "Marketplace de apps",
    "technical_support": "Soporte técnico",
    "partner_network": "Red de partners",
    "community": "Comunidad",
    "documentation": "Documentación",
    "market_share_installed_base_mx": "Cuota de mercado / base instalada MX",
    "api": "API",
    "ecommerce": "E-commerce",
    "third_party_connectors": "Conectores de terceros",
    "vendor_lock_in_data_portability": "Lock-in / portabilidad de datos",
    "mexico_market_maturity": "Madurez en el mercado MX",
    "learning_curve": "Curva de aprendizaje",
    "interface": "Interfaz",
}


def label(key):
    return FIELD_LABELS.get(key, prettify(key))


# Campos para el cuadro comparativo rapido
QUICK_FIELDS = [
    ("license_model", "Modelo de licencia"),
    ("license_price", "Precio"),
    ("hosting", "Despliegue"),
    ("edition_required_for_mx_localization", "Localizacion MX oficial"),
    ("sdk_api_integration_tier_gating", "SDK / API"),
    ("accounting_handoff_to_contpaqi_contabilidad", "Hand-off a CONTPAQi Contab."),
    ("vendor_lock_in_data_portability", "Lock-in / portabilidad"),
]

INTERNAL_KEYS = {"_source_file", "uncertain", "id", "item_id", "name", "item_name", "category"}

# Fallback: nombre de archivo -> id del outline (para JSON sin id/item_id)
FILENAME_TO_ID = {
    "Odoo_Community_Edition.json": "odoo_community",
    "CONTPAQi_Comercial_Start.json": "contpaqi_comercial_start",
    "CONTPAQi_Comercial_Pro.json": "contpaqi_comercial_pro",
    "CONTPAQi_Comercial_Premium.json": "contpaqi_comercial_premium",
    "Holos_ERP_HumNet.json": "holos_erp",
}


def flatten(d):
    """Aplana estructura plana o anidada por categoria a un dict campo->valor."""
    flat = {}
    for k, v in d.items():
        if k in ("uncertain", "_source_file"):
            continue
        if isinstance(v, dict):
            for k2, v2 in v.items():
                flat[k2] = v2
        else:
            flat[k] = v
    return flat


def gh_anchor(text):
    """Genera un ancla estilo GitHub a partir del texto del encabezado."""
    a = text.strip().lower()
    a = a.replace(" ", "-")
    a = re.sub(r"[^\w\-]", "", a, flags=re.UNICODE)
    return a


def prettify(key):
    return key.replace("_", " ").capitalize()


def is_uncertain(value, field_name, uncertain_list):
    if value is None:
        return True
    if isinstance(value, str):
        if value.strip() == "":
            return True
        if "[uncertain]" in value.lower():
            return True
    if field_name in uncertain_list:
        return True
    return False


def fmt_value(value):
    if isinstance(value, list):
        if all(isinstance(x, dict) for x in value):
            return "<br>".join(" | ".join(f"{k}: {v}" for k, v in d.items()) for d in value)
        return ", ".join(str(x) for x in value)
    if isinstance(value, dict):
        return "; ".join(f"{k}: {v}" for k, v in value.items())
    return str(value)


def toc_short(value):
    """Acorta un valor para el indice."""
    if value is None:
        return "n/d"
    s = str(value).strip()
    if "[uncertain]" in s.lower() or s == "":
        return "n/d"
    s = re.sub(r"\s+", " ", s)
    return s[:60] + ("..." if len(s) > 60 else "")


def load_items_order():
    with open(OUTLINE_PATH, encoding="utf-8") as f:
        outline = yaml.safe_load(f)
    topic = outline.get("topic", "Comparativa")
    order = [(it["id"], it["name"]) for it in outline.get("items", [])]
    return topic, order


def load_fields():
    with open(FIELDS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    cats = []
    for cat_key, cat in data.get("categories", {}).items():
        field_names = [fld["name"] for fld in cat.get("fields", [])]
        cats.append((cat_key, field_names))
    return cats


def load_results():
    items = {}
    for path in glob.glob(os.path.join(RESULTS_DIR, "*.json")):
        fname = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        item_id = d.get("id") or d.get("item_id") or FILENAME_TO_ID.get(fname, fname)
        items[item_id] = {
            "flat": flatten(d),
            "uncertain": d.get("uncertain", []),
            "source": fname,
        }
    return items


def main():
    topic, order = load_items_order()
    cats = load_fields()
    results = load_results()

    out = []
    out.append(f"# {topic}")
    out.append("")
    out.append("> Informe generado a partir de investigación web (rango: últimos 12 meses, corte 2026-06-11).")
    out.append("> Los valores no verificables se omiten; ver sección *Campos inciertos* por producto.")
    out.append("")

    # ---- Cuadro comparativo rapido ----
    out.append("## Cuadro comparativo rapido")
    out.append("")
    header = "| Campo | " + " | ".join(name for _id, name in order if _id in results) + " |"
    sep = "|---|" + "|".join(["---"] * sum(1 for _id, _ in order if _id in results)) + "|"
    out.append(header)
    out.append(sep)
    for fkey, flabel in QUICK_FIELDS:
        row = [flabel]
        for _id, _name in order:
            if _id not in results:
                continue
            flat = results[_id]["flat"]
            unc = results[_id]["uncertain"]
            val = flat.get(fkey)
            if is_uncertain(val, fkey, unc):
                row.append("n/d")
            else:
                s = re.sub(r"\s+", " ", str(val))
                row.append(s[:90] + ("..." if len(s) > 90 else ""))
        out.append("| " + " | ".join(row) + " |")
    out.append("")

    # ---- Indice ----
    out.append("## Indice")
    out.append("")
    for i, (_id, name) in enumerate(order, 1):
        if _id not in results:
            continue
        flat = results[_id]["flat"]
        anchor = gh_anchor(f"{i}-{name}")
        extras = []
        for fkey in TOC_FIELDS:
            sval = toc_short(flat.get(fkey))
            extras.append(f"{label(fkey)}: {sval}")
        out.append(f"{i}. [{name}](#{anchor}) — " + " | ".join(extras))
    out.append("")

    # ---- Detalle por item ----
    for i, (_id, name) in enumerate(order, 1):
        if _id not in results:
            continue
        flat = results[_id]["flat"]
        unc = results[_id]["uncertain"]
        out.append("---")
        out.append("")
        out.append(f"## {i}. {name}")
        out.append("")
        dev = flat.get("developer")
        if dev and not is_uncertain(dev, "developer", unc):
            out.append(f"*{dev}*")
            out.append("")

        used = set(INTERNAL_KEYS) | {"developer"}
        for cat_key, field_names in cats:
            label = CATEGORY_LABELS.get(cat_key, prettify(cat_key))
            rows = []
            for fname in field_names:
                used.add(fname)
                val = flat.get(fname)
                if is_uncertain(val, fname, unc):
                    continue
                rows.append((label(fname), fmt_value(val)))
            if not rows:
                continue
            out.append(f"### {label}")
            out.append("")
            out.append("| Campo | Valor |")
            out.append("|---|---|")
            for k, v in rows:
                v = v.replace("\n", "<br>")
                out.append(f"| **{k}** | {v} |")
            out.append("")

        # Otros campos no definidos en fields.yaml
        extra = []
        for k, v in flat.items():
            if k in used or k in INTERNAL_KEYS:
                continue
            if is_uncertain(v, k, unc):
                continue
            extra.append((label(k), fmt_value(v)))
        if extra:
            out.append("### Otra info")
            out.append("")
            out.append("| Campo | Valor |")
            out.append("|---|---|")
            for k, v in extra:
                out.append(f"| **{k}** | {v} |")
            out.append("")

        # Campos inciertos
        if unc:
            out.append("### Campos inciertos (no verificados)")
            out.append("")
            for fname in unc:
                out.append(f"- {label(fname)}")
            out.append("")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"OK -> {REPORT_PATH}")
    print(f"Items: {sum(1 for _id,_ in order if _id in results)} | Categorias: {len(cats)}")


if __name__ == "__main__":
    main()
