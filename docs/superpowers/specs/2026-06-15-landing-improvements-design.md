# Hum&Net Landing Page — Mejoras v2 (Capa de confianza)

**Fecha:** 2026-06-15
**Enfoque aprobado:** B — Capa de confianza
**Objetivo:** Captar leads + convencer a visitantes nuevos con señales claras de profesionalismo y confianza.

---

## Resumen de cambios

| Tipo | Secciones |
|------|-----------|
| Mejora | Stats, Servicios, Hôlos ERP, Form |
| Nueva | Clientes que confían, ¿Por qué Hum&Net? |
| Sin cambios | Hero (copy menor), Nav, Footer |

---

## Nueva estructura de página

```
1. Nav
2. Hero               (sin cambios estructurales; subtítulo más específico)
3. Stats              (+ íconos SVG con colores de marca)
4. Clientes que confían  ← NUEVA
5. Servicios          (tarjeta destacada + íconos en todas)
6. Hôlos ERP          (badge cloud-native + features concretas)
7. ¿Por qué Hum&Net?  ← NUEVA
8. Contacto / CTA     (form mailto: funcional)
9. Footer             (sin cambios)
```

---

## Sección por sección

### 1. Stats (mejora)

Añadir un ícono SVG outline sobre cada número animado. Los íconos usan los colores de marca rotando: magenta `#E91E63`, cyan `#00BCD4`, naranja `#FF9800`.

| Stat | Ícono | Color |
|------|-------|-------|
| 30+ Años de experiencia | Reloj (`clock`) | `#E91E63` |
| 200+ Empresas atendidas | Edificio (`building-2`: rect con ventanas) | `#00BCD4` |
| 500+ Proyectos entregados | Pulso (`activity`) | `#FF9800` |
| 98% Satisfacción | Estrella (`star`) | `#E91E63` |

Implementación: íconos SVG inline en el HTML (no dependencia externa). Tamaño 28×28px, `stroke-width: 1.5`, `fill: none`.

---

### 2. Clientes que confían (NUEVA)

**Posición:** Entre Stats y Servicios.

**Diseño:** Marquee infinito horizontal con loop continuo CSS (`animation: marquee`). Los logos desfilan de derecha a izquierda. Velocidad: ~30s por ciclo completo.

**Tratamiento de logos:**
- Por defecto: `filter: grayscale(1) opacity(0.6)`
- En hover: `filter: none`, transición 300ms
- Fondo de sección: oscuro consistente con el dark theme

**Estructura HTML:**
```html
<section class="clientes" id="clientes">
  <div class="section-head">
    <div class="eyebrow">Empresas que confían en nosotros</div>
    <h2>Más de 200 organizaciones ya transformaron su operación</h2>
  </div>
  <div class="marquee-track">
    <div class="marquee-inner">
      <!-- logos duplicados para loop continuo -->
      <img src="assets/img/clientes/logo-1.png" alt="Cliente 1">
      ...
      <!-- duplicado -->
      <img src="assets/img/clientes/logo-1.png" alt="Cliente 1">
      ...
    </div>
  </div>
</section>
```

**Assets:** Los logos reales del cliente se colocan en `assets/img/clientes/`. Mientras no estén disponibles, se usan placeholders con el nombre de la empresa en texto.

---

### 3. Servicios (mejora)

**Layout nuevo:** 2 filas.
- Fila 1: Una tarjeta ancha (`grid-column: 1 / -1`) para "Soluciones Empresariales" con gradiente `#E91E63→#00BCD4` en el borde/fondo, eyebrow "PRODUCTO ESTRELLA", ícono monitor SVG en magenta.
- Fila 2: 3 tarjetas iguales para Infraestructura, Innovación y Sinergia, cada una con su ícono SVG en color de acento.

**Íconos por tarjeta:**

| Servicio | Ícono | Color |
|----------|-------|-------|
| Soluciones Empresariales | `monitor` | `#E91E63` |
| Infraestructura y TI | `server` | `#00BCD4` |
| Innovación y Desarrollo | `code` | `#FF9800` |
| Sinergia | `users` | `#E91E63` |

---

### 4. Hôlos ERP (mejora)

**Badge pill** arriba del título:
```
☁ Cloud-native · Sin infraestructura adicional
```
Estilo: `background: rgba(0,188,212,0.12); color: #00BCD4; border: 1px solid rgba(0,188,212,0.3); border-radius: 20px; padding: 4px 14px; font-size: 13px`

**Features reescritas** (más concretas y verificables):

| Antes | Después |
|-------|---------|
| Personalizable y flexible para tu industria | Configurable por módulos: finanzas, inventarios, RRHH y ventas |
| Automatiza tareas repetitivas y libera a tu equipo | Automatización de aprobaciones, reportes y alertas en tiempo real |
| Escalable conforme crece tu empresa | Escala de 5 a 500+ usuarios sin cambiar de sistema |
| 100% en la nube, sin infraestructura adicional | 100% en la nube — sin servidores, sin mantenimiento |
| Integración nativa con CONTPAQi® | Integración certificada con toda la suite CONTPAQi® |

---

### 5. ¿Por qué Hum&Net? (NUEVA)

**Posición:** Entre Hôlos ERP y Contacto.

**Layout:** 4 tarjetas iguales en fila (misma grid que Servicios v1). Cada tarjeta: ícono SVG grande (32px) centrado arriba, título en `#F1F5F9`, descripción corta en `#64748B`.

**Contenido de los 4 diferenciadores:**

| # | Título | Descripción | Ícono | Color |
|---|--------|-------------|-------|-------|
| 1 | 30+ años transformando organizaciones | Décadas de experiencia comprobada en empresas mexicanas de todos los sectores. | `award` (trofeo/medalla) | `#E91E63` |
| 2 | Partner Platinum CONTPAQi® | El nivel de certificación más alto — solo los mejores distribuidores en México lo tienen. | `star` (estrella rellena) | `#FF9800` |
| 3 | Socios, no solo proveedores | Implementamos, capacitamos y acompañamos a tu equipo en el largo plazo. | `users` (dos siluetas) | `#00BCD4` |
| 4 | Tecnología + desarrollo humano | Única firma en México que integra ERP con desarrollo organizacional en una sola propuesta. | `zap` (rayo) | `#E91E63` |

**Eyebrow:** "Por qué elegirnos"
**Título de sección:** "La diferencia que transforma organizaciones."

---

### 6. Form de contacto (mejora)

**Comportamiento actual:** `onsubmit="return false;"` — no hace nada.

**Comportamiento nuevo:** Al hacer submit, abrir cliente de correo con campos pre-llenados:

```javascript
form.addEventListener('submit', function(e) {
  e.preventDefault();
  const name = form.querySelector('[aria-label="Nombre"]').value.trim();
  const email = form.querySelector('[aria-label="Correo electrónico"]').value.trim();
  const subject = encodeURIComponent(`Demo request — ${name}`);
  const body = encodeURIComponent(`Nombre: ${name}\nEmail: ${email}\n\nMe interesa agendar una demo de Hôlos ERP / CONTPAQi®.`);
  window.location.href = `mailto:ventas@humandnet.com?subject=${subject}&body=${body}`;
});
```

El botón de WhatsApp directo ya existe en la sección y permanece sin cambios.

---

## Assets necesarios

- `assets/img/clientes/` — directorio nuevo con logos PNG/SVG de clientes (provistos por el cliente; placeholders hasta entonces)
- Todos los íconos SVG se implementan inline en el HTML (no se requiere librería de íconos)

## Fuera de alcance (este spec)

- Integración con Hôlos ERP para leads/soporte → spec separado
- Testimonios de clientes con quotes → requiere contenido real
- FAQ section
- CTA flotante persistente
- Páginas adicionales de humandnet.com
