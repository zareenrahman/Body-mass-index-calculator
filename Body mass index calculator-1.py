"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 151788983
Name:       Zareen Rahman
Email:      zareen.rahman@tuni.fi
"""
from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # Create Labels for weight and height
        weight_label = Label(self.__mainwindow, text="Weight (kg):")
        weight_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        height_label = Label(self.__mainwindow, text="Height (cm):")
        height_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        # Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)
        self.__weight_value.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)
        self.__height_value.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Create a Button that will call the calculate_BMI-method.
        # Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow,
                                         text="Calculate BMI",
                                         command=self.calculate_BMI,
                                         bg="lightblue")
        self.__calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Create a Label that will show the decimal value of the BMI
        # after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="BMI:")
        self.__result_text.grid(row=3, column=0, columnspan=2, pady=5)

        # Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text="Explanation:")
        self.__explanation_text.grid(row=4, column=0, columnspan=2, pady=5)

        # Create a button that will call the reset_fields-method.
        self.__reset_button = Button(self.__mainwindow, text="Reset Fields",
                                     command=self.reset_fields, bg="yellow")
        self.__reset_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                    command=self.stop, bg="red")
        self.__stop_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Start the mainloop.
        self.__mainwindow.mainloop()

    def calculate_BMI(self):
        try:
            # Get weight and height values from entry components
            weight_str = self.__weight_value.get()
            height_str = self.__height_value.get()

            # Check for non-numeric weight and height
            if not self.is_valid_number(
                    weight_str) or not self.is_valid_number(height_str):
                raise ValueError("Error: height and weight must be numbers.")

            # Convert values to float
            weight = float(weight_str)
            height = float(height_str)

            # Check for non-positive weight and height
            if weight <= 0 or height <= 0:
                raise ValueError("Error: height and weight must be positive.")

            # Calculate BMI
            bmi = weight / ((height / 100) ** 2)  # Convert height to meters

            # Display BMI result
            self.__result_text.config(text=f"BMI: {bmi:.2f}")

            # Display verbal explanation
            self.display_explanation(bmi)

        except ValueError as e:
            # Handle errors (non-numeric input or non-positive values)
            self.__explanation_text.config(text=str(e))
            self.__result_text.config(text="BMI:")  # Reset result text
            self.reset_fields()

    def is_valid_number(self, value):
        """
        Helper method to check if a string represents a valid positive or negative number.
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    def reset_fields(self):
        """
        In error situations, this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.config(text="BMI:")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def display_explanation(self, bmi):
        # Display verbal explanation based on BMI value
        if 18.5 <= bmi <= 25:
            self.__explanation_text.config(text="Your weight is normal.")
        elif bmi > 25:
            self.__explanation_text.config(text="You are overweight.")
        else:
            self.__explanation_text.config(text="You are underweight.")

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
