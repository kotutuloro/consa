from server import app as application
from server import print_referrer
from model import connect_to_db

application.before_request(print_referrer)

connect_to_db(application)

if __name__ == "__main__":

    application.run()


