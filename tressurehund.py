print("find the tressure")
choice1 = input("choose left or right").lower()
if choice1 == "left":
    choice2 = input("choose swim or wait").lower()
    if choice2 == "wait":
        Choice3 = input("choose yellow red blue").lower()
        if Choice3 == "yellow":
            print("you win")
        else:
            print("you lose")
    else:
        print("you lose")
else:
    print("you lose")