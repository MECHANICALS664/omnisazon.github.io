# 🍽️ OmniSazón - Sistema de Restaurante

## 📋 Descripción General

Sistema completo para gestionar un restaurante mexicano con:
- **Frontend**: HTML, CSS, JavaScript (roles: Admin, Cocinero, Mesero)
- **Backend**: Flask + SQLite
- **Base de Datos**: SQLite con tabla de menú

---

## 🗂️ Estructura del Proyecto

```
restaurante/
├── frontend/
│   ├── index.html          # Login
│   ├── dashboard.html      # Panel principal
│   ├── mesero.html         # Tomar pedidos (conectado a BD)
│   ├── cocinero.html       # Ver pedidos de cocina
│   ├── admin.html          # Panel de administrador
│   ├── style.css           # Estilos compartidos
│   └── cargar-menu.js      # Script para cargar menú desde BD
├── app.py                  # Backend Flask
├── tablademenu.db          # Base de datos SQLite
├── requirements.txt        # Dependencias Python
└── README.md               # Este archivo
```

---

## 🚀 Cómo Ejecutar

### 1. Instalar Dependencias (Primera vez)

```bash
cd "c:\Users\mecha\OneDrive\Desktop\my project\restaurante"
python -m pip install -r requirements.txt
```

### 2. Iniciar el Servidor Backend

```bash
python app.py
```

El servidor estará disponible en: **http://localhost:5000**

### 3. Abrir el Frontend

Abre `frontend/index.html` en tu navegador.

---

## 👤 Credenciales de Prueba

Usa cualquier usuario con estos roles:

- **Admin**: Usuario: `admin` | Contraseña: `1234` | Rol: Admin
- **Mesero**: Usuario: `mesero` | Contraseña: `1234` | Rol: Mesero
- **Cocinero**: Usuario: `cocinero` | Contraseña: `1234` | Rol: Cocinero

---

## 📱 Funcionalidades

### Mesero (mesero.html)
✅ Ver menú desde la **Base de Datos SQLite**
✅ Agregar platillos al carrito
✅ Especificar cantidad de porciones
✅ Ver total del pedido
✅ Enviar pedido a cocina
✅ Iniciar nuevo pedido o agregar más items

### Cocinero (cocinero.html)
👀 Ver pedidos pendientes de cocina
✅ Marcar como completados

### Admin (admin.html)
📊 Panel de administración
📈 Estadísticas del restaurante

---

## 📊 Base de Datos

### Tabla: MENU

| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID | INTEGER | ID único del platillo |
| nombre | TEXT | Nombre del platillo |
| ingredientes | TEXT | Lista de ingredientes |
| precio | REAL | Precio en pesos |

### Platillos Actuales en la BD:
- Torta Ahogada ($89.99)
- Quesadilla ($60.34)
- Tacos al Pastor ($90.00)
- *... y más*

---

## 🔌 Endpoints API

### GET `/api/menu`
Obtiene todos los platillos del menú desde SQLite

**Respuesta:**
```json
{
  "success": true,
  "data": [
    {
      "id": 11092006,
      "nombre": "torta ahogada",
      "ingredientes": "carne, jamon, cebolla, aguacate, mayonesa, caldo",
      "precio": 89.99
    }
  ]
}
```

### GET `/api/menu/<id>`
Obtiene un platillo específico por ID

### POST `/api/pedidos`
Recibe un nuevo pedido desde el mesero

---

## 🛠️ Solución de Problemas

### El backend no se conecta
1. Verifica que el servidor esté corriendo: `python app.py`
2. Abre http://localhost:5000 en el navegador
3. Deberías ver: `{"message": "Backend de OmniSazón conectado ✅"}`

### El menú no carga
1. Verifica que `tablademenu.db` esté en la carpeta raíz
2. Abre la consola del navegador (F12) y busca errores
3. Verifica que el backend está respondiendo en `/api/menu`

### Puerto 5000 ocupado
Cambia el puerto en `app.py`:
```python
app.run(debug=True, port=8000)  # Cambia a 8000
```

Y actualiza la URL en `cargar-menu.js`:
```javascript
const BACKEND_URL = 'http://localhost:8000';
```

---

## 📝 Notas Importantes

- El carrito se guarda en `localStorage` del navegador
- Los pedidos se envían a cocina también vía `localStorage` (puedes cambiar a BD)
- SQLite no requiere servidor adicional de BD (está todo integrado)
- El CORS está habilitado para que frontend y backend se comuniquen

---

## 🔐 Seguridad Futura (Recomendaciones)

- [ ] Agregar autenticación real (JWT)
- [ ] Validar permisos en el backend
- [ ] Encriptar contraseñas
- [ ] Guardar pedidos en base de datos (no en localStorage)
- [ ] Añadir HTTPS en producción

---

## 📞 Soporte

Si tienes problemas:
1. Revisa la consola del navegador (F12)
2. Verifica que el servidor backend esté ejecutándose
3. Asegúrate que `tablademenu.db` existe en la carpeta del proyecto

---

**¡Bienvenido a OmniSazón! 🍽️🌮**
