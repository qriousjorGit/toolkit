from flask import Flask, render_template, url_for, request, redirect
from nopaywall import get_free_link
import webbrowser
from QR_gen2 import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("tools.html")

@app.route('/nopay')
def nopay():
    return render_template("nopay.html")

@app.route('/link', methods=['GET', 'POST'])
def show_link():
    data = request.form['url']
    print(data)
    if data.startswith("http"):
        free_link = get_free_link(data)
        #below works but too much clicking
        # return f"<h1>Paywalled link is: <a href='{data}'>{data}</a>,<br> Free link: <a target=_'_blank' href='{free_link}'>Found it!</a></h1>"
        webbrowser.open_new_tab(free_link)
        return redirect(free_link)
    else:
        return f"<p>Sorry, free version of the article not found</p>"

@app.route('/qrcode')
def get_qr_info():
    return render_template("qrcode.html")

@app.route('/show_code', methods=['POST'])
def show_code():
    fname = request.form['first_name']
    lname = request.form['last_name']
    mobile = request.form['mobile']
    email = request.form['email']
    vcard_data = get_data(lname, fname, mobile, email)
    gen_QR(vcard_data)
    return render_template("showcode.html")


if __name__ == "__main__":
    app.run(debug=True)