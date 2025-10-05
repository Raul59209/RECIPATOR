#METRIC TO IMPERIAL VOLUME
def Liters(x):
    print(x * 1.057, "quarts") if x * 1.057 < 4 else print(x * 0.264, "gallons")
        
def Milliliters(x):
    print(x * 0.0338, "fluid ounces") if x * 0.0338 < 8 else print(x * 0.0042, "cups")

#METRIC TO IMPERIAL WEIGHT
def Kilograms(x):
    print(x * 2.2046)

def Grams(x):
    print(x * 0.035, "ounces") if x * 0.035 <= 8 else print(x * 0.002205, "pounds")

def Milligrams(x):
    print(x*0.000035, "ounces")

#IMPERIAL TO METRIC VOLUME
def FlOunces(x):
    print(x * 29.57, "milliliters") if x * 29.57 < 1000 else print((x * 29.57) * .001, "liters")

def Cups(x):
    print(x * 236.6, "milliliters") if x * 236.6 < 1000 else print((x * 236.6) * .001, "liters")

def Quarts(x):
    print(x * 0.95, "liters")

def Gallons(x):
    print(x * 3.785, "liters")

#IMPERIAL TO METRIC WEIGHT
def Ounces(x):
    return(x * 28350, "milligrams") if x * 28350 < 1000 else (x * 28.35, "grams")

def Pounds(x):
    print(x * 453.59237, "grams") if x * 453.59237 < 1000 else print(x * 0.454, "kilograms")


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
    item = input("Type your ingredient like so 'carrots: 1.5 pounds'\n")

    # seperate ingredient and amount, adding to dictionary
    x = item.split(':')
    ingredients[x[0]] = x[1]

    # eventually be able to copy and paste ingredients and immediately have split into dictionary
    #eventually save Dictionary as a recipe

    #finding key and splitting value so that x[0] is the amount and [1] is the unit.
    boob = splitter(ingredients, x)

    #converting and storing in variable
    ingConv = RECIPATOR(float(boob[0]), boob[1])

    #updating key
    ingredients[x[0]] = " ".join(map(str, ingConv))
    print(ingredients)

ingredients()