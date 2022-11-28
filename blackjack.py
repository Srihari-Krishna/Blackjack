import random

K=10;Q=10;J=10;A=1
deck=[2,3,4,5,6,7,8,9,10,'K','Q','J','A']*4
suit=['heart','spade','clubs','diamond']*13
suit_value={'heart':'♥','spade':'♠' , 'clubs':'♣' , 'diamond':'♦' }

dealer=[]
user=[]
temp=[]

def make_card(hand):
    for i in hand:
        rsuit=random.choice(suit)
        z=suit_value[rsuit]
        if i==10:
            print("┌──────────┐")
            print("│{}. . . . │".format(10))
            print("│. . . . . │")
            print("│. . . . . │")
            print("│. . {} . . │".format(z))
            print("│. . . . . │")
            print("│. . . . . │")
            print("│. . . .{} │".format(10))
            print("└──────────┘")
        else:
            print("┌──────────┐")
            print("│{} . . . . │".format(i))
            print("│. . . . . │")
            print("│. . . . . │")
            print("│. . {} . . │".format(z))
            print("│. . . . . │")
            print("│. . . . . │")
            print("│. . . . {} │".format(i))
            print("└──────────┘")


def deal(checker1,checker2):
    if(checker1):
        dealer_card=random.choice(deck)
        dealer.append(dealer_card)
        deck.remove(dealer_card)
    if(checker2):    
        user_card=random.choice(deck)
        user.append(user_card)
        deck.remove(user_card)
        if(len(user)<2):
            deal(False,True)
    hit_stand()        

def hit_stand():
    print("DEALER HAS : ")
    dealer_copy=list(dealer)
    make_card(dealer_copy)
    input()
    print("YOU HAVE : ")
    user_copy=list(user)
    make_card(user_copy)
    input()
    user_input=input("Enter H/S for hit or stand : ")
    if(user_input=='H'):
        deal(False,True)

    if(user_input=='S'):
        dealer_hand()

def dealer_hand():
    temp=list(dealer)
    
    def tempsum():
        while('A' in temp):
            index=temp.index('A')
            temp[index]=0
        
        while('K' in temp):
            index=temp.index('K')
            temp[index]=10

        while('Q' in temp):
            index=temp.index('Q')
            temp[index]=10

        while('J' in temp):
            index=temp.index('J')
            temp[index]=10  

        temp_sum=sum(temp)


        while(0 in temp):
            temp.remove(0)
            temp_sum=sum(temp)
            if(temp_sum<11):
                temp_sum+=11
            else:
                temp_sum+=1    
    
    tempsum()
    while(sum(temp)<17):
        dealer_card=random.choice(deck)
        dealer.append(dealer_card)
        deck.remove(dealer_card)
        temp=list(dealer)
        tempsum()
    
    blackjack()    

def blackjack():
    print("DEALER HAS : ")
    dealer_copy=list(dealer)
    make_card(dealer_copy)
    input()
    
    print("YOU HAVE : ")
    user_copy=list(user)
    make_card(user_copy)
    input()
    
    
    
    
    while('A' in user):
        index=user.index('A')
        user[index]=0

    while('K' in user):
        index=user.index('K')
        user[index]=10

    while('Q' in user):
        index=user.index('Q')
        user[index]=10

    while('J' in user):
        index=user.index('J')
        user[index]=10        
    
    user_sum=sum(user)

    while 0 in user:
    
        user.remove(0)
        user_sum=sum(user)
        if(user_sum<11):
            user_sum+=11
        else:
            user_sum+=1    

          
    
    
    while('A' in dealer):
        index=dealer.index('A')
        dealer[index]=0
        
    while('K' in dealer):
        index=dealer.index('K')
        dealer[index]=10

    while('Q' in dealer):
        index=dealer.index('Q')
        dealer[index]=10

    while('J' in dealer):
        index=dealer.index('J')
        dealer[index]=10  

    dealer_sum=sum(dealer)


    while(0 in dealer):
        dealer.remove(0)
        dealer_sum=sum(dealer)
        if(dealer_sum<11):
            dealer_sum+=11
        else:
            dealer_sum+=1    

      

    if user_sum>21:
        print("YOU BUSTED. YOU LOSE!!")
        exit()

    if dealer_sum>21:
        print("Dealer Busted \n You win")
        exit()

    if user_sum==21:
        print("BLACKJACK! \n You win")
        exit()

    if user_sum<dealer_sum:
        print("YOU LOSE! ")
        exit()

    if user_sum>dealer_sum:
        print("YOU WIN")
        exit() 

    if user_sum==dealer_sum:
        print("Draw")
        exit()     

deal(True,True)                                  
