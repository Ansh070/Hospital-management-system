from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name = 'Ansh')

@app.route("/about")
def about():
    return "<h1>About Page Coming Soon!</h1>"

@app.route("/login")
def login():
    return "<h2>Login page coming soon</h2>"

if __name__ == '__main__':
    app.run(debug=True)