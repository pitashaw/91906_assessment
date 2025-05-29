def round_ans(val):
    """
    Rounds Currency to the nearest 2 decimal place
    :param val: Number to be rounded to 2 decimal places
    :return: Number rounded to the nearest 2 decimal places
    """
    var_rounded = round(val, 2)
    return "{:.2f}".format(var_rounded)


def to_AUD(to_convert):
    """
    Converts from NZD to AUD
    :param to_convert: Currency to be converted in NZD
    :return: Converted currency in AUD
    """

    answer = to_convert * 0.93
    return round_ans(answer)


def to_USD(to_convert):
    """
    Converts from NZD to USD
    :param to_convert: Currency to be converted in NZD
    :return: Converted currency in USD
    """
    answer = to_convert * 0.6
    return round_ans(answer)
