from flask import Flask, render_template, redirect, url_for, request, flash, session
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about_us.html')



if __name__ == '__main__':
    app.run(debug=True)
