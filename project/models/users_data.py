import sqlite3
db = sqlite3.connect('users.db')
db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email CHAR(100) NOT NULL, password CHAR(100), cpf CHAR(30), created DATETIME DEFAULT CURRENT_TIMESTAMP)")
db.execute("INSERT INTO users (email,password, cpf) VALUES ('teste@teste.com', '123', '12342434242')")
db.commit()