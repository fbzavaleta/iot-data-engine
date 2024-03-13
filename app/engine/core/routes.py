from flask import Blueprint, jsonify

from engine.core.services import thingspeaks_service


bp  =   Blueprint('config', __name__)
bp_v1   =   Blueprint('feed', __name__)

api_notes = {
    'api_version'   :   1.0,
    'developer'     :   '@fbzavaleta',
    'firmware'      :   'esp-idf',
    'device'        :   'esp32'
}

@bp.route('/',  methods=['GET'])
def index():
    return  jsonify(api_notes),   HttpStatus.OK.value

@bp.route('/conection-sensors',  methods=['POST'])
def recibe_data():
    return  jsonify(api_notes),   HttpStatus.OK.value    


@bp_v1.route('/',   methods=['GET'])
def index(): 
    payload =   ChannelFeed({'device': 'esp32', 'data':{'fiel1':23}})
    return  payload.to_response(),  HttpStatus.OK.value


@bp_v2.route('/',   methods=['GET'])
def index(): 
    pass