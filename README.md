# Online Course Application (Django Full-Stack)

This is a comprehensive full-stack application built with **Django**, **Python**, and **Bootstrap**. It features a dynamic course management system with an integrated examination and grading module.

## 🚀 Features
- **Course & Lesson Management:** Structured content hierarchy.
- **Automated Examination System:** Multiple-choice questions with automated grading.
- **Admin Dashboard:** Fully configured admin interface for content creators.
- **Bootstrap Styling:** Responsive design for various devices.

## 🛠️ Tech Stack
- **Backend:** Django 3.x / Python 3.x
- **Frontend:** HTML5, CSS3, Bootstrap 4
- **Database:** SQLite (Development)

## 📁 Project Structure
The project consists of the following key components:
- `models.py`: Defines the database schema for Courses, Questions, and Results.
- `views.py`: Handles the backend logic for exam submission and score calculation.
- `admin.py`: Customizes the admin dashboard experience.

---

# تطبيق الكورسات عبر الإنترنت (Django)

هذا تطبيق متكامل تم تطويره باستخدام إطار العمل **Django** ولغة **Python**، ويهدف إلى إدارة المحتوى التعليمي وتقديم نظام امتحانات مؤتمت.

## ✨ المميزات
- **إدارة المحتوى:** تنظيم الدروس والكورسات بشكل هرمي.
- **نظام امتحانات متقدم:** دعم الأسئلة متعددة الخيارات مع حساب تلقائي للدرجات.
- **لوحة تحكم إدارية:** واجهة مخصصة لإدارة المحتوى والأسئلة بسهولة.
- **تصميم متجاوب:** استخدام Bootstrap لضمان عمل الموقع على كافة الشاشات.

## 🚀 كيفية التشغيل (Local Development)
1. قم بتحميل المستودع: `git clone [Your-Repo-URL]`
2. تثبيت المتطلبات: `pip install -r requirements.txt`
3. تشغيل قاعدة البيانات: `python manage.py migrate`
4. تشغيل السيرفر: `python manage.py runserver`
