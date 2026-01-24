ch=input("Enter any Char: ")

match ch:
    case 'm':
        print("Male")
    case 'M':
        print("Male")
    case 'f':
        print("Female")
    case 'F':
        print("Female")
    case _:
        print("Third Gender")

