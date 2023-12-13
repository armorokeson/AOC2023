import sys
import re

CARDS = '123456789TJQKA'

def quicksort(hands):
    if len(hands) <= 1:
        return hands
    else:
        pivot = hands[0]
        left = [x for x in hands[1:] if compare_hands(x[:5], pivot[:5]) == -1]
        right = [x for x in hands[1:] if compare_hands(x[:5], pivot[:5]) == 1]
        return quicksort(left) + [pivot] + quicksort(right)

def compare_hands(hand1, hand2):
    first = calculate_strength(hand1)
    second = calculate_strength(hand2)
    if first > second: return 1
    if first < second: return -1
    return tie_break(hand1,hand2)

def calculate_strength(hand):
    possible_hands = [[1,1,1,1,1], [2,1,1,1], [2,2,1], [3,1,1], [3,2], [4,1], [5]]

    counts = {}
    for card in hand:
        counts[card] = (len(list(filter(lambda x: x == card, hand))))

    values = sorted(counts.values(), reverse=True)

    return possible_hands.index(values)+1

def tie_break(hand1, hand2):
    for i in range(5):
        if CARDS.index(hand1[i]) > CARDS.index(hand2[i]): return 1
        if CARDS.index(hand1[i]) < CARDS.index(hand2[i]): return -1
    return 0

def part1():
    file = open(sys.argv[-1], 'r')
    hands = file.read().split('\n')

    sorted_hands = quicksort(hands)

    winnings = 0
    for i in range(len(sorted_hands)):
        bid = int(re.search(r'\d+', sorted_hands[i][6:]).group())
        winnings += (bid*(i+1))

    print(winnings)

part1()