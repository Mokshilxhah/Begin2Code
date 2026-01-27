<p align="center">
  <svg width="100%" height="48" viewBox="0 0 1200 48" xmlns="http://www.w3.org/2000/svg">
    <style>
      .text {
        font-family: 'Inter', sans-serif;
        font-size: 28px;
        font-weight: 700;
        fill: #0d6efd;
      }
      .move {
        animation: slide 18s linear infinite;
      }
      @keyframes slide {
        from { transform: translateX(0); }
        to { transform: translateX(-600px); }
      }
    </style>

    <g class="move">
      <text x="0" y="32" class="text">
        Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;
      </text>
      <text x="600" y="32" class="text">
        Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;Begin2Code&nbsp;&nbsp;&nbsp;
      </text>
    </g>
  </svg>
</p>
>


<p align="center">
  <a href="https://begin2code.onrender.com"><b>🌐 Live Application</b></a>
</p>

---

## ⚡ What is Begin2Code?

**Begin2Code** is a **cloud-deployed EdTech platform** engineered to simulate a real-world learning product — covering **authentication, structured course delivery, transactional emails, dashboards, and scalable backend design**.

This project is not a demo app — it is built with **deployment constraints, production configuration, and interview-level system design** in mind.

---

## ☁️ Deployment & Infrastructure

<p align="center">
  <img src="https://skillicons.dev/icons?i=render,supabase" height="42"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Brevo_logo.svg" height="34"/>
</p>

| Layer | Platform | Reason |
|-----|--------|--------|
| Backend Hosting | **Render** | Zero-ops Flask deployment |
| Database | **Supabase (PostgreSQL)** | Managed, scalable, secure |
| Email | **Brevo SMTP** | Reliable transactional emails |

---

## 🧠 Core Engineering Highlights

- Modular **Flask Blueprint architecture**
- Secure **session-based authentication**
- OTP-based **email verification flow**
- Cloud-native **PostgreSQL integration**
- Environment-driven configuration (no secrets in code)
- Service-layer abstraction for email logic
- Production SMTP (not Gmail hacks)

---

## 🧰 Tech Stack (Compact View)

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,postgresql,html,css,js,bootstrap,git,github" height="36"/>
</p>

---

## 🚀 Functional Capabilities

### 👤 User System
- Register / Login / Logout
- Email OTP verification
- Secure session handling

### 📚 Learning Platform
- Course catalog
- Module-wise structured content
- Notes & learning resources
- Purchase flow with confirmation email

### 📧 Email Engine
- Custom-designed HTML emails
- OTP delivery
- Course purchase confirmation
- SMTP-based (Brevo)

### 📊 Dashboard
- Personalized user dashboard
- Purchased courses tracking
- Clean route separation

---

## 🏗️ Architecture Snapshot
Flask App
├── Blueprints (auth, dashboard)
├── Service Layer (email)
├── Supabase PostgreSQL
├── HTML/Jinja Templates
└── Cloud Deployment (Render)

---

## 🎯 Why This Project Stands Out (Interview POV)

- Uses **real SMTP infrastructure**, not mock email
- Handles **cloud DB + backend hosting separation**
- Clean separation of concerns (routes, services, data)
- Designed under **free-tier production constraints**
- Demonstrates backend decision-making, not just features

---

<p align="center">
  <sub>Mokshil Shah</sub>
</p>
