def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False

    # check numbers cannot be used in the middle of a plate
    number = False
    for c in s[2:]:
        if c.isdecimal() and number == False:
            if c == "0":
                return False
            number = True
        if c.isalpha() and number == True:
            return False

    return True




main()
