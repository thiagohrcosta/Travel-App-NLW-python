import uuid
from datetime import datetime, timedelta

from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect() 

def test_create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_infos = {
    'id': str(uuid.uuid4()),
    'destionation': 'Osasco',
    'start_date': datetime.strptime('02-01-2024', '%d-%m-%Y'),
    'end_date': datetime.strptime('02-01-2024', '%d-%m-%Y') + timedelta(days=5),
    'owner_name': 'John Doe',
    'owner_email': 'johndoe@email.com'
  }

  trips_repository.create_trip(trips_infos)

