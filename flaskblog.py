from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e0539a43dcb80257ff024b50ff0302f5'

posts = [
    {
        'author' : "sahil",
        'title' : "My first post",
        'content' : "Shit Posttt",
        'date' : "18/09/2018"
    },
    {
        'author' : "John Doe",
        'title' : "blog post 2",
        'content' : "Shit Posttt 2",
        'date' : "18/10/2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Register",form=form)

@app.route("/login"methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jalajlimaye@gmail.com' and form.password.data == 'password':
            flash('Login sucessful!','success')
            return redirect(url_for('/'))
        else:
            flash("Login Unsuccessful. Please try again.", 'danger')
    return render_template("login.html",title="Login",form=form)


if __name__ == "__main__":
    app.run(debug = True)