# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some
# helper functions that do part of the work, and then those helper functions will make our final
# function much easier to write.

# Also note: we will represent a arm of 3 dice as a single 3-digit integer. So the arm 4-3-2 will
# be represented by the integer 432. With that, let's start writing some code. Be sure to write
# your functions in the same order as given here, since later functions will make use of earlier
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by
# calling score, which you already wrote). The function should return two values -- the resulting arm
# and the score for that arm. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))


def bonusplaythreediceyahtzee(dice):
    d = str(dice)
    arm = int(d[-3:])
    dice = int(d[:-3])
    for x in str(arm):
        if (str(arm).count(x) == 3):
            return (arm, 20 + (int(x) * 3))
    arm, dice = armstep(arm, dice)
    arm, dice = armstep(arm, dice)
    h = list(armtodice(arm))
    for x in h:
        if h.count(x) == 3:
            return (arm, 20 + (x * 3))
        elif h.count(x) == 2:
            return (arm, 10 + (x * 2))
    return (arm, max(h))


def armstep(arm, dice):
    arm1 = list(armtodice(arm))
    temp = 0
    for x in arm1:
        if arm1.count(x) > 1:
            arm1 = [val for val in arm1 if val == x]
    temp = 3-len(arm1)

    if len(arm1) == 3:
        arm1 = [max(arm1)]
        temp = 3-len(arm1)

    while temp > 0:
        q = dice % 10
        dice //= 10
        arm1.append(q)
        temp -= 1

    return order_dice(arm1[0], arm1[1], arm1[2]), dice


def armtodice(arm):
    arm = str(arm)
    return (int(arm[0]), int(arm[1]), int(arm[2]))


def order_dice(a, b, c):
    arm = [a, b, c]
    high_pos = arm.index(max(arm))
    lowe_pos = arm.index(min(arm))

    mid_pos = [ind for ind in [0, 1, 2] if ind not in [high_pos, lowe_pos]][0]
    return arm[high_pos] * 100 + arm[mid_pos] * 10 + arm[lowe_pos]
