# Invoke like so:
# python3 -m mymodule.myfile

from .my42 import get_the_number

def myfunction():
    return get_the_number()

if __name__ == "__main__":
    print("myfunction returned", myfunction())
