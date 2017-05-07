#test.py
import math
def main():
    print("This program finds the real solutions to a test.\n")
    try:
        a,b,c=eval(input("Please enter the coefficients(a,b,c): "))
        discRoot=math.sqrt(b*b-4*a*c)
        root1=(-b+discRoot)/(2*a)
        root2=(-b-discRoot)/(2*a)
        print("\nThe solution are: ",root1,root2)
    except ValueError as exc0bj:
        if str(exc0bj)=="math domain error":
            print("No Real Roots.")
        else:
            print("You did't give me the right numbe of coefficients.")

    except NameError:
        print("\nYou did't enter three numbers.")

    except TypeError:
        print("\nYour inputs were not all numbers.")

    except SyntaxError:
        print("\n Yous input was not in the corror form. Missing comma?")

    except:
        print("\nsomething went wrong.sorry!")



main()


