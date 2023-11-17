import sqlite3


class Database:
	def __init__(self, name):
		self.name = name
		self.conn = sqlite3.connect(self.name)
		self.cursor = self.conn.cursor()

		if not self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'").fetchone():
			self.cursor.execute("CREATE TABLE users (email TEXT, name TEXT)")
	
	def create_user(self, email, name):
		if self.cursor.execute(f"SELECT name FROM users WHERE email='{email}'").fetchone() is None:
			self.cursor.execute(f"INSERT INTO users VALUES ('{email}', '{name}')")
		elif self.cursor.execute(f"SELECT name FROM users WHERE email='{email}'").fetchone() == "":
			self.cursor.execute(f"UPDATE users SET name='{name}' WHERE email='{email}'")
		self.conn.commit()
	
	def get_user_name(self, email):
		self.cursor.execute(f"SELECT name FROM users WHERE email='{email}'")
		name = self.cursor.fetchone()
		if name == None:
			name = ""
		else:
			name = name[0]
		return name
	
	def create_template(self, name, template):
		self.cursor.execute(f"INSERT INTO templates VALUES ('{name}', '{template}')")
		self.conn.commit()
	
	def get_templates(self):
		self.cursor.execute(f"SELECT template FROM templates")
		templates = self.cursor.fetchall()
		return templates
	
	def get_name_on_template(self, template):
		self.cursor.execute(f"SELECT name FROM templates WHERE template='{template}'")
		name = self.cursor.fetchone()[0]
		return name