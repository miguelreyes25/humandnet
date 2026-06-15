# Landing Page v2 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Añadir señales de confianza (logo wall, diferenciadores) y mejorar las secciones existentes (stats, servicios, hôlos, form) para aumentar conversión y percepción de profesionalismo.

**Architecture:** Proyecto estático HTML/CSS/JS puro. Sin build system. Todos los cambios van en tres archivos: `index.html`, `assets/css/styles.css`, `assets/js/main.js`. Los íconos son SVG inline (sin dependencia externa). Las animaciones usan GSAP ya cargado en la página.

**Tech Stack:** HTML5, CSS3 (variables CSS, CSS Grid, keyframes), Vanilla JS ES5 (IIFE con `'use strict'`), GSAP 3 + ScrollTrigger (ya cargados via CDN).

**Preview:** `python -m http.server 4321` desde la raíz del proyecto → abrir `http://localhost:4321`

---

## Archivos involucrados

| Archivo | Tipo | Cambios |
|---------|------|---------|
| `index.html` | Modificar | Stats (íconos), nueva sección Clientes, Servicios (nuevo layout), Hôlos (badge + features), nueva sección ¿Por qué?, form action |
| `assets/css/styles.css` | Modificar | Nuevas clases: `.stat-icon`, `.clientes`, `.marquee-*`, `.card-featured`, `.cards-featured`, `.porque`, `.porque-cards`, `.porque-card`, `.holos-badge` |
| `assets/js/main.js` | Modificar | Agregar lógica submit del form al final del IIFE |
| `assets/img/clientes/` | Crear directorio | Placeholder: archivo `.gitkeep` + README con instrucciones de logos |

---

## Task 1: Stats — íconos SVG con colores de marca

**Archivos:**
- Modificar: `index.html` (sección `.stats`)
- Modificar: `assets/css/styles.css` (agregar al final)

- [ ] **Paso 1: Agregar clase `.stat-icon` al CSS**

Abrir `assets/css/styles.css` y agregar al final:

```css
/* ---------- Stats icons ---------- */
.stat-icon{display:flex;justify-content:center;margin-bottom:14px;}
.stat-icon svg{display:block;}
```

- [ ] **Paso 2: Reemplazar el bloque de Stats en index.html**

Localizar la sección `<!-- STATS -->` en `index.html` y reemplazar su contenido por:

```html
<!-- STATS -->
<section class="stats" id="nosotros">
  <div class="stats-inner">
    <div class="stat" data-reveal>
      <div class="stat-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#E91E63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      </div>
      <div class="stat-num" data-count="30" data-suffix="+">0</div>
      <div class="stat-label">Años de experiencia</div>
    </div>
    <div class="stat" data-reveal>
      <div class="stat-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#00BCD4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
      </div>
      <div class="stat-num" data-count="200" data-suffix="+">0</div>
      <div class="stat-label">Empresas atendidas</div>
    </div>
    <div class="stat" data-reveal>
      <div class="stat-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#FF9800" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
      </div>
      <div class="stat-num" data-count="500" data-suffix="+">0</div>
      <div class="stat-label">Proyectos entregados</div>
    </div>
    <div class="stat" data-reveal>
      <div class="stat-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#E91E63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      </div>
      <div class="stat-num" data-count="98" data-suffix="%">0</div>
      <div class="stat-label">Satisfacción de clientes</div>
    </div>
  </div>
</section>
```

- [ ] **Paso 3: Verificar en navegador**

Iniciar servidor si no está corriendo: `python -m http.server 4321`
Abrir `http://localhost:4321` → sección Stats debe mostrar 4 íconos SVG sobre los números (reloj magenta, edificio cyan, pulso naranja, estrella magenta). Los números deben seguir animándose al hacer scroll.

- [ ] **Paso 4: Commit**

```bash
git add index.html assets/css/styles.css
git commit -m "feat: add SVG icons to stats section"
```

---

## Task 2: Sección "Clientes que confían" (marquee infinito)

**Archivos:**
- Modificar: `index.html` (insertar sección después de `<!-- STATS -->`)
- Modificar: `assets/css/styles.css` (agregar al final)
- Crear: `assets/img/clientes/` con `.gitkeep`

- [ ] **Paso 1: Crear directorio de logos y placeholder**

```bash
mkdir -p assets/img/clientes
touch assets/img/clientes/.gitkeep
```

- [ ] **Paso 2: Agregar CSS del marquee**

Agregar al final de `assets/css/styles.css`:

```css
/* ---------- Clientes marquee ---------- */
.clientes{padding:60px 0;overflow:hidden;border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
.clientes .section-head{padding:0 32px;}
.marquee-track{position:relative;overflow:hidden;margin-top:40px;}
.marquee-track::before,.marquee-track::after{
  content:'';position:absolute;top:0;bottom:0;width:120px;z-index:2;pointer-events:none;
}
.marquee-track::before{left:0;background:linear-gradient(90deg,var(--navy),transparent);}
.marquee-track::after{right:0;background:linear-gradient(-90deg,var(--navy),transparent);}
.marquee-inner{
  display:flex;align-items:center;gap:48px;
  width:max-content;
  animation:marquee 30s linear infinite;
}
.marquee-inner:hover{animation-play-state:paused;}
@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.client-logo{
  height:48px;width:auto;max-width:140px;object-fit:contain;
  filter:grayscale(1) opacity(0.55);
  transition:filter .3s;
  flex-shrink:0;
}
.client-logo:hover{filter:none;}
.client-logo-placeholder{
  height:48px;min-width:120px;
  display:flex;align-items:center;justify-content:center;
  background:rgba(255,255,255,0.04);
  border:1px solid var(--line);border-radius:8px;
  padding:0 20px;
  font-size:13px;font-weight:600;color:#475569;
  flex-shrink:0;white-space:nowrap;
}
@media(prefers-reduced-motion:reduce){
  .marquee-inner{animation:none!important;}
}
```

- [ ] **Paso 3: Insertar la sección en index.html**

Localizar el comentario `<!-- SERVICIOS -->` en `index.html` e insertar **antes** de él:

```html
<!-- CLIENTES -->
<section class="clientes" id="clientes">
  <div class="section-head" data-reveal>
    <div class="eyebrow">Empresas que confían en nosotros</div>
    <h2>Más de 200 organizaciones ya transformaron su operación</h2>
  </div>
  <div class="marquee-track" aria-label="Clientes de Hum&Net">
    <div class="marquee-inner">
      <!-- Set 1: reemplazar con <img class="client-logo" src="assets/img/clientes/nombre.png" alt="Empresa"> cuando tengas los logos -->
      <div class="client-logo-placeholder">Empresa A</div>
      <div class="client-logo-placeholder">Empresa B</div>
      <div class="client-logo-placeholder">Empresa C</div>
      <div class="client-logo-placeholder">Empresa D</div>
      <div class="client-logo-placeholder">Empresa E</div>
      <div class="client-logo-placeholder">Empresa F</div>
      <div class="client-logo-placeholder">Empresa G</div>
      <div class="client-logo-placeholder">Empresa H</div>
      <!-- Set 2: duplicado exacto del Set 1 para el loop infinito -->
      <div class="client-logo-placeholder">Empresa A</div>
      <div class="client-logo-placeholder">Empresa B</div>
      <div class="client-logo-placeholder">Empresa C</div>
      <div class="client-logo-placeholder">Empresa D</div>
      <div class="client-logo-placeholder">Empresa E</div>
      <div class="client-logo-placeholder">Empresa F</div>
      <div class="client-logo-placeholder">Empresa G</div>
      <div class="client-logo-placeholder">Empresa H</div>
    </div>
  </div>
</section>
```

> **Nota para logos reales:** Cuando tengas los PNGs/SVGs, colocarlos en `assets/img/clientes/` y reemplazar cada `<div class="client-logo-placeholder">Nombre</div>` por `<img class="client-logo" src="assets/img/clientes/nombre.png" alt="Nombre empresa">`. Duplicar también en el Set 2.

- [ ] **Paso 4: Verificar en navegador**

Recargar `http://localhost:4321` → entre Stats y Servicios debe aparecer una sección con placeholders desfilando horizontalmente en loop continuo. Los bordes laterales deben tener fade gradiente. Al pasar el cursor sobre la pista, la animación debe detenerse.

- [ ] **Paso 5: Commit**

```bash
git add index.html assets/css/styles.css assets/img/clientes/.gitkeep
git commit -m "feat: add Clientes marquee section with logo placeholders"
```

---

## Task 3: Servicios — tarjeta destacada + íconos

**Archivos:**
- Modificar: `index.html` (sección `.servicios`)
- Modificar: `assets/css/styles.css` (agregar nuevas clases, ajustar responsive)

- [ ] **Paso 1: Agregar CSS para el nuevo layout de Servicios**

Agregar al final de `assets/css/styles.css`:

```css
/* ---------- Servicios — featured layout ---------- */
.cards-featured{grid-template-columns:repeat(3,1fr);}
.card-featured{
  grid-column:1 / -1;
  display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center;
  background:linear-gradient(135deg,rgba(233,30,99,0.08),rgba(0,188,212,0.08));
  border-color:rgba(233,30,99,0.25);
}
.card-featured:hover{border-color:rgba(233,30,99,0.5);}
.card-featured .card-icon{
  width:56px;height:56px;
  background:rgba(233,30,99,0.12);border-radius:14px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.card-featured .card-eyebrow{
  font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  color:var(--magenta);margin-bottom:6px;
}
.card-featured h3{margin-bottom:8px;}
.card-icon{
  width:44px;height:44px;
  background:rgba(255,255,255,0.05);border-radius:12px;
  display:flex;align-items:center;justify-content:center;
  margin-bottom:18px;
}
@media(max-width:768px){
  .cards-featured{grid-template-columns:1fr;}
  .card-featured{grid-template-columns:1fr;}
}
```

- [ ] **Paso 2: Reemplazar la sección Servicios en index.html**

Localizar `<!-- SERVICIOS -->` y reemplazar todo el bloque hasta el cierre de la sección por:

```html
<!-- SERVICIOS -->
<section class="servicios" id="servicios">
  <div class="section-head" data-reveal>
    <div class="eyebrow">Lo que hacemos</div>
    <h2>Servicios que impulsan tu negocio</h2>
    <p>Acompañamos a tu organización en cada etapa de su transformación digital.</p>
  </div>
  <div class="cards cards-featured">
    <article class="card card-featured" data-reveal>
      <div class="card-accent"></div>
      <div class="card-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#E91E63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
      </div>
      <div>
        <div class="card-eyebrow">Producto estrella</div>
        <h3>Soluciones Empresariales</h3>
        <p>ERP y sistemas contables para optimizar toda tu operación. Desde Hôlos ERP® hasta la suite completa de CONTPAQi®.</p>
        <div class="card-tags">
          <span>Hôlos ERP®</span>
          <span>CONTPAQi® Contable</span>
          <span>CONTPAQi® Comercial</span>
          <span>Productividad</span>
        </div>
      </div>
    </article>
    <article class="card" data-reveal>
      <div class="card-accent"></div>
      <div class="card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00BCD4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
      </div>
      <h3>Infraestructura y TI</h3>
      <p>Servidores, hosting y nube para que tu tecnología nunca falle.</p>
      <div class="card-tags">
        <span>VPS</span><span>TSPlus</span><span>Hosting</span><span>Nube CONTPAQi®</span>
      </div>
    </article>
    <article class="card" data-reveal>
      <div class="card-accent"></div>
      <div class="card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF9800" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
      </div>
      <h3>Innovación y Desarrollo</h3>
      <p>Automatización, integraciones y agentes de IA para transformar tu empresa.</p>
      <div class="card-tags">
        <span>Desarrollo a la medida</span><span>RPA / Automatización</span><span>Agentes AI</span><span>Integraciones</span>
      </div>
    </article>
    <article class="card" data-reveal>
      <div class="card-accent"></div>
      <div class="card-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#E91E63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      </div>
      <h3>Sinergia</h3>
      <p>Desarrollo organizacional y humano para que tu equipo alcance su máximo potencial.</p>
      <div class="card-tags">
        <span>Desarrollo Organizacional</span><span>Clima laboral</span><span>Capacitación</span><span>Gestión del cambio</span>
      </div>
    </article>
  </div>
</section>
```

- [ ] **Paso 3: Verificar en navegador**

Recargar `http://localhost:4321` → sección Servicios debe mostrar "Soluciones Empresariales" como tarjeta ancha con gradiente magenta/cyan en el borde, ícono monitor, y eyebrow "Producto estrella". Las 3 tarjetas restantes deben estar en fila debajo, cada una con su ícono de color.

- [ ] **Paso 4: Commit**

```bash
git add index.html assets/css/styles.css
git commit -m "feat: redesign Servicios with featured card and SVG icons"
```

---

## Task 4: Hôlos ERP — badge cloud-native + features concretas

**Archivos:**
- Modificar: `index.html` (sección `.holos`)
- Modificar: `assets/css/styles.css` (agregar `.holos-badge`)

- [ ] **Paso 1: Agregar CSS del badge**

Agregar al final de `assets/css/styles.css`:

```css
/* ---------- Hôlos badge ---------- */
.holos-badge{
  display:inline-flex;align-items:center;gap:7px;
  background:rgba(0,188,212,0.10);
  color:var(--cyan);
  border:1px solid rgba(0,188,212,0.28);
  border-radius:20px;padding:5px 14px;
  font-size:13px;font-weight:600;
  margin-bottom:14px;
}
```

- [ ] **Paso 2: Reemplazar sección Hôlos ERP en index.html**

Localizar `<!-- HÔLOS ERP -->` y reemplazar todo el bloque por:

```html
<!-- HÔLOS ERP -->
<section class="holos" id="holos">
  <div class="holos-inner">
    <div class="holos-copy" data-reveal-left>
      <div class="eyebrow">Producto estrella</div>
      <div class="holos-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
        Cloud-native · Sin infraestructura adicional
      </div>
      <h2>Hôlos ERP<span class="reg">®</span>, tu operación en la nube</h2>
      <p>Centraliza finanzas, inventarios, ventas y producción en una sola plataforma diseñada para escalar con tu empresa.</p>
      <ul class="holos-feats">
        <li>Configurable por módulos: finanzas, inventarios, RRHH y ventas</li>
        <li>Automatización de aprobaciones, reportes y alertas en tiempo real</li>
        <li>Escala de 5 a 500+ usuarios sin cambiar de sistema</li>
        <li>100% en la nube — sin servidores, sin mantenimiento</li>
        <li>Integración certificada con toda la suite CONTPAQi®</li>
      </ul>
      <a href="#contacto" class="btn btn-primary">Solicitar una demo</a>
    </div>
    <div class="holos-visual" data-reveal-right>
      <img src="assets/img/holos-erp.png" alt="Hôlos ERP — interfaz holográfica">
    </div>
  </div>
</section>
```

- [ ] **Paso 3: Verificar en navegador**

Recargar `http://localhost:4321` → sección Hôlos ERP debe mostrar un pill/badge cyan con ícono de nube encima del título. Las 5 features deben tener texto específico y concreto (módulos, usuarios, etc.).

- [ ] **Paso 4: Commit**

```bash
git add index.html assets/css/styles.css
git commit -m "feat: add cloud-native badge and specific features to Hôlos ERP"
```

---

## Task 5: Sección "¿Por qué Hum&Net?"

**Archivos:**
- Modificar: `index.html` (insertar sección antes de `<!-- CTA -->`)
- Modificar: `assets/css/styles.css` (agregar al final)

- [ ] **Paso 1: Agregar CSS de la sección ¿Por qué?**

Agregar al final de `assets/css/styles.css`:

```css
/* ---------- ¿Por qué Hum&Net? ---------- */
.porque{padding:90px 32px;background:radial-gradient(ellipse at 50% 100%,rgba(0,188,212,0.06),transparent 60%);}
.porque-cards{
  max-width:var(--maxw);margin:0 auto;
  display:grid;grid-template-columns:repeat(4,1fr);gap:24px;
}
.porque-card{
  text-align:center;
  background:rgba(255,255,255,0.03);
  border:1px solid var(--line);border-radius:18px;
  padding:36px 24px;
  transition:transform .25s,border-color .25s,box-shadow .25s;
}
.porque-card:hover{
  transform:translateY(-6px);
  border-color:rgba(0,188,212,0.25);
  box-shadow:0 16px 40px rgba(0,0,0,0.35);
}
.porque-icon{
  width:56px;height:56px;border-radius:16px;
  display:flex;align-items:center;justify-content:center;
  margin:0 auto 20px;
}
.porque-icon-1{background:rgba(233,30,99,0.12);}
.porque-icon-2{background:rgba(255,152,0,0.12);}
.porque-icon-3{background:rgba(0,188,212,0.12);}
.porque-icon-4{background:rgba(233,30,99,0.12);}
.porque-card h3{
  font-family:'Inter Tight';font-size:18px;font-weight:700;
  margin-bottom:10px;line-height:1.3;
}
.porque-card p{color:var(--ink);font-size:14px;line-height:1.6;}
@media(max-width:1024px){.porque-cards{grid-template-columns:repeat(2,1fr);}}
@media(max-width:768px){.porque-cards{grid-template-columns:1fr;}}
```

- [ ] **Paso 2: Insertar la sección en index.html**

Localizar `<!-- CTA -->` en `index.html` e insertar **antes** de él:

```html
<!-- POR QUÉ HUM&NET -->
<section class="porque" id="porque">
  <div class="section-head" data-reveal>
    <div class="eyebrow">Por qué elegirnos</div>
    <h2>La diferencia que transforma organizaciones.</h2>
  </div>
  <div class="porque-cards">
    <div class="porque-card" data-reveal>
      <div class="porque-icon porque-icon-1">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#E91E63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>
      </div>
      <h3>30+ años transformando organizaciones</h3>
      <p>Décadas de experiencia comprobada en empresas mexicanas de todos los sectores.</p>
    </div>
    <div class="porque-card" data-reveal>
      <div class="porque-icon porque-icon-2">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#FF9800" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      </div>
      <h3>Partner Platinum CONTPAQi®</h3>
      <p>El nivel de certificación más alto — solo los mejores distribuidores en México lo tienen.</p>
    </div>
    <div class="porque-card" data-reveal>
      <div class="porque-icon porque-icon-3">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#00BCD4" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      </div>
      <h3>Socios, no solo proveedores</h3>
      <p>Implementamos, capacitamos y acompañamos a tu equipo en el largo plazo.</p>
    </div>
    <div class="porque-card" data-reveal>
      <div class="porque-icon porque-icon-4">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#E91E63" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      </div>
      <h3>Tecnología + desarrollo humano</h3>
      <p>Única firma en México que integra ERP con desarrollo organizacional en una sola propuesta.</p>
    </div>
  </div>
</section>
```

- [ ] **Paso 3: Agregar enlace "Por qué" en la nav** *(opcional pero recomendado)*

En `index.html`, dentro del `<nav class="nav-links">`, agregar después del enlace a `#nosotros`:

```html
<a href="#porque">¿Por qué?</a>
```

- [ ] **Paso 4: Verificar en navegador**

Recargar `http://localhost:4321` → antes del formulario de contacto debe aparecer una sección con 4 tarjetas en fila, cada una con ícono de color, título y descripción. Al hacer hover cada tarjeta debe elevarse ligeramente.

- [ ] **Paso 5: Commit**

```bash
git add index.html assets/css/styles.css
git commit -m "feat: add Por que Hum&Net section with 4 differentiator cards"
```

---

## Task 6: Form de contacto — mailto funcional

**Archivos:**
- Modificar: `assets/js/main.js` (agregar al final del IIFE, antes del cierre `}`)

- [ ] **Paso 1: Agregar lógica del form al final del IIFE en main.js**

En `assets/js/main.js`, localizar la línea `})();` al final del archivo y agregar **antes** de ella:

```javascript
  /* ---------- Contact form — mailto ---------- */
  var ctaForm = document.querySelector('.cta-form');
  if (ctaForm) {
    ctaForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var nameEl = ctaForm.querySelector('[aria-label="Nombre"]');
      var emailEl = ctaForm.querySelector('[aria-label="Correo electrónico"]');
      var name = nameEl ? nameEl.value.trim() : '';
      var email = emailEl ? emailEl.value.trim() : '';
      if (!name || !email) return;
      var subject = encodeURIComponent('Demo request — ' + name);
      var body = encodeURIComponent(
        'Nombre: ' + name + '\n' +
        'Email: ' + email + '\n\n' +
        'Me interesa agendar una demo de Hôlos ERP® / CONTPAQi®.'
      );
      window.location.href = 'mailto:ventas@humandnet.com?subject=' + subject + '&body=' + body;
    });
  }
```

- [ ] **Paso 2: Verificar comportamiento del form**

Abrir `http://localhost:4321` → ir a la sección de Contacto → llenar el campo "Tu nombre" y "tu@empresa.com" → hacer clic en "Agendar demo". Debe abrirse el cliente de correo predeterminado con:
- **Para:** `ventas@humandnet.com`
- **Asunto:** `Demo request — [nombre que escribiste]`
- **Cuerpo:** nombre, email y mensaje prellenados

Si no hay cliente de correo instalado, el navegador puede no abrir nada — es comportamiento esperado del `mailto:`.

- [ ] **Paso 3: Commit**

```bash
git add assets/js/main.js
git commit -m "feat: wire contact form to mailto with pre-filled subject and body"
```

---

## Verificación final

- [ ] Abrir `http://localhost:4321` y hacer scroll de arriba a abajo verificando:
  - [ ] Stats: 4 íconos SVG visibles sobre los números animados
  - [ ] Clientes: marquee desfilando, se pausa al hover
  - [ ] Servicios: tarjeta ancha "Soluciones Empresariales" arriba, 3 tarjetas iguales abajo con íconos
  - [ ] Hôlos ERP: badge cyan visible, 5 features con texto concreto
  - [ ] ¿Por qué Hum&Net?: 4 tarjetas con íconos de colores
  - [ ] Form de contacto: submit abre cliente de correo
  - [ ] Mobile (≤768px): todo se apila en columna, marquee sigue funcionando
- [ ] Commit final si hay ajustes menores pendientes:

```bash
git add -p
git commit -m "fix: final adjustments landing v2"
```
