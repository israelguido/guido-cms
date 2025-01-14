from flask import Blueprint, render_template
from app.core.database import MySQLDatabase
from app.blog.models.posts import Post

blog = Blueprint(
    'blog', 
    __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/blog/static'
)

# Configuração do banco de dados
db = MySQLDatabase(
    db_type="mysql",
    username="guido",
    password="Guido2024",
    host="db",
    port=3306,
    database="guido"
)


@blog.route('/')
def index():
    conn = db.get_session()
    # Criação das tabelas
    #db.create_tables()
    

    # posts = [
    #     {'title': 'Post 1', 'content': 'Content 1'},
    #     {'title': 'Post 2', 'content': 'Content 2'},
    # ]

    # Create
    # new_post = Post(
    #     title="Meu Segundo Post",
    #     slug="meu-segundo-post",
    #     content="Este é o conteúdo do meu Segundo post!",
    #     author="Israel Guido",
    #     is_published=True
    # )
    # conn.add(new_post)
    # conn.commit()

    #Lendo os posts
    posts = conn.query(Post).all()
    print(posts)
    return render_template('blog.html', title='Blog', posts=posts)

@blog.route('/<int:post_id>')
def post(post_id):
    conn = db.get_session()
    #retorno do post por id
    post = conn.query(Post).filter(Post.id == post_id).first()
    #post = {'title': f'Post {post_id}', 'content': f'Content {post_id}'}
    if not post:
        abort(404)

    return render_template('post.html', title=post.title, post=post)