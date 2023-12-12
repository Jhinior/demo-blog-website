from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/de09e0e706dadd0e0e6d")
data = response.json()

@app.route("/")
def home():
    return render_template("index.html",data = data)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/title/subtitle/date/author/body/<id>")
def blog(id):
    response = requests.get(url="https://api.npoint.io/de09e0e706dadd0e0e6d")
    data = response.json()
    return render_template("post.html",post=data[int(id)-1])

if __name__ == "__main__":
    app.run(debug=True)

