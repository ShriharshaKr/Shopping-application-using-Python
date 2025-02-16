# 🛒 Shopping Application  

## 📌 Overview 
This is a backend-based shopping application built with Python. It allows users to browse products, add items to a cart, proceed to checkout, and make payments. Admins can manage products and categories.

## 🚀 Features 
- User and Admin login with session management.
- Product catalog with multiple categories.
- Shopping cart functionality (add/remove items).
- Secure checkout with multiple payment methods.
- Admin can add, modify, or remove products and categories.

## 🔑 User & Admin Functionality  

### 👤 User Login  
- Enter a valid username and password.  
- If credentials match, a **session ID** is created.  
- Users can then view products, add to cart, and checkout.  

### 🔐 Admin Login  
- Only admins can modify products and categories.  
- If wrong credentials are entered, an **error message** appears.  

### 🛍️ Product & Cart Management  
- Users can **view products**, **add/remove items**, and **checkout**.  
- Admins can **add, modify, and delete products/categories**.  

### 💰 Checkout & Payment  
- Users select a **payment method** (Net Banking, PayPal, UPI).  
- Upon success, an **order confirmation message** is displayed.  

## 🏗️ Future Improvements  
🔹 Add a **GUI version** using Tkinter or Flask.  
🔹 Implement **database storage** instead of in-memory dictionaries.  
🔹 Include an **order history feature** for users.  

## Technologies Used
- **Python** as the programming language.
- **uuid** for session management.
- **sys** for handling system functions.


