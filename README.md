# FYP Project - Women-Centric Web Application

Welcome to the FYP Project! This web application is designed to provide a seamless and user-friendly experience for women. Built with Flask, Python, and Bootstrap, the application includes features such as user registration, profile management, and more.

## Features

- User Registration and Authentication
- Profile Management
- Admin Dashboard
- User Account Management
- Responsive Design with Bootstrap

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python (>= 3.x)
- pip (Python package installer)
- Virtual Environment (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/abaidbutt/Fortune-School.git
    cd fyp-project
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    Ensure you have SQLite installed. The project is configured to use SQLite, and the database file (`site.db`) will be created automatically.

5. **Run the application:**

    ```bash
    flask run
    ```

6. **Open your browser and navigate to:**

    ```arduino
    http://127.0.0.1:5000
    ```

## Running the Application

To run the application locally:

1. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the Flask development server:**

    ```bash
    flask run
    ```

3. **Access the application:**

    ```arduino
    http://127.0.0.1:5000
    ```

## Deployment

For deployment, you can use services like Heroku, AWS, or any other cloud provider that supports Flask applications. Ensure you have a `Procfile` and all necessary configurations set up for your deployment environment.

