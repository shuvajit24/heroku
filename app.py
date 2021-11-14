from flask import Flask, render_template, request
import joblib
app_flask = Flask(__name__)

loaded_model = joblib.load(r'D:\New System\Data Science\WVS\save_folder\Flask application\dib_78.pkl')
@app_flask.route('/')
def index():
    return 'hello world'

@app_flask.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app_flask.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app_flask.route('/contact')
def contacts():
    return render_template('contacts.html')

@app_flask.route('/enquiry')
def enquiry():
    return render_template('enquiry.html')

@app_flask.route('/login')
def login():
    return render_template('login.html')

@app_flask.route('/homepage1')
def homepage1():
    return render_template('homepage1.html')

@app_flask.route('/predict', methods = ['POST'])
def predict():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email = request.form.get('mail')
    phone = request.form.get('phonenumber')
    print(fname , lname , email , phone)

    return render_template('homepage1.html')

@app_flask.route('/homepage2')
def homepage2():
    return render_template('homepage2.html')



@app_flask.route('/predict1', methods = ['POST'])
def predict1():
    preg1 = request.form.get('preg')
    plas1 = request.form.get('plas')
    pres1 = request.form.get('pres')
    skin1 = request.form.get('skin')
    test1 = request.form.get('test')
    mass1 = request.form.get('mass')
    pedi1 = request.form.get('pedi')
    age1 = request.form.get('age')
    print(preg1 , plas1 , pres1 , skin1, test1, mass1, pedi1, age1)

    prediction = loaded_model.predict([[preg1, plas1, pres1, skin1, test1, mass1, pedi1, age1]])

    if prediction[0] == 1:
        val ='diabetic'
    else:
       val = 'not diabetic'

    return render_template('result.html', value = val)

if __name__== '__main__':
    app_flask.run(debug=True)


