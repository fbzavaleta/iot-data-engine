from flask import Blueprint, jsonify

from app.engine.core.services.thingspeaks_service import ThingSpeaksService
from app.engine.core.services.engine_service import EngineService
from app.engine.core.enums.http_status import HttpStatus
from flask import jsonify, request

"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

bp = Blueprint("engine", __name__)
bp_v1 = Blueprint("analytics", __name__)


@bp.route("/", methods=["GET"])
def index():
    payload = EngineService().get_api_notes
    return jsonify(payload), HttpStatus.OK.value


@bp.route("/configuration", methods=["POST"])
def configure_engine():
    request_data = request
    payload = EngineService(request=request_data).register_endpoint
    return jsonify(payload), HttpStatus.OK.value


@bp.route("/ingest", methods=["POST"])
def ingest_data():
    request_data = request
    payload = ThingSpeaksService(request=request_data).ingest_channel_description
    return jsonify(payload), HttpStatus.OK.value


@bp_v1.route("/", methods=["GET"])
def index():
    payload = EngineService().get_api_notes
    return jsonify(payload), HttpStatus.OK.value
