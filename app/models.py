from app import db


class SModel(db.Model):
    __tablename__ = 'abcobjs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    path= db.Column(db.String(120), index=True, unique=False)
    stat = db.relationship('ModStat', backref='object', uselist=False)
    def ReturnPath(self):
        return str(self.path)
    def __repr__(self):
        return '<{}>'.format(self.path)
class ModStat(db.Model):
    __tablename__ = "stat"
    id = db.Column(db.Integer, primary_key=True)
    model_name=db.Column(db.String(64),db.ForeignKey('abcobjs.name'))
    stat_path=db.Column(db.String(64),unique=False)
    body = db.Column(db.String(2000), index=True, unique=False)

