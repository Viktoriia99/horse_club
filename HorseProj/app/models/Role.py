from app import db


class Role(db.Model):
    __tablename__ = 'Roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, nullable=False)

    # client = db.relationship('Client', backref='role', lazy='dynamic')
    # trainer = db.relationship('Trainer', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role {}>'.format(self.role_name)
