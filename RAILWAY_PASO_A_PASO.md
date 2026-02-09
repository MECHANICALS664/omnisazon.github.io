# 🚀 RAILWAY: Guía Paso a Paso (Para Completos Novatos)

Si nunca has usado Railway, esta es tu guía completa.

---

## Paso 1: Preparar Git (si no lo tienes)

Si nunca has usado Git, descarga e instala:
- Windows: https://git-scm.com/download/win
- Mac: `brew install git`
- Linux: `sudo apt install git`

---

## Paso 2: Preparar tu Proyecto en GitHub

### 2.1 Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre: `omnisazon` (o el que prefieras)
3. Descripción: "Sistema de restaurante"
4. **Public** (importante para GitHub Pages)
5. Click "Create repository"

### 2.2 Subir tu código a GitHub

En terminal/PowerShell, dentro de tu carpeta del proyecto:

```bash
# Inicializar Git
git init

# Agregar todos los archivos
git add .

# Hacer primer commit
git commit -m "Initial commit - OmniSazón online ready"

# Agregar remoto (reemplaza TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/omnisazon.git

# Cambiar rama a main
git branch -M main

# Subir a GitHub
git push -u origin main
```

**¿Qué significa todo esto?**
- `git init` - Inicializar el tracking de cambios
- `git add .` - Agregar todos los archivos
- `git commit` - Guardar un "punto de restauración"
- `git remote add` - Decirle a Git dónde está GitHub
- `git push` - Subir los cambios a GitHub

---

## Paso 3: Railway - Crear Cuenta

1. Ve a https://railway.app
2. Click "Get Started"
3. Click "Deploy now"
4. Elige "GitHub" para registrarse
5. Autoriza Railway a acceder a tu GitHub
6. ¡Listo! Estás registrado

---

## Paso 4: Railway - Crear Nuevo Proyecto

1. Ve a https://dashboard.railway.app
2. Click "Create New Project"
3. Click "Deploy from GitHub repo"
4. Selecciona tu repositorio `omnisazon`
5. Click "Deploy"
6. **Espera 2-5 minutos**

---

## Paso 5: Railway - Obtener la URL

1. Espera a que Railway termine el deploy (verás un ✅)
2. Click en tu deployment
3. Ve a la sección "Deployments"
4. Haz click en el deployment activo
5. Busca la URL en la parte superior (algo como):
   ```
   https://omnisazon-production-2abc.up.railway.app
   ```
6. **Copia esta URL**

---

## Paso 6: Actualizar config.js con la URL

1. Abre el archivo `config.js` en tu editor
2. Busca esta línea:
   ```javascript
   const BACKEND_URL = isLocalhost 
       ? 'http://localhost:5000'
       : 'https://tu-backend-online.com';  // ← Actualiza ESTA línea
   ```
3. Reemplaza `https://tu-backend-online.com` con tu URL de Railway:
   ```javascript
   const BACKEND_URL = isLocalhost 
       ? 'http://localhost:5000'
       : 'https://omnisazon-production-2abc.up.railway.app';
   ```
4. **Guarda el archivo** (Ctrl+S o Cmd+S)

---

## Paso 7: Subir los cambios a GitHub

En terminal/PowerShell:

```bash
# Ver qué cambios hay
git status

# Agregar todos los cambios
git add .

# Hacer commit
git commit -m "Update backend URL for production"

# Subir a GitHub
git push
```

---

## Paso 8: Railway se redesplegará Automáticamente

1. Ve a https://dashboard.railway.app
2. Railway verá que hay cambios en GitHub
3. Automáticamente empezará a redeploy
4. Espera a que se complete (2-5 minutos)
5. Verás un ✅ cuando termine

---

## Paso 9: Verificar que Funciona

### 9.1 Verificar Backend está Online

1. Abre la URL de Railway en el navegador:
   ```
   https://omnisazon-production-2abc.up.railway.app/
   ```
2. Deberías ver algo como:
   ```json
   {"message": "Backend de OmniSazón conectado ✅", "status": "online"}
   ```
3. ✅ Backend está online

### 9.2 Prueba Desde tu Teléfono

1. **Mesero (teléfono):**
   - Abre: `https://tu-usuario.github.io/omnisazon/mesero.html`
   - Inicia sesión: usuario = "mesero", contraseña = "1234"
   - Toma un pedido
   - Haz click en "Enviar Pedido a Cocina"
   - Abre F12 → Console
   - Deberías ver: `✅ Pedido sincronizado con backend`

2. **Cocinero (PC):**
   - Abre: `https://tu-usuario.github.io/omnisazon/cocinero.html`
   - Inicia sesión: usuario = "cocinero", contraseña = "1234"
   - Espera 1-2 segundos
   - **Deberías ver el pedido del teléfono** ✅

---

## 🆘 Si Algo no Funciona

### "No veo el backend URL en línea"

**Solución:**
1. Verifica que la URL sea correcta: `https://omnisazon-production-2abc.up.railway.app/`
2. Espera 2-3 minutos más (a veces tarda)
3. En Railway dashboard, verifica que el status sea ✅

### "El pedido no llega al cocinero"

**Solución:**
1. Abre F12 → Console en mesero.html
2. Busca el mensaje de error
3. Verifica que `config.js` tenga la URL correcta
4. Haz `git push` nuevamente:
   ```bash
   git add config.js
   git commit -m "Fix backend URL"
   git push
   ```
5. Espera a que Railway redeploy
6. Recarga la página

### "Veo error de CORS"

**Solución:**
- El error debería estar resuelto con el código nuevo
- Verifica que `app.py` tenga `CORS(app)` (está en las líneas 8-9)

### "Error en consola: 'BACKEND_URL is not defined'"

**Solución:**
1. Verifica que `config.js` esté siendo cargado
2. En mesero.html, revisa que tenga:
   ```html
   <script src="config.js"></script>
   ```
3. Antes del script que la usa

---

## 📋 Checklist

- [ ] GitHub cuenta creada
- [ ] Repositorio `omnisazon` creado en GitHub
- [ ] Código subido a GitHub (`git push`)
- [ ] Railway cuenta creada
- [ ] Proyecto creado en Railway
- [ ] Deploy completado (✅)
- [ ] URL de Railway copiada
- [ ] `config.js` actualizado con URL
- [ ] Cambios pusheados a GitHub (`git push`)
- [ ] Railway redesplegó automáticamente
- [ ] Backend URL en navegador muestra JSON ✅
- [ ] Mesero.html carga correctamente
- [ ] Cocinero.html carga correctamente
- [ ] Pedido enviado desde teléfono
- [ ] Pedido aparece en PC de cocinero ✅

---

## 🎉 ¡Listo!

Tu sistema está online. Ahora:

- ✅ Puedes tomar pedidos desde tu teléfono (o cualquier dispositivo)
- ✅ El cocinero los recibe en tiempo real en su PC
- ✅ Funciona desde cualquier lugar (no solo local)
- ✅ Múltiples dispositivos pueden conectarse simultáneamente

---

## 💡 Tips

1. **Bookmarks:** Guarda las URLs en bookmarks para acceso rápido:
   - Mesero: `https://tu-usuario.github.io/omnisazon/mesero.html`
   - Cocinero: `https://tu-usuario.github.io/omnisazon/cocinero.html`

2. **Local Development:** Puedes seguir usando `http://localhost:5000` en desarrollo:
   ```bash
   python app.py
   ```

3. **Cambios Futuros:** Cada vez que hagas cambios, solo necesitas:
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   git push
   ```
   Railway redesplegará automáticamente.

---

**¿Preguntas?** Revisa `DEPLOYMENT_GUIDE.md` para información más detallada.
