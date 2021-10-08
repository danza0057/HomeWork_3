def division(var1, var2):
    try:
        div = var1 / var2
        return div
    except (ZeroDivisionError):
        return "Error!"


dig1, dig2 = int(input()), int(input())
print(division(dig1, dig2))
