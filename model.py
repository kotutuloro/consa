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
                               order_by="Concert.start_datetime",
                               secondary="users_concerts",
                               backref="users")

    def add_concert(self, songkick_id):
        """Add concert to user's list of saved concerts

        Adds association betwen user and the concert from the UserConcert table
        Return True if successful, False if unsuccessful
        """

        # Create new row in users_concerts table
        new_assoc = UserConcert(songkick_id=songkick_id,
                                user_id=self.user_id)

        # Add and commit new association and return True if successful
        try:
            db.session.add(new_assoc)
            db.session.commit()
            return True

        # Rollback transaction and return False if not successful
        except Exception, msg:
            db.session.rollback()
            print msg
            return False

    def remove_concert(self, songkick_id):
        """Removes concert from user's list of saved concerts

        Removes association betwen user and the concert from the UserConcert table
        Return True if successful, False if unsuccessful
        """

        # Delete all associations in users_concerts table between this user and concert
        # Return True if successful
        try:
            UserConcert.query.filter(UserConcert.songkick_id == songkick_id,
                                     UserConcert.user_id == self.user_id).delete()
            db.session.commit()
            return True

        # Rollback transaction and return False if not successful
        except Exception, msg:
            db.session.rollback()
            print msg
            return False

    def __repr__(self):
        return ("<User user_id={} email={}>"
                .format(self.user_id, self.email))


class Concert(db.Model):
    """Concerts"""

    __tablename__ = "concerts"

    songkick_id = db.Column(db.Integer,
                            primary_key=True)
    songkick_url = db.Column(db.String(256))
    artist = db.Column(db.String(64),
                       nullable=False)
    spotify_id = db.Column(db.String(64))
    venue = db.Column(db.String(64))
    city = db.Column(db.String(64))
    start_datetime = db.Column(db.DateTime)
    display_name = db.Column(db.String(128))

    @classmethod
    def create_from_form(cls, form):
        """Instantiate a new Concert using concert information from a form"""

        # Get concert data from form
        songkick_id = form.get('songkick-id')
        songkick_url = form.get('songkick-url')
        artist = form.get('artist')
        spotify_id = form.get('spotify-id')
        venue = form.get('venue')
        city = form.get('city')
        start_datetime = form.get('start-datetime')
        display_name = form.get('display_name')

        # Create new concert object from data
        new_concert = cls(songkick_id=songkick_id,
                          songkick_url=songkick_url,
                          artist=artist,
                          spotify_id=spotify_id,
                          venue=venue,
                          city=city,
                          start_datetime=start_datetime,
                          display_name=display_name,
                          )

        # Add and commit new concert and return True if successful
        try:
            db.session.add(new_concert)
            db.session.commit()
            return True

        # Rollback session and return False if unsuccessful
        except Exception, msg:
            db.session.rollback()
            print msg
            return False

    def __repr__(self):
        return ("<Concert songkick_id={} display_name={}>"
                .format(self.songkick_id, self.display_name))


class UserConcert(db.Model):
    """Association table between users and their saved concerts"""

    __tablename__ = "users_concerts"

    user_concert_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    songkick_id = db.Column(db.Integer,
                            db.ForeignKey('concerts.songkick_id'),
                            nullable=False)

    def __repr__(self):
        return ("<UserConcert user_id={} songkick_id={}>"
                .format(self.user_id, self.songkick_id))


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
