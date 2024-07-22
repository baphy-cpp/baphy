"""
Module contains functions for welcoming user.
"""

from rgbprint import gradient_print


def welcome():
    """
    Rich-print welcoming message
    """

    print("\033[1m", end="")
    gradient_print(
        "Baphy - C++ project setup made easy",
        start_color=0x3398DB,
        end_color=0xDB3398,
    )
    print("\033[0m")
