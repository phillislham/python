# project/app/__init__.py
sc("project/app/__init__.py")
from flask_login import LoginManager
objloginmngr = LoginManager()

@objloginmngr.user_loader
def load_user(username):
    pr(username,"load_user")
    from app.models.user_model import UserModel
    return UserModel.query(username)

def _get_config(flaskapp):
    # export FLASK_ENV=<development>
    sc("... getting config")
    from bootstrap.config import Config,DevelopmentConfig,ProductionConfig,TestingConfig

    strenv = flaskapp.config["ENV"]

    pr(strenv, "flaskapp.config[ENV]")
    if strenv == "development":
        return DevelopmentConfig
    elif strenv == "production":
        return ProductionConfig
    elif strenv == "testing":
        return TestingConfig
    else:
        return Config


def get_flaskapp():
    sc("... creando flaskapp")
    from flask_bootstrap import Bootstrap
    from flask import Flask
    
    #from auth.init import blueprint_auth
    from .auth import blueprint_auth
    
    flaskapp = Flask(__name__)
    Config = _get_config(flaskapp)    

    # se pasa a una clase de configuracion (config.py)
    # flaskapp.config["SECRET_KEY"] = "SUPER SECRET KEY"
    # con esto se cifra la info de la cookie
    # esto habria que cambiarlo a un hash más seguro, para el ejemplo nos vale
    flaskapp.config.from_object(Config)

    #bug(objloginmngr,"objloginmngr")
    objloginmngr.login_view = "auth.login"
    objloginmngr.login_message = "Please first login"
    objloginmngr.login_message_category = "warning"    
    objloginmngr.init_app(flaskapp)

    flaskapp.register_blueprint(blueprint_auth)
    Bootstrap(flaskapp)
    return flaskapp