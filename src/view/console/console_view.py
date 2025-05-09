"""This module contains the main function of the console application."""
import sys
sys.path.append("src")

from model.logic import (
    payment_fee_calc_while_studying, payment_fee_calc_after_studying
)

def ask_information():
    """Ask the user for the information needed to calculate the payment fee."""
    while True:
        credit_type = input("Enter the type of credit you want \n 1 for 30%\n 2 for 60%\n"
        " 3 for 100%\n")
        list_options = ["1", "2", "3"]
        if credit_type in list_options:
            credit_type = int(credit_type)  # We convert to integer after validating the input
            break
        print("Invalid option. Please enter 1, 2, or 3.")

    while True:
        try:
            college_enrollment = float(input("Enter the amount of college enrollment per"
            " semester: "))
            if college_enrollment > 0:  # We make ensure it is a positive number
                break
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid option. Please enter a valid number.")

    while True:
        try:
            semesters = int(input("Enter the number of semesters you want to calculate for: "))
            if semesters > 0:  # We ensure that the number of semesters is positive
                break
            else:
                print("Invalid number of semesters. Please enter a positive integer.")
        except ValueError:
            print("Invalid option. Please enter a valid integer.")

    return credit_type, college_enrollment, semesters


def main():
    """Main function of the console application."""
    print("---- Welcome to the ICETEX simulator :p ----")
    while True:
        credit_type, college_enrollment, semesters = ask_information()
        fee_while_studying = payment_fee_calc_while_studying(
            credit_type, college_enrollment, semesters
        )
        print(f"Your monthly fee while studying is: {fee_while_studying}")
        fee_after_studying = payment_fee_calc_after_studying(
            credit_type, college_enrollment, semesters
        )
        print(f"Your monthly fee after studying is: {fee_after_studying}")

        if input("Do you want to calculate another fee? (yes/no): ").lower() != "yes":
            print("Thanks for using the ICETEX simulator. Goodbye!")
            break

if __name__ == '__main__':
    main()
