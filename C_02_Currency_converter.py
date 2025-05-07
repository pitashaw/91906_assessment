from tkinter import *
import conversion_rounding as cr


class Converter():
    """
    currency conversion tool (USD to NZD or NZD to USd)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = []

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.currency_heading = Label(self.currency_frame,
                                  text="Currency Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.currency_heading.grid(row=0)

        instructions = ("Please enter a currency below and then press "
                        "one of the buttons to convert it from USD "
                        "to NZD")
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
            ["To USD", "#990099", 0, 0],
            ["To AUD", "#009900", 0, 1],
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
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)


    def check_currency(self,min_currency,):
        """
        Checks currency is valid and either invokes calculation
         function or shows a custom error
        """
        # Retrieve currency to be converted
        to_convert = self.currency_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.currency_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_currency}"
        has_errors = "no"

        # checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_currency:
                self.convert(min_currency, to_convert)
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.answer_error.config(text=error, fg="#9C0000", font=("Arial", "10", "bold"))
            self.currency_entry.config(bg="#F4CCCC")
            self.currency_entry.delete(0, END)

    def convert(self, min_currency, to_convert):
        """
        Converts currency and updates answer label. Also stores
        calculations for Export / History feature
        """

        if min_currency == 1:
            answer = cr.to_USD(to_convert)
            answer_statement = f"{to_convert} NZD is {answer} USD"

        else:
            answer = cr.to_AUD(to_convert)
            answer_statement = f"{to_convert} NZD is {answer} AUD"

        # enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)


        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer)
        print(self.all_calculations_list)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Convertor")
    Converter()
    root.mainloop()
