from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
from .models import db, Company, TaxRecord
from .forms import CompanyForm, TaxRecordForm
from datetime import datetime

main_bp = Blueprint('main', __name__)

# --------------------
# Company Management
# --------------------
@main_bp.route('/companies', methods=['GET', 'POST'])
def companies():
    form = CompanyForm()
    if form.validate_on_submit():
        new_company = Company(name=form.name.data, industry=form.industry.data)
        db.session.add(new_company)
        db.session.commit()
        flash("Company added successfully!", "success")
        return redirect(url_for('main.companies'))
    companies = Company.query.all()
    return render_template('company_list.html', form=form, companies=companies)

@main_bp.route('/companies/edit/<int:id>', methods=['GET', 'POST'])
def edit_company(id):
    company = Company.query.get_or_404(id)
    form = CompanyForm(obj=company)
    if form.validate_on_submit():
        company.name = form.name.data
        company.industry = form.industry.data
        db.session.commit()
        flash("Company updated successfully!", "success")
        return redirect(url_for('main.companies'))
    return render_template('edit_company.html', form=form, title="Edit Company")

# --------------------
# Tax Records Management
# --------------------
@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = TaxRecordForm()
    companies = Company.query.all()
    form.company_id.choices = [(c.id, c.name) for c in companies]

    current_year = datetime.now().year
    due_dates = [
        f"04/15/{current_year}", f"06/15/{current_year}",
        f"09/15/{current_year}", f"01/15/{current_year+1}"
    ]
    form.due_date.choices = [(d, d) for d in due_dates]

    if form.validate_on_submit():
        new_record = TaxRecord(
            company_id=form.company_id.data,
            amount=form.amount.data,
            payment_date=form.payment_date.data,
            status=form.status.data,
            due_date=datetime.strptime(form.due_date.data, "%m/%d/%Y")
        )
        db.session.add(new_record)
        db.session.commit()
        flash("Tax record saved successfully!", "success")
        return redirect(url_for('main.index'))

    records = TaxRecord.query.all()
    return render_template('list_records.html', form=form, records=records)

@main_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_record(id):
    record = TaxRecord.query.get_or_404(id)
    form = TaxRecordForm(obj=record)

    # Update dropdown values dynamically
    companies = Company.query.all()
    form.company_id.choices = [(c.id, c.name) for c in companies]

    current_year = datetime.now().year
    due_dates = [
        f"04/15/{current_year}", f"06/15/{current_year}",
        f"09/15/{current_year}", f"01/15/{current_year+1}"
    ]
    form.due_date.choices = [(d, d) for d in due_dates]

    if form.validate_on_submit():
        record.company_id = form.company_id.data
        record.amount = form.amount.data
        record.payment_date = form.payment_date.data
        record.status = form.status.data
        record.due_date = datetime.strptime(form.due_date.data, "%m/%d/%Y")
        db.session.commit()
        flash("Tax record updated successfully!", "success")
        return redirect(url_for('main.index'))
    return render_template('edit_tax.html', form=form, title="Edit Tax Record")

@main_bp.route('/delete/<int:id>', methods=['POST'])
def delete_record(id):
    record = TaxRecord.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    flash("Record deleted successfully!", "success")
    return redirect(url_for('main.index'))

# --------------------
# Filter for Due Dates
# --------------------
@main_bp.route('/filter_summary', methods=['GET'])
def filter_summary():
    due_date = request.args.get('due_date')
    tax_rate = float(request.args.get('tax_rate', 0))
    records = TaxRecord.query.filter_by(due_date=datetime.strptime(due_date, "%m/%d/%Y")).all()

    total_amount = sum(record.amount for record in records)
    tax_due = total_amount * tax_rate

    return jsonify({
        "total_amount": total_amount,
        "tax_due": tax_due,
        "records": [
            {"id": r.id, "company": r.company.name, "amount": r.amount, "status": r.status}
            for r in records
        ]
    })
