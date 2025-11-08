# app.py - Final Clean Version for Render Deployment (No DB)

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# Gukosora Itegeko rya Environment
app = Flask(__name__)

# --- ROUTES Z'INGENZI ---

# 1. Route ya Homepage (Iki ni cyo kigabanya ikosa)
@app_flask.route('/') # Koresha app_flask
def index():
    try:
        # Genzura neza ko index.html iri muri templates
        return render_template('index.html') 
    except Exception as e:
        # Ibi bitwereka ikosa nyaryo niba application yanze
        print(f"Error rendering index.html: {e}") 
        return "Internal Error: Check Flask logs for template or variable errors.", 500

# 2. Routes z'Icyerekezo 
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
    # ... (Yakira amakuru, nta DB) ...
    name = request.form.get('name')
    email = request.form.get('email')
    # ... (yakira andi makuru) ...
    
    print(f"Akwandikisha Mashya Yagezeho: {name}")
    return redirect(url_for('booking_success')) 

@app.route('/success')
def booking_success():
    return render_template('confirmation.html')

# --- Gutangiza Application ---
if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port=port, debug=True)