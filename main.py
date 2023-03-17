import requests
from flask import Flask, render_template, url_for, request, redirect
from nopaywall import get_free_link
import webbrowser
from qrgenerator import generate_qr

# END_POINT = "http://api.qrserver.com/v1/create-qr-code/?data=HelloWorld!&size=100x100"
# r = requests.get(END_POINT)
#
# print(type(r))

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
        return redirect(url_for('nopay'))
    else:
        return f"<p>Sorry, free version of the article not found</p>"

@app.route('/qrcode')
def get_qr_info():
    return render_template("qrcode.html")

@app.route('/showcode', methods=['POST'])
def gen_qrcode():
    data = request.form['qrdata']
    # print(data)
    # qr_link = generate_qr(data)
    # print(qr_link)
    # return f"<a href=http://api.qrserver.com/v1/create-qr-code/?data={data}&size=100x100> Link </a>"
    return redirect(f"http://api.qrserver.com/v1/create-qr-code/?data={data}&size=100x100")




if __name__ == "__main__":
    app.run(debug=True)