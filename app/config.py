from os import environ, path, pardir
from dotenv import load_dotenv

env_path = path.abspath(path.join(path.dirname(__file__), pardir))
load_dotenv(path.join(env_path, 'env.env'))

class Config:
    #SECRET_KEY = environ.get('SECRET_KEY')

    
    url = environ.get('DB_URI')
    url = url[:8] + "ql" + url[8:]
    SQLALCHEMY_DATABASE_URI = url