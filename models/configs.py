# -*- coding: utf-8 -*-

from gluon.tools import Auth, Mail
from gluon.custom_import import track_changes


##################################################
### Set DEBUG
##################################################
DEBUG = request.is_local


##################################################
### Reload modules
##################################################
track_changes(DEBUG)


##################################################
### Database config
##################################################
if DEBUG:     
    db = DAL('sqlite://storage.sqlite')
else:
    db = DAL('postgres://username:password@localhost:5432/database')


##################################################
### Mail settings
##################################################
mail = Mail()      
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'mail'         
mail.settings.login = 'username:password' 


##################################################
### Database config
##################################################
session.connect(request, response, db=db)


##################################################
### Generic views
##################################################    
response.generic_patterns = ['*'] if DEBUG else ['*.json']


##################################################
### Application data
##################################################
response.title = 'Base app'
response.subtitle = 'Aplicación Base'
response.meta.author = 'jCarlo0s'
response.meta.email = 'me@jcarlosandrade.com'
response.meta.description = ''
response.meta.keywords = ''
response.meta.copyright = 'Copyright 2012' 


##################################################
### Auth settings
##################################################
auth = Auth(db,hmac_key=Auth.get_or_create_key()) 
auth.define_tables()                           
auth.settings.mailer = mail                    
auth.settings.create_user_groups = False
auth.settings.formstyle = 'divs'
auth.settings.remember_me_form = False
auth.settings.actions_disabled = ['register']
auth.settings.login_url = URL('main', 'index')
auth.settings.logout_next = URL('default', 'index')
auth.settings.login_next = URL('main', 'index')

