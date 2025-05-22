import conversion_rounding as cr  # make sure this file exists with to_AUD and to_USD functions



def check_currency(question):
    convert_to_usd = 1
    # to_convert = convert_to_usd

    error = "Enter a valid number greater than or equal to 1"
    has_errors = False

    while has_errors == False:

        try:
            to_convert = float(input(question))
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
        answer_statement = f"{to_convert} NZD is {answer} USD"
        return answer_statement
    else:
        answer = cr.to_AUD(to_convert)
        answer_statement = f"{to_convert} NZD is {answer} AUD"
        return answer_statement


# Main program

currency = check_currency("Enter a number to convert: ")
print(f"Currency conversion: {currency}")
