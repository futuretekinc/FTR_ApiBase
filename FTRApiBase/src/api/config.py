# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example

SQLITE3 = "sqlite:///D:/tmp/single_db.db"
MYSQL_OPER='mysql+pymysql://root:4rnekd9wkd@ftr-app.japanwest.cloudapp.azure.com/ftr_app_db?charset=utf8'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = MYSQL_OPER

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = DEBUG
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_POOL_SIZE = 20
#SQLALCHEMY_POOL_TIMEOUT = 60
SQLALCHEMY_POOL_RECYCLE = 500


DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

WTF_CSRF_ENABLED = True

# Secret key for signing cookies
# SECRET_KEY = "secret"
SECRET_KEY = '#RGWwfwiuwWEFwef23$#25d-2023'
SESSION_COOKIE_NAME='futuretek_cookies'
PERMANENT_SESSION_LIFETIME=timedelta(31) # 31days








