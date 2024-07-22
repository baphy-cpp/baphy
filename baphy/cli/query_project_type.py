"""
Module contains a function to query the user for the project type.
"""

import questionary

from baphy.choices import Choices, ProjectTypeChoice


def query_project_type(user_choices: Choices):
    """
    Query the user for the project type and store it in the user_choices.

    Args:
        user_choices (Choices): An object that contains choices for the project type.

    Returns:
        None
    """
    # Ask the user to select a project type
    result_value = questionary.select(
        "Select project type:",
        choices=[x.value for x in ProjectTypeChoice],  # List of project type choices
    ).ask()

    # Set the selected project type in user_choices
    user_choices.project_type = ProjectTypeChoice(result_value)
