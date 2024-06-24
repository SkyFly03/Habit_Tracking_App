# Habit Tracking App

## Description
This Habit Tracking App is designed to help users create, track, and analyze their habits. 
It allows users to define habits with specific periodicities (daily or weekly), log their completion, and analyze their progress. 
The goal is for users to set their own goals and monitor their logged data, which may boost motivation to change daily routines and may create an overall well-being in the long run.

## Features
The Habit Tracking App helps users to:
- Create new habits with a start date and periodicity.
- Log entries for each habit, marking them as completed on specific dates and times.
- View all habits with details like name, start date, and periodicity.
- Analyze habits to get insights like the longest streak and habits grouped by periodicity.
- Delete habits that are no longer needed.

## Installation
To get started with the Habit Tracking App, follow these steps:

### Prerequisites
- Python 3.7 or later
- Virtual environment setup (recommended)

### Step-by-Step Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/habit-tracking-app.git
    cd habit-tracking-app
    ```

2. **Create and activate a virtual environment (Windows):**
   ```sh
        python -m venv venv
        venv\Scripts\activate
   ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Preload the database with sample data (recommended for testing):**
    ```sh
    python preload_db.py
    ```

## Usage
Here's how to use the Habit Tracking App:

1. **Run the application:**
    ```sh
    python main.py
    ```
    You will be greeted with a menu and asked to choose from various options such as adding a habit, viewing habits, analyzing habits, logging entries, and deleting habits.
    
      

2. **Add a new habit:**

    Follow the prompts to enter the habit name, start date, and periodicity (daily or weekly). For example, create a habit called "No Netflix Binging" with a daily periodicity to help reduce screen time.


3. **Log an entry:**

    Select a habit and enter the date  (YYYY-MM-DD) and time (HH:MM) of the entry, or leave it blank for the current time. This helps you keep track of when you completed your habit.


4. **Analyze habits:**

    Choose from different analysis options to see streaks, longest run streaks, and habits by periodicity. For instance, analyze your "No Netflix Binging" habit to see how many days you've successfully avoided binge-watching. :)


5. **Delete a habit:**

    Remove habits that you no longer want to track to keep your habit list up-to-date and focused.

### Example
Let's imagine you're trying to stay connected with your Grandma by making sure you call her every week. Use the Habit Tracking App to create a weekly habit called "Call Grandma." Each week, log your success when you remember to give her a ring. Over time, you can analyze your habit and see how many consecutive weeks you've managed to stay in touch. Celebrate your streaks and let the app cheer you on! Plus, Grandma will surely appreciate the regular updates and stories from her favorite grandchild!
## Tests
To ensure that all functionalities of the Habit Tracking App are working correctly, you can run tests using "pytest ." Testing helps validate that the code works as expected and helps catch any bugs or issues.

### Run tests:
1. **Install pytest (if not already installed):**
    ```sh
    pip install pytest
    ```

2. **Run the tests:**
    ```sh
    pytest .
    ```
    This will execute all test cases and provide a report on the functionality of the app.

By running these tests, you can verify that habit creation, logging, analysis, and deletion functionalities are working correctly. Regular testing helps maintain the quality and reliability of the application.

## Motivational Tip
Building habits takes time and consistency. Don´t forget to celebrate small victories along the way, and don't be too hard on yourself if you miss a day/week. Keep using the Habit Tracking App to stay motivated and track your progress. Remember, it's better to have small goals, than no goals at all. You've got this!


