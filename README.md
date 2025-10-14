# Hospital-Booking-System

### ✍ Description 
The Hospital Appointment System is a Django-based web application that allows patients to book, view, and manage their medical appointments easily.
Doctors can view their scheduled appointments, and admins can manage doctors and patient records.
The system aims to simplify hospital scheduling, reduce manual errors, and improve communication between patients and healthcare providers

---
### 🚀 Features
- 👨‍💼 Doctor Managment : Doctor can add , view and delete doctor with their specialization
- 📃 Appointments List : display all appointments for both doctor and patient
- ⏰ Patient Appointments : patient can book appointments with availabel doctors
- 🛠 Edit/Delete Appointments : Update or remove existing appointments
- 🔐 User Authentication: Patients can sign up, log in, and log out securely.

---
### 🧱 Technologies Used  
- Backend: Django (Python)
- Database: PostgreSQL
- Frontend: HTML, CSS
- Tools: Git, Visual Studio Code , PostgreSQL , Lucidchart (ERD design)

---
## ScreenShot 📸
### ERD 
<img src="https://git.generalassemb.ly/sundus03/my-project/assets/55694/8dedfc09-bfdb-41a2-90ae-314098ef5c32" width = "400" >

### Homepage
<img src ="https://git.generalassemb.ly/sundus03/my-project/assets/55694/22586b58-96c0-47d4-9ca8-a282640bab06" width ="400">

### Homepage after login
<img src ="https://git.generalassemb.ly/sundus03/my-project/assets/55694/44773629-e6ae-44eb-b496-472f546bbdc5">

---
### 📖 User stories :
-User Sign Up and Login :
First, users (Patient , Doctor) create an account by signing up, providing a username and password. Once registered, they log in to access the app’s features securely.

-Book an appointment :
as a user i want to create a new appointment with a doctor so that i can reserve a date and time for consultation

-View appointment list : 
As a user i want to see all my upcoming appointments , So that I can keep track of my scheduled visits

-Edit appointment :
As a user i want to edit the date or time of my appointment , So that I can reschedule if I am unavailable

-Cancel appointment :
As a user i want to delete an appointment i no longer need , So that the doctor’s schedule remains free for others

-Show doctor list :
As a user i want to see a list of available doctors , So that I can choose which doctor to book an appointment with

---
### 🔍 Install and Run the Project
- Clone the repository:
```
git clone https://github.com/yourusername/hospital-appointment-system.git
cd hospital-appointment-system
```
- Create and activate a virtual environment:
```
python -m venv venv
source venv\Scripts\activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```
- Run server :
```
python manage.py runserver
```
---
## Author Credits👩‍💻
- GitHub: [SundusMoa](https://github.com/SundusMoa)
- Linkedin : [Sundus](www.linkedin.com/in/sundus-abu-baker-152b772b3)









