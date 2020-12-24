from app import db


class Trainer(db.Model):
    __tablename__ = 'Trainers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, index=True, unique=True)
    phone = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String, mullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)

    # schedule = db.relationship('Schedule', backref='trainer', lazy='dynamic')

    def __repr__(self):
        return '<Trainer {} {}>'.format(self.name, self.surname)
