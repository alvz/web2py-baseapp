###
##	Installation file. for development
##
##	Create the root user for login
###

from models.users import Users
user = Users(db, auth)

def index():
	return dict(message='ok')

def make_groups():
	user.create_groups()
	return dict(message='Grupos creados')

def make_root():
	user.create(first_name='Root', last_name='Admin',
		password='enter', email='root@localhost', role='root')
	return dict(message='User root created!')