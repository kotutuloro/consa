from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """App users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    email = db.Column(db.String(64),
                      nullable=False,
                      unique=True)
    password = db.Column(db.String(64),
                         nullable=False)

    concerts = db.relationship("Concert",
                               secondary="users_concerts",
                               backref="users")

    def __repr__(self):
        return ("<User user_id={} email={}>"
                .format(self.user_id, self.email))


class Concert(db.Model):
    """Concerts"""

    __tablename__ = "concerts"

    concert_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    songkick_id = db.Column(db.Integer,
                            nullable=False)
    songkick_url = db.Column(db.String(256))
    artist = db.Column(db.String(64),
                       nullable=False)
    venue = db.Column(db.String(64))
    city = db.Column(db.String(64))
    start_datetime = db.Column(db.DateTime)

    def __repr__(self):
        return ("<Concert concert_id={} artist={}>"
                .format(self.concert_id, self.artist))


class UserConcert(db.Model):
    """Association table between users and their saved concerts"""

    __tablename__ = "users_concerts"

    user_concert_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    concert_id = db.Column(db.Integer,
                           db.ForeignKey('concerts.concert_id'),
                           nullable=False)

    def __repr__(self):
        return ("<UserConcert user_id={} concert_id={}>"
                .format(self.user_id, self.concert_id))


##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///spotapp'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # If this module is run interactively, it will still be
    # able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
