# Trello-like Task Management Platform

این پروژه یک پلتفرم مدیریت کارها و همکاری تیمی شبیه Trello است که با استفاده از Django و Django REST Framework توسعه داده شده است. کاربران می‌توانند ورک‌اسپیس ایجاد کنند، اعضا را دعوت کنند، برد و تسک بسازند و نقش‌ها و وظایف را مدیریت نمایند.

## ویژگی‌ها

- **ورک‌اسپیس (Workspace):** ایجاد و مدیریت ورک‌اسپیس‌ها با قابلیت عضویت چند کاربر و تعیین نقش (عضو، ادمین و ...).
- **برد (Board):** ساخت بردهای مختلف برای هر ورک‌اسپیس جهت دسته‌بندی تسک‌ها.
- **تسک (Task):** ایجاد، ویرایش و تخصیص تسک به اعضا با وضعیت، لیبل و تاریخ‌های مختلف.
- **گزارش‌ها:** مشاهده گزارش‌های روزانه و ماهانه از انجام کارها.
- **سیستم احراز هویت:** ثبت‌نام، ورود و خروج کاربران.
- **رابط کاربری وب:** صفحات HTML با Bootstrap و قالب‌بندی مناسب برای مدیریت آسان‌تر.
- **API:** ارائه API برای مدیریت برد، تسک، وضعیت و لیبل با سطح دسترسی مناسب (فقط اعضای گروه board_admin مجاز به مدیریت کامل هستند).
- **مستندسازی Swagger:** مستندات API با drf-yasg و دسترسی از طریق `/swagger/`.

## ساختار پروژه

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

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.11+
- PostgreSQL
- [pip](https://pip.pypa.io/en/stable/)
- (اختیاری) Docker و Docker Compose

### مراحل نصب

1. **کلون کردن مخزن:**
   ```bash
   git clone <repo-url>
   cd trello
   ```

2. **ساخت محیط مجازی و نصب وابستگی‌ها:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **تنظیم دیتابیس:**
   - یک دیتابیس PostgreSQL بسازید و اطلاعات آن را در `web_django/settings.py` وارد کنید.

4. **اجرای مهاجرت‌ها:**
   ```bash
   python manage.py migrate
   ```

5. **ساخت ابرکاربر (اختیاری):**
   ```bash
   python manage.py createsuperuser
   ```

6. **اجرای سرور:**
   ```bash
   python manage.py runserver
   ```

7. **(اختیاری) اجرای پروژه با Docker:**
   ```bash
   docker-compose up --build
   ```

## اجرای تست‌ها

برای اجرای تست‌های پروژه:
```bash
python manage.py test
```

## نقاط ورود مهم

- **صفحه اصلی:** `/`
- **ورود:** `/login/`
- **ثبت‌نام:** `/register/`
- **لیست ورک‌اسپیس‌ها:** `/workspaces/`
- **مستندات API:** `/swagger/`
- **API بردها:** `/boards/api/boards/`

## دسترسی‌ها و سطوح کاربری

- فقط اعضای گروه `board_admin` می‌توانند برد و تسک را از طریق API مدیریت کنند.
- اعضای ورک‌اسپیس می‌توانند تسک‌ها و بردهای مربوط به ورک‌اسپیس خود را مشاهده کنند.

## توسعه‌دهندگان

- [نام شما یا تیم توسعه‌دهنده]

## لایسنس

این پروژه تحت لایسنس MIT ارائه می‌شود.

---

### دیاگرام ارتباطی مدل‌ها

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
