import sqlite3

#подключения в базы данных
connection= sqlite3.connect('my_users.db')

#переводчик с sql на pyton
sql=connection.cursor()

#создания таблицы
sql.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER, user_name TEXT);')

# добавит данные на таблицу
# sql.execute('INSERT INTO users(user_id, user_name) VALUES (1,"Pavel");')
# sql.execute('INSERT INTO users(user_id, user_name) VALUES (2,"Sasha");')

#фиксируем изменения
connection.commit()

#запрос с филтрасии
print(sql.execute('SELECT * FROM users WHERE user_id=5;').fetchall())

#удалит данные
# sql.execute('DELETE FROM users WHERE user_name="Pavel";')
connection.commit()
print(sql.execute('SELECT * FROM users;').fetchall())

sql.execute('UPDATE users SET user_name="URG" WHERE user_id=1;')
sql.execute('UPDATE users SET user_id=5 WHERE user_name="URG";')
sql.execute('UPDATE users SET user_name="URG" WHERE user_id=1;')
sql.execute('UPDATE users SET user_name="jack", user_id=3 WHERE user_id=2;')

connection.commit()

print(sql.execute('SELECT * FROM users;').fetchall())
