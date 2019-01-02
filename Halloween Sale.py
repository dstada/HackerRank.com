def howManyGames(prijs, d, m, budget):
    # Return the number of games you can buy
    besteed_bedrag = 0
    gekocht = 0
    while besteed_bedrag + prijs <= budget:       # Zolang besteed bedrag niet meer is dan budget s
        # koop vindt plaats
        besteed_bedrag += prijs     # besteed bedrag ophogen met de prijs
        gekocht += 1                # aantal gekocht ophogen
        print("gekocht: {}".format(gekocht))
        print("gekocht voor {}".format(prijs))
        if prijs - d >= m:           # zolang prijs niet onder de onderwaarde komt
            prijs -= d              # prijs kleiner maken met d
            print("prijs kleiner gemaakt met {} tot {}".format(d, prijs))
        else:
            prijs = m
        print("besteed: {}".format(besteed_bedrag))
    return gekocht


if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)
    print(answer)
    """
    20 3 6 80 --> 6
    
    20 3 6 85 --> 7
    """