# app.py - Python Backend (Gukoresha Flask)

# Byaba ngombwa ko ubanza gushyiraho Flask muri system yawe: pip install Flask
from flask import Flask, render_template, request, redirect, url_for

# Icyitonderwa: Muri code ya nyayo, twakoresha Database (SQLAlchemy)
# kugira ngo tubike aya makuru, tuyakuremo, ndetse turenze amateriki yafashwe.

app = Flask(__name__)

# Route ya Homepage (Dutekereje ko iri mu dosiye 'index.html')
@app.route('/')
def index():
    # Uzakenera gushyira amadosiye yawe ya HTML muri folder yitwa 'templates'
    return render_template('index.html')

# Route yo Kwakira Amakuru aturuka kuri Form (contact.html)
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    # 1. Kwakira Amakuru yoherejwe na Form
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    date = request.form.get('date') # Itariki yaturutse kuri input type="date"
    time = request.form.get('time') # Isaha yaturutse kuri input hidden (Javascript yayujuje)
    
    # 2. Kwemeza ko Amakuru yose ahari (Simple Validation)
    if not all([name, email, service, date, time]):
        print("ERROR: Amakuru ntabwo yuzuye!")
        return "Amakuru ntabwo yuzuye! Subira inyuma.", 400

    # 3. Kubika/Gukorana n'Amakuru (Iki ni igice cy'ingenzi cya Backend)
    
    # Kubika mu buryo bwa Console (Urugero)
    print("------------------------------------------------")
    print("Akwandikisha Mashya Yagezeho:")
    print(f"Amazina: {name}")
    print(f"Email: {email}")
    print(f"Serivisi: {service}")
    print(f"Itariki: {date} saa {time}")
    print("------------------------------------------------")

    # >>> IGICE CY'UMWANYA (SLOT CHECK) NO KUBIKA MURI DATABASE CYAGOMBA KUBA HANO <<<
    # Urugero:
    # is_available = check_database_availability(date, time)
    # if is_available:
    #     save_to_database(name, email, service, date, time)
    # else:
    #     return "Mbi! Uyu mwanya wafashwe. Tora indi saha.", 409
    
    # 4. Gusubiza Umukiriya kuri Page yemeza (Confirmation)
    # Icyitonderwa: Tugomba gukora page nshya 'confirmation.html'
    return redirect(url_for('booking_success'))

@app.route('/success')
def booking_success():
    return "Murakoze! Kwandikisha kwanyu kwemejwe. Tuzabahamagara."
    # Icyiza ni ugukora return render_template('confirmation.html')

if __name__ == '__main__':
    # Iki cyerekezo kibanza kugerageza gushaka 'templates' folder na 'static' folder
    app.run(debug=True) # debug=True ituma ihinduka ryose ririboneka
    
    
    
    
    # app.py - Python Backend (Harimo Database ya SQLite)
from flask import Flask, render_template, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

# 1. Gutegura Application na Database
app = Flask(__name__)
# Gushyira database mu dosiye imwe mu folder ya Saloon
# Izitwa 'salon_bookings.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon_bookings.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

# 2. Gukora Uburanga bwa Data (Model)
# Iyi Class igaragaza uburyo buri 'booking' buzabikwa muri Database
#class Booking(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  name = db.Column(db.String(100), nullable=False)
   # email = db.Column(db.String(100), nullable=False)
    #service = db.Column(db.String(100), nullable=False)
    #date = db.Column(db.String(20), nullable=False)
    #time = db.Column(db.String(10), nullable=False)
    #timestamp = db.Column(db.DateTime, default=datetime.utcnow)
   
# 3. Kurema Database iyo application itangiye
#with app.app_context():
    # Iki kirema dosiye 'salon_bookings.db' niba idahari
 #   db.create_all()

# 4. Routes nk'uko twari twabikoze mbere
@app.route('/')
def index():
    # Ubanza gushyira amadosiye ya HTML muri 'templates' folder
    return render_template('index.html')

@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    # Kwakira amakuru
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    date = request.form.get('date')
    time = request.form.get('time')
    
    if not all([name, email, service, date, time]):
        return "Amakuru ntabwo yuzuye! Subira inyuma.", 400

    # >>> IGICE CYO KUREBA N'IKUBAKA MURI DATABASE <<<
    try:
        # A. Kureba niba Isaha idafashwe (Simple Check)
        # Twashobora kongeramo Logic ihamye ya Python kureba amasaha y'akazi (6:00-21:00)
        
        # B. Kureba niba uwo mwanya utarafashwe
        #existing_booking = Booking.query.filter_by(date=date, time=time).first()
        #if existing_booking:
            # Niba umwanya uyafashwe
          #  print(f"ERROR: Umwanya kuri {date} saa {time} wafashwe na {existing_booking.name}.")
            # Tugomba gukora page nshya ivuga ko byanze
         #   return render_template('booking_failed.html', date=date, time=time) 

        # C. Kubika Booking Nshya muri Database
        new_booking = Booking(name=name, email=email, service=service, date=date, time=time)
     #   db.session.add(new_booking)
      #  db.session.commit()
        
        print(f"SUCCESS: Booking ya {name} yemejwe kuri {date} saa {time}.")
        
        # D. Gusubiza Umukiriya kuri Confirmation Page
       # return redirect(url_for('booking_success'))

    except Exception as e:
        print(f"Database Error: {e}")
        return "Hagize ikibazo kibaho mu kwandikisha. Ongera ugerageze.", 500

@app.route('/success')
def booking_success():
    # Wazamara gukora 'confirmation.html'
    return render_template('confirmation.html')

# Route nshya yo kureba bookings zose (Admin only!)
@app.route('/admin-bookings')
def view_bookings():
    # Iri jambo rigaragaza bookings zose. Uzakenera gushyiraho urusaku rwa login/password!
    bookings = Booking.query.order_by(Booking.timestamp.desc()).all()
    # Muri production, washyiraho render_template('admin_page.html', bookings=bookings)
    output = "<h1>Bookings Zose:</h1>"
    for booking in bookings:
        output += f"<p>ID: {booking.id} | Izina: {booking.name} | Serivisi: {booking.service} | Igihe: {booking.date} saa {booking.time}</p>"
    return output


if __name__ == '__main__':
    app.run(debug=True)
    # app.py (Ikosora ku Gice cya Admin)

# Route nshya yo kureba bookings zose (Admin only!)
#@app.route('/admin-bookings')
#def view_bookings():
    # Kugaragaza Bookings zose, zitondekanye kuva ku iheruka (descending)
 #   bookings = Booking.query.order_by(Booking.timestamp.desc()).all()
    
    # Iki ni igice cy'ingenzi! Duhaye Template amakuru (bookings)
    #return render_template('admin_bookings.html', bookings=bookings)