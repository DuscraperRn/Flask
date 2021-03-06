import re
from flask import Flask,render_template,request
import gspread

gc=gspread.service_account(filename='flask-profile.json')
sc=gc.open('falsk-profile')

shProf=sc.get_worksheet(0)
shCon=sc.get_worksheet(1)
shCon.append_row(['1','@gmail','2'])

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        shCon.append_row([request.form['name'],request.form['email'],request.form['message']])
    #return render_template('index.html')
    profile={
        'about': shProf.acell('B1').value,
        'email': shProf.acell('B2').value,
        'education': shProf.acell('B3').value,
        'work': shProf.acell('B4').value  
    }
    return render_template('index.html',profile=profile)

@app.route('/contact')
def contact():
    return render_template('contacts.html')