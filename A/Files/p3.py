def minion_game(stg):
    kevin_score = 0
    stuart_score = 0
    vowels = 'AEIOU'

    for i in range(len(stg)):
        if stg[i] in vowels:
            kevin_score += (len(stg)-i)
        else:
            stuart_score += (len(stg)-i)

    if kevin_score > stuart_score:
        print("kevin",kevin_score)
    elif kevin_score < stuart_score:
        print("stuart",stuart_score)
    else:
        print("draw")

s = input("Enter the String: ")
minion_game(s)        