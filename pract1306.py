import math 


def igorek(a,b,c):
    try:
        y=(math.factorial(a)-math.sqrt(b)/c**3)
    except ZeroDivisionError:
        result = ["there is zero division"]
    except ValueError:
        result ={"ValueError":"cant sqrt negative"}
    except TypeError:
        result_1 ={ "this is not number"}
        result =set(result_1)
    else:
        result = round(y ,4)
    return result
    