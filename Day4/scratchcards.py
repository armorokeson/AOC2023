import sys
import re

def part1():
    pile = open(sys.argv[-1], 'r').read().split('\n')
    
    total = 0
    for card in pile:
        split_card = re.split('[:|\|]', card)
        winning_numbers = re.findall(r'\d+', split_card[1])
        card_numbers = re.findall(r'\d+', split_card[2])
        
        wins = 0
        for num in winning_numbers:
            if num in card_numbers:
                wins += 1
        
        total += 0 if wins <= 0 else (2**(wins-1))
        
    print(total)
    
def part2():
    pile = open(sys.argv[-1], 'r').read().split('\n')
    
    cards = []
    for card in pile:
        split_card = re.split('[:|\|]', card)
        card_num = int(re.findall(r'\d+', split_card[0])[0])
        winning_numbers = re.findall(r'\d+', split_card[1])
        card_numbers = re.findall(r'\d+', split_card[2])
        
        wins = 0
        for num in winning_numbers:
            if num in card_numbers:
                wins += 1
                
        for i in range(card_num, card_num+wins):
            pile.append(pile[i])
            
    print(len(pile))
      
part2()
    
    