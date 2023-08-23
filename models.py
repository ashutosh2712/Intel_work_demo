from Intel_work_demo import db


class Workload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    run_uri = db.Column(db.String(40), nullable=False)
    workload = db.Column(db.String(100), nullable=False)
    testcase = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime)
    cloud = db.Column(db.String(10))
    microarchitecture = db.Column(db.String(100))
    unit = db.Column(db.String(10))
    value = db.Column(db.Integer)
