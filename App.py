from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my website"
@app.route('/contact')
def contact_page():
    return "contact page"
@app.route('/gallary')
def Phote_name():
    return "photo name"
@app.route('/home')
def Home_Lander():
    return "home lander"

if __name__ == "__main__":
    app.run()