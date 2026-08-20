import sqlite3
import shutil
from pathlib import Path

conn = sqlite3.connect('data/phoenix.db')
conn.execute('UPDATE videos SET script_json = "", status = "created" WHERE id = 11')
conn.commit()

p = Path('data/output/v11_work')
if p.exists():
    shutil.rmtree(p)

print('CLEARED V11 CACHE')
