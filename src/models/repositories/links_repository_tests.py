import pytest 
import uuid

from .links_repository import LinksRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

trip_id = '2dea828f-c1ae-4286-b99f-5d637d414cf7'
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason='database interaction')
def test_registry_link():
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  link_infos = {
    'id': link_id,
    'trip_id': trip_id,
    'link': 'somelink.com',
    'title': 'Hotel Residency'
  }

  link_repository.registry_link(link_infos)

@pytest.mark.skip(reason='database interaction')
def test_find_links_from_trip():
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  response = link_repository.find_links_from_trip(trip_id)

  assert isinstance(response, list)
  assert isinstance(response[0], tuple)

