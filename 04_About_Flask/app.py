from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/fancy")
def Hello_world_fancy():
    return """
    <html>
        <body>
            <h1>Greeting!</h1>
        </body>
    </html>
    """


#  using render_template()
@app.route("/first")
def frist_page():
    return render_template("first_page.html")


# intro to Jinja
@app.route("/jinja")
def jinja_page():
    return render_template("jinja_intro.html", name="Vicky Raut", template_name="jinja2")


# Expressions
@app.route("/expressions")
def expressions():
    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition & subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # concatination
    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        # interpolation
        "color": "brown",
        "animal_one": "fox",
        "animal_two": "dog",

        # addition & subtraction
        "orange_amount": 10,
        "apple_amount": 20,
        "donate_amount": 15,

        # concatenation
        "first_name": "Captain",
        "last_name": "Marvel"
    }

    return render_template("expressions.html", **kwargs)


# Conditionals & Loops
@app.route("/loop-conditionals/")
def loopsConditionals():
    user_os = {
        "alice": "Windows",
        "bob": "MacOS",
        "charlie": "Ubuntu 20.04",
        "dave": "Windows 11",
        "eve": "Fedora 34",
        "frank": "Debian 11",
        "grace": "macOS Monterey",
        "heidi": "Arch Linux",
        "ivan": "Linux"
    }
    return render_template("loops_and_conditionals.html", user_os=user_os)
