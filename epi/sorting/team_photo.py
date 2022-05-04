'''

[5,10,13]
[2,100,200]


'''
def teamPhoto(team1, team2):
    team1.sort()
    team2.sort()

    oneFront = True
    for height1, height2 in zip(team1, team2):
        if height1 > height2:
            oneFront = False
            break
    
    twoFront = True
    for height1, height2 in zip(team1, team2):
        if height2 > height1:
            twoFront = False
            break

    return oneFront or twoFront