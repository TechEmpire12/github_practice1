def text(text, space, color_code=None):
    white_space = " "
    if len(str(text)) > space:
        return
    calc = space - len(str(text))
    if color_code:
        final = "\033[{}m{}{}\033[0m".format(color_code,text, white_space * calc)
        return final
    else:
        final = "{}{}".format(text, white_space * calc)
        return final

def gap(text, space, symbol=" ", color_code=None):
    half = symbol * int(space / 2)
    if color_code:
        final = "\033[{}m{} {} {}\033[0m".format(color_code, half, text, half)
        return final
    else:
        final = "{} {} {}".format(half, text, half)
        return final