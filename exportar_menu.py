#!/usr/bin/env python3
"""Exportar tabla de platillos desde SQLite a frontend/menu.json

Uso:
  python exportar_menu.py [--db PATH] [--table NAME]

Si no se especifica --db, intenta 'tablamenu.db' y 'tablademenu.db'.
Si no se especifica --table, el script intentará detectar una tabla con nombre
relacionado a 'menu' o 'platill' y, si no la encuentra, usará la primera tabla.
"""
from pathlib import Path
import sqlite3
import json
import argparse
import sys


DEFAULT_DBS = ["tablamenu.db", "tablademenu.db"]
OUT_PATH = Path(__file__).parent / 'frontend' / 'menu.json'


def find_db(path_arg: str = None):
    if path_arg:
        p = Path(path_arg)
        if p.exists():
            return p
        raise FileNotFoundError(f"DB not found: {p}")
    for name in DEFAULT_DBS:
        p = Path(name)
        if p.exists():
            return p
    raise FileNotFoundError("No SQLite DB found. Searched: %s" % ", ".join(DEFAULT_DBS))


def choose_table(conn, table_arg: str = None):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [r[0] for r in cur.fetchall()]
    if not tables:
        raise RuntimeError('No tables found in DB')
    if table_arg:
        if table_arg in tables:
            return table_arg
        raise RuntimeError(f"Table '{table_arg}' not found in DB")

    # Prefer tables with 'menu' or 'platill' in name
    for t in tables:
        tn = t.lower()
        if 'menu' in tn or 'platill' in tn or 'platillo' in tn or 'platillos' in tn:
            return t

    # fallback to first table
    return tables[0]


def export_table(db_path: Path, table: str):
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info('{table}')")
    cols = [r['name'] if isinstance(r, sqlite3.Row) else r[1] for r in cur.fetchall()]

    # case-insensitive mapping
    lower_map = {c.lower(): c for c in cols}
    name_col = lower_map.get('nombre') or lower_map.get('name') or None
    price_col = lower_map.get('precio') or lower_map.get('price') or lower_map.get('precio_unit') or None
    desc_col = lower_map.get('descripcion') or lower_map.get('descripcion') or lower_map.get('desc') or lower_map.get('description') or None

    # If some columns are missing, we will still export but with defaults
    cur.execute(f"SELECT * FROM '{table}'")
    rows = cur.fetchall()
    out = []
    for r in rows:
        # r is sqlite3.Row, supports mapping access by column name
        nombre = r[name_col] if name_col and name_col in r.keys() else ''
        precio = r[price_col] if price_col and price_col in r.keys() else 0
        descripcion = r[desc_col] if desc_col and desc_col in r.keys() else ''
        # Normalize types
        try:
            precio = float(precio) if precio is not None else 0
        except Exception:
            precio = 0
        out.append({
            'nombre': str(nombre).strip(),
            'precio': precio,
            'descripcion': str(descripcion).strip()
        })
    conn.close()
    return out


def write_json(data, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Exportar tabla de platillos a frontend/menu.json')
    parser.add_argument('--db', '-d', help='Ruta al archivo SQLite (.db)')
    parser.add_argument('--table', '-t', help='Nombre de la tabla a exportar')
    args = parser.parse_args()

    try:
        dbp = find_db(args.db)
    except FileNotFoundError as e:
        print('❌', e)
        sys.exit(1)

    try:
        conn = sqlite3.connect(str(dbp))
        table = choose_table(conn, args.table)
        conn.close()
    except Exception as e:
        print('❌', e)
        sys.exit(1)

    try:
        data = export_table(dbp, table)
        write_json(data, OUT_PATH)
        print(f"✅ Exported {len(data)} items from table '{table}' in {dbp} -> {OUT_PATH}")
    except Exception as e:
        print('❌ Error exporting:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
