from app import db


class Owner(db.Model):
    __tablename__ = 'Owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, index=True, unique=True)
    phone = db.Column(db.String, index=True, unique=True)

    # horse = db.relationship('Horse', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<Owner {}>'.format(self.name)
