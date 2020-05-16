import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIPAY_APPID = "2016091800537304"
APP_PRIVATE_KEY = open(os.path.join(BASE_DIR, 'alipay_config/app_rsa_private_key.pem'), 'r').read()
ALIPAY_PUBLIC_KEY = open(os.path.join(BASE_DIR, 'alipay_config/alipay_rsa_public_key.pem'), 'r').read()


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "BSDsdfdsfDSFSADasdfsdf"


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "tgops123..",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask",
    }
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "z769776939@163.com"
    MAIL_PASSWORD = "z139034"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "tgops123..",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "tgops123..",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "tgops123..",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}

ADMINS = ('admin', 'libai')

FILE_PATH_PREFIX = "/static/uploads/icons"
UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')
