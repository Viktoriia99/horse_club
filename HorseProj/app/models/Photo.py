from app import db


class Photo(db.Model):
    __tablename__ = 'Photos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    horse_id = db.Column(db.Integer, db.ForeignKey('Horses.id'), nullable=False)

    def __repr__(self):
        return '<Photo {} of {}>'.format(self.name, self.horse_id)
