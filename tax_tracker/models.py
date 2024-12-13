from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True, index=True)
    industry = db.Column(db.String(100))

    tax_records = db.relationship('TaxRecord', backref='company', lazy=True)

class TaxRecord(db.Model):
    __tablename__ = 'tax_records'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False,index=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default='unpaid')
    due_date = db.Column(db.Date, nullable=False)
