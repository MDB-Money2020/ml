from flask import Flask


suggestion_server_app = Flask(__name__)


@suggestion_server_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    return 'lol'

if __name__ == '__main__':
    suggestion_server_app.run()
