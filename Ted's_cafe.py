from flask import Flask, render_template, redirect, url_for, request, flash, session
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about_us.html')

@app.route('/contact_us')
def contact(): 
    return render_template('contact_us.html')

@app.route('/menu')
def menu(): 
    return render_template('menu.html')

@app.route('/checkout_pay')
def checkout(): 
    return render_template('checkout_pay.html')

@app.route('/checkout')
def checkout_1(): 
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
