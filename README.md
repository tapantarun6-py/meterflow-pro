# 🚀 MeterFlow – Usage-Based API Billing Platform

MeterFlow is a full-stack SaaS platform that allows developers to create APIs, generate API keys, track usage, and calculate billing based on requests.

---

## 📌 Features

* 🔐 User Authentication (JWT-based login)
* 🔑 API Key Generation
* 📊 Usage Tracking (per request)
* 💰 Billing Calculation (usage-based)
* ⚡ FastAPI backend for high performance
* 🎨 React frontend dashboard

---

## 🧱 Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite (can upgrade to PostgreSQL)
* JWT Authentication

### Frontend

* React (Create React App)
* Fetch API

---

## 📁 Project Structure

meterflow-pro/
│
├── backend/
│   └── app/
│       ├── api/
│       ├── core/
│       ├── models/
│       ├── schemas/
│       ├── services/
│       └── main.py
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       └── App.js

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/meterflow-pro.git
cd meterflow-pro

---

### 2️⃣ Backend Setup

cd backend
pip install -r requirements.txt

Run server:
uvicorn app.main:app --reload

👉 Backend runs on:
http://127.0.0.1:8000

---

### 3️⃣ Frontend Setup

cd frontend
npm install
npm start

👉 Frontend runs on:
http://localhost:3000

---

## 🧪 API Endpoints

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| POST   | /login        | User login       |
| POST   | /generate-key | Generate API key |
| GET    | /use-api      | Track API usage  |
| GET    | /analytics    | View analytics   |

---

## 🔐 Demo Credentials

Username: tarun1206
Password: ttt111

---

## 📊 How It Works

1. User logs in
2. Generates an API key
3. Makes API calls
4. System tracks usage
5. Billing is calculated automatically

---

## 🚀 Future Improvements

* 🔥 Redis-based rate limiting
* 💳 Stripe payment integration
* 📈 Advanced analytics dashboard
* 🏢 Multi-tenant support
* 🌐 Deployment on AWS / Render

---

## 💼 Resume Description

**MeterFlow – API Billing Platform**

* Built a scalable API usage tracking and billing system
* Implemented JWT authentication and API key management
* Developed full-stack app using FastAPI and React
* Designed usage-based pricing engine

---

## 📄 License

This project is open-source and free to use.

---

## 🙌 Author

**Tarun Tapan Tripathy**
