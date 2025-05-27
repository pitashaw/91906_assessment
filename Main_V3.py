from tkinter import *
from functools import partial
import conversion_rounding as cr  # make sure this file exists with to_AUD and to_USD functions
from datetime import date


# Basic framework for converter
class Converter:
    def __init__(self):
        self.all_calculations_list = []

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.currency_heading = Label(self.currency_frame,
                                      text="WubbaLubbaBux™:Currency Converter, "
                                           "Sponsored by Your Mom’s Third Cousin’s Dog ",
                                      font=("Arial", "16", "bold"))
        self.currency_heading.grid(row=0)

        instructions = ("Please enter an amount in NZD below and then press "
                        "one of the buttons to convert it to AUD or USD.")
        self.currency_instructions = Label(self.currency_frame,
                                           text=instructions,
                                           wraplength=250, width=40,
                                           justify="left")
        self.currency_instructions.grid(row=1)

        self.currency_entry = Entry(self.currency_frame, font=("Arial", "14"))
        self.currency_entry.grid(row=2, padx=10, pady=10)

        self.answer_error = Label(self.currency_frame, text="Please enter a number",
                                  fg="#084C99", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=4)

        # Buttons
        button_details_list = [
            ["To AUD", "#990099", partial(self.check_currency, 0), 0, 0],
            ["To USD", "#009900", partial(self.check_currency, 1), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", self.to_history, 1, 1]
        ]

        self.button_ref_list = []

        for item in button_details_list:
            btn = Button(self.button_frame,
                         text=item[0], bg=item[1],
                         fg="#FFFFFF", font=("Arial", "12", "bold"),
                         width=12, command=item[2])
            btn.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.button_ref_list.append(btn)

        self.to_help_button = self.button_ref_list[2]
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    # Checks that the user inputs a number greater than or equal to 1
    def check_currency(self, convert_to_usd):
        to_convert = self.currency_entry.get()

        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.currency_entry.config(bg="#FFFFFF")

        error = "Enter a valid number greater than or equal to 1"
        has_errors = False

        try:
            to_convert = float(to_convert)
            if to_convert >= 1:
                self.convert(convert_to_usd, to_convert)
            else:
                has_errors = True

        except ValueError:
            has_errors = True

        if has_errors:
            self.answer_error.config(text=error, fg="#9C0000", font=("Arial", "10", "bold"))
            self.currency_entry.config(bg="#F4CCCC")
            self.currency_entry.delete(0, END)

    # Uses conversion rounding to calculate the currency conversions and display the answer
    def convert(self, convert_to_usd, to_convert):
        if convert_to_usd:
            answer = cr.to_USD(to_convert)
            answer_statement = f"{to_convert} NZD is {answer} USD"
        else:
            answer = cr.to_AUD(to_convert)
            answer_statement = f"{to_convert} NZD is {answer} AUD"

        self.to_history_button.config(state=NORMAL)
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)

    # Help/Info button
    def to_help(self):
        DisplayHelp(self)

    # History/Export button
    def to_history(self):
        HistoryExport(self, self.all_calculations_list)


# Help/Info contents
class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()
        partner.to_help_button.config(state=DISABLED)
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"),
                                        bg=background)
        self.help_heading_label.grid(row=0)

        help_text = ("To use the program, enter an amount in NZD, then click "
                     "'To AUD' or 'To USD'.\n\n"
                     "You can view and export your conversion history using the "
                     "'History / Export' button. "
                     "These calculations are accurate as of 15/05/2025.")
        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left", bg=background)
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # Closes the help box
    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# History/Export contents
class HistoryExport:
    def __init__(self, partner, calculations):
        self.history_box = Toplevel()
        partner.to_history_button.config(state=DISABLED)
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        calc_amount = "all your" if len(calculations) <= 5 else f"your recent calculations - " \
                                                                f"showing 5 / {len(calculations)}"
        recent_intro_txt = f"Below are {calc_amount} calculations."

        newest_first_list = list(reversed(calculations))
        newest_first_string = "\n".join(newest_first_list[:5])

        export_instruction_txt = ("Please push <Export> to save your calculations in a file. "
                                  "If the filename already exists, it will be replaced.")

        label_details = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            [newest_first_string, ("Arial", "14"), "#D5E8D4"],
            [export_instruction_txt, ("Arial", "11"), None]
        ]

        self.label_refs = []
        for i, (text, font_style, bg) in enumerate(label_details):
            lbl = Label(self.history_box, text=text, font=font_style,
                        bg=bg, wraplength=300, justify="left", pady=10, padx=20)
            lbl.grid(row=i)
            self.label_refs.append(lbl)

        self.export_filename_label = self.label_refs[3]

        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        Button(self.history_button_frame, font=("Arial", "12", "bold"),
               text="Export", bg="#004C99", fg="#FFFFFF", width=12,
               command=lambda: self.export_data(calculations)).grid(row=0, column=0, padx=10, pady=10)

        Button(self.history_button_frame, font=("Arial", "12", "bold"),
               text="Close", bg="#666666", fg="#FFFFFF", width=12,
               command=partial(self.close_history, partner)).grid(row=0, column=1, padx=10, pady=10)

    # Exports history to a text file
    def export_data(self, calculations):
        today = date.today()
        file_name = f"currency_{today.strftime('%Y_%m_%d')}.txt"

        with open(file_name, "w") as f:
            f.write("***** Currency Calculations ******\n")
            f.write(f"Generated: {today.strftime('%d/%m/%Y')}\n\n")
            f.write("Here is your calculation history (oldest to newest)...\n")
            for item in calculations:
                f.write(item + "\n")

        self.export_filename_label.config(bg="#009900",
                                          text=f"Export Successful! File: {file_name}",
                                          font=("Arial", "12", "bold"))

    # Closes the history/export box
    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()