from flask import Flask, render_template, url_for
app = Flask(__name__)

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


@app.route("/home")
def hello():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")


if __name__ == "__main__":
    app.run(debug = True)