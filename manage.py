from app import create_app
from app.extensions import db
from app.models.users import User
from werkzeug.security import generate_password_hash
from datetime import datetime

app = create_app()

if __name__ == '__main__':
    # Exemplo de comando para criar as tabelas (sem Flask CLI)
    with app.app_context():
        db.create_all()
        print("Tabelas criadas!")
        
        u = User(
            username="admin", 
            password=generate_password_hash("admin123")
        )
        db.session.add(u)
        db.session.commit()

        print(f"Usuário '{u.username}' criado com sucesso!")