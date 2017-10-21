from flask import Flask
import os


suggestion_server_app = Flask(__name__)


@suggestion_server_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    return 'lol'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    suggestion_server_app.run(port=port)
