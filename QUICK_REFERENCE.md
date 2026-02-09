# 🚀 QUICK REFERENCE - Pega esto en bookmarks

## En 30 segundos: ¿Qué tengo que hacer?

1. **Desplegar backend en Railway:**
   - Ve a https://railway.app
   - Conecta GitHub
   - Deploy from repo
   - Copia URL que te da

2. **Edita config.js:**
   - Reemplaza `'https://tu-backend-online.com'` con tu URL de Railway
   - Guarda

3. **Git push:**
   ```bash
   git add .
   git commit -m "Online"
   git push
   ```

4. **Prueba:**
   - Teléfono: mesero.html
   - PC: cocinero.html
   - ¿Aparece el pedido? ✅

---

## URLs

```
Frontend Mesero:
https://tu-usuario.github.io/omnisazon/mesero.html

Frontend Cocinero:
https://tu-usuario.github.io/omnisazon/cocinero.html

Backend (después de desplegar):
https://omnisazon-prod-xxxxx.up.railway.app/
```

---

## Archivos Importantes

| Archivo | Para qué |
|---------|----------|
| config.js | URL del backend (CAMBIAR ESTO) |
| api-sync.js | Sincronización (NO tocar) |
| app.py | Backend (NO tocar) |
| mesero.html | Frontend mesero (ya actualizado) |
| cocinero.html | Frontend cocinero (ya actualizado) |

---

## Logs Esperados (F12 Console)

**Mesero al enviar:**
```
✅ Pedido sincronizado con backend
```

**Cocinero esperando:**
```
📥 Pedidos actualizados desde backend: 1
```

---

## Cambios Principales

✅ Backend ahora acepta pedidos remotos
✅ Mesero envía vía HTTP (no localStorage)
✅ Cocinero recibe vía HTTP (sincronización automática)
✅ Fallback a localStorage si falla internet

---

## Comando TODO en Uno (si sabes git)

```bash
git add . && git commit -m "Deploy" && git push
```

---

## Troubleshooting Ultra-Rápido

| Problema | Solución |
|----------|----------|
| No funciona | Esperá 5 min más |
| Backend offline | Verifica Railway dashboard |
| URL incorrecta | Edita config.js nuevamente |
| No sincroniza | F12 → Console → busca errores |
| CORS error | Espera redeploy de Railway |

---

## Docs Completos

- `RESUMEN_PARA_TI.md` - Lee primero
- `QUICK_START.md` - 5 minutos
- `RAILWAY_PASO_A_PASO.md` - Detallado
- `CHECKLIST_DEPLOYMENT.md` - Paso a paso
- `CAMBIOS_REALIZADOS.md` - Técnico

---

**Guardá esto en bookmarks para futuras deployments!** 📌
