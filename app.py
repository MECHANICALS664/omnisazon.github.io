from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Almacenamiento en memoria para pedidos (en producción usar BD)
kitchen_orders = []
completed_orders = []

def get_db_connection():
    """Conectar a la base de datos SQLite"""
    conn = sqlite3.connect('tablademenu.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Backend de OmniSazón conectado ✅", "status": "online"})

@app.route('/api/menu', methods=['GET'])
def get_menu():
    """Obtener todos los platillos del menú"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM MENU')
        platillos = cursor.fetchall()
        conn.close()
        
        menu = []
        for platillo in platillos:
            menu.append({
                'id': platillo['ID'],
                'nombre': platillo['nombre'],
                'ingredientes': platillo['ingredientes'],
                'precio': platillo['precio']
            })
        
        return jsonify({"success": True, "data": menu})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/menu/<int:platillo_id>', methods=['GET'])
def get_platillo(platillo_id):
    """Obtener un platillo específico"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM MENU WHERE ID = ?', (platillo_id,))
        platillo = cursor.fetchone()
        conn.close()
        
        if not platillo:
            return jsonify({"success": False, "error": "Platillo no encontrado"}), 404
        
        return jsonify({"success": True, "data": {
            'id': platillo['ID'],
            'nombre': platillo['nombre'],
            'ingredientes': platillo['ingredientes'],
            'precio': platillo['precio']
        }})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==================== RUTAS DE PEDIDOS ====================

@app.route('/api/pedidos', methods=['POST'])
def crear_pedido():
    """Crear un nuevo pedido desde el mesero"""
    try:
        data = request.json
        
        # Validar datos básicos
        if not data or 'items' not in data:
            return jsonify({"success": False, "error": "Datos de pedido inválidos"}), 400
        
        # Agregar metadata
        data['created_at'] = datetime.now().isoformat()
        data['status'] = 'pendiente'
        
        # Guardar en memoria
        kitchen_orders.append(data)
        
        print(f"✅ Pedido recibido: Mesa {data.get('table')}, Items: {len(data['items'])}")
        
        return jsonify({
            "success": True, 
            "message": "Pedido recibido exitosamente",
            "order_id": data.get('id'),
            "data": data
        }), 201
    except Exception as e:
        print(f"❌ Error creando pedido: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/pedidos/cocina', methods=['GET'])
def get_kitchen_orders():
    """Obtener todos los pedidos pendientes de cocina"""
    try:
        # Filtrar solo pedidos pendientes
        pending_orders = [order for order in kitchen_orders if order.get('status') == 'pendiente']
        
        print(f"📋 Enviando {len(pending_orders)} pedidos pendientes a cocina")
        
        return jsonify({
            "success": True,
            "data": pending_orders,
            "total": len(pending_orders)
        })
    except Exception as e:
        print(f"❌ Error obteniendo pedidos: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/pedidos/<int:order_id>', methods=['PATCH'])
def update_order_status(order_id):
    """Actualizar estado de un pedido"""
    try:
        data = request.json
        new_status = data.get('status')
        
        if not new_status:
            return jsonify({"success": False, "error": "Estado no especificado"}), 400
        
        # Buscar el pedido
        for order in kitchen_orders:
            if order.get('id') == order_id:
                order['status'] = new_status
                order['updated_at'] = datetime.now().isoformat()
                
                # Si está completado, mover a completed_orders
                if new_status == 'completado':
                    completed_orders.append(order)
                
                print(f"✅ Pedido {order_id} actualizado a: {new_status}")
                
                return jsonify({
                    "success": True,
                    "message": f"Pedido actualizado a {new_status}",
                    "data": order
                })
        
        return jsonify({"success": False, "error": "Pedido no encontrado"}), 404
    except Exception as e:
        print(f"❌ Error actualizando pedido: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/pedidos/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Eliminar un pedido"""
    try:
        global kitchen_orders
        
        # Filtrar el pedido a eliminar
        initial_length = len(kitchen_orders)
        kitchen_orders = [order for order in kitchen_orders if order.get('id') != order_id]
        
        if len(kitchen_orders) < initial_length:
            print(f"✅ Pedido {order_id} eliminado")
            return jsonify({"success": True, "message": "Pedido eliminado"})
        else:
            return jsonify({"success": False, "error": "Pedido no encontrado"}), 404
    except Exception as e:
        print(f"❌ Error eliminando pedido: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/pedidos/stats/resumen', methods=['GET'])
def get_stats():
    """Obtener estadísticas de pedidos"""
    try:
        return jsonify({
            "success": True,
            "pending": len([o for o in kitchen_orders if o.get('status') == 'pendiente']),
            "in_progress": len([o for o in kitchen_orders if o.get('status') == 'en_progreso']),
            "completed": len(completed_orders),
            "total_orders": len(kitchen_orders) + len(completed_orders)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    print("🍽️ Servidor OmniSazón iniciando...")
    print("📍 Escuchando en http://localhost:5000")
    print("ℹ️  Presiona CTRL+C para detener")
    app.run(debug=True, port=5000, host='0.0.0.0')
