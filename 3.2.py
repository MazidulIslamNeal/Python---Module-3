cabin_class = input("Please enter the cabin clas you want travel(LUX/A/B/C): ")

LUX = "upper-deck cabin with a balcony."
A = "above the car deck, equipped with a window."
B = "windowless cabin, above the car desk."
C = "windowless cabin, below the car desk."

if cabin_class == "LUX":
    print (f"You have chosen {LUX}")
elif cabin_class == "A":
    print(f"You have chosen {A}")
elif cabin_class == "B":
    print (f"You have chosen {B}")
elif cabin_class == "C":
    print (f"You have chosen {C}")
else:
    print("Invalid cabin class.Please enter LUX/A/B/C.")
