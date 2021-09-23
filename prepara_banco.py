import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', password='password', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE `jogoteca`;")
# conn.commit()
# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO emails.usuarios (id, nome, password) VALUES (%s, %s, %s)',
      [
            ('kaleu', 'Kaleu Melo', 'adm2020'),
            ('mariana', 'Mariana Branco', 'adm2323'),
            ('ewaldo', 'Ewaldo Bezerra', 'adm1919')
      ])

cursor.execute('select * from emails.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo logins
cursor.executemany(
      'INSERT INTO emails.logins (nome, email, senha) VALUES (%s, %s, %s)',
      [
            ('Kaleu Melo', 'kaleu_mt@hotmail.com', 'adm123'),
            ('Kelen Melo', 'ye_melo@hotmail.com', 'adm123'),
            ('Kalene Melo', 'kalene_melo13@hotmail.com', 'adm123')
      ])

cursor.execute('select * from emails.logins')
print(' -------------  Logins:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()