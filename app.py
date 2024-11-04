from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/form')
def show_form():
    return render_template("form.html", prompts = story.prompts)

@app.route('/form', methods=["post"])
def save_answers():
    answers = request.form.to_dict()
    result = story.generate(answers)
    return render_template("/story.html", result=result)