## 🛒 হাট-বাজার (HaatBazar) – Grocery Management System

**HaatBazar** is a full-stack grocery management system designed for local markets and small businesses. It offers a beautiful user interface with robust backend functionality. Vendors can efficiently manage their products and handle customer orders through an intuitive dashboard.

### 📌 Tech Stack
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, FastAPI
- **Database**: MySQL
- **Testing**: Pytest
- **DevOps**: Docker

### Screenshot UI

![image](https://github.com/user-attachments/assets/7a90b462-57c4-463a-bc37-4997085c5482)
![image](https://github.com/user-attachments/assets/ee750f67-0704-41c3-adfc-23ab14519001)
![image](https://github.com/user-attachments/assets/760b9f7f-0c50-4afc-898f-f45bf6939a6e)
![image](https://github.com/user-attachments/assets/c152c84f-a92c-4dd2-a715-cb6c314facf0)


### Features

1. ***Product Management***
    - Add, edit, and delete products
    - View product list in table format
    
2. ***Order Management***
    - Create new orders
    - View all orders with details
    - Auto-calculate total price per order

3. Backend API built using FastAPI for managing products and orders

### 🧪 Testing

- Backend API fully tested using **Pytest**
- Modular and maintainable code structure

### 🐳 Docker Support
- Fully Dockerized application

### ⚙️ Installation Guide 

***Prerequisites***
- Python 3.x installed
- MySQL installed and running
- venv (Virtual Environment)

### 🛠️ Setup Instructions

  1. Clone the repository
      ```
      git clone https://github.com/tushar-3549/HaatBazar
      cd HaatBazar
      ```

   2. Create a virtual environment
      ```
      python -m venv venv
      ```

  3. Activate the virtual environment
      ```
      source venv/bin/activate (On macOS/Linux)
      venv\Scripts\activate (On Windows)
      ```

   4. Install the required dependencies
      ```
      pip install -r requirements.txt
      ```
### 🛢️ MySQL Setup
- Start your MySQL server.
- Create a database (eg: grocery_store)
- Create four tables (eg: products, orders, uom, order_details)
### ER Diagram

![grocery_store](https://github.com/user-attachments/assets/85f37ee5-3963-403e-bd55-15c7f5701298)
 
