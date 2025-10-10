######## UPDATE NOTES: CAN TAKE MULTIPLE INGREDIENTS AND ACCEPTS UNIT ABBREVIATIONS ########


# THE CALCULATOR
def RECIPATOR(x, y):
#METRIC TO IMPERIAL VOLUME
    if y[:3] == "lit" or y == 'l':
        return(x * 1.057, "quarts") if x * 1.057 < 4 else (x * 0.264, "gallons")
    
    elif y[:9] == "millilit" or y == "ml":
        return(x * 0.0338, "fluid ounces") if x * 0.0338 < 8 else (x * 0.0042, "cups")
#METRIC TO IMPERIAL WEIGHT
    elif y[:3] == "kil" or y == "kg":
        return(x * 2.2046)
    
    elif y[:3] == "gra" or y == "g":
        return(x * 0.035, "ounces") if x * 0.035 <= 8 else (x * 0.002205, "pounds")
    
    elif y[:9] == "milligra" or y == "mg":
        return(x*0.000035, "ounces")
#IMPERIAL TO METRIC VOLUME
    elif y[:3] == "flu" or y[:4] == "floz":
        return(x * 29.57, "milliliters") if x * 29.57 < 1000 else ((x * 29.57) * .001, "liters")
    
    elif y[:3] == "cup":
        return(x * 236.6, "milliliters") if x * 236.6 < 1000 else ((x * 236.6) * .001, "liters")
    
    elif y[:3] == "qua":
        return(x * 0.95, "liters")
    
    elif y[:3] == "gal":
        return(x * 3.785, "liters")
#IMPERIAL TO METRIC WEIGHT
    elif y[:3] == "oun" or y == "oz":
        return(x * 28350, "milligrams") if x * 28350 < 1000 else (x * 28.35, "grams")
    
    elif y[:3] == "pou" or y[:2] == "lb":
        return(x * 453.59237, "grams") if x * 453.59237 < 1000 else (x * 0.454, "kilograms")

    else:
        print("Try again")

def splitter(y, x):
    splitter = y.get(x[0]).split()
    return splitter

def batch():
    size = input("How much does this recipe make?")
    

# MAIN PROGRAM
def ingredients():
    # CREATING KEYS FROM INGREDIENTS WITH ENTRIES
    ingredients = {}
    item = input("Type your ingredient like so 'carrots: 1.5 pounds, cow milk: 1 gallon'\n")

    
    entry = item.split(',')         # seperate ingredients with amounts
    #entry = item.split("\n")
    for i in entry:             #For every block of ('ingredient: amount'),
        amount = i.split(':')       #create ingredient and amount tuple
        #somehow make it right here so that it checks if it starts with a number and then maybe invert it to it follows the previous logic
        ingredients[amount[0]] = amount[1]          # enter key and value in dictionary
        split = splitter(ingredients, amount)                   #finding key and splitting value so that amount[0] is the figure and [1] is the unit.
        ingConv = RECIPATOR(float(split[0]), split[1])          #converting and storing in variable
        ingredients[amount[0]] = " ".join(map(str, ingConv))    #updating key

    #eventually save Dictionary as a recipe
    #make an option to see both amounts side -by -side
    #make it so you can enter number first as well
    #check if item[0] is number or letter and go from there
    #make it possible to scale up and down
    print(ingredients)
#    ask = input("Do you want to scale up or down?")
#    if ask.lower() == "yes":
#        batch()


ingredients()
