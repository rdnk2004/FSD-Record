# Full Stack Development (FSD) - Academic Record & Lab Exercises

A comprehensive repository housing Full Stack Web Development lab exercises, code samples, and web applications built across core technologies including **HTML5**, **CSS3**, **JavaScript**, and **Python / Django Framework**.

---

## 📁 Repository Organization

```text
FSD-Record/
├── HTML-CSS-JS-FSD/         # Cycle 1: Web Development Fundamentals (HTML, CSS, JavaScript)
│   ├── index.html           # Tribute Page (Franz Beckenbauer)
│   ├── bill_generator.html  # Interactive Bill & Invoice Generator
│   ├── result_calculator.html# Student Grade & Result Calculator
│   ├── employee_report.html # Employee Salary & Performance Report Generator
│   ├── restaurant.html      # Restaurant Menu & Order System
│   ├── product.html         # Product Showcase & Catalog Page
│   ├── gallery.html         # Responsive Image Gallery
│   ├── event.html           # Event Registration & Handling
│   ├── survey.html          # Dynamic Survey Form
│   ├── register.html        # User Registration Form
│   ├── password-toggle.html # Password Show/Hide Toggle Utility
│   ├── color_changer.html   # Dynamic Theme / Color Changer
│   ├── font-sizer.html      # Dynamic Font Size Adjuster
│   ├── image_switcher.html  # Interactive Image Carousel / Switcher
│   ├── parallax.html        # Parallax Effect Webpage
│   ├── greeting.html        # Dynamic Time-based Greeting
│   └── wikipedia.html       # Wikipedia Replica Article Page
│
├── FSD-Django-Record/       # Cycle 2: Full-Stack Web Applications (Django Framework)
│   ├── product_inventory/   # Program 1: Product Inventory Management System
│   ├── course_registration/ # Program 2: Student Course Registration System
│   ├── employee_management/ # Program 3: Department & Employee Management System
│   └── flight_booking/      # Program 4: Flight Booking System
│
└── README.md                # Main Academic Record Documentation
```

---

## 🚀 Module Overview

### 🎨 Cycle 1: HTML, CSS & JavaScript Fundamentals (`HTML-CSS-JS-FSD`)

This directory contains frontend web development exercises focusing on semantic structure, styling, dynamic DOM manipulation, form validation, and event handling.

| Category | File Name | Description | Key Technologies |
| :--- | :--- | :--- | :--- |
| **Interactive Utilities** | `bill_generator.html` | Dynamic itemized bill & invoice calculator. | DOM Manipulation, JS Logic |
| | `result_calculator.html` | Calculates total marks, average, percentage, and grade classification. | JS Calculations, Form Inputs |
| | `employee_report.html` | Generates employee payroll, allowances, deductions, and net salary reports. | Dynamic Table DOM Rendering |
| | `password-toggle.html` | Interactive password visibility show/hide toggle input. | JS Event Listeners |
| | `color_changer.html` | Dynamic background and element color switcher tool. | CSS Styles & JS Events |
| | `font-sizer.html` | Dynamic text font size adjuster (increment/decrement). | CSS Style Manipulation |
| | `image_switcher.html` | Interactive image viewer and switcher component. | JS State & DOM Manipulation |
| | `greeting.html` | Dynamic time-based user greeting system. | JS Date API |
| **Pages & Layouts** | `index.html` | Tribute page for legendary footballer Franz Beckenbauer ("Der Kaiser"). | Semantic HTML5, CSS Styling |
| | `restaurant.html` | Restaurant food menu page with custom styling and layout. | CSS Layouts, Forms |
| | `product.html` | Product catalog grid showcase. | CSS Card Design, Flexbox/Grid |
| | `gallery.html` | Responsive image gallery with smooth hover effects. | CSS Layouts & Transitions |
| | `parallax.html` | Multi-layered parallax scrolling web page. | CSS Parallax Properties |
| | `wikipedia.html` | Wikipedia article clone demonstrating typography & content layout. | HTML Formatting, CSS |
| **Forms & Input Handling** | `register.html` | Student/User registration form with structured fields. | Form Controls & Validation |
| | `survey.html` | Custom survey questionnaire form. | Form Controls, Radio/Checkboxes |
| | `event.html` | Event registration and interactive event listener handling. | Form Controls & JS Events |

---

### 🐍 Cycle 2: Full-Stack Web Applications (`FSD-Django-Record`)

Built using **Python 3** and **Django Web Framework**, this section contains modular full-stack CRUD applications featuring relational database models, dynamic template rendering, searching, and filtering.

#### 1. Product Inventory Management System (`product_inventory`)
* **Features**: Category-wise product management, stock update/tracking, case-insensitive product search, and deletion.
* **Key Models**: `Category`, `Product`
* **Location**: `FSD-Django-Record/product_inventory`

#### 2. Course Registration System (`course_registration`)
* **Features**: Student registration, course creation & management, student-course enrollment mapping with semester tracking, and search functionality.
* **Key Models**: `Student`, `Course`, `Enrollment`
* **Location**: `FSD-Django-Record/course_registration`

#### 3. Employee Management System (`employee_management`)
* **Features**: Department creation, employee profile management (Name, ID, Email, Salary, Department), department-wise filtering, and name search.
* **Key Models**: `Department`, `Employee`
* **Location**: `FSD-Django-Record/employee_management`

#### 4. Flight Booking System (`flight_booking`)
* **Features**: Flight search by origin/destination/keyword, flight details cards & available seats tracking, instant flight booking, passenger booking history table with cancellations, CRUD flight management dashboard (Add, Edit, Delete flights), and Django Admin integration.
* **Key Models**: `Flight`, `Booking`
* **Location**: `FSD-Django-Record/flight_booking`


---

## ⚙️ Getting Started & Execution Guide

### Prerequisites
* Web Browser (Chrome, Firefox, Edge, Safari) for HTML/CSS/JS frontend files.
* Python 3.8+ & Django installed for backend Django applications.

---

### Running Frontend Exercises (`HTML-CSS-JS-FSD`)
Directly open any `.html` file in a web browser, or serve using a local HTTP server:

```bash
cd HTML-CSS-JS-FSD
python -m http.server 8000
```
Then visit `http://localhost:8000/` in your browser.

---

### Running Django Projects (`FSD-Django-Record`)

1. **Navigate to the Django directory**:
   ```bash
   cd FSD-Django-Record
   ```

2. **Activate Virtual Environment & Install Django**:
   ```powershell
   # On Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install django
   ```

3. **Launch a specific project**:
   - **Product Inventory**:
     ```powershell
     cd product_inventory
     python manage.py runserver
     ```
   - **Course Registration**:
     ```powershell
     cd course_registration
     python manage.py runserver
     ```
   - **Employee Management**:
     ```powershell
     cd employee_management
     python manage.py runserver
     ```

4. Access the web applications at `http://127.0.0.1:8000/`.

---

## 🛠️ Built With

* **HTML5 / CSS3 / JavaScript (ES6+)** - Core frontend technologies.
* **Python 3** - Backend programming language.
* **Django Web Framework** - MVT architectural framework for web apps.
* **SQLite3** - Relational database engine.
