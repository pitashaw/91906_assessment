from tkinter import *
from functools import partial  # to prevent unwanted windows
import conversion_rounding as cr
from datetime import date


class Converter:
    """
    Currency conversion tool (NZD to AUD or NZD to USD)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = []

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.currency_heading = Label(self.currency_frame,
                                  text="currencyerature Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.currency_heading.grid(row=0)

        instructions = ("Please enter a currencyerature below and then press "
                        "one of the buttons to convert it from centigrade "
                        "to Fahrenheit.")
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
                                  fg="#084C99", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["To Celsius", "#990099", 0, 0],
            ["To Fahrenheit", "#009900", 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", self.to_history, 1, 1]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve to_help button
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_currency(self, min_currency):
        """
        Checks currencyerature is valid and either invokes calculation
        function or shows a custom error
        """

        # Retrieve currencyerature to be converted
        to_convert = self.currency_entry.get()

        # Reset label and entry box(if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.currency_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_currency}"
        has_errors = "no"

        # checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_currency:
                # error = ""
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
        if min_currency == 1:
            answer = cr.to_USD(to_convert)
            answer_statement = f"{to_convert}NZD is {answer}AUD"  # Fixed parentheses here
        else:
            answer = cr.to_AUD(to_convert)
            answer_statement = f"{to_convert}NZD is {answer}USD"  # Fixed parentheses here

        # Enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        # Update the answer_error label with the result
        self.answer_error.config(text=answer_statement)

        # Append the calculation to the history list
        self.all_calculations_list.append(answer_statement)

        # Print the list of calculations for debugging purposes
        print(self.all_calculations_list)

    def to_help(self):
        """
            Open help dialogue box and disables button
            (so that users cant create multiple help boxes).
            """
        DisplayHelp(self)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self, self.all_calculations_list)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'release' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To yse the program, simply enter the currencyerature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit.. \n\n" \
                    " Note that -273 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible " \
                    "currencyerature). If you try to convert a " \
                    "currencyerature that is less than -273 degrees C, " \
                    "you will get an error message. \n\n" \
                    "To see your " \
                    "calculation history and export it to a text " \
                    "file, please click the 'History / Export' button."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        # List and loop to set background colour on
        # everything except the buttons.
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
                Closes help dialogue box (and enables help button)
                """
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'release' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # background colour and text for calculation area
        if len(calculations) <= 5:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {5} / {len(calculations)}")

        # strings for 'long' labels...
        recent_intro_txt = (f"Below are {calc_amount} calculations "
                            "(to the nearest degree).")

        # Create string from calculations list (newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(newest_first_list) <= 5:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        # If we have more than five items...
        else:
            for item in newest_first_list[:5 - 1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[5 - 1]

        export_instruction_txt = ("Please push <Export> to save your calculations in"
                                  "file. If the filename already exists, it will be replaced.")

        # Label list (label text | format |bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11",), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None],
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # Retrieve export instruction label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons (two columns)
        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        button_ref_list = []

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def export_data(self, calculations):
        # **** Get current date for heading and file name ****
        today = date.today()

        # Get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"currency_{year}_{month}_{day}"

        # edit label so users know that their export has been done
        success_string = ("Export Successful! The file is called"
                          f"{file_name}.txt")
        self.export_filename_label.config(bg="#009900", text=success_string,
                                          font=("Arial", "12", "bold"))

        # write data to text file.
        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("***** Currency Calculations ******\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldest to newest)...\n")

            # write the item to file
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")

    def close_history(self, partner):
        """
        Closes history dialogue box (and enables history button)
        """
        # Put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("currency Convertor")
    Converter()
    # uncomment the line below to see what it does (helps instance understanding)
    # convert_it_two = Converter (root)
    root.mainloop()