######## UPDATE NOTES: CAN TAKE MULTIPLE INGREDIENTS ########

#METRIC TO IMPERIAL VOLUME
def Liters(x):
    return(x * 1.057, "quarts") if x * 1.057 < 4 else (x * 0.264, "gallons")
        
def Milliliters(x):
    return(x * 0.0338, "fluid ounces") if x * 0.0338 < 8 else (x * 0.0042, "cups")

#METRIC TO IMPERIAL WEIGHT
def Kilograms(x):
    return(x * 2.2046)

def Grams(x):
    return(x * 0.035, "ounces") if x * 0.035 <= 8 else (x * 0.002205, "pounds")

def Milligrams(x):
    return(x*0.000035, "ounces")

#IMPERIAL TO METRIC VOLUME
def FlOunces(x):
    return(x * 29.57, "milliliters") if x * 29.57 < 1000 else ((x * 29.57) * .001, "liters")

def Cups(x):
    return(x * 236.6, "milliliters") if x * 236.6 < 1000 else ((x * 236.6) * .001, "liters")

def Quarts(x):
    return(x * 0.95, "liters")

def Gallons(x):
    return(x * 3.785, "liters")

#IMPERIAL TO METRIC WEIGHT
def Ounces(x):
    return(x * 28350, "milligrams") if x * 28350 < 1000 else (x * 28.35, "grams")

def Pounds(x):
    return(x * 453.59237, "grams") if x * 453.59237 < 1000 else (x * 0.454, "kilograms")


# THE CALCULATOR
def RECIPATOR(x, y):
    if y[:3] == "lit":
        return Liters(float(x))
    
    elif y[:9] == "millilit":
        return Milliliters(float(x))
    
    elif y[:3] == "kil":
        return Kilograms(float(x))
    
    elif y[:3] == "gra":
        return Grams(float(x))
    
    elif y[:9] == "milligra":
        return Milligrams(float(x))
    
    elif y[:3] == "flu":
        return FlOunces(float(x))
    
    elif y[:3] == "cup":
        return Cups(float(x))
    
    elif y[:3] == "qua":
        return Quarts(float(x))
    
    elif y[:3] == "gal":
        return Gallons(float(x))
    
    elif y[:3] == "oun":
        return Ounces(float(x))
    
    elif y[:3] == "pou":
        return Pounds(float(x))

    else:
        print("Try again")

def splitter(y, x):
    splitter = y.get(x[0]).split()
    return splitter

# MAIN PROGRAM
def ingredients():
    # CREATING KEYS FROM INGREDIENTS WITH ENTRIES
    ingredients = {}
    item = input("Type your ingredient like so 'carrots: 1.5 pounds, cow milk: 1 gallon'\n")

    
    entry = item.split(',')         # seperate ingredients with amounts
    for i in entry:             #For every block of ('ingredient: amount'),
        amount = i.split(':')       #create ingredient and amount tuple
        ingredients[amount[0]] = amount[1]          # enter key and value in dictionary
        split = splitter(ingredients, amount)                   #finding key and splitting value so that amount[0] is the figure and [1] is the unit.
        ingConv = RECIPATOR(float(split[0]), split[1])          #converting and storing in variable
        ingredients[amount[0]] = " ".join(map(str, ingConv))    #updating key

    #eventually save Dictionary as a recipe
    #make an option to see both amounts side -by -side
    #make it so you can enter number first as well
    #be able to enter lb(s), g, oz
    #check if item[0] is number or letter and go from there
    print(ingredients)


ingredients()