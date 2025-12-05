import sqlite3
import json

conn = sqlite3.connect('tablademenu.db')
cursor = conn.cursor()

# Obtener tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [table[0] for table in cursor.fetchall()]
print("Tablas:", tables)

# Obtener estructura de cada tabla
for table in tables:
    cursor.execute(f"PRAGMA table_info({table});")
    columns = cursor.fetchall()
    print(f"\nTabla: {table}")
    print("Columnas:")
    for col in columns:
        print(f"  - {col[1]} ({col[2]})")
    
    # Mostrar algunos registros
    cursor.execute(f"SELECT * FROM {table} LIMIT 3;")
    rows = cursor.fetchall()
    print(f"Registros (muestra): {rows}")

conn.close()
