
app_name = "BapyMonitor"

SECRET_KEY = 'SuperSecretTempKey'
PASSWORD_SALT = 'KosherSalt'


class Config:
    NAME = app_name
    DEBUG = False
    USE_AUTH = True
    SECURITY_PASSWORD_SALT = PASSWORD_SALT


class DevConfig(Config):
    DEBUG = True
    JWT_COOKIE_SECURE = False
    SECURITY_SEND_REGISTER_EMAIL = False


class ProdConfig(Config):
    pass
