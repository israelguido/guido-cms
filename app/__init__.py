from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.main.routes import main
    from app.blog.routes import blog
    
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix='/blog')
    
    return app