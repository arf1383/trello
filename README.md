# Trello-like Task Management Platform

<div align="center">
  <img src="https://img.shields.io/badge/Django-3.2-green?style=flat-square&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/PostgreSQL-14-blue?style=flat-square&logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/REST%20API-DRF-orange?style=flat-square&logo=fastapi" alt="DRF">
</div>

---

<p align="center">
  <b>پلتفرم مدیریت کارها و همکاری تیمی شبیه Trello با Django</b>
</p>

---

## ✨ ویژگی‌ها

- <b>ورک‌اسپیس (Workspace):</b> ایجاد و مدیریت ورک‌اسپیس‌ها با قابلیت عضویت چند کاربر و تعیین نقش (عضو، ادمین و ...)
- <b>برد (Board):</b> ساخت بردهای مختلف برای هر ورک‌اسپیس جهت دسته‌بندی تسک‌ها
- <b>تسک (Task):</b> ایجاد، ویرایش و تخصیص تسک به اعضا با وضعیت، لیبل و تاریخ‌های مختلف
- <b>گزارش‌ها:</b> مشاهده گزارش‌های روزانه و ماهانه از انجام کارها
- <b>سیستم احراز هویت:</b> ثبت‌نام، ورود و خروج کاربران
- <b>رابط کاربری وب:</b> صفحات HTML با Bootstrap و قالب‌بندی مناسب برای مدیریت آسان‌تر
- <b>API:</b> ارائه API برای مدیریت برد، تسک، وضعیت و لیبل با سطح دسترسی مناسب (فقط اعضای گروه board_admin مجاز به مدیریت کامل هستند)
- <b>مستندسازی Swagger:</b> مستندات API با drf-yasg و دسترسی از طریق `/swagger/`

---

## 🗂️ ساختار پروژه

```
trello/
├── boards/                # اپلیکیشن مدیریت برد و تسک
├── hello/                 # اپلیکیشن مدیریت پیام‌ها، ورک‌اسپیس و کاربران
├── web_django/            # تنظیمات پروژه Django
├── manage.py              # اسکریپت مدیریت Django
├── requirements.txt       # وابستگی‌های پروژه
├── Dockerfile             # فایل داکر برای اجرای پروژه
├── docker-compose.yml     # اجرای پروژه و دیتابیس با Docker
└── README.md              # این فایل
```

---

## ⚙️ نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.11+
- PostgreSQL
- [pip](https://pip.pypa.io/en/stable/)
- (اختیاری) Docker و Docker Compose

### مراحل نصب

1. <b>کلون کردن مخزن:</b>
   ```bash
   git clone <repo-url>
   cd trello
   ```
2. <b>ساخت محیط مجازی و نصب وابستگی‌ها:</b>
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. <b>تنظیم دیتابیس:</b>
   - یک دیتابیس PostgreSQL بسازید و اطلاعات آن را در `web_django/settings.py` وارد کنید.
4. <b>اجرای مهاجرت‌ها:</b>
   ```bash
   python manage.py migrate
   ```
5. <b>ساخت ابرکاربر (اختیاری):</b>
   ```bash
   python manage.py createsuperuser
   ```
6. <b>اجرای سرور:</b>
   ```bash
   python manage.py runserver
   ```
7. <b>(اختیاری) اجرای پروژه با Docker:</b>
   ```bash
   docker-compose up --build
   ```

---

## 🧪 اجرای تست‌ها

برای اجرای تست‌های پروژه:
```bash
python manage.py test
```

---

## 🚪 نقاط ورود مهم

- <b>صفحه اصلی:</b> `/`
- <b>ورود:</b> `/login/`
- <b>ثبت‌نام:</b> `/register/`
- <b>لیست ورک‌اسپیس‌ها:</b> `/workspaces/`
- <b>مستندات API:</b> `/swagger/`
- <b>API بردها:</b> `/boards/api/boards/`

---

## 🔐 دسترسی‌ها و سطوح کاربری

- فقط اعضای گروه <b>board_admin</b> می‌توانند برد و تسک را از طریق API مدیریت کنند.
- اعضای ورک‌اسپیس می‌توانند تسک‌ها و بردهای مربوط به ورک‌اسپیس خود را مشاهده کنند.

---

## 👨‍💻 توسعه‌دهندگان

- [نام شما یا تیم توسعه‌دهنده]

---

## 📄 لایسنس

این پروژه تحت لایسنس MIT ارائه می‌شود.

---

## 🗺️ دیاگرام ارتباطی مدل‌ها

```mermaid
erDiagram
    USER ||--o{ WORKSPACE : member
    WORKSPACE ||--o{ BOARD : has
    BOARD ||--o{ TASK : has
    TASK }o--|| USER : assigned_to
    TASK }o--|| STATUS : status
    TASK }o--o{ LABEL : labels
    STATUS ||--o{ TASK : used_in
    LABEL ||--o{ TASK : tagged
