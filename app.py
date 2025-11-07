# app.py - Final Clean Version for Render Deployment (No DB)

from flask import Flask, render_template, request, redirect, url_for
# Nta hantu hakoreshejwe: from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Gukosora Itegeko rya Environment
app = Flask(__name__)

# --- ROUTES Z'INGENZI ---

# 1. Route ya Homepage (Iki ni cyo kigabanya ikosa)
@app.route('/')
def index():
    # Render_template ikoreshwa gusa. Nta variable zoherezwa.
    return render_template('index.html')

# 2. Routes z'Icyerekezo (Genzura neza ko Link zihuye na HTML)
@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/woman')
def woman():
    return render_template('woman.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# 3. Route yo Kwandikisha (Submission)
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    name = request.form.get('name')
    # ... (yakira amakuru yose) ...

    # Sigaza gusa amabwiriza yo kwemeza
    print(f"Akwandikisha Mashya Yagezeho: {name}")

    # Redirects to /success
    return redirect(url_for('booking_success')) 

@app.route('/success')
def booking_success():
    return render_template('confirmation.html')

# --- Gutangiza Application ---
# Iki gice kirirengagizwa na Gunicorn, ariko kigumaho
if __name__ == '__main__':
    app.run(debug=True)