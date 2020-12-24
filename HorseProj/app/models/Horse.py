from app import db


class Horse(db.Model):
    __tablename__ = 'Horses'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Owner.id'), nullable=False)

    # photo = db.relationship('Photo', backref='horse', lazy='dynamic')
    # schedule = db.relationship('Schedule', backref='horse', lazy='dynamic')
    # occupancy = db.relationship('StableOccupancy', backref='horse', lazy='dynamic')

    def __repr__(self):
        return '<Horse {}>'.format(self.nickname)
