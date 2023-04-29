import mysql.connector
from mysql.connector import Error


class RecordNotFoundError(Exception):
	pass


class DB_operations:
	def get_connection(self):
		connection = mysql.connector.connect(
			host='localhost',
			user='root',
			password='Manjusha@17',
			port='3306',
			database='manjushadb'
		)
		return connection

	def create_table(self):
		query = '''
			create table students(id int primary key auto_increment, name varchar(50) not null,
			semester int, branch varchar(50), phone_num varchar(10) unique);
		'''
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(query)
			print('Table created successfully')
		except:
			print('Error while creating table')
		finally:
			db_cursor.close()
			connection.close()

	def insert_fixed_row(self):
		query = '''
			insert into students(name, semester, branch, phone_num) values('Pranav', 5, 'Comp-Sc', 
			9080706050);
		'''
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(query)
			print('Successfully inserted a row')
		except:
			print('Error while inserting row into the table')
		finally:
			db_cursor.close()
			connection.close()

	def insert_rows(self):
		query = '''
			INSERT INTO students (name, semester, branch, phone_num) VALUES (%s, %s, %s, %s);
		'''
		data = [
			('Bhesshm', 7, 'Mech', 9099909999),
			('Dron', 7, 'Mech', 9990999099),
			('Krip', 6, 'EEE', 9999009999)
		]
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.executemany(query, data)
			connection.commit()
			print('Successfully inserted multiple rows')
		except:
			print('Error while inserting row into the table')
		finally:
			db_cursor.close()
			connection.close()

	def insert_dynamic_row(self, name, semester, branch, phone_num):
		insert_student = ("insert into students "
				 "(name, semester, branch, phone_num) "
				 "values (%s, %s, %s, %s)")
		data_student = (name, semester, branch, phone_num)
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(insert_student, data_student)
			connection.commit()
			print('Successfully inserted a row')
		except:
			print('Error while inserting row into the table')
		finally:
			db_cursor.close()
			connection.close()

	def read_all_rows(self):
		query = '''	select * from students; '''
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(query)
			records = db_cursor.fetchall()
			print('%-3s %-12s %-3s %-6s %-10s'%('ID', 'NAME', 'SEM', 'BRANCH', 'PHONE_NUM'))
			for r in records:
				print('%-3s %-12s %-3s %-6s %-10s' % (r[0], r[1], r[2], r[3], r[4]))
			print('Successfully retrieved all rows')
		except(Exception, Error) as error:
			print(error)
		finally:
			if connection is not None:
				db_cursor.close()
				connection.close()

	def read_row_by_id(self, *id):
		query = '''	select * from students where id = %s; '''
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(query, id)
			rec = db_cursor.fetchone()
			if rec is None:
				raise RecordNotFoundError
			print('%-3s %-12s %-3s %-6s %-10s' % ('ID', 'NAME', 'SEM', 'BRANCH', 'PHONE_NUM'))
			print('%-3s %-12s %-3s %-6s %-10s' % (rec[0], rec[1], rec[2], rec[3], rec[4]))
			print('Successfully retrieved the target row')
		except(Exception, Error) as error:
			print(error)
		except RecordNotFoundError:
			print('Student with id = {} not found'.format(id[0]))
		finally:
			if connection is not None:
				db_cursor.close()
				connection.close()
		return rec

	def update_row_by_id(self, *data):
		query = '''	update students set phone_num = %s where id = %s ; '''
		try:
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(query, data)
			connection.commit()
			print('Successfully Updated the Phone Number')
			print(db_cursor.rowcount, "record(s) affected")
		except(Exception, Error) as error:
			print(error)
		finally:
			if connection is not None:
				db_cursor.close()
				connection.close()

	def delete_row_by_id(self, *data):
		query = '''	delete from students where id = %s ; '''
		try:
			record = self.read_row_by_id(data[0])
			if record is None:
				print('Student with id = {} not found'.format(data[0]))
				return
			connection = self.get_connection()
			db_cursor = connection.cursor()
			db_cursor.execute(query, data)
			connection.commit()
			print('Successfully deleted a row')
			print(db_cursor.rowcount, "record(s) affected")
			if connection is not None:
				db_cursor.close()
				connection.close()
		except(Exception, Error) as error:
			print(error)
		finally:
			pass

db_oprs = DB_operations()
db_oprs.create_table()
db_oprs.delete_row_by_id(6)
