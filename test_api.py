import urllib.request
import json

try:
    response = urllib.request.urlopen('http://localhost:5000/api/menu')
    data = json.loads(response.read().decode())
    print('✅ Servidor respondiendo correctamente')
    print(f'Platillos en BD: {len(data["data"])}')
    print('\nPrimeros platillos:')
    for platillo in data['data'][:3]:
        print(f"  - {platillo['nombre'].strip()}: ${platillo['precio']}")
except Exception as e:
    print(f'❌ Error: {e}')
