import addFilm,readFlim, updateFilm, deleteFlim, filmReports

# create a function 
def filmsMenuOptions():
    # options is an integer variable 
    options = 0
    # print(type(options))

    # optionsList is a list data structure with string elements/items
    optionsList = ["1","2","3","4","5","6"]

    userChoices = "films MenuOptions\nEnter:\n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Reports.\n6. Exit."
    # check and then execute code if the value held in the options variable is not present in the list 
    while options not in optionsList:
        print(userChoices)

        # re-assign the value in the options variable
        options = input("Enter an option from the films Menu choices above: ")

        # check if the value held in options not in the optionsList
        if options not in optionsList:
            print(f"{options} is not a valid choice in the films menu!")
        # print(type(options))
    return options


# create a boolean variable 
mainProgram = True
print(type(mainProgram))
while mainProgram: # same while True
    # create mainMenu variable and initialise/assign it with the function songsMenuOptions()
    mainMenu = filmsMenuOptions()

    # if user input is 1 or 2 or 3 or 4 or 5 or  6
    if mainMenu == "1":
        # call/invoke the respective module(file) and the function from the file
        readFlim.read()
    elif mainMenu == "2":
        addFilm.insert()
    elif mainMenu == "3":
        updateFilm.update()
    elif mainMenu == "4":
        deleteFlim.delete()
    elif mainMenu == "5":
        filmsMenuOptions.Reports()
    else:
        mainProgram = False
        input("Press enter to exit the program : ")