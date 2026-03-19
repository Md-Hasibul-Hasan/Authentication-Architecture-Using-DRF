# 🔐 DRF_Auth – Complete JWT Authentication System

![Django](https://img.shields.io/badge/Django-4.x-green)
![DRF](https://img.shields.io/badge/DRF-REST_Framework-red)
![JWT](https://img.shields.io/badge/Auth-JWT-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

DRF_Auth is a production-ready authentication system built with Django REST Framework and JWT (JSON Web Tokens).

It provides secure authentication with:

- User Registration
- Email Verification
- Login
- JWT Token Generation
- Token Refresh & Verify
- Profile Management
- Password Change
- Password Reset via Email

---

# 🚀 Features

- ✅ JWT Authentication (Access & Refresh Tokens)
- ✅ User Registration API
- ✅ Email Verification System
- ✅ Secure Login API
- ✅ Profile API (Protected)
- ✅ Change Password API
- ✅ Send Reset Password Email
- ✅ Reset Password via Token
- ✅ Token Verify & Refresh
- ✅ Admin Panel Support
- ✅ Scalable API Architecture

---

# 📡 Available API Endpoints

## 🔑 Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/user/register/` | Register new user |
| POST | `/api/user/login/` | Login user |
| POST | `/api/user/token/` | Obtain JWT access & refresh tokens |
| POST | `/api/user/token/refresh/` | Refresh access token |
| POST | `/api/user/token/verify/` | Verify token validity |

---

## 📧 Email Verification

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/user/verify-email/<uid>/<token>/` | Verify email address |

---

## 👤 User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/user/profile/` | Get user profile (Protected) |
| POST | `/api/user/change-password/` | Change password |
| POST | `/api/user/send-reset-password-email/` | Send password reset email |
| POST | `/api/user/reset-password/<uid>/<token>/` | Reset password |

---

## 🛠️ Admin Panel

```
/admin/
```

---

# 🔄 Authentication Flow

### 1️⃣ Register User
POST → `/api/user/register/`

### 2️⃣ Verify Email
Click verification link:
```
/api/user/verify-email/<uid>/<token>/
```

### 3️⃣ Login User
POST → `/api/user/login/`

Response:
```json
{
  "access": "access_token_here",
  "refresh": "refresh_token_here"
}
```

### 4️⃣ Access Protected Routes

Include header:

```
Authorization: Bearer your_access_token
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django |
| API Framework | Django REST Framework |
| Auth | JWT (SimpleJWT) |
| Database | SQLite |
| Email | Django Email Backend |

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/DRF_Auth.git
cd DRF_Auth
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If needed:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Run Server

```bash
python manage.py runserver
```

---

# 🔐 JWT Configuration Example

In `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

---

# 📬 Example Login Request

POST `/api/user/login/`

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

---

# 🔮 Future Improvements

- Role-Based Permissions
- Social Login (Google/GitHub)
- Swagger / OpenAPI Documentation
- Account Lockout System
- Rate Limiting
- Two-Factor Authentication (2FA)

---

# 🎯 Learning Outcomes

This project demonstrates:

- JWT Authentication
- Secure Token Handling
- Email Verification Flow
- Password Reset Workflow
- Protected API Endpoints
- REST API Architecture
- Production-Ready Backend Design

---

# 👨‍💻 Author

Md Hasibul Hasan  
Backend Developer (Django & DRF)

---

# 📜 License

This project is developed for educational and portfolio purposes.
