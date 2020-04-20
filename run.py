from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/Project1")
@app.route("/Cultural_Center")
def Project1():
    return render_template('Cultural_Center.html', title='Project1')

@app.route("/Project2")
def Project2():
    return render_template('Project2.html', title='Project2')

@app.route("/Project3")
def Project3():
    return render_template('Project3.html', title='Project3')

@app.route("/Project4")
def Project4():
    return render_template('Project4.html', title='Project4')

@app.route("/Project5")
def Project5():
    return render_template('Project5.html', title='Project5')

@app.route("/Project6")
def Project6():
    return render_template('Project6.html', title='Project6')

if __name__ == '__main__':
    app.run(debug=True)
