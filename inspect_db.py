import sqlite3
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()
print(cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
for tbl in ['employees', 'orderDetails', 'orders']:
    print('---', tbl, '---')
    try:
        rows = cur.execute(f'SELECT * FROM {tbl} LIMIT 3').fetchall()
        print(rows)
        print([c[1] for c in cur.execute(f'PRAGMA table_info({tbl})').fetchall()])
    except Exception as e:
        print('ERR', e)
conn.close()
