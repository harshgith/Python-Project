def main():
    z(10)
    z(1)
    z(15)
    z(9)
    z(450)
    z(21)
    z(4)
    
def z(number):
    if number %3 ==0 and number %5 ==0:
        print("zoom")
    elif number %3 ==0:
        print("zip")
    elif number %5 ==0:
        print("zap")
    else:
        print("invalid Number")
main()