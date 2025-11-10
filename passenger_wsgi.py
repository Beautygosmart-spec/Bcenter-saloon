# passenger_wsgi.py
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app import app as application # Iyi ni yo itangiza app yawe!