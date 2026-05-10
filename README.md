# 🔐 DRF Advanced Authentication System

![Django](https://img.shields.io/badge/Django-5.x-green)
![DRF](https://img.shields.io/badge/DRF-REST_Framework-red)
![JWT](https://img.shields.io/badge/Auth-JWT-blue)
![Security](https://img.shields.io/badge/Security-Advanced-success)
![Status](https://img.shields.io/badge/Status-Production_Ready-success)

A complete advanced authentication system built with Django REST Framework and JWT authentication.

This project provides enterprise-level authentication features including:

- JWT Authentication
- Email Verification
- OTP Verification
- Two-Factor Authentication (2FA)
- Google Login
- Session Management
- Login History Tracking
- Password Reset
- Account Lockout Protection
- Rate Limiting
- Secure Profile Management

---

# ✨ Features

## 🔑 Authentication

- JWT Access & Refresh Tokens
- Token Rotation
- Token Blacklisting
- Secure Login System
- Google OAuth Login
- Protected APIs

## 📧 Email Verification

- Verification Link
- OTP Verification
- Resend Verification Email
- OTP Expiration & Retry Protection

## 🔒 Security Features

- Account Lockout After Failed Login Attempts
- OTP Attempt Limiting
- Rate Limiting
- Refresh Token Blacklisting
- Secure Password Validation
- Logout From All Devices
- Logout From Specific Device

## 🛡️ Two-Factor Authentication (2FA)

- Email-based OTP Authentication
- Enable / Disable 2FA
- 2FA Verification During Login
- 2FA Audit Logs
- 2FA Attempt Locking

## 👤 User Features

- Profile Management
- Profile Image Upload
- Change Password
- Change Email with OTP Verification
- Delete Account

## 📊 Activity Tracking

- Login History
- Device Session Tracking
- IP Address Logging
- User-Agent Tracking

## ⚙️ Admin Features

- Fully Customized Django Admin
- User Session Monitoring
- Login History Monitoring
- 2FA Activity Logs
- Profile Image Preview

---

# 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5 |
| API Framework | Django REST Framework |
| Authentication | SimpleJWT |
| Database | SQLite / PostgreSQL |
| Email Service | Django Email Backend |
| OAuth | Google OAuth |
| Security | JWT Blacklisting + Throttling |

---

# 📡 API Endpoints

## 🔐 Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth_api/register/` | Register user |
| POST | `/auth_api/login/` | Login user |
| POST | `/auth_api/logout/` | Logout current device |
| POST | `/auth_api/logout-all/` | Logout all devices |
| POST | `/auth_api/auth/google/` | Google login |

---

## 📧 Email Verification

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth_api/verify-email/<uid>/<token>/` | Verify email using link |
| POST | `/auth_api/verify-otp/` | Verify email using OTP |
| POST | `/auth_api/resend-verification/` | Resend verification email |

---

## 🔑 JWT Token APIs

| Method | Endpoint |
|---|---|
| POST | `/auth_api/token/` |
| POST | `/auth_api/token/refresh/` |
| POST | `/auth_api/token/verify/` |

---

## 👤 User Profile

| Method | Endpoint |
|---|---|
| GET | `/auth_api/profile/` |
| PATCH | `/auth_api/profile/` |

---

## 🔒 Password Management

| Method | Endpoint |
|---|---|
| POST | `/auth_api/change-password/` |
| POST | `/auth_api/send-reset-password-email/` |
| POST | `/auth_api/reset-password/<uid>/<token>/` |

---

## 📩 Email Change

| Method | Endpoint |
|---|---|
| POST | `/auth_api/change-email/request/` |
| POST | `/auth_api/change-email/confirm/` |

---

## 🛡️ Two-Factor Authentication

| Method | Endpoint |
|---|---|
| POST | `/auth_api/2fa/setup/` |
| POST | `/auth_api/2fa/enable/` |
| POST | `/auth_api/2fa/verify/` |
| POST | `/auth_api/2fa/disable/` |
| GET | `/auth_api/2fa/status/` |

---

## 📊 Activity & Session Management

| Method | Endpoint |
|---|---|
| GET | `/auth_api/login-history/` |
| GET | `/auth_api/active-sessions/` |
| DELETE | `/auth_api/delete-session/<id>/` |

---

## ❌ Account Management

| Method | Endpoint |
|---|---|
| POST | `/auth_api/delete-account/` |

---

# 🔄 Authentication Flow

## Registration Flow

1. User registers
2. Verification email sent
3. User verifies account via:
   - Verification link
   - OR OTP
4. Account becomes active

---

## Login Flow

### Without 2FA

1. User logs in
2. JWT tokens returned
3. Session created

### With 2FA

1. User logs in
2. OTP sent to email
3. User verifies OTP
4. JWT tokens returned

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/drf-advanced-auth.git
cd drf-advanced-auth
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

---

# ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_password
EMAIL_FROM=your_email@gmail.com

FRONTEND_URL=http://localhost:3000
```

---

# 🔐 JWT Configuration

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

---

# 🧪 Example Login Request

## Request

```json
{
  "email": "hasib@example.com",
  "password": "Password123"
}
```

---

## Response

```json
{
  "msg": "Login Successful",
  "token": {
    "refresh": "refresh_token_here",
    "access": "access_token_here"
  },
  "user": {
    "id": 1,
    "name": "Hasib",
    "email": "hasib@example.com"
  }
}
```

---

# 🛡️ Security Features Included

- JWT Authentication
- Refresh Token Rotation
- Refresh Token Blacklisting
- Account Lockout Protection
- OTP Expiration
- OTP Attempt Limiting
- Login Rate Limiting
- Password Validation
- Session Tracking
- Device Logout
- IP Address Logging

---

# 📂 Project Structure

```bash
DRF_Auth/
│
├── auth_api/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   ├── renderers.py
│
├── DRF_Auth/
│   ├── settings.py
│   ├── urls.py
│
├── mediafiles/
├── staticfiles/
├── manage.py
└── README.md
```

---

# 🚀 Future Improvements

- SMS-based OTP
- Authenticator App (TOTP)
- Redis Token Storage
- Docker Support
- Swagger / OpenAPI Documentation
- Email Templates
- OAuth Providers (GitHub/Facebook)
- Role-Based Access Control (RBAC)

---

# 👨‍💻 Author

**Md Hasibul Hasan**

Backend Developer — Django & DRF

---

# 📜 License

This project is intended for educational, portfolio, and production-learning purposes.