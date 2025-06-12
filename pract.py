import math as m


def equalize(a,b):
    try:
        y=m.sqrt(((a+b)**3)/(a-b)**2)
    except ZeroDivisionError:
        result = "there is zero division"
        raise ZeroDivisionError("dfslh")
    except ValueError:
        result ="cant sqrt negative"
    except TypeError:
        result = "this is not number"
    else:
        result = round(y ,4)
    return result