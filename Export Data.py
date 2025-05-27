from datetime import date

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