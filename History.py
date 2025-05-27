from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date


class Converter:
    """
    Currency conversion tool (NZD to USD or NZD to AUD)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = ['This is a test',
                                      '10.0 NZD is 16.70 AUD',
                                      '10.0 NZD is 6.00 USD',
                                      '17.00 NZD is 10.20 USD'
                                      ]

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.to_history_button = Button(self.currency_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self, self.all_calculations_list)


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
        recent_intro_txt = (f"Below are {calc_amount} calculations"
                            "-showing 5/6 calculations "
                            "(to the nearest degree).")

        # Create string from calculations list (the newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(newest_first_list) <= 5:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        # If we have more than five items...
        else:
            for item in newest_first_list[:5-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[5-1]

        export_instruction_txt = ("Please push <Export> to save your calculations in"
                                  "file. If the filename already exists, it will be replaced.")

        self.calculations = calculations

        # Label list (label text | format |bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11",), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None]
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

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["Export", "#004C99", self.export_data, 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def export_data(self):
        today = date.today()
        file_name = f"currency_{today.strftime('%Y_%m_%d')}.txt"

        with open(file_name, "w") as f:
            f.write("***** Currency Calculations ******\n")
            f.write(f"Generated: {today.strftime('%d/%m/%Y')}\n\n")
            f.write("Here is your calculation history (oldest to newest)...\n")
            for item in self.calculations:
                f.write(item + "\n")

        self.export_filename_label.config(bg="#009900",
                                          text=f"Export Successful! File: {file_name}",
                                          font=("Arial", "12", "bold"))

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
    root.title("Currency Converter")
    Converter()
    root.mainloop()
