# **Tax Payment Tracking System**


This project is a Tax and Payment Tracking System for small businesses like LLCs, S-Corps, or C-Corps. It allows users 
to track tax payments, manage tax records, and view tax breakdowns dynamically. The project is built using Flask, MySQL,
Bootstrap, and integrated with Flask-Migrate for database management.



## **Project Overview**

### **Features**

#### **Manage Companies:**

* Add new companies.
* Edit existing company details (name and industry).

#### **Manage Tax Records:**

* Add new tax payment records.
* Edit existing tax records.
* Delete tax records with confirmation prompts.

#### **Dynamic Tax Summary:**

* Filter tax records by due dates (April 15, June 15, September 15, January 15 of the next year).
* Enter a tax rate to calculate the tax due dynamically.

#### **Responsive UI:**

* Built using Bootstrap for a clean and modern look.
* Scrollable tables for handling large datasets.

#### **Database Migrations:**

* Flask-Migrate integrated for smooth database schema migrations.


## **Tech Stack**

* Backend: Flask (Python)
* Database: MySQL
* Frontend: Bootstrap 5, HTML, JavaScript (with Fetch API)
* Database Migration: Flask-Migrate
* ORM: SQLAlchemy



## **Database Schema**

The project uses two main tables:

#### **Company Table:**

* id: Primary key.
* name: Company name (unique, indexed).
* industry: Industry type (indexed).

#### **TaxRecord Table:**

* id: Primary key.
* company_id: Foreign key (references Company.id).
* amount: Payment amount.
* payment_date: Date of tax payment.
* status: Payment status (paid or unpaid).
* due_date: Due date for the tax payment.


## **Setup Instructions**

### **Prerequisites**

Make sure you have the following installed:

1. Python 3.8+
2. PostgreSQL
3. Flask and required dependencies.

**Step 1: Clone the Repository**

`git clone <repository-link>`

`cd tax-payment-tracker`


**Step 2: Install Dependencies**


Create a virtual environment and install the required packages:

**Create virtual environment**

`python3 -m venv venv`

**Activate virtual environment**

`source venv/bin/activate`  # For Linux/Mac

`venv\Scripts\activate`     # For Windows

**Install dependencies**

`pip install -r requirements.txt`


**Step 3: Configure the Database**

```sql
CREATE DATABASE tax_tracker_db;
```

Update the database URI in config.py:

`SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost:5432/tax_tracker_db"`

Replace username, password, and tax_tracker_db with your PostgreSQL credentials and database name.


**Step 4: Initialize the Database**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```



**Step 5: Run the Application**

Start the Flask development server:

`flask run`


Access the application at:

http://127.0.0.1:5000

## **Usage**

1. Manage Companies

Navigate to /companies to add or edit company details.

2. Manage Tax Records

* Navigate to the home page (/).
* Add a new tax record using the form.
* Edit or delete existing tax records.

3. View Tax Summary

Use the "Filter by Due Date" dropdown to view records for a specific due date.
Enter a tax rate (e.g., 6% as 0.06) to calculate the tax due dynamically.





### **Endpoints**

### **API Endpoints**

| **Endpoint**            | **Method** | **Description**                               |
|--------------------------|------------|-----------------------------------------------|
| `/`                     | GET, POST  | Add new tax records and view all records.     |
| `/edit/<int:id>`        | GET, POST  | Edit an existing tax record.                  |
| `/delete/<int:id>`      | POST       | Delete a tax record.                          |
| `/companies`            | GET, POST  | Add and view companies.                       |
| `/companies/edit/<id>`  | GET, POST  | Edit an existing company.                     |
| `/filter_summary`       | GET        | Filter tax records by due date and tax rate.  |


