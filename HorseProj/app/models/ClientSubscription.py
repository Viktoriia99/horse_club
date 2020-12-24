from app import db
import datetime


class ClientSubscription(db.Model):
    __tablename__ = 'ClientsSubscriptions'

    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date, nullable=False, default=datetime.date.today().strftime("%Y-%m-%d"))  # check
    subscription_id = db.Column(db.Integer, db.ForeignKey('Subscriptions.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Clients.id'), nullable=False)
    available_lessons = db.Column(db.Integer, nullable=False, default=0)

    # schedule = db.relationship('Schedule', backref='client_sub', lazy='dynamic')

    def __repr__(self):
        return '<Client {} subscription {}>'.format(self.client_id, self.subscription_id)
