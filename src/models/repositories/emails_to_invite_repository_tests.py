import pytest 
import uuid
from datetime import datetime, timedelta

from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from .emails_to_invite_repository import EmailsToInviteRepository

from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = '2dea828f-c1ae-4286-b99f-5d637d414cf7'

@pytest.mark.skip(reason='database interaction')
def test_registry_email():
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)

  emails_trips_infos = {
    'id': str(uuid.uuid4()),
    'trip_id': trip_id,
    'email': 'trip@trip.com'
  }

  emails_to_invite_repository.registry_email(emails_trips_infos)

@pytest.mark.skip(reason='database interaction')
def test_find_emails_from_trip():
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)

  emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
  print()
  print(emails)