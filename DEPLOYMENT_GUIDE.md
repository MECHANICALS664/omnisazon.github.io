# 🍽️ OmniSazón - Guía de Despliegue Online

Este documento explica cómo desplegar OmniSazón en línea para que funcione desde cualquier dispositivo (teléfono, PC, tablet).

## 📋 Cambios Realizados para Funcionar Online

Se han implementado los siguientes cambios para que el sistema funcione en línea:

### 1. **Configuración Centralizada** (`config.js`)
- Detecta automáticamente si estás en desarrollo (localhost) o producción
- Centraliza la URL del backend en un solo lugar
- Facilita cambiar entre ambientes

### 2. **Sincronización de Pedidos** (`api-sync.js`)
- Nueva clase `OrderSync` que maneja comunicación con backend
- Envía pedidos desde mesero al backend en tiempo real
- El cocinero recibe actualizaciones automáticas cada segundo
- Fallback a localStorage si no hay conexión (offline-first)

### 3. **Backend Mejorado** (`app.py`)
- Ahora guarda pedidos en memoria
- Ruta `/api/pedidos` para crear pedidos (POST)
- Ruta `/api/pedidos/cocina` para obtener pedidos pendientes (GET)
- Ruta `/api/pedidos/<id>` para actualizar estado (PATCH)
- CORS habilitado para acceso desde cualquier dominio

### 4. **Frontend Actualizado**
- `mesero.html`: Envía pedidos al backend cuando hace clic en "Enviar a Cocina"
- `cocinero.html`: Sincroniza automáticamente con backend cada 1 segundo

---

## 🚀 Pasos para Desplegar

### **Opción A: Usar Railway (Recomendado - GRATIS)**

Railway ofrece hosting gratis para aplicaciones Flask y es muy fácil de usar.

#### Paso 1: Crear cuenta en Railway
1. Ve a https://railway.app
2. Haz clic en "Get Started"
3. Regístrate con GitHub o email

#### Paso 2: Preparar el proyecto
1. Sube tu proyecto a GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/tu-usuario/omnisazon.git
   git push -u origin main
   ```

#### Paso 3: Desplegar en Railway
1. En Railway, haz clic en "Create New Project"
2. Selecciona "Deploy from GitHub"
3. Elige tu repositorio `omnisazon`
4. Railway detectará automáticamente que es un proyecto Python
5. Espera a que se despliegue (2-5 minutos)

#### Paso 4: Obtener la URL
1. Ve a "Deployments"
2. Haz clic en tu deployment
3. Busca la URL (algo como `https://omnisazon-production-xxxx.up.railway.app`)

#### Paso 5: Actualizar config.js
```javascript
const BACKEND_URL = isLocalhost 
    ? 'http://localhost:5000'
    : 'https://omnisazon-production-xxxx.up.railway.app';  // 👈 Usa tu URL de Railway
```

#### Paso 6: Commit y push
```bash
git add config.js
git commit -m "Update backend URL for production"
git push
```

Railway redesplegará automáticamente.

---

### **Opción B: Usar Render (GRATIS)**

1. Ve a https://render.com
2. Regístrate
3. Crea un nuevo "Web Service"
4. Conecta tu GitHub
5. Espera a que se despliegue
6. Copia la URL y actualiza `config.js`

---

### **Opción C: Usar Heroku (PAGO - $7/mes)**

Heroku descontinuó su plan gratuito, pero sigue siendo una opción.

---

## 📱 Cómo Usar Desde Tu Teléfono

Una vez desplegado en línea:

1. **Mesero (teléfono):**
   - Abre: `https://tu-github-pages.com/mesero.html`
   - Inicia sesión como "mesero"
   - Toma pedidos normalmente
   - Cuando hagas clic en "Enviar Pedido a Cocina", se enviará al backend

2. **Cocinero (PC):**
   - Abre: `https://tu-github-pages.com/cocinero.html`
   - Inicia sesión como "cocinero"
   - Los pedidos aparecerán automáticamente (se sincroniza cada 1 segundo)
   - Marca los pedidos como completados

---

## 🔧 Verificar que Todo Funciona

### En la consola del navegador (F12 → Console):

**Mesero:**
- Deberías ver logs como `📤 Enviando pedido al backend...`
- Luego `✅ Pedido sincronizado con backend`

**Cocinero:**
- Deberías ver `🔄 Iniciando sincronización automática...`
- Luego `📥 Pedidos actualizados desde backend: X`

### Si algo falla:

1. Verifica que `config.js` tenga la URL correcta del backend
2. Abre las Developer Tools (F12) → Network → verifica requests a `/api/pedidos`
3. Comprueba que el backend esté en línea: visita `https://tu-backend.com/` en el navegador

---

## 🛠️ Configuración de Variables de Entorno (Opcional)

Si usas Railway/Render, puedes agregar variables de entorno:

En Railway:
1. Ve a tu proyecto
2. Variables → Add Variable
3. Nombre: `FLASK_ENV`, Valor: `production`

---

## 📊 Troubleshooting

### "No se conecta al backend"
- Verifica que la URL en `config.js` sea correcta
- Comprueba que el backend esté en línea
- Abre la consola del navegador (F12) para ver errores

### "Los pedidos no llegan al cocinero"
- Recarga la página de cocinero
- Verifica que ambos estén accediendo por la misma URL del backend
- Mira en Network → XHR requests si se envían correctamente

### "Funciona local pero no online"
- Asegúrate de haber actualizado `config.js` con la URL correcta
- Haz commit y push de los cambios
- Espera a que GitHub Pages se redepliegue (1-2 minutos)

---

## 📝 Archivos Importantes

- `config.js` - Configuración de URL del backend
- `api-sync.js` - Lógica de sincronización
- `app.py` - Backend Flask
- `mesero.html` - Frontend para mesero
- `cocinero.html` - Frontend para cocinero

---

## ✅ Checklist de Despliegue

- [ ] Proyecto subido a GitHub
- [ ] Backend desplegado en Railway/Render/Heroku
- [ ] URL del backend actualizada en `config.js`
- [ ] Cambios commitados y pusheados
- [ ] GitHub Pages está habilitado (Settings → Pages)
- [ ] Ambas páginas cargan correctamente
- [ ] Puedes tomar un pedido en mesero.html
- [ ] El pedido aparece en cocinero.html

---

¡Listo! Tu sistema OmniSazón ahora funciona en línea desde cualquier dispositivo. 🎉
