from os import system, name

#The "legend" for Roman numerals

legend = {"I" : 1,
          "V" : 5,
          "X" : 10,
          "L" : 50,
          "C" : 100,
          "D" : 500,
          "M" : 1000}


def romanToInt(inputS):

    listinputS = list(inputS) # Turns the input into an array of letters
    output = 0
    skip = 0
    for index, elem in enumerate(listinputS):
        if skip == 1: #line 28 decides if the iteration should be skipped because of a subtraction
            skip = 0
            continue
        if index+1 < len(listinputS):
            if legend.get(elem) < legend.get(listinputS[index+1]):
                calc = legend.get(listinputS[index+1]) - legend.get(elem)
                output = output + calc
                skip = 1
            else:
                output = output + legend.get(elem)
        else:
            output = output + legend.get(elem)    
    print(output)

while True:
    if name == 'nt':
        system('cls')
  
    else:
        system('clear')
    inputS = input("Enter a correct Roman numeral: ")
    romanToInt(inputS)
    check = input("Try a different number ?( Y/N ) \n")
    if check == "Y":
        continue
    else:
        break

#TODO
#Check for incorrect numbers