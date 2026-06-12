# Comparativa Odoo Community vs CONTPAQi Comercial (Start/Pro/Premium) vs Hôlos ERP

> Informe generado automaticamente a partir de investigacion web (rango: ultimos 12 meses, corte 2026-06-11).
> Los valores no verificables se omiten; ver seccion *Campos inciertos* por producto.

## Cuadro comparativo rapido

| Campo | Odoo Community Edition | CONTPAQi Comercial Start | CONTPAQi Comercial Pro | CONTPAQi Comercial Premium | Hôlos ERP (Hum&Net) |
|---|---|---|---|---|---|
| Modelo de licencia | Open-source. The Community Edition is free software licensed under LGPL v3 (no license fee... | Proprietary, closed-source. Sold under an annual subscription (Licenciamiento Anual) that ... | Proprietary, closed-source commercial software. Sold under an annual subscription (licenci... | Proprietary, closed-source. Historically sold as a perpetual 'tradicional' license; CONTPA... | n/d |
| Precio | n/d | n/d | n/d | n/d | n/d |
| Despliegue | Primarily on-premise / self-hosted (own server or any cloud VPS/IaaS). Odoo's managed clou... | On-premise desktop application (Windows). Can be hosted on a local PC/server or accessed v... | On-premise by default (installed on Windows desktop/server, local or LAN multi-user). Can ... | On-premise (desktop/client-server) by default; can be hosted on a private/cloud Windows se... | Cloud (SaaS, 'In Cloud'). Accessed via web browser (holoserp.app). Also offers CONTPAQi Es... |
| Localizacion MX oficial | This is the central caveat. Odoo's full, officially-supported Mexican localization — notab... | Mexican fiscal localization is native and built into every CONTPAQi Comercial tier includi... | Mexican fiscal localization (CFDI 4.0, SAT compliance) is native and built into every paid... | Mexican fiscal localization is built into the product natively (it is a Mexican product); ... | n/d |
| SDK / API | No tier gating of programmatic integration. The full ORM and external APIs (XML-RPC and JS... | No SDK/programmatic integration at the Start tier. The CONTPAQi Comercial SDK is exclusive... | SDK access is GATED to Premium only. CONTPAQi Comercial Pro does NOT include the Comercial... | SDK access is gated to the Premium tier only - Start and Pro do not include the SDK. The C... | n/d |
| Hand-off a CONTPAQi Contab. | n/d | Yes - native export/integration of accounting vouchers (polizas) directly into CONTPAQi Co... | Strong native ecosystem advantage: Comercial Pro integrates directly with CONTPAQi Contabi... | Native, tight integration: a 'Contabilizar' action and the Contabilizacion/interface modul... | Native/built-in. The platform is centered on CONTPAQi Contabilidad and Tesorera (HumandNet... |
| Lock-in / portabilidad | Lowest lock-in profile in the comparison. Open-source LGPL v3 code plus a standard Postgre... | High vendor lock-in. Proprietary closed-source Windows product on annual subscription, wit... | Significant vendor lock-in: proprietary, closed format; annual subscription required to ke... | Significant vendor lock-in: proprietary closed-source product, proprietary SQL schema, CON... | n/d |

## Indice

1. [Odoo Community Edition](#1-odoo-community-edition) — License price: n/d | License model: Open-source. The Community Edition is free software licensed... | Edition required for mx localization: This is the central caveat. Odoo's full, officially-supporte...
2. [CONTPAQi Comercial Start](#2-contpaqi-comercial-start) — License price: n/d | License model: Proprietary, closed-source. Sold under an annual subscriptio... | Edition required for mx localization: Mexican fiscal localization is native and built into every C...
3. [CONTPAQi Comercial Pro](#3-contpaqi-comercial-pro) — License price: n/d | License model: Proprietary, closed-source commercial software. Sold under a... | Edition required for mx localization: Mexican fiscal localization (CFDI 4.0, SAT compliance) is na...
4. [CONTPAQi Comercial Premium](#4-contpaqi-comercial-premium) — License price: n/d | License model: Proprietary, closed-source. Historically sold as a perpetual... | Edition required for mx localization: Mexican fiscal localization is built into the product native...
5. [Hôlos ERP (Hum&Net)](#5-hôlos-erp-humnet) — License price: n/d | License model: n/d | Edition required for mx localization: n/d

---

## 1. Odoo Community Edition

*Odoo S.A.*

### Informacion basica

| Campo | Valor |
|---|---|
| **Developer** | Odoo S.A. |
| **Country of origin** | Belgium (Ramillies/Grand-Rosière). Originally founded as TinyERP/OpenERP. |
| **Current version** | Odoo 19 (released October 2025, at Odoo Experience 2025). Odoo 18 (October 2024) is also widely deployed in production. Major versions ship annually. |
| **License model** | Open-source. The Community Edition is free software licensed under LGPL v3 (no license fee, perpetual right to use, modify, and redistribute). This contrasts with Odoo Enterprise, which is proprietary and sold as an annual per-user subscription. Community has no subscription cost; the trade-off is no included vendor support and a reduced module set. |

### Costo / TCO

| Campo | Valor |
|---|---|
| **Licensing scheme** | No licensing fee and no renewal scheme for the Community Edition — it is perpetually free under LGPL v3. There is no annual-vs-perpetual distinction because there is no paid license; you may run any version indefinitely. (This is structurally different from CONTPAQi, which is migrating to an annual licensing model in 2026 separating new license vs renewal, and from Odoo Enterprise's annual subscription.) Cost recurrence in Community comes only from optional hosting, support contracts with partners, and PAC stamping fees. |
| **Included users** | Unlimited users at no license cost — there is no per-user license fee in the Community Edition. Practical user concurrency is bounded only by server/hardware sizing, not by licensing. (This differs sharply from CONTPAQi's base-user counts and per-network-user fees.) |
| **Additional user and rfc cost** | MXN $0 per additional user for the license — Community has no per-user charge and no RFC-based limits or fees. There is no concept of 'additional RFC cost' as in CONTPAQi; an Odoo database can handle multiple companies/RFCs (multi-company) without extra licensing fees, subject only to server capacity and any partner/PAC per-RFC stamping arrangements. Adding users increases hardware/hosting load but not license cost. |
| **Hidden costs** | Significant and often underestimated: (1) Hosting/infrastructure — Odoo.sh managed hosting is Enterprise-only, so Community must self-host on a VPS/server (VPS from ~USD $5-20/mo for tiny setups, much more for production-grade with backups/monitoring). (2) Custom development — features delivered via drag-and-drop Odoo Studio in Enterprise must be hand-coded in Community (cited as the single biggest cost surprise). (3) OCA/third-party module maintenance — free modules can break on annual upgrades and require patching. (4) Mexican localization — practical CFDI compliance relies on OCA/third-party modules plus a PAC subscription (per-timbre or bundle fees). (5) Training and lack of official vendor support. (6) Version upgrade projects every cycle. |

### Despliegue

| Campo | Valor |
|---|---|
| **Hosting** | Primarily on-premise / self-hosted (own server or any cloud VPS/IaaS). Odoo's managed cloud offerings — Odoo Online (SaaS) and Odoo.sh — are reserved for the Enterprise/paid editions, so Community cannot use Odoo.sh. Hybrid is possible only via self-managed cloud hosting. Effectively: self-hosted on-premise or self-hosted in a third-party cloud. |
| **Hardware requirements** | Self-hosted. Minimum ~2 vCPU and 4 GB RAM; production recommended ~4 vCPU and 8 GB+ RAM. A single VPS with 4-8 GB RAM comfortably serves up to ~25 users (Odoo + PostgreSQL on one box); beyond ~100 users the PostgreSQL database should be split onto a dedicated server. SSD storage required. |
| **Operating system** | Server runs on Linux (recommended/standard for production), Windows, and macOS; production deployments are predominantly Linux. Requires PostgreSQL (versions 12-17 supported on Odoo 18/19; PostgreSQL 16 recommended) — no other database engine is supported. Client side is fully web-browser based (cross-platform). |
| **Mobile app availability** | Yes. Web interface is fully responsive (usable on any mobile browser). Odoo also publishes native mobile apps for Android and iOS that connect to a Community server. POS can run on phones/tablets via the responsive web client and the mobile app; numerous third-party/OCA mobile POS modules also exist. Note: some advanced native mobile features and Odoo Studio are Enterprise-oriented. |

### Funcionalidad comercial

| Campo | Valor |
|---|---|
| **Sales** | Full sales management in Community: quotations, sales orders, customer management, multi-currency, taxes, and conversion of quotes to orders/invoices. Includes the Sales app and online quotation basics. Some advanced sales features (e.g., certain subscription/contract automations, advanced eSign workflows) are Enterprise-only. |
| **Purchasing** | Full purchase management in Community: purchase orders, requests for quotation (RFQ), vendor management, vendor price lists, and procurement rules (reordering). Integrates with Inventory and Accounting modules. Core procurement is complete; some automated/AI-assisted purchasing aids are Enterprise. |
| **Inventory warehouses** | Strong multi-warehouse inventory in Community: multiple warehouses and locations, internal transfers, lots/serial-number tracking, multiple units of measure, and basic routes. Advanced logistics features such as barcode-app-driven operations, advanced replenishment, and some WMS/quality automations are Enterprise-only. |
| **Point of sale** | Included in Community (Point of Sale app): touchscreen sales, sessions, cash control, and offline-capable operation. Runs in browser, on tablets, and via the mobile app. Hardware integration (receipt printers, scanners) is supported. Some advanced POS features and certain hardware/loyalty integrations lean Enterprise. |
| **Crm** | Included in Community: leads/opportunities pipeline, Kanban stages, activities, and basic lead scoring. Marketing-automation, advanced reporting dashboards, and some AI lead features are Enterprise. |
| **Price lists** | Yes. Pricelists with rules by customer, product, quantity, date ranges, and discounts; multi-currency pricing. Available in Community via the Sales/Inventory apps. |
| **Document bulk load** | Supported through standard import/export tools (CSV/XLSX import on virtually every model) and the external ORM/XML-RPC/JSON-RPC API for programmatic bulk loading. There is no per-tier crippling of bulk import as noted for CONTPAQi Premium-vs-Pro; bulk import is uniformly available in Community. The OCR-based 'Documents/Accounting AI' auto-data-capture, however, is an Enterprise feature. |

### Cumplimiento fiscal MX

| Campo | Valor |
|---|---|
| **Cfdi 40** | Technically supported. The base Mexican EDI modules (l10n_mx, l10n_mx_edi, l10n_mx_edi_40) exist in the Odoo Community source tree and can generate and stamp CFDI 4.0. However, Odoo S.A. officially positions and maintains the polished Mexican localization (including the easiest PAC stamping path via Odoo IAP credits and the SAT accounting reports) for the Enterprise edition; in Community, robust, production-grade CFDI 4.0 compliance in practice relies on OCA/third-party modules (e.g., the OCA l10n-mexico project / l10n_mx_cfdi) configured with a PAC. So CFDI 4.0 is achievable but is community/third-party-driven in this tier, not turn-key official. |
| **Edition required for mx localization** | This is the central caveat. Odoo's full, officially-supported Mexican localization — notably the SAT accounting reports (DIOT, XML Pólizas / contabilidad electrónica via l10n_mx_reports and related modules) and the frictionless built-in PAC stamping — is gated to Odoo Enterprise (a paid annual subscription). The Community (free) edition contains the base CFDI EDI building blocks but, for complete CFDI 4.0 + SAT reporting compliance, depends on OCA/third-party modules and manual PAC integration. In short: official, complete MX localization effectively requires Enterprise; Community requires community/third-party modules. |
| **Pac provider flexibility** | Flexible / open. Because Community relies on community-built PAC connectors, the customer can choose among supported PACs (Solución Factible, Quadrum/Finkok, SW Sapien, and others available as modules) rather than being locked to a single vendor ecosystem. This contrasts with vendors that bind stamping to their own PAC. The trade-off is that each PAC needs a compatible/maintained connector module. |

### Contabilidad

| Campo | Valor |
|---|---|
| **Accounting integration** | Native double-entry Accounting is included in Community (the 'Accounting'/Invoicing core): chart of accounts, journals, invoicing, payments, bank reconciliation, and standard financial statements. However, the advanced 'Accounting' app features — automated bank-feed synchronization, follow-up/dunning automation, advanced/dynamic financial reports, and the Mexican SAT reports — are Enterprise-only. Community provides solid base accounting but not the full Enterprise accounting suite. |

### Escalabilidad / modulos

| Campo | Valor |
|---|---|
| **Available modules** | Broad: Community ships core business apps including Sales, Purchase, Inventory, Manufacturing (MRP), Accounting/Invoicing (base), CRM, Point of Sale, Project, HR (base), Website, eCommerce, Email Marketing (basic), and more. Enterprise adds 40+ additional apps/features (Odoo Studio, advanced Accounting, Helpdesk with SLAs, Field Service, advanced Marketing Automation, advanced MRP/quality, native mobile enhancements, AI features). The Community module catalog is substantial but a subset of the full Odoo offering. |
| **Extensibility** | Very high. Open LGPL v3 source means full code access; the modular Python/XML framework with the Odoo ORM allows deep customization, new modules, inherited views, and business-logic overrides. This is one of Community's biggest advantages over closed Mexican software. The caveat: customization requires developer skill (no Odoo Studio low-code tool in Community), and customizations must be maintained across annual upgrades. |
| **Sdk api integration tier gating** | No tier gating of programmatic integration. The full ORM and external APIs (XML-RPC and JSON-RPC) are available in the free Community edition — every model and method is accessible programmatically out of the box. This is a strategic contrast with CONTPAQi, which restricts its SDK to the Premium tier; Odoo exposes its ORM/API across all editions, including the free one. |
| **App marketplace** | Yes — the Odoo Apps Store (apps.odoo.com) hosts thousands of free and paid modules, many compatible with or built for Community, plus the OCA (Odoo Community Association) GitHub repositories providing free, community-maintained modules including the Mexican localization (l10n-mexico) project. |

### Soporte y ecosistema

| Campo | Valor |
|---|---|
| **Technical support** | No official Odoo S.A. support is included with the Community Edition (support and SLAs are an Enterprise benefit). Users rely on self-service, community forums, and — for production needs — paid engagements with Odoo partners/integrators. This absence of bundled vendor support is a core trade-off of the free tier. |
| **Partner network** | Strong in Mexico. Odoo has an active partner network, led by Gold Partners such as Vauxoo (the first Gold Partner in Mexico, ~12+ years, 150+ implementations, operating across Latin America), plus numerous other local partners and freelance developers. Partners deliver implementation, localization, hosting, and support for Community deployments. |
| **Community** | Large and active global open-source community: the Odoo Community Association (OCA) maintains hundreds of free modules (including the Mexican localization), public GitHub repositories, active forums, and a sizeable developer talent pool. Mexico specifically has a notable community of Odoo developers and accounting/SME adopters. |
| **Documentation** | Extensive official online documentation (per major version) covering apps, developer framework, and the Mexican fiscal localization, plus abundant third-party tutorials, partner blogs, and community Q&A. Documentation quality is generally high, though some Mexican-localization specifics are oriented toward the Enterprise feature set. |

### Integraciones

| Campo | Valor |
|---|---|
| **Api** | Robust and fully available in Community. External API via XML-RPC and JSON-RPC exposes all ORM models and methods for read/write/search and method calls; the internal ORM enables module-level integration. No edition restriction on API access — a key advantage of the open platform. |
| **Ecommerce** | Yes — the Website and eCommerce apps are included in Community, providing an integrated online store tied to Inventory, Sales, and Accounting. Some advanced website/eCommerce features and certain payment/shipping connectors are Enterprise-oriented. |
| **Third party connectors** | Available via the Apps Store / OCA and partner development: connectors for payment gateways, shipping carriers, marketplaces (e.g., Amazon, MercadoLibre via third-party modules), banks (bank statement import; live bank-feed sync is Enterprise), and PACs. Many connectors are community/paid third-party rather than first-party, and quality/maintenance varies. |

### Estrategico

| Campo | Valor |
|---|---|
| **Vendor lock in data portability** | Lowest lock-in profile in the comparison. Open-source LGPL v3 code plus a standard PostgreSQL database means full ownership and portability: data lives in an open relational schema, can be exported (CSV/XLSX, SQL dump, API), and the software can be self-hosted indefinitely on any infrastructure with no vendor able to revoke access. There is no proprietary file format. The practical lock-in that does exist is to custom code/modules and to the chosen partner/PAC, not to the vendor. This is a strategic advantage versus proprietary Mexican software with closed formats. |
| **Mexico market maturity** | Moderate for the Mexican-fiscal context. As a global ERP, Odoo is mature and feature-rich, and its MX localization has progressed through CFDI 4.0 and Carta Porte. But the strongest, most up-to-date Mexican-compliance experience is tied to the paid Enterprise edition; in the free Community tier, MX fiscal maturity depends on OCA/third-party modules, custom addenda work, and the absence of native CONTPAQi/SAT-report integration. It is well-adapted as a business platform but less 'turn-key' for Mexican tax compliance than local incumbents in this specific tier. |

### Usabilidad

| Campo | Valor |
|---|---|
| **Learning curve** | Moderate to steep. The platform is broad and powerful; end-user operation of individual apps is reasonably approachable thanks to a modern UI, but configuring the system, the Mexican localization, and any customization requires meaningful expertise. Community is steeper than Enterprise because there is no Odoo Studio low-code tooling and no vendor support, pushing more setup onto developers/partners. |
| **Interface** | Modern, clean, web-based UI consistent across apps, with Kanban/list/form/calendar/pivot views and a responsive design. Odoo 19 further refined the design. The interface quality is a recognized strength; the same core UI is shared between Community and Enterprise (Enterprise adds some polish, mobile, and Studio). |

### Campos inciertos (no verificados)

- License price
- Implementation cost
- Maintenance renewal cost
- Tco 1 3 years
- Xml volume multibranch capacity
- Timbrado stamping
- Complementos
- Addendas
- Sat connection
- Accounting handoff to contpaqi contabilidad
- Market share installed base mx

---

## 2. CONTPAQi Comercial Start

*Computación en Acción, S.A. de C.V. (CONTPAQi), a Mexican software company. CONTPAQi Comercial Start is the entry tier of the CONTPAQi Comercial product line.*

### Informacion basica

| Campo | Valor |
|---|---|
| **Developer** | Computación en Acción, S.A. de C.V. (CONTPAQi), a Mexican software company. CONTPAQi Comercial Start is the entry tier of the CONTPAQi Comercial product line. |
| **Country of origin** | Mexico |
| **License model** | Proprietary, closed-source. Sold under an annual subscription (Licenciamiento Anual) that includes automatic updates, official CONTPAQi support and new versions at no extra cost. A monthly option also exists. CONTPAQi has moved its desktop line to annual licensing (no longer perpetual). Available in mono-RFC (single company) and multi-RFC (multi-company) variants. |

### Costo / TCO

| Campo | Valor |
|---|---|
| **Licensing scheme** | Annual subscription licensing (Licenciamiento Anual), renewed every year; a monthly licensing option also exists. CONTPAQi's 2026 public price list explicitly separates 'licencia nueva' (new license) from 'renovacion/actualizacion' (renewal), with renewal priced lower than a new license. Users and RFCs can only be expanded during the license validity period. This reflects CONTPAQi's broader 2026 migration of its desktop products to annual subscription. |

### Despliegue

| Campo | Valor |
|---|---|
| **Hosting** | On-premise desktop application (Windows). Can be hosted on a local PC/server or accessed via a hosted/cloud-desktop service offered by some distributors, but the product itself is a Windows desktop system, not native SaaS. |
| **Operating system** | Microsoft Windows (desktop and Windows Server). Compatibility notices have covered Windows 7/8/Server 2012 in older versions; current versions target supported Windows releases. |

### Funcionalidad comercial

| Campo | Valor |
|---|---|
| **Sales** | Yes. Supports the full commercial document cycle: quotations, orders, remissions, sales invoices and returns. Generates CFDI 4.0 from sales tickets/documents. |
| **Purchasing** | Yes. Supports purchasing documents (purchase orders, purchases and returns) and supplier management. |
| **Inventory warehouses** | Basic inventory control with warehouse management, alternate codes and supplier codes. Detailed inventory control such as series and lots (lotes) is a Pro-tier feature and is not included in Start. |
| **Point of sale** | Yes. Built-in point of sale with barcode scanner support, multiple payment methods, cash reconciliation (cortes de caja), real-time inventory and one-click CFDI 4.0 from a sales ticket. POS is a core strength of the Start tier. |
| **Price lists** | Yes. Multiple price lists, plus promotions and discounts by customer. |
| **Xml volume multibranch capacity** | Designed for low XML/fiscal volume and single-location small businesses. High XML/fiscal load and multi-branch (multisucursal) handling are Premium-tier capabilities; Start does not target multi-branch or high-volume scenarios. CFDI folios themselves are unlimited. |

### Cumplimiento fiscal MX

| Campo | Valor |
|---|---|
| **Cfdi 40** | Yes. Native CFDI 4.0 issuance (invoices, REP/payment receipts, Carta Porte, expense vouchers, credit notes), generated directly and compliant with SAT requirements. Unlimited folios at no cost. |
| **Edition required for mx localization** | Mexican fiscal localization is native and built into every CONTPAQi Comercial tier including Start; it is not gated behind a higher paid tier. CONTPAQi is a Mexico-only product purpose-built for SAT/CFDI compliance. |
| **Timbrado stamping** | Native stamping (timbrado) integrated into the system, processed through CONTPAQi's own PAC ecosystem. Folios are unlimited at no extra cost. PAC automatic validations apply (e.g., SAT catalog keys, postal codes, vehicle plates for Carta Porte). |
| **Complementos** | Supports SAT complementos including Carta Porte (version 3.1, effective July 17, 2024) and Pagos/REP (recibo electronico de pago), as well as credit notes and expense documents, all as CFDI 4.0. |
| **Pac provider flexibility** | Low flexibility: stamping is tied to CONTPAQi's own integrated PAC ecosystem rather than allowing free choice of an external PAC. This is part of the CONTPAQi closed-ecosystem model. |
| **Sat connection** | Fiscal/SAT compliance for issuance (CFDI 4.0, complementos) is native. Full electronic accounting (contabilidad electronica), DIOT and policy generation are achieved by integrating with CONTPAQi Contabilidad; Start integrates/exports accounting vouchers (polizas) to CONTPAQi Contabilidad rather than performing electronic accounting itself. |

### Contabilidad

| Campo | Valor |
|---|---|
| **Accounting integration** | No full accounting module within Start. It integrates with CONTPAQi Bancos (auto-updating accounts receivable/payable) and with CONTPAQi Contabilidad for electronic accounting compliance. Includes CONTPAQi Business Intelligence dashboards for business indicators. |
| **Accounting handoff to contpaqi contabilidad** | Yes - native export/integration of accounting vouchers (polizas) directly into CONTPAQi Contabilidad. This tight same-vendor handoff is a key ecosystem advantage (and lock-in factor) of the CONTPAQi suite, available from the Start tier. |

### Escalabilidad / modulos

| Campo | Valor |
|---|---|
| **Available modules** | Start unlocks a basic subset of the shared Comercial Start/Pro program: POS, sales/purchase documents, basic warehouse inventory, multiple price lists, CFDI 4.0/timbrado, Business Intelligence dashboards, and integration to CONTPAQi Bancos and Contabilidad. Advanced modules (series/lots, accounts receivable customer management, commissions by salesperson, deeper executive reports, projects) are reserved for Pro; high-volume/multi-branch and SDK for Premium. |
| **Extensibility** | Limited at the Start tier. No programmatic SDK access. Customization is largely confined to configuration; deeper extensibility/integration requires moving up to Premium (SDK). |
| **Sdk api integration tier gating** | No SDK/programmatic integration at the Start tier. The CONTPAQi Comercial SDK is exclusive to the Premium tier, which is the edition used for enterprise integration projects and advanced development. Start (and Pro) cannot access the SDK. |

### Soporte y ecosistema

| Campo | Valor |
|---|---|
| **Technical support** | Official CONTPAQi technical support is included with the active annual license (subscription includes support, automatic updates and new versions). Day-to-day support is also delivered through the authorized distributor/partner network. |
| **Partner network** | Extensive nationwide network of authorized CONTPAQi distributors and partners across Mexico (including Platinum/Gold tiers), providing sales, implementation, training and support. |
| **Documentation** | Extensive official documentation in Spanish: manuals, technical cards, knowledge base (conocimiento.contpaqi) and blog guides covering features, CFDI and complementos. |
| **Market share installed base mx** | CONTPAQi is one of the dominant administrative/accounting software vendors in Mexico with a very large installed base, making it a de-facto standard among SMEs and accountants; the Comercial Pro tier is described as the best-selling of the line, and Start serves the entry/small-business segment. High talent availability among Mexican accountants/distributors. |

### Integraciones

| Campo | Valor |
|---|---|
| **Api** | No public API/SDK at the Start tier (SDK is Premium-only). Integration is achieved mainly through the native CONTPAQi suite (Bancos, Contabilidad) rather than an open programmatic interface. |

### Estrategico

| Campo | Valor |
|---|---|
| **Vendor lock in data portability** | High vendor lock-in. Proprietary closed-source Windows product on annual subscription, with a proprietary data format and a closed PAC ecosystem; deep native handoff to CONTPAQi Contabilidad/Bancos reinforces staying within the suite. Data portability is limited to CFDI XML exports and standard report/file exports rather than open database access (no SDK at Start tier). |
| **Mexico market maturity** | Very mature and purpose-built for the Mexican market. Native CFDI 4.0, complementos (Carta Porte 3.1, REP), SAT compliance and tight integration with Mexican electronic accounting via CONTPAQi Contabilidad. Designed exclusively for Mexican fiscal/commercial requirements. |

### Usabilidad

| Campo | Valor |
|---|---|
| **Learning curve** | Low. Start is positioned for small businesses and operations with 1-2 employees; simple POS-and-invoicing oriented workflow makes it the easiest tier to adopt. |

### Campos inciertos (no verificados)

- Current version
- License price
- Implementation cost
- Included users
- Additional user and rfc cost
- Maintenance renewal cost
- Hidden costs
- Tco 1 3 years
- Hardware requirements
- Mobile app availability
- Crm
- Document bulk load
- Addendas
- App marketplace
- Community
- Ecommerce
- Third party connectors
- Interface

---

## 3. CONTPAQi Comercial Pro

*CONTPAQi (Computación en Acción, S.A. de C.V.), a 100% Mexican enterprise-software vendor focused on accounting, fiscal and administrative solutions.*

### Informacion basica

| Campo | Valor |
|---|---|
| **Developer** | CONTPAQi (Computación en Acción, S.A. de C.V.), a 100% Mexican enterprise-software vendor focused on accounting, fiscal and administrative solutions. |
| **Country of origin** | Mexico |
| **License model** | Proprietary, closed-source commercial software. Sold under an annual subscription (licenciamiento anual) model; traditional perpetual licenses were discontinued (only valid until 2018) and CONTPAQi has migrated its 2026 price list fully to the annual scheme, splitting pricing between new license vs. renewal. |

### Costo / TCO

| Campo | Valor |
|---|---|
| **Licensing scheme** | Annual subscription. CONTPAQi completed its migration to the annual licensing model in the 2026 price list (effective 2 January 2026), discontinuing traditional perpetual licenses. Pricing explicitly separates 'licencia nueva' (new license) from 'renovación' (annual renewal), with renewal cheaper than a new license. Remaining days roll over when renewing within validity. |
| **Included users** | 1 user included in the base license. |
| **Hidden costs** | Potential additional costs: training/courses, extended distributor support contracts, PAC stamping timbres (CFDI stamp credits, billed separately/by usage), integration with CONTPAQi Contabilidad (separate product license), additional RFCs/users, and the recurring annual renewal itself. SDK is NOT available in Pro, so any programmatic integration requires upgrading to Premium (a tier-jump cost). |

### Despliegue

| Campo | Valor |
|---|---|
| **Hosting** | On-premise by default (installed on Windows desktop/server, local or LAN multi-user). Can be run in the cloud via third-party/distributor hosting (e.g., remote desktop / CONTPAQi-authorized cloud hosting), but it is not a native SaaS product. |

### Funcionalidad comercial

| Campo | Valor |
|---|---|
| **Sales** | Full sales cycle: quotes, sales orders, invoices (CFDI), credit notes, returns, and payment complements (REP). Salesperson management and commissions by salesperson. Accounts receivable control with customer balances. |
| **Purchasing** | Full purchasing cycle: purchase orders, supplier documents, accounts payable, and supplier balance control. Costing of inventory tied to purchases. |
| **Crm** | Basic customer management (clients, receivables, contact data); no full-featured CRM/opportunity-pipeline module. CRM-style relationship management is limited compared to dedicated CRM systems. |

### Cumplimiento fiscal MX

| Campo | Valor |
|---|---|
| **Cfdi 40** | Yes. Current versions support CFDI 4.0 issuance (invoices, credit notes, payment complements), aligned with SAT requirements. Older documentation referenced CFDI 3.3, but the maintained 2025-2026 versions are CFDI 4.0 compliant. |
| **Edition required for mx localization** | Mexican fiscal localization (CFDI 4.0, SAT compliance) is native and built into every paid tier of CONTPAQi Comercial including Pro — there is no separate paid 'localization' add-on as with foreign ERPs; Mexican compliance is the core value proposition of the product. |
| **Timbrado stamping** | CFDI stamping (timbrado) is done through CONTPAQi's own authorized PAC ecosystem. CONTPAQi is one of the leading SAT-authorized PACs in Mexico; stamping is integrated into the product. Stamp credits (timbres) are typically purchased separately by usage. |
| **Complementos** | Supports SAT complementos including Carta Porte (3.x — currently 3.1) for goods transport, Pagos/REP (payment receipts complement), and cancellation flows, across the Comercial Start/Pro/Premium line. |

### Contabilidad

| Campo | Valor |
|---|---|
| **Accounting integration** | No full general-ledger accounting module inside Comercial Pro; accounting is handled by the separate CONTPAQi Contabilidad product. Pro generates the commercial documents and feeds accounting via native integration. |
| **Accounting handoff to contpaqi contabilidad** | Strong native ecosystem advantage: Comercial Pro integrates directly with CONTPAQi Contabilidad to generate accounting entries (pólizas) automatically — with a single click from the commercial document, accounting entries for all commercial operations can be created. This tight, automatic póliza hand-off is a core lock-in/ecosystem benefit of staying within the CONTPAQi suite. |

### Escalabilidad / modulos

| Campo | Valor |
|---|---|
| **Available modules** | Functional modules/blocks across the Comercial line: sales, purchasing, inventory (with series, lots, locations, pedimentos, costing), treasury, accounts receivable/payable, price lists, salesperson commissions, executive reports, XML import, extra fields, and security/permissions. Pro sits in the middle: more than Start (advanced inventory, more reports, customization of processes, basic production), below Premium (multi-company, projects, high XML volume, SDK). |
| **Extensibility** | Limited extensibility within Pro: customizable processes, extra fields, and report customization, but NO programmatic SDK access. Deep custom development/integration requires upgrading to Premium. |
| **Sdk api integration tier gating** | SDK access is GATED to Premium only. CONTPAQi Comercial Pro does NOT include the Comercial SDK; only the Premium tier exposes the SDK used for enterprise integration and advanced custom development. This is a key tier-gating limitation versus open ERPs that expose APIs at every tier. |

### Soporte y ecosistema

| Campo | Valor |
|---|---|
| **Technical support** | Official support delivered primarily through CONTPAQi's network of authorized distributors, plus a phone support center, online help materials, video tutorials and webinars. Free remote installation and initial post-sale support are included. |
| **Partner network** | Large nationwide network of authorized distributors/partners across Mexico (master distributors, Platinum/Oro tiers, etc.), providing implementation, training and support. Strong, mature channel presence throughout Mexico. |
| **Documentation** | Official manuals, technical cards (cartas técnicas), comparison tables and knowledge-base articles are publicly available online (conocimiento.blob.core.windows.net), in Spanish, well-maintained. |

### Estrategico

| Campo | Valor |
|---|---|
| **Vendor lock in data portability** | Significant vendor lock-in: proprietary, closed format; annual subscription required to keep the system operational and compliant; stamping tied to CONTPAQi's PAC ecosystem; tight coupling to CONTPAQi Contabilidad. Data can be exported (XML/reports/Excel) but there is no open database/source. Migrating away is non-trivial compared to an open-source ERP. Switching to richer integration also forces an upgrade to Premium (intra-ecosystem lock-in). |
| **Mexico market maturity** | Extremely high maturity for the Mexican market — purpose-built for Mexican fiscal/CFDI/SAT requirements, continuously updated for regulatory changes (CFDI 4.0, Carta Porte 3.1, etc.). This is its strongest differentiator versus generic/global ERPs. |

### Campos inciertos (no verificados)

- Current version
- License price
- Implementation cost
- Additional user and rfc cost
- Maintenance renewal cost
- Tco 1 3 years
- Hardware requirements
- Operating system
- Mobile app availability
- Inventory warehouses
- Point of sale
- Price lists
- Document bulk load
- Xml volume multibranch capacity
- Addendas
- Pac provider flexibility
- Sat connection
- App marketplace
- Community
- Market share installed base mx
- Api
- Ecommerce
- Third party connectors
- Learning curve
- Interface

---

## 4. CONTPAQi Comercial Premium

*CONTPAQi (Computación en Acción, S.A. de C.V.)*

### Informacion basica

| Campo | Valor |
|---|---|
| **Developer** | CONTPAQi (Computación en Acción, S.A. de C.V.) |
| **Country of origin** | Mexico |
| **License model** | Proprietary, closed-source. Historically sold as a perpetual 'tradicional' license; CONTPAQi has shifted its commercial strategy toward annual subscription licensing, with annual ('anual') licensing the dominant and promoted scheme for 2026 (perpetual 'tradicional' licenses still exist but are being phased toward annual). Per-user (network seat) licensing. |

### Costo / TCO

| Campo | Valor |
|---|---|
| **Included users** | 1 user included in the base license. |

### Despliegue

| Campo | Valor |
|---|---|
| **Hosting** | On-premise (desktop/client-server) by default; can be hosted on a private/cloud Windows server or via partner-provided cloud hosting (escritorio virtual). No native multi-tenant SaaS web app from CONTPAQi for this product. Multi-branch uses a central server with remote points consolidating data. |
| **Operating system** | Microsoft Windows (desktop and Windows Server); requires Microsoft SQL Server backend. Not available for macOS/Linux natively. |

### Funcionalidad comercial

| Campo | Valor |
|---|---|
| **Sales** | Full commercial sales cycle: quotes, sales orders, remissions/delivery notes, invoices, credit/debit notes; supports income, expense and transfer CFDI document types, professional-fee and rental receipts. Configurable document workflows and folios. |
| **Purchasing** | Purchasing management: purchase orders, supplier documents, receipt of goods, reception of supplier CFDIs into the system. |
| **Inventory warehouses** | Strong multi-warehouse (multialmacen) inventory: units of measure and weight, series, lots, pedimentos, barcode generation, and up to 3 product characteristics (e.g., size, color, style). Designed to handle high information volumes. |
| **Price lists** | Multiple price lists and commercial policies/discount rules; per-customer and per-product pricing configuration. |
| **Xml volume multibranch capacity** | Positioned as the top tier for high XML/fiscal volume and multi-branch (multisucursal) operation: central server with remote branches/POS consolidating data in real time, high-volume reporting via the Reporteador, and SQL Server backend to sustain large transaction/XML loads. Recommended for operations exceeding ~20 concurrent terminals (with special implementation). |

### Cumplimiento fiscal MX

| Campo | Valor |
|---|---|
| **Cfdi 40** | Native CFDI 4.0 support: issuance, reception, validation, cancellation and storage of electronic invoices in line with SAT requirements. Fiscal/SAT changes are delivered through updates included in the annual license. |
| **Edition required for mx localization** | Mexican fiscal localization is built into the product natively (it is a Mexican product); no separate paid localization layer is required. Premium is the top edition of the line and includes the fullest commercial+fiscal feature set, but CFDI 4.0 compliance itself is present across the Comercial editions. |
| **Timbrado stamping** | Includes unlimited CFDI stamping (timbrado ilimitado) within the annual license using CONTPAQi's own stamping infrastructure (no external PAC contract required). Timbrado and cancellation are also exposed through the SDK for programmatic document automation. |
| **Pac provider flexibility** | Closed ecosystem: stamping is provided through CONTPAQi's own PAC infrastructure bundled with the license rather than free choice among third-party PACs. This is a vendor-controlled advantage (no separate PAC fee) but limits PAC-provider flexibility. |

### Contabilidad

| Campo | Valor |
|---|---|
| **Accounting integration** | No full general-ledger accounting inside Comercial Premium; it configures accounting account segments (general and additional/variable segments) and generates pólizas for commercial operations to be consumed by a dedicated accounting system. |
| **Accounting handoff to contpaqi contabilidad** | Native, tight integration: a 'Contabilizar' action and the Contabilizacion/interface module generate accounting pólizas (sales, payments, etc.) from commercial documents and synchronize them directly into CONTPAQi Contabilidad with a single click, avoiding double entry. This is a key ecosystem lock-in/advantage that strongly favors keeping accounting within CONTPAQi. |

### Escalabilidad / modulos

| Campo | Valor |
|---|---|
| **Available modules** | Part of the CONTPAQi suite: integrates with CONTPAQi Contabilidad, Bancos, Nominas, Factura Electronica/Xml en Linea and others. Within Premium: multi-warehouse inventory, full document cycle, Reporteador (reporting), multi-branch, multi-RFC. Other suite modules are licensed separately. |
| **Extensibility** | Highly extensible at the top tier via the SDK and direct SQL database access, enabling custom developments, ERP/e-commerce/web integrations and automation that lower tiers cannot do. |
| **Sdk api integration tier gating** | SDK access is gated to the Premium tier only - Start and Pro do not include the SDK. The CONTPAQi Comercial SDK is a COM-based library consumed from .NET/C# Windows applications (Console, WinForms, WPF) and supports login, opening companies, reading/creating/editing catalogs, creating documents, stamping and canceling. It is the standard path for enterprise integration and advanced developments; programmatic work can also be done by accessing the SQL database directly. (By contrast, Odoo exposes its ORM/XML-RPC/JSON-RPC API on every tier including Community.) |

### Soporte y ecosistema

| Campo | Valor |
|---|---|
| **Technical support** | Official CONTPAQi support included with the annual license (CONTPAQi help chat for 1 year), plus front-line support delivered by the authorized distributor/partner that sold the license. |
| **Partner network** | Very large authorized distributor/partner network across Mexico (Platinum/Oro/etc. tiers), providing sales, implementation, training and SDK development services nationwide. |
| **Documentation** | Extensive Spanish-language documentation: technical cards (cartas tecnicas), manuals, knowledge base, and SDK reference published by CONTPAQi. |

### Estrategico

| Campo | Valor |
|---|---|
| **Vendor lock in data portability** | Significant vendor lock-in: proprietary closed-source product, proprietary SQL schema, CONTPAQi-controlled stamping/PAC, and a strong pull to keep accounting in CONTPAQi Contabilidad via native póliza handoff. Data is technically extractable through the SDK, SQL queries and XML/CFDI files, but there is no open standard format and migrating off the suite is non-trivial. Contrasts with Odoo's open-source code and open API/data portability. |
| **Mexico market maturity** | Extremely mature and purpose-built for the Mexican market: native CFDI 4.0, SAT compliance, Carta Porte, addendas, Multi-RFC and built-in stamping, backed by a deep Mexican partner ecosystem. Mexico fiscal fit is a core strength. |

### Campos inciertos (no verificados)

- Current version
- License price
- Licensing scheme
- Implementation cost
- Additional user and rfc cost
- Maintenance renewal cost
- Hidden costs
- Tco 1 3 years
- Hardware requirements
- Mobile app availability
- Point of sale
- Crm
- Document bulk load
- Complementos
- Addendas
- Sat connection
- App marketplace
- Community
- Market share installed base mx
- Api
- Ecommerce
- Third party connectors
- Learning curve
- Interface

---

## 5. Hôlos ERP (Hum&Net)

*HumandNet / Compromiso Humano (Mexican enterprise software company with 30+ years of experience; CONTPAQi Platinum Business Partner). Brands used: Hum&Net, Compromiso Humano. Sites: compromisohumano.com, humandnet.com, holoserp.app*

### Informacion basica

| Campo | Valor |
|---|---|
| **Developer** | HumandNet / Compromiso Humano (Mexican enterprise software company with 30+ years of experience; CONTPAQi Platinum Business Partner). Brands used: Hum&Net, Compromiso Humano. Sites: compromisohumano.com, humandnet.com, holoserp.app |
| **Country of origin** | Mexico |

### Despliegue

| Campo | Valor |
|---|---|
| **Hosting** | Cloud (SaaS, 'In Cloud'). Accessed via web browser (holoserp.app). Also offers CONTPAQi Escritorio Virtual to run CONTPAQi desktop systems from the cloud/browser. |

### Contabilidad

| Campo | Valor |
|---|---|
| **Accounting integration** | Strong native accounting integration. Finance/accounting is delivered through CONTPAQi Contabilidad and CONTPAQi Tesorera (apps 'Contabiliza', 'Analiza', 'Contabilidad'): XML processing, recurring vouchers, VAT control, declarations, reports. |
| **Accounting handoff to contpaqi contabilidad** | Native/built-in. The platform is centered on CONTPAQi Contabilidad and Tesorera (HumandNet is a CONTPAQi Platinum partner), so accounting entries/policies flow directly into CONTPAQi Contabilidad. This deep CONTPAQi coupling is a core ecosystem advantage. |

### Escalabilidad / modulos

| Campo | Valor |
|---|---|
| **Available modules** | Integrated suite of apps covering finance/accounting (Contabilidad, Contabiliza, Tesorera), fiscal analysis (Analiza), CONTPAQi Escritorio Virtual (cloud desktop), commercial/ERP operations, and Organizational Development / Human Talent (Desarrollo Organizacional). Marketed as fully integrated, no inter-software interfaces needed. |

### Soporte y ecosistema

| Campo | Valor |
|---|---|
| **Partner network** | Backed by HumandNet's distributor/consultant network and the broader CONTPAQi partner channel in Mexico. Third-party CONTPAQi distributors (e.g., Meraki Consultores, Alyan Consultores) also promote Holos. |

### Campos inciertos (no verificados)

- Current version
- License model
- License price
- Licensing scheme
- Implementation cost
- Included users
- Additional user and rfc cost
- Maintenance renewal cost
- Hidden costs
- Tco 1 3 years
- Hardware requirements
- Operating system
- Mobile app availability
- Sales
- Purchasing
- Inventory warehouses
- Point of sale
- Crm
- Price lists
- Document bulk load
- Xml volume multibranch capacity
- Cfdi 40
- Edition required for mx localization
- Timbrado stamping
- Complementos
- Addendas
- Pac provider flexibility
- Sat connection
- Extensibility
- Sdk api integration tier gating
- App marketplace
- Technical support
- Community
- Documentation
- Market share installed base mx
- Api
- Ecommerce
- Third party connectors
- Vendor lock in data portability
- Mexico market maturity
- Learning curve
- Interface
