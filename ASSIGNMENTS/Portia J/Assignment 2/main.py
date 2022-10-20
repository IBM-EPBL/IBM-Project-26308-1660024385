from flask import Flask, render_template, url_for, redirect
from flask_db2 import DB2
import ibm_db
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

# database details
# cant create a db because it is not free :(

hostname = "myhostname"
uid="username"
password ="password"
driver="driver name"
dbname = "db2"
port="5000"
protocol = "TCPIP"

dsn=("DRIVER={0};""DATABASE={1};""HOSTNAME={2};""PORT={3};""PROTOCOL={4};""UID={5};""PWD={6};").format(driver,dbname,hostname,port,protocol,uid,password)
try:
    db = DB2.connect(dsn,"","")
    print("Connected to database")
except:
    print("Unable to connect")


#sample register and login code

app = Flask(__name__)

bcrypt = Bcrypt(app)





@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user:
    #         if bcrypt.check_password_hash(user.password, form.password.data):
    #             login_user(user)
    #             return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    # logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    # form = RegisterForm()

    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data)
    #     new_user = User(username=form.username.data, password=hashed_password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)


# practical login code ,can be run if the db is accessible for free


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(80), nullable=False)


# class RegisterForm(FlaskForm):
#     username = StringField(validators=[
#                            InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

#     password = PasswordField(validators=[
#                              InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         existing_user_username = User.query.filter_by(
#             username=username.data).first()
#         if existing_user_username:
#             raise ValidationError(
#                 'That username already exists. Please choose a different one.')


# class LoginForm(FlaskForm):
#     username = StringField(validators=[
#                            InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

#     password = PasswordField(validators=[
#                              InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

#     submit = SubmitField('Login')
