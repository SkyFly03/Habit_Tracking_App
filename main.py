"""
This module provides the main interface for interacting with the habit tracker.
"""

from db import Database
from habit import Habit
import questionary
from datetime import datetime

def main():
    """
    Main function to run the habit tracker application.
    """
    db = Database()

    greeting_message = """                   
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Welcome! Ready to build some healthy habits? Select an option from the menu below:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    while True:
        action = questionary.select(
            greeting_message,
            choices=["Add Habit", "View Habits", "Analyze Habit", "Log Entry", "Delete Habit", "Exit"]
        ).ask()

        if action == "Add Habit":
            name = questionary.text("Enter the name of the habit (type 'menu' to return to main menu):").ask()
            if name.lower() == 'menu':
                continue

            start_date_str = questionary.text("Enter the start date (YYYY-MM-DD) (type 'menu' to return to main menu):").ask()
            if start_date_str.lower() == 'menu':
                continue

            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                time_str = questionary.text("Enter the start time of the habit (HH:MM) or leave blank for current time:").ask()
                if time_str.lower() == 'menu':
                    continue

                if time_str:
                    start_datetime = datetime.strptime(f"{start_date_str} {time_str}", '%Y-%m-%d %H:%M')
                else:
                    start_datetime = datetime.now().replace(second=0, microsecond=0)

                periodicity = questionary.select(
                    "Select the periodicity of the habit (type 'menu' to return to main menu):",
                    choices=["daily", "weekly"]
                ).ask()
                if periodicity.lower() == 'menu':
                    continue

                habit = Habit(name=name, start_date=start_datetime, log=[], periodicity=periodicity)
                db.add_habit(habit)
                print(f"Habit '{name}' added with {periodicity} periodicity.")
            except ValueError:
                print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
                print("Returning to the main menu.")

        elif action == "View Habits":
            habits = db.get_all_habits()
            if not habits:
                print("No habits found.")
            for habit in habits:
                print(f"Habit: {habit.name}, Start Date: {habit.start_date}, Periodicity: {habit.periodicity}")

        elif action == "Analyze Habit":
            analyze_habits(db)

        elif action == "Log Entry":
            habits = db.get_all_habits()
            if not habits:
                print("No habits found.")
                continue

            habit_names = [habit.name for habit in habits] + ["Return to main menu"]
            habit_name = questionary.select(
                "Select a habit to log an entry for or type 'menu' to return to main menu:",
                choices=habit_names
            ).ask()

            if habit_name == "Return to main menu" or habit_name.lower() == 'menu':
                continue

            habit = db.get_habit(habit_name)
            date_str = questionary.text("Enter the date of the entry (YYYY-MM-DD) (type 'menu' to return to main menu):").ask()
            if date_str.lower() == 'menu':
                continue

            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                time_str = questionary.text("Enter the time of the entry (HH:MM) or leave blank for current time:").ask()
                if time_str.lower() == 'menu':
                    continue

                if time_str:
                    log_datetime = datetime.strptime(f"{date_str} {time_str}", '%Y-%m-%d %H:%M')
                else:
                    log_datetime = datetime.now().replace(second=0, microsecond=0)

                habit.log_entry(log_datetime)
                db.save_db()
                print(f"Logged entry for habit: {habit.name} on {log_datetime.strftime('%Y-%m-%d %H:%M')}")
            except ValueError:
                print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
                print("Returning to the main menu.")

        elif action == "Delete Habit":
            habits = db.get_all_habits()
            if not habits:
                print("No habits found.")
                continue

            habit_names = [habit.name for habit in habits] + ["Return to main menu"]
            habit_name = questionary.select(
                "Select a habit to delete or type 'menu' to return to main menu:",
                choices=habit_names
            ).ask()

            if habit_name == "Return to main menu" or habit_name.lower() == 'menu':
                continue

            db.delete_habit(habit_name)
            print(f"Habit '{habit_name}' deleted.")

        elif action == "Exit":
            break

def analyze_habits(db):
    """
    Analyzes habits and provides various options.

    Args:
        db (Database): The database object to interact with.
    """
    action = questionary.select(
        "Select an analytical function:",
        choices=["Analyze a specific habit", "Longest run streak of all habits", "Longest run streak for a given habit", "List habits by periodicity", "Return to main menu"]
    ).ask()

    if action == "Analyze a specific habit":
        analyze_specific_habit(db)

    elif action == "Longest run streak of all habits":
        longest_streak, habit_name = db.get_longest_streak_all_habits()
        print(f"The longest run streak of all habits is {longest_streak} entries by '{habit_name}'.")

    elif action == "Longest run streak for a given habit":
        longest_streak_for_habit(db)

    elif action == "List habits by periodicity":
        list_habits_by_periodicity(db)

    elif action == "Return to main menu":
        return

def analyze_specific_habit(db):
    """
    Analyzes a specific habit's current streak.

    Args:
        db (Database): Database object to interact with.
    """
    habits = db.get_all_habits()
    if not habits:
        print("No habits found.")
        return

    habit_names = [habit.name for habit in habits]
    habit_name = questionary.select(
        "Select a habit to analyze:",
        choices=habit_names
    ).ask()

    if habit_name is None:
        return

    habit = db.get_habit(habit_name)
    print(f"Analyzing habit: {habit.name}")

    # Perform analysis
    streak = habit.calculate_streak()
    print(f"Current streak: {streak} {habit.periodicity} entries")

def longest_streak_for_habit(db):
    """
    Returns the longest streak for a specific habit.

    Args:
        db (Database): Database object to interact with.
    """
    habits = db.get_all_habits()
    if not habits:
        print("No habits found.")
        return

    habit_names = [habit.name for habit in habits]
    habit_name = questionary.select(
        "Select a habit to get the longest run streak:",
        choices=habit_names
    ).ask()

    if habit_name is None:
        return

    longest_streak = db.get_longest_streak_for_habit(habit_name)
    habit = db.get_habit(habit_name)
    if habit.periodicity == 'weekly':
        print(f"The longest run streak for habit '{habit_name}' is {longest_streak} week(s).")
    else:
        print(f"The longest run streak for habit '{habit_name}' is {longest_streak} day(s).")

def list_habits_by_periodicity(db):
    """
    Lists habits by their periodicity.

    Args:
        db (Database): Database object to interact with.
    """
    periodicity = questionary.select(
        "Select the periodicity:",
        choices=["daily", "weekly"]
    ).ask()
    habits = db.get_habits_by_periodicity(periodicity)
    if not habits:
        print(f"No {periodicity} habits found.")
    for habit in habits:
        print(f"Habit: {habit.name}, Start Date: {habit.start_date}")

if __name__ == "__main__":
    main()

