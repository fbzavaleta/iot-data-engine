from flask import Blueprint, jsonify

from engine.core.services import thingspeaks_service
from engine.core.services import engine_service
from engine.core.enums.http_status import HttpStatus
from flask import jsonify, request

bp  =   Blueprint('config', __name__)
bp_v1   =   Blueprint('feed', __name__)


@bp.route('/',  methods=['GET'])
def index():
    payload = engine_service().get_api_notes
    return  jsonify(payload),   HttpStatus.OK.value

@bp.route('/configuration',  methods=['POST'])
def configure_engine():
    return  jsonify(api_notes),   HttpStatus.OK.value    


@bp_v1.route('/',   methods=['GET'])
def index(): 
    payload = engine_service().get_api_notes
    return  jsonify(payload),   HttpStatus.OK.value
