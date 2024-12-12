from flask import Blueprint, render_template

blog = Blueprint(
    'blog', 
    __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/blog/static'
    )

@blog.route('/')
def index():
    posts = [
        {'title': 'Post 1', 'content': 'Content 1'},
        {'title': 'Post 2', 'content': 'Content 2'},
    ]
    return render_template('blog.html', title='Blog', posts=posts)

@blog.route('/<int:post_id>')
def post(post_id):
    post = {'title': f'Post {post_id}', 'content': f'Content {post_id}'}
    return render_template('post.html', title=post['title'], post=post)