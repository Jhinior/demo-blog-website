from flask import Flask, render_template ,request
import requests
import smtplib
import os
USER_NAME = os.environ["EMAIL"]
PASSWORD = os.environ["PASS"]
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/de09e0e706dadd0e0e6d")
data = response.json()

@app.route("/")
def home():
    return render_template("index.html",data = data)

@app.route("/contact",methods=["POST","GET"])
def contact():
    change = True
    if request.method == "POST":
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=USER_NAME,password=PASSWORD)
        connection.sendmail(to_addrs=USER_NAME,from_addr=USER_NAME,msg=f"Subject: Fan Message \n\n\n"
                                                                       f"You got a message from: {request.form['name']}\n"
                                                                       f"Mail: {request.form['email']}\n"
                                                                       f"Phone: {request.form['phone']}\n"
                                                                       f"Content: {request.form['message']} ")
        connection.close()
        change = False
        return  render_template("contact.html",change = change)
    else :
        return render_template("contact.html",change = change)

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

