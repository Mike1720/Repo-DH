def division(dividendo, divisor):
    try:
        result = dividendo // divisor
        return result
    except ZeroDivisionError:
        return "Error, no es posible dividir entre 0"
    finally:
        result = 0


print(division(10, 0))
print("MENSAJE IMPORTANTE")


def text_int(txt):
    try:
        num = int(txt)
    except ValueError:
        return "Este texto no es un número"
    finally:
        num = None
    return num


print(text_int("123"))
print(text_int("oa"))
