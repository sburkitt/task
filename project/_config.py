import os 

#base directory
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
#secret = os.urandom(24).encode('hex')
SECRET_KEY = "653de1ef80bb17ebe8267941802ba3967c785c6a7929e858"


#path for database:
DATABASE_PATH = os.path.join(basedir, DATABASE)