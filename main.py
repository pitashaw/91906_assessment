from tkinter import *
import conversion_rounding as cr

class Converter():
    """
    Currency conversion tool (NZD to GBP, NZD to USD, USD to GBP or inverse)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.currency_heading = Label(self.currency_frame,
                                  text="Currency Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.currency_heading.grid(row=0)

        instructions = ("Please enter a currency below and then use "
                        "the drop down menu and enter button between "
                        "your chosen currencies.")
        self.currency_instructions = Label(self.currency_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.currency_instructions.grid(row=1)

        self.currency_entry = Entry(self.currency_frame,
                                font=("Arial", "14")
                                )
        self.currency_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.currency_frame, text=error,
                                  fg="#004C99", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / expert buttons
        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["To NZD", "#990099", lambda: self.check_currency(c.ABS_ZERO_NZD), 0, 0],
            ["To USD", "#009900", lambda: self.check_currency(c.ABS_ZERO_USD), 0, 1],
            ["To AUD", "#009900", lambda: self.check_currency(c.ABS_ZERO_AUD), 0, 2],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[4].config(state=DISABLED)
