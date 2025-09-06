from flask import Flask, render_template, redirect, url_for, request, flash, session
import os 

app = Flask(__name__)

items = [1,2,3,4,5,6,7,8]


"""DEBUG!!! This is a list of dictionaries, each dictionary represents an item with its name as the key and price as the value.-------------------------------------------------
This data will come from a database. All of the items must be strings, in the format. Current max reccomended name length is 84 at a stretch. """,
DB_ITEMS = [
    # first item has silly name to test formatting with long strings. DEBUG
    {'id': '1', 'image': 'https://i.postimg.cc/FFYNBdR5/flat-white.jpg', 'name': 'Flat White Of your dreams PHD Esq the fifth prince of edenburogh the butcher of cork', 'price': '5.00'},
    {'id': '2', 'image': 'https://i.postimg.cc/4NtZXDVW/latte.jpg', 'name': 'Latte', 'price': '5.50'},
    {'id': '3', 'image': 'https://i.postimg.cc/mgs4kmSB/hot-chocolate.jpg', 'name': 'Hot Chocolate', 'price': '5.00'},
    {'id': '4', 'image': 'https://i.postimg.cc/YCzHWQXg/black-coffee.jpg', 'name': 'Black Coffee', 'price': '4.50'},
    {'id': '5', 'image': 'https://i.postimg.cc/BvndPkP9/scones.jpg', 'name': 'Scones', 'price': '4.00'},
    {'id': '6', 'image': 'https://i.postimg.cc/mgwvDBDy/chocolate-cake.jpg', 'name': 'Chocolate Cake', 'price': '4.50'},
    {'id': '7', 'image': 'https://i.postimg.cc/ZR2tSHRk/caramel-slice.jpg', 'name': 'Caramel Slice', 'price': '4.50'},
    {'id': '8', 'image': 'https://i.postimg.cc/SKQp7j5P/poached-egg-toast.jpg', 'name': 'Poached Egg on Toast', 'price': '7.00'},
]

@app.route('/')
def home(): 
    return redirect(url_for('menu'))

@app.route('/contact_us')
def contact(): 
    return render_template('contact_us.html')

@app.route('/menu')
def menu(): 
    return render_template('menu.html', items=DB_ITEMS) #"""DB_items""" parse here

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
