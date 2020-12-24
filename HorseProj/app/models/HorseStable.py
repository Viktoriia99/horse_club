from app import db


class HorseStable(db.Model):
    __tablename__ = 'HorseStables'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)  # check

    # occupancy = db.relationship('StableOccupancy', backref='stable', lazy='dynamic')

    def __repr__(self):
        return '<Stable {}>'.format(self.number)
