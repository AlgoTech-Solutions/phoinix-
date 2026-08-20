import sqlite3

conn = sqlite3.connect('data/phoenix.db')
conn.execute('UPDATE videos SET script_json = "{}" WHERE script_json = ""')
conn.commit()

print('FIXED DB')
