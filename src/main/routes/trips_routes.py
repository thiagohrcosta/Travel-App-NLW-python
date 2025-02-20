from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint('trip_routes', __name__)

from src.controllers.trip_creator import TripCretor
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_creator import ParticipantCreator
from src.controllers.activity_creator import ActivityCreator

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

from src.models.settings.db_connection_handler import db_connection_handler

@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  emails_repository = EmailsToInviteRepository(conn)
  controller = TripCretor(trips_repository, emails_repository)

  response = controller.create(request.json)

  return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>', methods=['GET'])
def find_trip(trip_id):
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  controller = TripFinder(trips_repository)

  response = controller.find_trip_details(trip_id)

  return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>/confirm', methods=['GET'])
def confirm_trip(trip_id):
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  controller = TripConfirmer(trips_repository)

  response = controller.confirm(trip_id)

  return jsonify(response['body']), response['status_code']

@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
def create_trip_link(trip_id):
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  controller = LinkCreator(links_repository)

  response = controller.create(request.json, trip_id)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<trip_id>/links", methods=["GET"])
def find_trip_link(trip_id):
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  controller = LinkFinder(links_repository)

  response = controller.find(trip_id)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<trip_id>/invites", methods=["POST"])
def invite_to_trip(trip_id):
  conn = db_connection_handler.get_connection()
  participants_repository = ParticipantRepository(conn)
  emails_repository = EmailsToInviteRepository(conn)
  controller = ParticipantCreator(participants_repository, emails_repository)

  response = controller.create(request.json, trip_id)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<trip_id>/activities", methods=["POST"])
def create_activity(trip_id):
  conn = db_connection_handler.get_connection()
  activities_repository = ActivitiesRepository(conn)
  controller = ActivityCreator(activities_repository)

  response = controller.create(request.json, trip_id)

