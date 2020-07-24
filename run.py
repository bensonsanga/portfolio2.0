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

@app.route("/project")
def project():
    return render_template('project.html', title='project')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/Cultural_Center")
def Cultural_Center():
    return render_template('Cultural_Center.html', title='Cultural_Center')

@app.route("/Technocity")
def Technocity():
    return render_template('Technocity.html', title='Technocity')

@app.route("/Community_Center")
def Community_Center():
    return render_template('Community_Center.html', title='Community_Center')

@app.route("/Kindergartten")
def Kindergartten():
    return render_template('Kindergartten.html', title='Kindergartten')

@app.route("/Exhibiton_Design")
def Exhibiton_Design():
    return render_template('Exhibiton_Design.html', title='Exhibiton_Design')

@app.route("/Social_Hub")
def Social_Hub():
    return render_template('Social_Hub.html', title='Social_Hub')

@app.route("/hub")
def hub():
    return render_template('hub.html', title='hub')

@app.route("/fab")
def fab():
    return render_template('fab.html', title='fab')

if __name__ == '__main__':
    app.run(debug=True)
