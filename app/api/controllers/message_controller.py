from flask import Blueprint

message_controller = Blueprint('message_controller', __name__)

@message_controller.route('/messages', methods=['GET'])
def get_all_messages():
    return 'Hello world!'

@message_controller.route('/messages/<message_id:string>', methods=['GET'])
def get_message(message_id):
    return 'Hello world!'