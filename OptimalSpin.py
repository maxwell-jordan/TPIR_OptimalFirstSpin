
def main():
    opponentTotal = 65
    bestCurrentOption = 5
    bestRolls = 0
    currentOption = 60
    while currentOption < opponentTotal:
        overRolls = currentOption / 5
        underRolls = (opponentTotal - currentOption - 5) / 5
        goodRolls = 20 - (overRolls + underRolls)
        if goodRolls > bestRolls:
            bestCurrentOption = currentOption
            bestRolls = goodRolls
        currentOption = currentOption + 5

    print("The best option is " + str(bestCurrentOption))
    print("The best number of rolls is " + str(bestRolls))

    return



if __name__ == "__main__":
    main()
