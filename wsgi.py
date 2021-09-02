from flask import *

app = Flask(__name__)

@app.route("/")
def WARNING_PAGE():
        return render_template("warning.html")

