from flask import Flask
from optparse import OptionParser


suggestion_server_app = Flask(__name__)


@suggestion_server_app.route('/', methods=['GET', 'POST'])
def retrieve_command():
    return 'lol'

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--port", dest="portnum",
                      help="Enter port number for server", metavar=False)
    options, args = parser.parse_args()
    if options.portnum is None:
        suggestion_server_app.run()
    else:
        PORT = int(options.portnum)
        suggestion_server_app.run(host=None, port=PORT)
