class Config:
    APP_MODE = 'development' # 'production' or 'development'
    DEBUG = True # True or False this will print stuff to debug
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False