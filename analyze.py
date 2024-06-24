"""
This module analyzes habits stored in the database.
"""

import questionary
from db import Database
from habit import Habit

def analyze_habits():
    """
    Displays the current streak for a selected habit from the database.

    Steps:
    1. Retrieves all habits.
    2. Prompts user to select a habit.
    3. Calculates and displays the selected habit's streak.
    """
    db = Database()
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

if __name__ == "__main__":
    analyze_habits()
