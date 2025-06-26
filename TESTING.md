# django_iberica
![Iberica News|Blog banner](static/image/frontpage.png)

---

## 🧪 TESTING.md

### 📋 Overview

This document outlines the testing procedures for the **Iberica News|Blog** Django project, including manual testing of UI features, Django backend testing, and user story validation.

---

## ✅ Manual Testing

### 🔐 User Authentication

| Feature                 | Test Scenario                                      | Expected Outcome                          | Pass/Fail |
|------------------------|----------------------------------------------------|-------------------------------------------|-----------|
| Register               | New user signs up with valid data                 | Account is created and redirected to login | ✅        |
| Login                  | Valid credentials                                 | Redirect to homepage, Add Post and Logout shown | ✅   |
| Login                  | Invalid credentials                               | Displays error message                     | ✅        |
| Logout                 | Click Logout link                                 | User is logged out, Login/Register shown   | ✅        |

---

### 📝 Post Management

| Feature     | Test Scenario                                 | Expected Outcome                        | Pass/Fail |
|------------|------------------------------------------------|-----------------------------------------|-----------|
| Add Post   | Authenticated user submits valid form          | Post appears on home page               | ✅        |
| Edit Post  | User edits their own post                      | Updates saved and reflected in UI       | ✅        |
| Delete Post| User deletes their own post                    | Post no longer exists                   | ✅        |
| Permissions| Non-owner tries to edit/delete post            | Access denied or redirected             | ✅        |

---

### 🗂️ Categories & Navigation

| Feature      | Test Scenario                        | Expected Outcome                        | Pass/Fail |
|-------------|---------------------------------------|-----------------------------------------|-----------|
| Categories   | Click on a category in navbar         | Posts filtered by selected category     | ✅        |
| Responsive   | Resize browser or test mobile view    | Navbar adapts, dropdown toggles work    | ✅        |

---

### 🔍 Search Functionality

| Feature | Test Scenario                    | Expected Outcome                                 | Pass/Fail |
|--------|-----------------------------------|--------------------------------------------------|-----------|
| Search | Enter a keyword in navbar search  | Results page shows matching post titles/content  | ✅        |
| Search | Enter gibberish                   | Message displays "no results found"             | ✅        |

---

### 🛠️ Admin Dashboard

| Feature       | Test Scenario                                  | Expected Outcome                       | Pass/Fail |
|---------------|-------------------------------------------------|----------------------------------------|-----------|
| Admin Access  | Superuser logs in at /admin/                    | Access to Django admin dashboard       | ✅        |
| Category CRUD | Admin adds/edits/deletes categories             | Changes reflected in navbar            | ✅        |
| Content Mod   | Admin edits or deletes any post/comment         | Changes appear immediately             | ✅        |

---

## 👥 User Story Testing

| User Story                                                                 | Tested? |
|----------------------------------------------------------------------------|---------|
| As a visitor, I can register and log in to post blogs                     | ✅      |
| As a user, I can create, update, and delete my own blog posts            | ✅      |
| As a visitor, I can view blog posts by category or search term           | ✅      |
| As an admin, I can manage users and content via the Django admin panel   | ✅      |

---

## 📱 Responsive Design Testing

Tested using:

- ✅ Google Chrome Developer Tools (mobile/tablet/desktop breakpoints)
- ✅ Safari and Firefox browsers
- ✅ iPhone 14 and Android (Samsung Galaxy S23) physical devices

---

All warnings addressed ✅

---

## 🧪 Known Issues

| Issue                              | Notes                                 |
|-----------------------------------|---------------------------------------|
| Search does not highlight keyword | Enhancement for future version        |

---

## ✅ Final Notes

All core functionality has been tested manually and with unit tests. Project is stable, responsive, and secure based on current requirements.
