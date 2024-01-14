# Car Rental Feedback Site

Welcome to the Car Rental Feedback Site, a basic yet functional web application designed to facilitate user feedback on car rentals. This project is an educational endeavor to deepen my understanding of Django, focusing on the implementation of Django Forms and Model Forms. Users can post reviews about their car rental experiences, which are then stored in a database via Django models. An admin page is available to oversee and manage these reviews.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Access](#admin-access)

## Features

- **User Reviews:** Users can post reviews about their car rental experiences.
- **Persistent Data Storage:** Reviews are saved in a database using Django models.
- **Admin Page:** An admin page for administrators to view and manage user reviews.

## Installation

1. Clone the repository to your local machine:

   \```bash
   git clone https://github.com/yourusername/car-rental-feedback.git
   \```

2. Navigate to the project directory:

   \```bash
   cd car-rental-feedback
   \```

## Usage

1. Run database migrations:

   \```bash
   python manage.py migrate
   \```

2. Create a superuser account for admin access:

   \```bash
   python manage.py createsuperuser
   \```

3. Start the development server:

   \```bash
   python manage.py runserver
   \```

4. Access the site at `http://127.0.0.1:8000/` to post reviews.

## Admin Access

- To manage user reviews, access the Django admin panel at `http://127.0.0.1:8000/admin/`.
- Log in with the superuser credentials you created.
- Navigate to the reviews section to view, edit, or delete reviews as needed.
