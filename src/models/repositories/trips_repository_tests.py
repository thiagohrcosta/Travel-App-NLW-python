import pytest 
import uuid
from datetime import datetime, timedelta

from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect() 
trip_id = '2dea828f-c1ae-4286-b99f-5d637d414cf7'

@pytest.mark.skip(reason='database interaction')
def test_create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_infos = {
    'id': str(uuid.uuid4()),
    'destination': 'Osasco',
    'start_date': datetime.strptime('02-01-2024', '%d-%m-%Y'),
    'end_date': datetime.strptime('02-01-2024', '%d-%m-%Y') + timedelta(days=5),
    'owner_name': 'John Doe',
    'owner_email': 'johndoe@email.com'
  }

  trips_repository.create_trip(trips_infos)

@pytest.mark.skip(reason='database interaction')
def test_find_by_id():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trip = trips_repository.find_trip_by_id(trip_id)
  print(trip)

@pytest.mark.skip(reason='database interaction')
def test_update_trip_stats():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trip = trips_repository.update_trip_status(trip_id)
  print(trip)



