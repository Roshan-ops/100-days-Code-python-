print(" Welcome to the Treasure Isalnd. \n Are you read to find some tresaure? ")
print(" YOur MIssion is to find the treasure without making wrong choise \n let's are you the choosen one ?" )
first = input("Which direction do you want to move ? Left or right ?")
first = first.lower()
if first =="left":
    print(" Let's keep on walking")

    print(" Look there a jungle")
    second = Input (" What to do to cross the jungle, Search weapon or search food")
    second = second.lower()

    if second == "Search weapon":
        print(" Great idea lets do this")

        print(" look there is a wolf, he is comming at us")
        third = input(" Choose between two, Fight or run" )
        third = third.(lower)

        if third == "fight":
            print("Use you weapon and fight")

        else:
            print("Run like there is no tommorrow  ! wolf catches you game over")

            print ("This is the last huddule chose carefully" )
             fourth = input (" Choose between four side  holes? East, west, south and north " )
             fourth = fourth.lower()

             if fourth == "East":
                print("East or west east is the best but no in this case you fall in to trap ! Game Over " )

            elif fourth == "west":
                print(" Well done you have chose the wrong side hole ! game over" )

            elif fourth == " south":
                print(" Welcome to hell, You have came very far but no far enough. Be my lunch !! Game Over " )

            else:
                print(" We got our lucky man the choose one. Yo have won the game ! Congurational")

    else:
        print(" Animal smells the food and came after you, game over")



else:
    print("Let's climb the ladder... game over") 