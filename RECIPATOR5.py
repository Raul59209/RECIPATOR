######## UPDATE NOTES: CAN TAKE MULTIPLE INGREDIENTS, ACCEPTS UNIT ABBREVIATIONS, AND ANY INPUT STYLE ########
import json

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
    

# MAIN PROGRAM
def ingredients():
    # CREATING KEYS FROM INGREDIENTS WITH ENTRIES
    ingredients = {}
    pantry = {}
    item = input("Type your ingredients: \n")

    
    entry = item.split(', ')         # seperate ingredients with amounts
    #entry = item.split("\n")
    entries = {}                    # dictionary to hold each ingredient entry
    convEntries = {}                # dictionary to hold converted entries
    for i in range(len(entry)):     #For every block of ('ingredient: amount'),
        entries[i] = entry[i]       # create a numbered key for each entry in the dictionary
    uny = None              # unit variable
    numy = None                         
    for r in range(len(entries)):       # for every entry in the dictionary
        ingy = entries[r].split(' ')    # split each entry into a list of words
        for i in ingy:          # for every word in the list
            if i == 'ounces' or i == 'ounce' or i == 'oz' or i == 'pounds' or i == 'pound' or i == 'lb' or i == 'lbs' or i == 'grams' or i == 'gram' or i == 'g' or i == 'fluid ounces' or i == 'fluid ounce' or i == 'floz' or i == 'gallon' or i == 'gallons' or i == 'liters' or i == 'liter' or i == 'l' or i == 'quarts' or i == 'quart' or i == 'cups' or i == 'cup' or i == 'ml' or i == 'mg' or i == 'kg':
                uny = i
            elif i.isnumeric():
                numy = i
            else:
                pass
            
        ingy.remove(numy)           # remove the number from the list
        ingy.remove(uny)            # remove the unit from the list
        entries[' '.join(ingy)] = numy, uny  # create a new key with the ingredient name and assign it a tuple of (number, unit)
        del entries[r]         # delete the old numbered key    


    for i in entries:
        convEntries[i] = RECIPATOR(float(entries[i][0]), entries[i][1])

    print(entries)
    print(convEntries)

    # pantryQ = input("Would you like to add to your pantry?")
    # if 'y' in pantryQ.lower():
    #     print(f"Here's your current pantry: ")
    #     with open('pantry.json', 'r') as f:
    #         pantry = json.load(f)
    #         print(pantry)
    #     ingredient = input("What ingredient would you like to add to your pantry? ")
    #     amount = input("How much do you have? (number) ")
    #     units = input("What unit is that in or do you have it in pieces? ")
    #     for i in pantry:
    #         if i == ingredient:
    #             pantry[i] = pantry((i)[1]) + amount, units
    #         else:
    #             pantry.add(i)
    #     with open('pantry.json', 'a') as f:
    #        f.write(pantry)
    # question = input("Would you like to save your recipe? Yes or No: ")
    # if 'y' in question.lower():
    #     nameIs = input("What is the name of this recipe? ")
    #     unitIs = input("Would you like to save it converted or unconverted? C/U: ")
    #     with open('cookbook.py', 'a') as f:
    #         if unitIs.lower() == 'u':
    #             unitIs = entries
    #         else:
    #             unitIs = convEntries
    #         f.write(f"{nameIs} = {unitIs}\n")
    #     print("Recipe saved to cookbook.")

ingredients()