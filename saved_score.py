import shelve

# Adding player score to the file
def score_add(play):
    fil = shelve.open("score.txt")

    # if player id is on the file then use its score
    # else create it and use its score
    if str(play.id) in fil:
        score_ = fil[str(play.id)]
    else:
        fil[str(play.id)] = [0, 0]
        score_ = fil[str(play.id)]

    return (score_, fil)

# Adding a point to losing score
def lose_plus(play):

    (score_, fil) = score_add(play)

    fil[str(play.id)] = [score_[0], score_[1]+1]

    fil.close

# Adding a point to winning score
def win_plus(play):
    
    (score_, fil) = score_add(play)

    fil[str(play.id)] = [score_[0]+1, score_[1]]

    fil.close