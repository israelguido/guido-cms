from flask import Blueprint, render_template
from app.backend.forms.LoginForm import LoginForm

backend = Blueprint(
    'backend', 
    __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/backend/static'
    )

@backend.route('/')
def index():
    return render_template('backend.html', title='Backend')

@backend.route('/login', methods=['GET', 'POST'])
def login():
    username = None
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''
        
    return render_template('login.html', title='Login Backend', username=username, form=form)