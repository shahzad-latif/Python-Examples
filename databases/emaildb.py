import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM counts WHERE email=?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts (email, count) VALUES ( ? , 1)', (email,))
    else: 
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

conn.commit()

rows = conn.execute('SELECT email, count FROM counts ORDER BY count DESC LIMIT 10')

for row in rows:
    print(str(row[0]), row[1])
