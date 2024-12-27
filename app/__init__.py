from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.main.routes import main
    from app.blog.routes import blog
    from app.backend.routes import backend
    
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(backend, url_prefix='/backend')
    
    return app