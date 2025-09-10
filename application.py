from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "f7Gk3mQ2pX9sL8vD4wR1bZ0a"
# Secret key for session management, ONLY FOR UNIMPORTANT DATA. We would use a third party service for real payments.
# In a real application, we would probably use a postgreSQL database since it has cryptographic features, and is more secure.


# Simulated database of items, in a real application this would be replaced with a database query. 
#  Unfortunately a database is out of scope for this project, so we will use a list of dictionaries to simulate a database.
DB_ITEMS = [
    {'id': '1', 'image': 'https://i.postimg.cc/FFYNBdR5/flat-white.jpg', 'name': 'Flat White', 'price': '5.00'},
    {'id': '2', 'image': 'https://i.postimg.cc/4NtZXDVW/latte.jpg', 'name': 'Latte', 'price': '5.50'},
    {'id': '3', 'image': 'https://i.postimg.cc/mgs4kmSB/hot-chocolate.jpg', 'name': 'Hot Chocolate', 'price': '5.00'},
    {'id': '4', 'image': 'https://i.postimg.cc/YCzHWQXg/black-coffee.jpg', 'name': 'Black Coffee', 'price': '4.50'},
    {'id': '5', 'image': 'https://i.postimg.cc/BvndPkP9/scones.jpg', 'name': 'Scones', 'price': '4.00'},
    {'id': '6', 'image': 'https://i.postimg.cc/mgwvDBDy/chocolate-cake.jpg', 'name': 'Chocolate Cake', 'price': '4.50'},
    {'id': '7', 'image': 'https://i.postimg.cc/ZR2tSHRk/caramel-slice.jpg', 'name': 'Caramel Slice', 'price': '4.50'},
    {'id': '8', 'image': 'https://i.postimg.cc/SKQp7j5P/poached-egg-toast.jpg', 'name': 'Poached Egg on Toast', 'price': '7.00'},
    {'id': '9', 'image': 'https://i.postimg.cc/rz6KLxyb/glass-cold-beer-wooden-surface-sunny-day.jpg', 'name': 'Beer Of The Day', 'price': '6.00'},
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
    return render_template('menu.html', items=DB_ITEMS)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.form.get('item_id')
    qty = int(request.form.get('qty', 1))

    item = next((i for i in DB_ITEMS if i['id'] == item_id), None)
    if item:
        cart = session.get('cart', [])
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
        session['cart'] = cart
    return redirect(url_for('menu'))

@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    total = sum(i['price'] * i['qty'] for i in cart)
    return render_template('checkout.html', cart=cart, total=total)

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

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item_id = request.form.get('item_id')
    cart = session.get('cart', [])
    cart = [i for i in cart if i['id'] != item_id]
    session['cart'] = cart
    return redirect(url_for('checkout'))

@app.route('/checkout_pay', methods=['GET', 'POST'])
def checkout_pay():
    if request.method == 'GET':
        # Get total from query parameter
        total = request.args.get('total', 0)
        return render_template('checkout_pay.html', total=total)

    if request.method == 'POST':
        card_name = request.form.get('card_name', '').strip()
        card_no = request.form.get('card_no', '').replace(' ', '')
        cvc = request.form.get('cvc', '').strip()
        expiry = request.form.get('expiry', '').strip()

        # Validation
        errors = []
        if not card_name:
            errors.append("Cardholder name is required.")
        if not (card_no.isdigit() and len(card_no) == 16):
            errors.append("Card number must be 16 digits.")
        if not (cvc.isdigit() and len(cvc) == 3):
            errors.append("CVC must be 3 digits.")
        try:
            exp_date = datetime.strptime(expiry, "%m/%y")
            if exp_date < datetime.now():
                errors.append("Card has expired.")
        except:
            errors.append("Expiry date must be in MM/YY format.")

        if errors:
            for e in errors:
                flash(e)
            return redirect(url_for('checkout_pay'))

        session.pop('cart', None) # Clear cart after payment
        flash("Payment successful!")
        return redirect(url_for('menu'))
    

if __name__ == '__main__':
    app.run(debug=True)

application = app
