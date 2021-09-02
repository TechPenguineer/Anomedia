from flask import *

app = Flask(__name__)

@app.route("/")
def WARNING_PAGE():
        return render_template("warning.html")

if __name__ == "__main__":
    app.run(port=2010)