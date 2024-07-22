"""
This module contains the main entry point for the Baphy CLI.
It contains the `main` function, which is responsible for parsing the command line arguments,
querying the user for input, and running the logic of the program.
"""

import typer
from typer import run
from typing_extensions import Annotated

from . import cli
from .choices import Choices
from .setup_project import setup_project
from .template_engine import create_environment


def main(
    target: Annotated[
        str,
        typer.Argument(help="Name of directory/project to create", show_default=False),
    ]
):
    """
    Main function for the Baphy CLI.

    Args:
        target (str): Name of the directory/project to create.
    """
    # Create the Jinja2 environment
    env = create_environment()

    # Create a Choices object to store user choices
    user_choices = Choices()

    # Create a dictionary to store template variables
    template_variables = {}

    # Welcome the user
    cli.welcome()

    cli.query_project_info(target, template_variables)
    cli.query_project_type(user_choices)
    cli.query_package_manager(user_choices)
    cli.query_testing_framework(user_choices)

    # Print the template variables
    print(template_variables)
    print(user_choices)

    # Set up the project using the template variables
    setup_project(env, template_variables)


def cli_entry():
    """
    Entry point for the Baphy CLI.
    """

    # Run the main function, which is defined in the facade module.
    # This is the entry point for the CLI, which is responsible for
    # parsing the command line arguments, querying the user for
    # input, and running the logic of the program.
    run(main)
