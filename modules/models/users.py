###
##	Users class 
###

from gluon import *

class Users(object):

	## Constructor
	def __init__(self, db, auth):
		"""
		Initialize variables
		"""
		self.db = db
		self.auth = auth

	def create_groups(self):
		self.auth.add_group('root', 'Administradores')

	def create(self, **kwargs):
		"""
		Create new user
		"""
		if self.exist(kwargs['email']):
			return False
		else:
			password = self.db.auth_user.password.validate(kwargs['password'])[0]
			user = self.db.auth_user.insert(first_name=kwargs['first_name'],
					last_name=kwargs['last_name'], password=password,
					email=kwargs['email'])
			return	True

	def exist(self, email):
		"""
		Check if user exists
		"""
		query = self.db(self.db.auth_user.email == email)
		count = query.count()
		return True if count > 0 else False

	def delete(self, id):
		"""
		Delete User
		"""
		try:
			self.db(self.db.auth_user.id == id).delete()
			return True
		except:
			return False