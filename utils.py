def get_value(text, variables):
    value = ""

    # _expression = expression(text, variables)
    # print(_expression)
    # if _expression:
    #     value = _expression

    if text.startswith("'") or text.startswith('"'):
        value = text[1:-1]
    
    if value == "":
        if text in variables:
            value = variables[text]
            if value.startswith("'") or value.startswith('"'):
                value = value[1:-1]
        else:
            print("Variable \"{}\" not found.".format(text))
            exit()

    return value

# def expression(text, variables):
#     if "==" in text:
#         text_list = text.split("==")
#         val1 = get_value(text_list[0], variables)
#         val2 = get_value(text_list[1], variables)
#         print(val1)
#         print(val2)
#         return val1 == val2
#     elif "!=" in text:
#         text_list = text.split("!=")
#         return get_value(text_list[0], variables) != get_value(text_list[1], variables)
#     else:
#         return None
