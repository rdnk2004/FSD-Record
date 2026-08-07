# Full Stack Development (FSD) - Django Lab Record Exercises

This repository contains three independent Django full-stack web applications developed for academic lab exercises and record submission.

---

## 📂 Repository Structure

```text
Django-Cycle2/
├── product_inventory/       # Program 1: Product Inventory Management System
│   ├── manage.py
│   ├── inventory_project/
│   └── inventory_app/
├── course_registration/     # Program 2: Course Registration System
│   ├── manage.py
│   ├── registration_project/
│   └── course_app/
├── employee_management/     # Program 3: Employee Management System
│   ├── manage.py
│   ├── employee_project/
│   └── employee_app/
├── flight_booking/          # Program 4: Flight Booking System
│   ├── manage.py
│   ├── flight_booking_project/
│   └── booking_app/
├── venv/                    # Virtual Environment
├── .gitignore               # Git Ignore Configuration
└── README.md                # Project Documentation
```

---

## 📋 Program Overview

### 1. Product Inventory Management System (`product_inventory`)
* **Question**: Design and develop a Product Inventory Management System using Django that supports category-wise product management, product searching, stock updates, and product deletion.
* **Key Models**: `Category`, `Product`
* **Key Features**:
  - Add, update, view, and delete products.
  - Category-based product filtering.
  - Search products by name using case-insensitive lookup.

### 2. Course Registration System (`course_registration`)
* **Question**: Develop a course registration system using student, course and enrolment models.
* **Key Models**: `Student`, `Course`, `Enrollment`
* **Key Features**:
  - Student registration and details modification.
  - Course creation and management.
  - Student-Course enrollment mapping with semester details.
  - Search enrollments by student name or filter by course.

### 3. Employee Management System (`employee_management`)
* **Question**: Design and develop an Employee Management System using Django that supports department-wise employee management, employee searching, details updating, and employee removal.
* **Key Models**: `Department`, `Employee`
* **Key Features**:
  - Department creation and categorization.
  - Employee profile management (Name, ID, Email, Salary, Department).
  - Department-wise employee filtering and name searching.

### 4. Flight Booking System (`flight_booking`)
* **Question**: Design and develop a flight booking system (Booking table for all display) with an elegant available flights page, Django admin page, models for flight details and bookings, a management page with a table listing all flights with options for updating and deleting, searching flights by criteria, and booking options.
* **Key Models**: `Flight`, `Booking`
* **Key Features**:
  - Available flights display with elegant cards, status badges, and booking options.
  - Flight search & filter by keyword/flight #, origin, and destination.
  - Flight Booking table displaying all passenger bookings with cancellation options.
  - Flight Management Dashboard with full CRUD table (Add, Update, Delete flight records).
  - Django Admin interface for model management (`/admin/`).

---

## ⚙️ Prerequisites & Setup Instructions

### 1. Clone or Open the Repository
```bash
cd "Django-Cycle2"
```

### 2. Activate Virtual Environment & Install Dependencies
```powershell
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Install Django if needed:
pip install django
```

---

## 🚀 Running the Projects

Each exercise is contained within its own dedicated folder. Navigate into any project directory to run its development server.

### Option A: Run Product Inventory Management
```powershell
cd product_inventory
python manage.py runserver
```
* Access at: `http://127.0.0.1:8000/`

### Option B: Run Course Registration System
```powershell
cd course_registration
python manage.py runserver
```
* Access at: `http://127.0.0.1:8000/`

### Option C: Run Employee Management System
```powershell
cd employee_management
python manage.py runserver
```
* Access at: `http://127.0.0.1:8000/`

### Option D: Run Flight Booking System
```powershell
cd flight_booking
python manage.py runserver
```
* Access at: `http://127.0.0.1:8000/`
* Admin Access at: `http://127.0.0.1:8000/admin/` (User: `admin`, Pass: `admin123`)


---

## 📝 Database Migrations

Database tables (`db.sqlite3`) are already migrated and pre-seeded with sample initial data. To re-apply migrations manually:

```powershell
python manage.py makemigrations
python manage.py migrate
```
