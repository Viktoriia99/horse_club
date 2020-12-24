from app import db


class Plan(db.Model):
    __tablename__ = 'Plans'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False)

    #sub = db.relationship('Subscription', backref='plan', lazy='dynamic')

    def __repr__(self):
        return '<Plan amount {} with discount in {}% >'.format(self.amount, self.discount)
