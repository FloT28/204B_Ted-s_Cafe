from flask import Flask, render_template, redirect, url_for, request, flash, session
import os 

app = Flask(__name__)

items = [1,2,3,4,5,6,7,8]
DB_ITEMS = {
    'item1': 3.80,
}
@app.route('/')
def home(): 
    return redirect(url_for('menu'))

@app.route('/contact_us')
def contact(): 
    return render_template('contact_us.html')

@app.route('/menu')
def menu(): 
    return render_template('menu.html', item=DB_ITEMS) #"""DB_items""" parse here

@app.route('/checkout_pay')
def checkout(): 
    return render_template('checkout_pay.html')

@app.route('/checkout')
def checkout_1(): 
    return render_template('checkout.html')

@app.route('/about_us')
def about_us(): 
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run(debug=True)
