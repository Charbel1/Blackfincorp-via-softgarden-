

def is_multip(number, mult):
    return number % mult == 0

const = 100

for num in range(1,const):
    if is_multip(num,5) and is_multip(num,3):
        print("VINCLE")
    elif is_multip(num,5):
        print("ClE")
    elif is_multip(num,3):
        print("VIN")
    else:
        print(num)

