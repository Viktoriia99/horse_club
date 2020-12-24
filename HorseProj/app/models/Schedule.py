from app import db


class Schedule(db.Model):
    __tablename__ = 'Schedule'

    id = db.Column(db.Integer, primary_key=True)
    client_sub_id = db.Column(db.Integer, db.ForeignKey('ClientSubscriptions.id'), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('Trainers.id'), nullable=False)
    horse_id = db.Column(db.Integer, db.ForeignKey('Horses.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    begin_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Schedule {} {}>'.format(self.id, self.trainer_id)
