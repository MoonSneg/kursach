from flask import Flask, render_template

app = Flask(__name__)

nav = [
    {"title": "Главная", "URL": "/" },
    {"title": "Об авторе", "URL": "/about" },
    {"title": "Глоссарий", "URL": "/glossary" },
]

hero = [
    {"title": "Танджиро", "URL": "/tanjiro" },
    {"title": "Незуко", "URL": "/nezuko" },
    {"title": "Томиока", "URL": "/tamioka" },
    ]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.context_processor
def global_context_character():
    return {
        "hero": hero
    }


@app.route("/")
def hello_world():
    return render_template("index.html", name="Главная")

@app.route("/about")
def about_view():
    return render_template("about.html", name="Об авторе")

@app.route("/glossary")
def glossary_view():
    return render_template("glossary.html", name="Глоссарий")

@app.route("/tanjiro")
def character_tanj():
    return render_template("tanjiro.html", name="Танджиро")

@app.route("/nezuko")
def character_nezuko():
    return render_template("nezuko.html", name="Незуко")

@app.route("/tamioka")
def character_tamioka():
    return render_template("tamioka.html", name="Тамиока")