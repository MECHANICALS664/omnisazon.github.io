# ⚡ INSTRUCCIONES RÁPIDAS - Ejecutar Online

## El Problema Original
Tu sistema solo funcionaba localmente porque:
- El frontend (HTML/JS) estaba en GitHub Pages
- El backend (Flask) corría solo en tu PC (`localhost:5000`)
- Los pedidos se guardaban en `localStorage` (no se sincronizaban entre dispositivos)

## La Solución Implementada

Se han agregado 3 archivos principales:

1. **`config.js`** - Detecta automáticamente localhost vs producción
2. **`api-sync.js`** - Sincroniza pedidos en tiempo real entre dispositivos
3. **`app.py` actualizado** - Ahora acepta y distribuye pedidos correctamente

## Pasos para Poner Online

### 1️⃣ Elije una plataforma de hosting (elige UNA):

| Plataforma | Precio | Facilidad | Tiempo Deploy |
|-----------|--------|----------|---------------|
| Railway   | GRATIS | ⭐⭐⭐   | 2-5 min      |
| Render    | GRATIS | ⭐⭐⭐   | 2-5 min      |
| Heroku    | $7/mes | ⭐⭐⭐⭐  | 1-2 min      |

**Recomendación: Usa Railway (es gratis y muy fácil)**

---

### 2️⃣ Desplegar Backend en Railway (5 minutos)

```bash
# En tu terminal, en la carpeta del proyecto:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USUARIO/omnisazon.git
git push -u origin main
```

Luego:
1. Ve a https://railway.app
2. Regístrate con GitHub
3. Crea nuevo proyecto → Deploy from GitHub
4. Selecciona `omnisazon`
5. Railway desplegará automáticamente
6. Espera 2-5 minutos
7. Ve a tu dashboard y copia la URL (algo como `https://omnisazon-prod-xxxxx.up.railway.app`)

---

### 3️⃣ Actualizar `config.js` con tu URL

Abre `config.js` y cambia:

```javascript
const BACKEND_URL = isLocalhost 
    ? 'http://localhost:5000'
    : 'https://omnisazon-prod-xxxxx.up.railway.app';  // ← Actualiza esto
```

Luego:
```bash
git add config.js
git commit -m "Update backend URL"
git push
```

---

### 4️⃣ Prueba desde tu teléfono

1. **Mesero (teléfono):**
   - Abre: `https://tu-usuario.github.io/omnisazon.github.io-main/mesero.html`
   - Inicia sesión como "mesero"
   - Toma un pedido
   - Haz clic en "Enviar Pedido a Cocina"

2. **Cocinero (PC):**
   - Abre: `https://tu-usuario.github.io/omnisazon.github.io-main/cocinero.html`
   - Inicia sesión como "cocinero"
   - **Deberías VER EL PEDIDO del teléfono** ✅

---

## 🔍 Verificar que Funciona

Abre F12 (Developer Tools) en ambos navegadores:

**Mesero:**
- Deberías ver en la consola: `✅ Pedido sincronizado con backend`

**Cocinero:**
- Deberías ver: `📥 Pedidos actualizados desde backend: 1`

---

## 🆘 Si Algo No Funciona

### "No me aparece el pedido en la cocina"

1. Verifica que `config.js` tenga la URL correcta
2. Abre F12 → Network → busca requests a `/api/pedidos`
3. Refresca la página de cocinero

### "Error de CORS"

Railway ya tiene CORS configurado en `app.py`, así que no debería haber problema.

### "Backend no está online"

Ve a tu dashboard de Railway y verifica que el deployment esté activo (verde).

---

## 📱 Flujo Completo

```
Teléfono (Mesero)          PC (Cocinero)
    │                           │
    │ Toma pedido               │
    │ Envía a Backend ─────────→ Backend
    │                           │
    │                    ←────── Backend
    │                     Sincroniza c/1s
    │                           │
    │                      Ve el pedido ✅
    │                           │
    │ ←──────────────────── Marca completado
    │
```

---

## ✅ Checklist Final

- [ ] Proyecto en GitHub
- [ ] Backend desplegado en Railway/Render
- [ ] `config.js` actualizado con URL correcta
- [ ] Cambios pusheados a GitHub
- [ ] Mesero.html carga desde teléfono
- [ ] Cocinero.html carga desde PC
- [ ] Pedido aparece en cocina cuando lo envías
- [ ] Status se actualiza cuando marcas como completado

**¡Listo! 🎉 Tu sistema está online y funciona desde cualquier dispositivo.**

---

## 📚 Documentación Completa

Lee `DEPLOYMENT_GUIDE.md` para instrucciones más detalladas y troubleshooting.
