# 🚀 Django CMS Backend (DRF)

This project is a **production-ready Content Management System (CMS) backend** built using **Django and Django REST Framework** as part of a backend engineering internship assessment.

It provides APIs for managing website content, courses, careers, forms, and media, which can be consumed by any frontend (e.g., React or Next.js).

---

## 📌 Features

- **Custom User Model:** Secure authentication and user management.
- **Admin Panel:** Fully configured Django admin for effortless content management.
- **Singleton Pages:** Managed content for Home, About, Services, and Career pages.
- **Course Management:** Detailed course structures including modules and FAQs.
- **Career Portal:** Job and internship listings with dynamic application handling.
- **Form Submissions:** Contact forms, demo requests, and admissions with file upload support.
- **Media Management:** Gallery, project portfolios, and partner logo management.
- **REST APIs:** Comprehensive endpoints with filtering, searching, and JSON-based dynamic content.
- **File Validation:** Strict validation for PDF resumes (max 5MB) and image types.

---

## 🛠️ Tech Stack

- **Framework:** Django 4.2+
- **API:** Django REST Framework 3.14+
- **Language:** Python 3.10+
- **Database:** SQLite (Development) / PostgreSQL (Recommended for Production)
- **Image Handling:** Pillow
- **Environment Management:** python-decouple

---

## 📁 Project Structure

```text
cms_backend/
│
├── pages/          # Static & singleton content management
├── courses/        # Course models, modules, and FAQ logic
├── careers/        # Job positions and career page content
├── forms_app/      # Form submission handling & file uploads
├── gallery/        # Media, projects, and partner management
├── users/          # Custom user model and authentication
│
├── cms_backend/    # Project settings and URL configurations
├── media/          # Directory for user-uploaded files
└── manage.py       # Django CLI


## ⚙️ Setup Instructions

1️⃣ Clone Repository
code
Bash
git clone cms_backend
cd cms_backend

2️⃣ Create Virtual Environment
code
Bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate   
# Activate on macOS/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
code
Bash
pip install -r requirements.txt

4️⃣ Setup Environment Variables
Create a .env file in the root directory:
code
Env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

5️⃣ Run Migrations
code
Bash
python manage.py makemigrations
python manage.py migrate

6️⃣ Create Superuser
code
Bash
python manage.py createsuperuser

7️⃣ Run Server
code
Bash
python manage.py runserver

## 🔗 API Endpoints ## 

📄 Pages
GET /api/v1/pages/home/ - Home page data
GET /api/v1/pages/about/ - About page data
GET /api/v1/pages/services/ - Services page data
GET /api/v1/pages/site/meta/ - Site-wide metadata (Logo, Contact, Socials)

🎓 Courses
GET /api/v1/courses/ - List all courses
GET /api/v1/courses/<slug>/ - Individual course details
GET /api/v1/courses/search/?q= - Search courses

💼 Careers
GET /api/v1/careers/page/ - Career page CMS content
GET /api/v1/careers/positions/ - List open jobs/internships
GET /api/v1/careers/positions/<id>/ - Job details

📝 Forms (POST)
POST /api/v1/forms/contact/ - General inquiries
POST /api/v1/forms/demo-request/ - Request a demo
POST /api/v1/forms/admission/ - Course admissions
POST /api/v1/forms/internship-apply/<id>/ - Apply for a position

🖼️ Gallery & Media
GET /api/v1/gallery/ - All gallery items
GET /api/v1/gallery/projects/ - Portfolio projects
GET /api/v1/gallery/partners/ - Partner logos

🔐 Admin Panel
Access the dashboard at: http://127.0.0.1:8000/admin/
Key features for Admins:
Full CRUD on courses and modules.
Review and download form submissions (Resumes/PDFs).
Update site-wide metadata (SEO, Contact info).
Manage job openings and internship listings.

📦 Validation Features
File Uploads: Restricted to PDF only for resumes; size limit 5MB.
Images: Format validation for JPG, PNG, and WebP.
Data Integrity: JSON field structure validation for dynamic sections.
Fields: Built-in email and phone number format enforcement.

## 🚀 Production Notes
Change DEBUG to False in .env.
Use Gunicorn or Uvicorn as the WSGI/ASGI server.
Set up Nginx for reverse proxy and static file serving.
Connect a production database like PostgreSQL.
Configure AWS S3 or Cloudinary for media file storage.

## 👨‍💻 Author
Paras Rathour
⭐ Submission Notes
This project fulfills the following requirements:
Implementation of all 18+ required models.
Clean, decoupled Django app architecture.
Full Admin Panel customization.
Robust REST API suite with proper status codes.
File upload handling and validation logic.