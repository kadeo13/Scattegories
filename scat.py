#!/usr/bin/python
import random
import time
import sys

CATEGORIES = [{'prompt': "A Boy's Name", 'used':False}, {'prompt': "A River", 'used':False}, {'prompt': "An Animal", 'used':False}, {'prompt': "Things That Are Cold", 'used':False}, {'prompt': "Insects", 'used':False}, {'prompt': "TV Shows", 'used':False}, {'prompt': "Things That Grow", 'used':False}, {'prompt': "Fruits", 'used':False}, {'prompt': "Things That Are Black", 'used':False}, {'prompt': "School Subjects", 'used':False}, {'prompt': "Movie Titles", 'used':False}, {'prompt': "Musical Instruments", 'used':False}, {'prompt': "Authors", 'used':False}, {'prompt': "Bodies Of Water", 'used':False}, {'prompt': "A Bird", 'used':False}, {'prompt': "Countries", 'used':False}, {'prompt': "Cartoon Characters", 'used':False}, {'prompt': "Holidays", 'used':False}, {'prompt': "Things That Are Square", 'used':False}, {'prompt': "In The USA", 'used':False}, {'prompt': "Clothing", 'used':False}, {'prompt': "A Relative", 'used':False}, {'prompt': "Games", 'used':False}, {'prompt': "Sport's Stars", 'used':False}, {'prompt': "School Supplies", 'used':False}, {'prompt': "Things That Are Hot", 'used':False}, {'prompt': "Heroes", 'used':False}, {'prompt': "A Girl's Name", 'used':False}, {'prompt': "Fears", 'used':False}, {'prompt': "TV Stars", 'used':False}, {'prompt': "Colors", 'used':False}, {'prompt': "A Fish", 'used':False}, {'prompt': "Vegetable", 'used':False}, {'prompt': "Provinces or States", 'used':False}, {'prompt': "Sports equipment", 'used':False}, {'prompt': "Tools", 'used':False}, {'prompt': "Breakfast Foods", 'used':False}, {'prompt': "Flowers", 'used':False}, {'prompt': "Ice Cream Flavors", 'used':False}, {'prompt': "A Drink", 'used':False}, {'prompt': "Toys", 'used':False}, {'prompt': "Cities", 'used':False}, {'prompt': "Things in the kitchen", 'used':False}, {'prompt': "Ocean things", 'used':False}, {'prompt': "Nicknames", 'used':False}, {'prompt': "Hobbies", 'used':False}, {'prompt': "Parts of the Body", 'used':False}, {'prompt': "Sandwiches", 'used':False}, {'prompt': "Items In A Magazine", 'used':False}, {'prompt': "World Leaders", 'used':False}, {'prompt': "School Subjects", 'used':False}, {'prompt': "Excuses For Being Late", 'used':False}, {'prompt': "Presidents", 'used':False}, {'prompt': "Things That Jump/Bounce", 'used':False}, {'prompt': "Television Stars", 'used':False}, {'prompt': "Things In A Park", 'used':False}, {'prompt': "Foreign Cities", 'used':False}, {'prompt': "Stones/Gems", 'used':False}, {'prompt': "Musical Instruments", 'used': False}, {'prompt': "Nicknames" , 'used': False}, {'prompt': "Things In The Sky", 'used': False}, {'prompt': "Pizza Toppings", 'used': False}, {'prompt': "Colleges/Universities", 'used': False}, {'prompt': "Fish", 'used': False}, {'prompt': "Countries", 'used': False}, {'prompt': "Things That Have Spots", 'used': False}, {'prompt': "Historical Figures", 'used': False}, {'prompt': "Something You're Afraid Of", 'used': False}, {'prompt': "Terms Of Endearment", 'used': False}, {'prompt': "Items In This Room", 'used': False}, {'prompt': "Drugs/Medicine", 'used': False}, {'prompt': "Fictional Characters", 'used': False}, {'prompt': "Menu Items", 'used': False}, {'prompt': "Newspapers", 'used': False}, {'prompt': "Capitals", 'used': False}, {'prompt': "Candy", 'used': False}, {'prompt': "Expensive Items", 'used': False}, {'prompt': "Footwear", 'used': False}, {'prompt': "Something You Keep Hidden", 'used': False}, {'prompt': "Items In A Suitcase", 'used': False}, {'prompt': "Things With Tails", 'used': False}, {'prompt': "Electronics", 'used': False}, {'prompt': "Crimes", 'used': False}, {'prompt': "Things That Are Sticky", 'used': False}, {'prompt': "Awards/Ceremonies", 'used': False}, {'prompt':"Cars" , 'used': False}, {'prompt': "Spices/Herbs", 'used': False}, {'prompt': "Bad Habits", 'used': False}, {'prompt': "Cosmetics/Toiletries", 'used': False}, {'prompt': "Celebrities", 'used': False}, {'prompt': "Cooking Utensils", 'used': False}, {'prompt': "Reptiles/Amphibians", 'used': False}, {'prompt': "Parks", 'used': False}, {'prompt': "Leisure Activities", 'used': False}, {'prompt': "Things You're Allergic To", 'used': False}, {'prompt': "Restaurants", 'used': False}, {'prompt': "Notorious People", 'used': False}, {'prompt': "Breakfast Food", 'used': False}, {'prompt': "Things In A Medicine Cabinet", 'used': False}, {'prompt': 'Toys', 'used': False}, {'prompt': 'Household Chores', 'used': False}, {'prompt': 'Bodies Of Water', 'used': False}, {'prompt': 'Authors', 'used': False}, {'prompt': 'Halloween Costumes', 'used': False}, {'prompt': 'Weapons', 'used': False}, {'prompt': 'Things That Are Round', 'used': False}, {'prompt': 'Words Associated With Exercise', 'used': False}, {'prompt': 'Singers/Bands', 'used': False}, {'prompt': 'Song Titles', 'used': False}, {'prompt': 'Villains', 'used': False}, {'prompt': 'Famous Duos And Trios', 'used': False}, {'prompt': 'Games', 'used': False}, {'prompt': 'Literary Characters', 'used': False}, {'prompt': 'Store Names', 'used': False}, {'prompt': 'Personality Traits', 'used': False}, {'prompt': 'Things That Use A Remote', 'used': False}, {'prompt': 'Offensive Words', 'used': False}, {'prompt': 'Words Ending In N', 'used': False}, {'prompt': 'Things People Gossip About', 'used': False}]
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V','W','Y','Z']
print "Player 1 Name: "
p1 = raw_input()
p1Score = 0
print "Player 2 Name: "
p2 = raw_input()
p2Score = 0

print "How many rounds? "
rounds = int(raw_input())
rounds = range(rounds)

print "Welcome " + str(p1) + " and " + str(p2) + "!" 

for i in rounds:
    print "Press enter when ready to start the round..."
    wait = raw_input()
    r = i + 1
    scatList = []
    letter = ALPHABET[random.randint(0,23)]  
    for x in range(8):
       promptUsed = False
       while promptUsed != True:
           rand = random.randint(0, 118)
           prompt = CATEGORIES[rand]
           if prompt['used'] == False:
               promptUsed = True
               CATEGORIES[rand]['used'] = True
       q = prompt['prompt']
       scatList.append(q)

    print "Round " + str(r)
    print "Letter: " + letter
    print "Here's the list: "
    for j in range(len(scatList)):
        print str(j+1) + ".  " + str(scatList[j]) 
    print "Press enter to begin 60 sec timer."
    w = raw_input()
    print "GO!"
    t = 60
    while t > 0:
        sys.stdout.write('\r{:02d}s'.format(t))
        t -= 1
        sys.stdout.flush()
        time.sleep(1)
    print "\nSTOP!!!"
    print "How many points did " + p1 + " get?"
    s = raw_input()
    p1Score += int(s)
    print "How many points did " + p2 + " get?"
    d = raw_input()
    p2Score += int(d)
print "GAME OVER!"
print p1 + " Score: " + str(p1Score)
print p2 + " Score: " + str(p2Score)
if p1Score > p2Score:
    print p1 + " wins!"
elif p2Score > p1Score:
    print p2 + " wins!"
else:
    print "It's a tie. Everyone wins!"

