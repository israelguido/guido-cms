import os
from flask import Flask
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from app.extensions import db
from app.models.users import User

# Inicializa o gerenciador de login
login_manager = LoginManager()



def create_app():
    app = Flask(__name__)
    
    #flask-login config
    app.secret_key = "guido-cms-secret-key"    
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        """Função que retorna o usuário a partir do user_id."""
        return User.get_by_id(user_id)  # Ajuste para a forma como você busca no banco
    
    #register routes
    from app.main.routes import main
    from app.blog.routes import blog
    from app.backend.routes import backend
    
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(backend, url_prefix='/backend')
    
    # Database config
    db_url = os.getenv("DATABASE_URL", "mysql+pymysql://guido:Guido2024@db:3306/guido")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    from app.models.users import User # Importa o model para

    return app