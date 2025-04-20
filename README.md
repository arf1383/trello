<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <title>پلتفرم مدیریت کارها و همکاری تیمی - Trello Clone</title>
  <link rel="stylesheet" href="assets/readme-style.css">
</head>
<body>
  <div class="container">
    <h1>پلتفرم مدیریت کارها و همکاری تیمی</h1>
    <div class="badges">
      <img src="https://img.shields.io/badge/Django-3.2-green?style=flat-square&logo=django" alt="Django">
      <img src="https://img.shields.io/badge/PostgreSQL-14-blue?style=flat-square&logo=postgresql" alt="PostgreSQL">
      <img src="https://img.shields.io/badge/REST%20API-DRF-orange?style=flat-square&logo=fastapi" alt="DRF">
    </div>
    <p class="project-desc">
      <b>پلتفرم مدیریت کارها و همکاری تیمی شبیه Trello با Django</b>
    </p>

    <h2>🎨 نمونه محیط پروژه</h2>
    <div class="screenshots">
      <img src="images/10.png" alt="نمونه اول" />
      <img src="images/12.png" alt="نمونه دوم" />
      <br/>
      <i>نمونه‌ای از محیط پلتفرم</i>
    </div>

    <h2>✨ ویژگی‌ها</h2>
    <ul>
      <li>🧑‍💼 <b>ورک‌اسپیس (Workspace):</b> ایجاد و مدیریت ورک‌اسپیس‌ها با قابلیت عضویت چند کاربر و تعیین نقش (عضو، ادمین و ...)</li>
      <li>🗂️ <b>برد (Board):</b> ساخت بردهای مختلف برای هر ورک‌اسپیس جهت دسته‌بندی تسک‌ها</li>
      <li>📝 <b>تسک (Task):</b> ایجاد، ویرایش و تخصیص تسک به اعضا با وضعیت، لیبل و تاریخ‌های مختلف</li>
      <li>📊 <b>گزارش‌ها:</b> مشاهده گزارش‌های روزانه و ماهانه از انجام کارها</li>
      <li>🔑 <b>سیستم احراز هویت:</b> ثبت‌نام، ورود و خروج کاربران</li>
      <li>🌐 <b>رابط کاربری وب:</b> صفحات HTML با Bootstrap و قالب‌بندی مناسب برای مدیریت آسان‌تر</li>
      <li>🛠️ <b>API:</b> ارائه API برای مدیریت برد، تسک، وضعیت و لیبل با سطح دسترسی مناسب (فقط اعضای گروه <code>board_admin</code> مجازند)</li>
      <li>📄 <b>مستندسازی Swagger:</b> مستندات API با drf-yasg و دسترسی از طریق <code>/swagger/</code></li>
    </ul>

    <h2>🗂️ ساختار پروژه</h2>
    <pre class="structure"><code>trello/
├── boards/                # 🗂️ اپلیکیشن مدیریت برد و تسک
├── hello/                 # 💬 اپلیکیشن مدیریت پیام‌ها، ورک‌اسپیس و کاربران
├── web_django/            # ⚙️ تنظیمات پروژه Django
├── manage.py              # 🛠️ اسکریپت مدیریت Django
├── requirements.txt       # 📦 وابستگی‌های پروژه
├── Dockerfile             # 🐳 فایل داکر برای اجرای پروژه
├── docker-compose.yml     # 🐳 اجرای پروژه و دیتابیس با Docker
└── README.md              # 📄 این فایل
</code></pre>

    <h2>⚙️ نصب و راه‌اندازی</h2>
    <h3>پیش‌نیازها</h3>
    <ul>
      <li>🐍 Python 3.11+</li>
      <li>🐘 PostgreSQL</li>
      <li>📦 <a href="https://pip.pypa.io/en/stable/">pip</a></li>
      <li>🐳 (اختیاری) Docker و Docker Compose</li>
    </ul>
    <h3>مراحل نصب</h3>
    <ol>
      <li><b>کلون کردن مخزن:</b>
        <pre><code>git clone &lt;repo-url&gt;
cd trello
</code></pre>
      </li>
      <li><b>ساخت محیط مجازی و نصب وابستگی‌ها:</b>
        <pre><code>python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
</code></pre>
      </li>
      <li><b>تنظیم دیتابیس:</b> یک دیتابیس PostgreSQL بسازید و اطلاعات آن را در <code>web_django/settings.py</code> وارد کنید.</li>
      <li><b>اجرای مهاجرت‌ها:</b>
        <pre><code>python manage.py migrate
</code></pre>
      </li>
      <li><b>ساخت ابرکاربر (اختیاری):</b>
        <pre><code>python manage.py createsuperuser
</code></pre>
      </li>
      <li><b>اجرای سرور:</b>
        <pre><code>python manage.py runserver
</code></pre>
      </li>
      <li><b>(اختیاری) اجرای پروژه با Docker:</b>
        <pre><code>docker-compose up --build
</code></pre>
      </li>
    </ol>

    <h2>🧪 اجرای تست‌ها</h2>
    <pre><code>python manage.py test
</code></pre>

    <h2>🚪 نقاط ورود مهم</h2>
    <ul>
      <li>🏠 <b>صفحه اصلی:</b> <code>/</code></li>
      <li>🔐 <b>ورود:</b> <code>/login/</code></li>
      <li>📝 <b>ثبت‌نام:</b> <code>/register/</code></li>
      <li>🗂️ <b>لیست ورک‌اسپیس‌ها:</b> <code>/workspaces/</code></li>
      <li>📄 <b>مستندات API:</b> <code>/swagger/</code></li>
      <li>🛠️ <b>API بردها:</b> <code>/boards/api/boards/</code></li>
    </ul>

    <h2>🔐 دسترسی‌ها و سطوح کاربری</h2>
    <ul>
      <li>فقط اعضای گروه <b>🛡️ board_admin</b> می‌توانند برد و تسک را از طریق API مدیریت کنند.</li>
      <li>اعضای ورک‌اسپیس می‌توانند تسک‌ها و بردهای مربوط به ورک‌اسپیس خود را مشاهده کنند.</li>
    </ul>

    <h2>👨‍💻 توسعه‌دهندگان</h2>
    <ul>
      <li><span title="Alireza Rahmani Firouzja">👨‍💻 Alireza Rahmani Firouzja</span></li>
    </ul>

    <h2>📄 لایسنس</h2>
    <p>این پروژه تحت لایسنس MIT ارائه می‌شود.</p>

    <h2>🗺️ دیاگرام ارتباطی مدل‌ها</h2>
    <pre><code>USER ||--o{ WORKSPACE : member
WORKSPACE ||--o{ BOARD : has
BOARD ||--o{ TASK : has
TASK }o--|| USER : assigned_to
TASK }o--|| STATUS : status
TASK }o--o{ LABEL : labels
STATUS ||--o{ TASK : used_in
LABEL ||--o{ TASK : tagged
</code></pre>
  </div>
</body>
</html>
