from flask import Flask, render_template, redirect, url_for, request, flash, session
import os 

app = Flask(__name__)

app.secret_key = os.urandom(24)  # Secret key for session management

Itemlist = []


"""DEBUG!!! This is a list of dictionaries, each dictionary represents an item with its name as the key and price as the value.-------------------------------------------------
This data will come from a database. All of the items must be strings, in the format. Current max reccomended name length is 84 at a stretch. """,
DB_ITEMS = [
    # first item has silly name to test formatting with long strings. DEBUG
    {'id': '1', 'image': 'https://i.postimg.cc/FFYNBdR5/flat-white.jpg', 'name': 'Flat White', 'price': '5.00'},
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

@app.route('/about_us')
def about_us(): 
    return render_template('about_us.html')

@app.route('/menu')
def menu(): 
    return render_template('menu.html', items=DB_ITEMS) #"""DB_items""" parse here

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.form.get('item_id')
    qty = int(request.form.get('qty', 1))

    item = next((i for i in DB_ITEMS if i['id'] == item_id), None)
    if item:
        cart = session.get('cart', [])

        # Check if item already in cart
        existing_item = next((i for i in cart if i['id'] == item_id), None)
        if existing_item:
            existing_item['qty'] += qty
        else:
            cart.append({
                'id': item['id'],
                'name': item['name'],
                'price': float(item['price']),
                'qty': qty,
                'image': item['image']
            })

        session['cart'] = cart  # Save back to session

    return redirect(url_for('menu'))


@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    total = sum(i['price'] * i['qty'] for i in cart)
    return render_template('checkout.html', cart=cart, total=total)

@app.route('/checkout_pay')
def checkout_pay(): 
    return render_template('checkout_pay.html')

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item_id = request.form.get('item_id')
    cart = session.get('cart', [])
    cart = [i for i in cart if i['id'] != item_id]
    session['cart'] = cart
    return redirect(url_for('checkout'))

@app.route('/update_cart', methods=['POST'])
def update_cart():
    item_id = request.form.get('item_id')
    qty = int(request.form.get('qty', 1))
    cart = session.get('cart', [])
    for item in cart:
        if item['id'] == item_id:
            item['qty'] = qty
            break
    session['cart'] = cart
    return redirect(url_for('checkout'))

if __name__ == '__main__':
    app.run(debug=True)
