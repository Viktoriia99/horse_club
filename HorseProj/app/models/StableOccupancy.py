from app import db
import datetime


class StableOccupancy(db.Model):
    __tablename__ = 'StablesOccupancy'

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date, nullable=False, default=datetime.date.today().strftime("%Y-%m-%d"))  # check
    owner_id = db.Column(db.Integer, nullable=False)
    horse_id = db.Column(db.Integer, db.ForeignKey('Horses.id'), nullable=False)
    stables_id = db.Column(db.Integer, db.ForeignKey('HorseStables.id'), nullable=False)

    def __repr__(self):
        return '<Stable number {}>'.format(self.stables_id)
