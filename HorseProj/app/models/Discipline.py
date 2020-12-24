from app import db


class Discipline(db.Model):
    __tablename__ = 'Disciplines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    # sub = db.relationship('Subscription', backref='discipline', lazy='dynamic')

    def __repr__(self):
        return '<Discipline {}>'.format(self.name)
