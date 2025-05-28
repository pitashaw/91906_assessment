import conversion_rounding as cr  # Ensure this module has to_AUD and to_USD functions


def check_currency(question):
    convert_to_usd = 1  # 1 for USD, 0 for AUD
    error = "Enter a valid number greater than or equal to 1 with up to 9 digits"

    while True:
        user_input = input(question)

        try:
            # Check digit length (excluding decimal point and commas)
            digits_only = user_input.replace(".", "").replace(",", "")
            if not digits_only.isdigit() or len(digits_only) > 9:
                raise ValueError

            to_convert = float(user_input)
            if to_convert >= 1:
                answer = convert(convert_to_usd, to_convert)
                return answer
            else:
                print(error)

        except ValueError:
            print(error)


def convert(convert_to_usd, to_convert):
    if convert_to_usd:
        answer = cr.to_USD(to_convert)
        return f"{to_convert} NZD is {answer} USD"
    else:
        answer = cr.to_AUD(to_convert)
        return f"{to_convert} NZD is {answer} AUD"


# Main program
currency = check_currency("Enter a number to convert: ")
print(f"Currency conversion: {currency}")
