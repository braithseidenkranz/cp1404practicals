COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff", "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50", "Amber": "#ffbf00", "Antique White": "#faebd7", "Amethyst": "#9966cc", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
print(COLOUR_TO_CODE)

max_colour_length = max(len(colour) for colour in COLOUR_TO_CODE)
for colour, code in COLOUR_TO_CODE.items():
    print(f"{colour:{max_colour_length}} is {code}")


colour = input("Enter colour: ").title()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").title()