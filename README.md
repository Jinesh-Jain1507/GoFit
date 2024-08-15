# GoFit

GoFit is a web application designed to help users track and manage their fitness goals. Built with Python and JavaScript, this platform enables users to log workouts, monitor progress, and maintain a healthy lifestyle.

## Features

- **Workout Monitoring**: Track your daily workouts and excercises.
- **Calorie Management**: Visualize your fitness journey with charts and stats.
- **Yoga Assistent**: 50+ Yoga Poses for Yoga lovers along with tutorial and benefits
- **Fitness Chatbot**: Still having doubts? Ask our chatbot to guide you through your fitness journey
- **Responsive Design**: Accessible on both desktop and mobile devices.

## Technologies Used

- **Django**: Python web framework for building the backend of the website.
- **HTML/CSS**: Frontend markup and styling.
- **Bootstrap**: Frontend framework for responsive design.
- **SQLite**: Database system for storing blog posts, comments, and user data.
- **OpenAI API**: API used to create the AI based chatbot

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jinesh-Jain1507/AmbulanceAid.git

2. **Navigate to the project directory**:
   ```bash
   cd Ambulance aid

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv env

4. **Activate the virtual environment**:

   - **On Windows:
     ```bash
     .\env\Scripts\activate
   - **On macOS/Linux:
     ```bash
     source env/bin/activate

5. Install python (https://www.python.org/downloads/) then install django:
   ```bash
   pip install django

6. Create the database schema
   ```bash
   python manage.py migrate

7. Create a superuser (admin user) for accessing the admin panel:
   ```bash
   python manage.py createsuperuser

8. Create a .env file similar to the .env.sample file.
9. Get your API key from [OpenAI](https://platform.openai.com/) and another from [API Ninjas](https://api-ninjas.com/api) add it to the .env file

10. Start the development server:
   ```bash
   python manage.py runserver
  ```
Open your web browser and navigate to http://localhost:8000 to access the website.
