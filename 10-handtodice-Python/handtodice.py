# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().


def handtodice(hand):
    # your code goes here
    dice = hand
    num1 = dice % 10
    dice = dice//10
    num2 = dice % 10
    dice = dice//10
    num3 = dice % 10
    return num3, num2, num1
