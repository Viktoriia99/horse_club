from app import db


class Client(db.Model):
    __tablename__ = 'Clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, index=True, unique=True)
    phone = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String, mullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)

    # cli_sub = db.relationship('ClientSubscription', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<Client {} {}>'.format(self.name, self.surname)
