from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from app.backend.forms.LoginForm import LoginForm
from app.models.users import User

backend = Blueprint(
    'backend', 
    __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/backend/static'
    )

@backend.route('/')
@login_required
def index():
    return render_template('backend.html', title='Backend')

@backend.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.get_by_username(username)  # Busca o usuário no BD
        if user and user.verify_password(password):
            login_user(user)  # Flask-Login faz o login de fato
            flash("Login efetuado com sucesso!", "success")
            return redirect(url_for('backend.index'))
        else:
            flash("Usuário ou senha inválidos.", "danger")

    return render_template('login.html', 
                           title='Login Backend', 
                           form=form,
                           username=form.username.data)

@backend.route('/logout')
@login_required
def logout():
    """
    Encerra a sessão do usuário atual.
    """
    logout_user()
    return redirect(url_for("backend.login"))