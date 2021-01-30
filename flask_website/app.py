from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def indef():
    stonks = [
        "GME",
        "APC" #AlpacaCoin,
        "TSLA",
        "NOK",
        "MSFT",
        "APPL",
        "FLT",
        "HIVE",
        "BTC",
        "ETH"
    ]
    return render_template("index.html", stonks=stonks)

if __name__ == "__main__":
    app.run(debug=True)