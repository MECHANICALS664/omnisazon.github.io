# ✅ CHECKLIST PARA PONER ONLINE

Usa este checklist para asegurarte que todo está listo.

---

## 📋 PASO 0: VERIFICAR QUE TENGAS TODO

- [ ] Python instalado (`python --version`)
- [ ] Git instalado (`git --version`)
- [ ] Cuenta en GitHub (https://github.com)
- [ ] Proyecto en GitHub (`omnisazon` repository)

**Si no cumples con estos, primero:**
- Instala Python: https://python.org
- Instala Git: https://git-scm.com
- Crea GitHub account: https://github.com/signup

---

## ⚙️ PASO 1: PREPARAR CÓDIGO LOCAL

- [ ] Has leído `RESUMEN_PARA_TI.md` (2 minutos)
- [ ] Entiendes que config.js es la "llave mágica"
- [ ] Encontraste el archivo `config.js` en tu carpeta
- [ ] `app.py` está actualizado (con rutas de /api/pedidos)
- [ ] `mesero.html` tiene importados `config.js` y `api-sync.js`
- [ ] `cocinero.html` tiene importados `config.js` y `api-sync.js`

**Verificar con:**
```bash
# Desde terminal, en tu carpeta
cat config.js
cat api-sync.js
```

---

## 🔗 PASO 2: SUBIR A GITHUB

- [ ] Abrí terminal/PowerShell en mi carpeta del proyecto
- [ ] Ejecuté: `git init`
- [ ] Ejecuté: `git add .`
- [ ] Ejecuté: `git commit -m "Initial commit"`
- [ ] Ejecuté: `git remote add origin https://github.com/MI_USUARIO/omnisazon.git`
- [ ] Ejecuté: `git branch -M main`
- [ ] Ejecuté: `git push -u origin main`
- [ ] Verified en GitHub.com que mi código está ahí

**Verificar visitando:**
```
https://github.com/MI_USUARIO/omnisazon
```

---

## 🚀 PASO 3: DESPLEGAR EN RAILWAY

- [ ] Visité https://railway.app
- [ ] Creé cuenta con GitHub
- [ ] Hice clic en "Create New Project"
- [ ] Seleccioné "Deploy from GitHub repo"
- [ ] Escogí mi repositorio `omnisazon`
- [ ] Clickeé "Deploy"
- [ ] Esperé 2-5 minutos
- [ ] Vi el ✅ verde indicando deployment exitoso
- [ ] Copié la URL (ej: `https://omnisazon-prod-xxxxx.up.railway.app`)

**Verificar visitando la URL en el navegador y viendo:**
```json
{
  "message": "Backend de OmniSazón conectado ✅",
  "status": "online"
}
```

---

## ✏️ PASO 4: ACTUALIZAR config.js

- [ ] Abrí `config.js` en mi editor
- [ ] Encontré la línea con `'https://tu-backend-online.com'`
- [ ] Reemplacé con mi URL de Railway
- [ ] Guardé el archivo (Ctrl+S)
- [ ] Verifiqué que pone: `'https://omnisazon-prod-xxxxx.up.railway.app'`
- [ ] No tiene más el texto `tu-backend-online`

**El archivo debe verse:**
```javascript
const BACKEND_URL = isLocalhost 
    ? 'http://localhost:5000'
    : 'https://omnisazon-prod-xxxxx.up.railway.app';  // ← AQUÍ está tu URL real
```

---

## 📤 PASO 5: PUSH A GITHUB

- [ ] Abro terminal en mi carpeta
- [ ] Ejecuto: `git status` (veo que config.js tiene cambios)
- [ ] Ejecuto: `git add .`
- [ ] Ejecuto: `git commit -m "Update backend URL for production"`
- [ ] Ejecuto: `git push`
- [ ] Ver en GitHub que los cambios se subieron

**Verificar en:**
```
https://github.com/MI_USUARIO/omnisazon/blob/main/config.js
```

---

## 🔄 PASO 6: RAILWAY REDEPLOY AUTOMÁTICO

- [ ] Railway detecta cambios en GitHub
- [ ] Railway automáticamente inicia redeploy
- [ ] Veo el progress en Railway dashboard
- [ ] Espero 2-5 minutos
- [ ] Veo ✅ verde cuando termina

**Railway lo hace automáticamente, solo espera.**

---

## 🧪 PASO 7: PRUEBA FINAL

### 7.1 Verificar Backend

- [ ] Abro navegador
- [ ] Visito: `https://omnisazon-prod-xxxxx.up.railway.app/`
- [ ] Veo JSON con "Backend conectado ✅"
- [ ] ✅ Backend está online

### 7.2 Verificar Mesero (TELÉFONO)

- [ ] Abro navegador en teléfono
- [ ] Visito: `https://MI_USUARIO.github.io/omnisazon/mesero.html`
- [ ] Página carga correctamente
- [ ] Inicio sesión (mesero / 1234)
- [ ] Tomo un pedido (agrego items)
- [ ] Hago clic en "Enviar Pedido a Cocina"
- [ ] Abro F12 → Console
- [ ] Veo mensaje: `✅ Pedido sincronizado con backend`
- [ ] Cierto el mensaje de éxito en pantalla

### 7.3 Verificar Cocinero (PC)

- [ ] Abro navegador en PC
- [ ] Visito: `https://MI_USUARIO.github.io/omnisazon/cocinero.html`
- [ ] Página carga correctamente
- [ ] Inicio sesión (cocinero / 1234)
- [ ] Espero 1-2 segundos
- [ ] **VERPEDIDO ENVIADO DEL TELÉFONO** ✅✅✅
- [ ] Abro F12 → Console
- [ ] Veo: `📥 Pedidos actualizados desde backend: 1`
- [ ] El pedido muestra correctamente la mesa y los items

---

## 🎉 PASO 8: ¡LISTO!

Si completaste TODOS los pasos anteriores:

✅ Tu sistema está 100% online
✅ Funciona desde teléfono y PC simultáneamente
✅ Los pedidos se sincronizan en tiempo real
✅ El cocinero recibe los pedidos del mesero

**FELICIDADES!** 🚀🎉

---

## 🆘 TROUBLESHOOTING

Si algo no funciona, verifica en orden:

### "Backend no carga"
- [ ] ¿La URL es correcta? (revisar en Railway dashboard)
- [ ] ¿Pasaron 5+ minutos desde el deploy? (esperar más)
- [ ] ¿Status es ✅? (en Railway dashboard)

### "Pedido no llega al cocinero"
- [ ] ¿Frontend cargó bien? (check HTML loaded)
- [ ] ¿Abrí F12 en ambas ventanas? (verificar console)
- [ ] ¿config.js tiene URL correcta? (grep config.js)
- [ ] ¿Esperé 1-2 segundos? (no es instantáneo)

### "Error CORS"
- [ ] ¿app.py tiene CORS(app)? (line 8)
- [ ] ¿Backend está online? (visita base URL)
- [ ] ¿Esperé 5+ minutos? (redeploy puede tardar)

### "Error: config no está definido"
- [ ] ¿mesero.html tiene `<script src="config.js"></script>`?
- [ ] ¿Está ANTES de otros scripts?
- [ ] ¿Refrescaste la página? (F5 o Ctrl+Shift+R)

---

## 📊 RESUMEN RÁPIDO

| Paso | Acción | Tiempo |
|------|--------|--------|
| 0 | Verificar que tengas todo | 2 min |
| 1 | Verificar código local | 2 min |
| 2 | Git push a GitHub | 2 min |
| 3 | Desplegar en Railway | 5 min |
| 4 | Actualizar config.js | 2 min |
| 5 | Git push cambios | 2 min |
| 6 | Esperar redeploy | 5 min |
| 7 | Prueba final | 5 min |
| **TOTAL** | | **~27 min** |

---

## 💾 COMANDOS RÁPIDOS

Si necesitas copiar/pegar:

```bash
# Paso 2: Subir a GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/MI_USUARIO/omnisazon.git
git branch -M main
git push -u origin main

# Paso 5: Push después de editar config.js
git add .
git commit -m "Update backend URL"
git push
```

---

## 🎯 ÉXITO = TODOS LOS ✅

Si tienes todos los ✅ en esta página:

**¡Felicidades! Tu sistema está 100% online.** 🚀

---

**Última cosa:** Guarda esta página en bookmarks. La necesitarás cada vez que despliegues cambios en el futuro.
