from app import db


class Subscription(db.Model):
    __tablename__ = 'Subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lesson_plan_id = db.Column(db.Integer, db.ForeignKey('Planes.id'), nullable=False)
    discipline_id = db.Column(db.Integer, db.ForeignKey('Disciplines.id'), nullable=False)

    # cli_sub = db.relationship('ClientSubscription', backref='subscript', lazy='dynamic')

    def __repr__(self):
        return '<Subscription {}>'.format(self.name)
