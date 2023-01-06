a =10^100000
b = 9

#value = int(input("enter the value"))

try:
    print("Resource Open")
    print(a/b)

except ZeroDivisionError:
    print("Unable to divide by Zero")

except ValueError:
    print("please valid input")

except SyntaxError:
    print("Syntax error")


except Exception:
    print("Something went wrong")

finally:
    print("resource is closed")





