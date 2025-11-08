# app.py - FINAL VERSION WITH POSTGRESQL/SQLALCHEMY

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os 
from flask_sqlalchemy import SQLAlchemy # Iyi module igomba kwinjira

# Gukosora Itegeko rya Environment
app = Flask(__name__)

# --- CONFIGURATION Y'INGENZI YA DATABASE ---

# Gushyiraho Database URI: Render irazishaka muri Environment
# Iyi irahita isoma DATABASE_URL twashyize kuri Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Kwemeza SQLAlchemy
db = SQLAlchemy(app)

# --- DEFINITION YA DATABASE MODEL ---
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False) # Twibanda kuri Datetime

    def __repr__(self):
        return f'<Booking {self.name}>'

# --- ROUTES Z'INGENZI (Tugomba guhindura /submit-booking) ---

@app.route('/')
def index():
    return render_template('index.html') 

# ... (Andi ma routes nka /men, /woman, /contact) ...

# 3. Route yo Kwandikisha (Submission)
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    # Kwakira amakuru
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    date = request.form.get('date')
    time = request.form.get('time')
    
    # Guhuza Itariki n'Igihe
    date_time_str = f"{date} {time}"
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

    # Kurema Record nshya
    new_booking = Booking(
        name=name, 
        email=email, 
        service=service, 
        date_time=date_time_obj
    )
    
    try:
        # Kubika Database
        db.session.add(new_booking)
        db.session.commit()
        print(f"Booking nshya yabitswe: {name}")
        return redirect(url_for('booking_success'))
    except Exception as e:
        print(f"Error kubika Booking: {e}")
        return "Database save error.", 500


@app.route('/success')
def booking_success():
    return render_template('confirmation.html')
# --- Gutangiza Application ---
if __name__ == '__main__':    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)