from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    """Conectar a la base de datos SQLite"""
    conn = sqlite3.connect('tablademenu.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Backend de OmniSazón conectado ✅"})

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

@app.route('/api/pedidos', methods=['POST'])
def crear_pedido():
    """Crear un nuevo pedido"""
    try:
        data = request.json
        # Aquí puedes guardar el pedido en BD si lo deseas
        return jsonify({"success": True, "message": "Pedido recibido", "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    print("🍽️ Servidor OmniSazón iniciando...")
    app.run(debug=True, port=5000)
