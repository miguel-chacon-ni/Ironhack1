#!/usr/bin/env python
# coding: utf-8

# In[33]:


n_player=27
empire=list([])
foreign_regions={"Anatolia":3, "Syria":3, "Phoenicia":3, "Judea":3, "Gaza":3, "Egypt":3, "Mesopotamia":3, "Persia":3, "Bactria":3}


# In[34]:


#Attacker has three or more infantry and defender has two or more 
def three_v_two():
    global foreign_regions
    global n_player
    global c
    x=input ("Type Roll to attack!")
    if x!="Roll":
        print("ERROR: You must type 'Roll'")
    attacker_roll=[]
    defender_roll=[]
    while len(attacker_roll)<3:
        attacker_roll.append(random.randint(1,6))

    while len(defender_roll)<2:
        defender_roll.append(random.randint(1,6))

    attacker_roll.sort(reverse=True)
    defender_roll.sort(reverse=True)
    if x=="Roll":
        print ("You got " + str(attacker_roll[0])+ ", "+str(attacker_roll[1])+", and "+str(attacker_roll[2]) + "!")
        print ("Your opponent got " + str(defender_roll[0])+ " and "+str(defender_roll[1])+ "!")
    if defender_roll[0]>=attacker_roll[0] and defender_roll[1]>=attacker_roll[1]:
        n_player=n_player-2
        print("You've lost both battles and are down two infantry!")
    if defender_roll[0]<attacker_roll[0] and defender_roll[1]<attacker_roll[1]:
        foreign_regions[c]=foreign_regions[c]-2
        print("You've won both battles!"+ c + " is down two infatry!")
    if defender_roll[0]<attacker_roll[0] and defender_roll[1]>=attacker_roll[1]:
        n_player=n_player-1
        foreign_regions[c]=foreign_regions[c]-1
        print("You've lost the first battle but won the second! You've each lost one infantry!")
    if defender_roll[0]>=attacker_roll[0] and defender_roll[1]<attacker_roll[1]:
        n_player=n_player-1
        foreign_regions[c]=foreign_regions[c]-1
        print("You've won the first battle but lost the second! You're each down one infantry!")
    print("You have " + str(n_player) + " infantry left. "+ str(foreign_regions[c]) + " infantry remain garrisoned in " + c)


# In[35]:


#Attacker has three or more and defender has one
def three_v_one():
    global foreign_regions
    global n_player
    x=input ("Type Roll to attack!")
    if x!="Roll":
        print("ERROR: You must type 'Roll'")
    attacker_roll=[]
    defender_roll=[]
    while len(attacker_roll)<3:
        attacker_roll.append(random.randint(1,6))

    while len(defender_roll)<1:
        defender_roll.append(random.randint(1,6))

    attacker_roll.sort(reverse=True)
    defender_roll.sort(reverse=True)
    if x=="Roll":
        print ("You got " + str(attacker_roll[0])+ ", "+str(attacker_roll[1])+", and "+str(attacker_roll[2]) + "!")
        print ("Your opponent got " + str(defender_roll[0])+ "!")
        results=[]
    if defender_roll[0]>=attacker_roll[0]:
        n_player=n_player-1
        print("You've lost the battle and are down one infantry!")
    if defender_roll[0]<attacker_roll[0]:
        foreign_regions[c]=foreign_regions[c]-1
        print("You've won the battle and taken the region!")
    print("You have " + str(n_player) + " infantry left. "+ str(foreign_regions[c]) + " infantry remain garrisoned in " + c)


# In[36]:


##Attacker has two infanrty and defender has two or more 
def two_v_two():
    global foreign_regions
    global n_player
    x=input ("Type Roll to attack!")
    if x!="Roll":
        print("ERROR: You must type 'Roll'")
    attacker_roll=[]
    defender_roll=[]
    while len(attacker_roll)<2:
        attacker_roll.append(random.randint(1,6))

    while len(defender_roll)<2:
        defender_roll.append(random.randint(1,6))

    attacker_roll.sort(reverse=True)
    defender_roll.sort(reverse=True)
    if x=="Roll":
        print ("You got " + str(attacker_roll[0])+ ", "+str(attacker_roll[1])+ "!")
        print ("Your opponent got " + str(defender_roll[0])+ " and "+str(defender_roll[1])+ "!")
    results=[]
    if defender_roll[0]>=attacker_roll[0] and defender_roll[1]>=attacker_roll[1]:
        n_player=n_player-2
        print("You've lost both battles and have lost the war!")
    if defender_roll[0]<attacker_roll[0] and defender_roll[1]<attacker_roll[1]:
        foreign_regions=foreign_regions-2
        print("You've won both battles! Your opponent is down two infatry!")
    if defender_roll[0]<attacker_roll[0] and defender_roll[1]>=attacker_roll[1]:
        n_player=n_player-1
        foreign_regions=foreign_regions-1
        print("You've lost the first battle but won the second! You've each lost one infantry!")
    if defender_roll[0]>=attacker_roll[0] and defender_roll[1]<attacker_roll[1]:
        n_player=n_player-1
        foreign_regions=foreign_regions-1
        print("You've won the first battle but lost the second! You're each down one infantry!")
    print("You have " + str(n_player) + " infantry left. "+ str(foreign_regions[c]) + " infantry remain garrisoned in " + c)


# In[37]:


#Attacker has two and defender has one
def two_v_one():
    global foreign_regions
    global n_player    
    x=input ("Type Roll to attack!")
    if x!="Roll":
        print("ERROR: You must type 'Roll'")
    attacker_roll=[]
    defender_roll=[]
    while len(attacker_roll)<2:
        attacker_roll.append(random.randint(1,6))

    while len(defender_roll)<1:
        defender_roll.append(random.randint(1,6))

    attacker_roll.sort(reverse=True)
    defender_roll.sort(reverse=True)
    if x=="Roll":
        print ("You got " + str(attacker_roll[0])+ ", "+str(attacker_roll[1])+ "!")
        print ("Your opponent got " + str(defender_roll[0])+ "!")
        results=[]
    if defender_roll[0]>=attacker_roll[0]:
        n_player=n_player-1
        print("You've lost the battle and are down one infantry!")
    if defender_roll[0]<attacker_roll[0]:
        foreign_regions=foreign_regions-1
        print("You've won the battle and taken the region!")
    print("You have " + str(n_player) + " infantry left. "+ str(foreign_regions[c]) + " infantry remain garrisoned in " + c)


# In[38]:


##Attacker has one infanrty and defender has two or more 
n_player=3
n_cpu=3
def one_v_two():
    global foreign_regions
    global n_player
    x=input ("Type Roll to attack!")
    if x!="Roll":
        print("ERROR: You must type 'Roll'")
    attacker_roll=[]
    defender_roll=[]
    while len(attacker_roll)<1:
        attacker_roll.append(random.randint(1,6))

    while len(defender_roll)<2:
        defender_roll.append(random.randint(1,6))

    attacker_roll.sort(reverse=True)
    defender_roll.sort(reverse=True)
    if x=="Roll":
        print ("You got " + str(attacker_roll[0])+"!")
        print ("Your opponent got " + str(defender_roll[0])+ " and "+str(defender_roll[1])+ "!")
    results=[]
    if defender_roll[0]>=attacker_roll[0]:
        n_player=n_player-1
        print("You've lost the battle and the war!")
    if defender_roll[0]<attacker_roll[0]:
        foreign_regions=foreign_regions-1
        print("You've won the battle and captured the region!")
    print("You have " + str(n_player) + " infantry left. "+ str(foreign_regions[c]) + " infantry remain garrisoned in " + c)


# In[39]:


##Attacker has one infanrty and defender has one 
def one_v_one():
    global foreign_regions
    global n_player
    x=input ("Type Roll to attack!")
    if x!="Roll":
        print("ERROR: You must type 'Roll'")
    attacker_roll=[]
    defender_roll=[]
    while len(attacker_roll)<1:
        attacker_roll.append(random.randint(1,6))

    while len(defender_roll)<1:
        defender_roll.append(random.randint(1,6))

    attacker_roll.sort(reverse=True)
    defender_roll.sort(reverse=True)
    if x=="Roll":
        print ("You got " + str(attacker_roll[0])+"!")
        print ("Your opponent got " + str(defender_roll[0])+ "!")
    results=[]
    if defender_roll[0]>=attacker_roll[0]:
        n_player=n_player-1
        print("You've lost the battle and the war!")
    if defender_roll[0]<attacker_roll[0]:
        foreign_regions=foreign_regions-1
        print("You've won the battle")
    print("You have " + str(n_player) + " infantry left. "+ str(foreign_regions[c]) + " infantry remain garrisoned in " + c)


# In[ ]:


def battle():
    global foreign_regions
    global n_player

    if n_player >=3 and foreign_regions[c] >=2:
        three_v_two()
    if n_player >=3 and foreign_regions[c] ==1:
        three_v_one()
    if n_player ==2 and foreign_regions[c] >=2:
        two_v_two()
    if n_player ==2 and foreign_regions[c] ==1:
        two_v_one()
    if n_player ==1 and foreign_regions[c] >=2:
        one_v_two
    if n_player ==1 and foreign_regions[c] ==1:
        one_v_one()
    if foreign_regions[c]==0:
        print("You've captured "+ c)
        empire.append(c)
        print("You currently hold"+str(set(empire)))
        if c=="Anatolia":
            print("In May 334 BC, Alexander crossed the Dardanelles into Asia Minor, then a part of the Persian Empire. In northwestern Anatolia, near the site of Troy, his army confronted and defeated a combined force of Persian vassals and Greek Mercenaries. The battle of Granicus River marked Alexander’s first major victory against the Persian empire and cleared the way for his advance into Asia.")
    while foreign_regions[c]!=0 and len(empire)<9:
        battle()
    if foreign_regions[c]==0 and len(empire)<9:
        choose_conquest()
    


# In[ ]:


def choose_conquest():
    global n_player
    global c
    global empire
    global foreign_regions
    if len(empire)>=9:
        print("Alexander wept, for there were no more wolrds left to conquer. You have won!")
    if len(empire)<9:
        c=input ("Which region will you conquer: Anatolia, Syria, Phoenicia, Judea, Gaza, Egypt, Mesopotamia, Persia or Bactria?")
        if c=='Anatolia' or c=='Syria' or c=='Phoenicia' or c=='Judea' or c=='Gaza' or c=='Egypt' or c=='Mesopotamia' or c=='Persia' or c=='Bactria':
            print("You are invading " +c+ "!")
            print("There are "+str(foreign_regions[c])+" divisions garrisoned in "+c)
        battle()


# In[ ]:


def launch_game():
    import random
    global n_player
    global empire
    global foreign_regions
    n_player=27
    empire=list([])
    foreign_regions={"Anatolia":3, "Syria":3, "Phoenicia":3, "Judea":3, "Gaza":3, "Egypt":3, "Mesopotamia":3, "Persia":3, "Bactria":3}
    choose_conquest()


# In[42]:


launch_game()

