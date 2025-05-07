def round_ans(val):
    """
    Rounds temperature to the nearest degree
    :param val: Number to be rounded
    :return: Number rounded to the nearest degree
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_AUD(to_convert):
    """
    Converts from NZD to AUD
    :param to_convert: Temperature to be converted in NZD
    :return: Converted temperature in AUD
    """

    answer = to_convert * 1.67
    return round_ans(answer)


def to_USD(to_convert):
    """
    Converts from NZD to USD
    :param to_convert: Temperature to be converted in NZD
    :return: Converted temperature in USD
    """
    answer = to_convert * 0.6
    return round_ans(answer)


# Main routine / Testing starts here
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]
#
# for item in to_f_test:
#     ans = to_fahrenheit(item)
#     print(f"{item} C is {ans} F")
#
# print()
#
# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item} F is {ans} C")
#