from tkinter import *
from tkinter import messagebox
import random

deck=[]
dealer=[]
player=[]
player_score=0
dealer_score=0
player_ace=False  
dealer_ace=False

def shuffle():
    
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    for suit in suits:
        
        for card in range(1, 11):
            name = 'cards/{}_{}.png'.format(str(card), suit)
            card_image = PhotoImage(file=name)
            deck.append((card, card_image ))

        for card in face_cards:
            name = 'cards/{}_{}.png'.format(str(card), suit)
            card_image = PhotoImage(file=name)
            deck.append((10, card_image )) 

    hit()
    hit()
    dealer_card=random.choice(deck)
    dealer.append(dealer_card[1])
    value=dealer_card[0]
    dealer_compute(value)
    deck.remove(dealer_card)
    
    dframe=Label(dealer_frame ,image=dealer_card[1]).pack(side='left', padx=20 , pady=20)

def dealer_hit():

    while(dealer_score<17):

        dealer_card=random.choice(deck)
        dealer.append(dealer_card[1])
        value=dealer_card[0]
        dealer_compute(value)
        deck.remove(dealer_card)
    
        dframe=Label(dealer_frame ,image=dealer_card[1]).pack(side='left', padx=20,pady=20)
    blackjack()

def hit():

    player_card=random.choice(deck)
    player.append(player_card[1])
    value=player_card[0]
    player_compute(value)
    deck.remove(player_card)
    pframe=Label(player_frame,image=player_card[1]).pack(side='left',padx=20,pady=20)
    
def player_compute(val):

    global player_score , player_ace
    if val==1 and not player_ace:
        player_ace=True
        val=11
    player_score +=val

    if player_score > 21 and player_ace:
        player_score -=10
        player_ace=False

def dealer_compute(val):
    
    global dealer_score , dealer_ace
    if val==1 and not dealer_ace:
        dealer_ace=True
        val=11
    dealer_score +=val

    if dealer_score > 21 and dealer_ace:
        dealer_score-=10
        dealer_ace=False    

def new_game():
    
    for widgets in player_frame.winfo_children():
      widgets.destroy()

    for widgets in dealer_frame.winfo_children():
      widgets.destroy()  

    global deck, dealer, player, player_score,dealer_score,player_ace,dealer_ace  
    deck=[]
    dealer=[]
    player=[]
    player_score=0
    dealer_score=0
    player_ace=False  
    dealer_ace=False

    shuffle()
    
def blackjack():
    cond=True
    if player_score>21:
        messagebox.showinfo("Result","You BUSTED!")
        cond=False
    elif dealer_score>21:
        messagebox.showinfo("Result","Dealer busted. You Win!")
        cond=False

    if player_score==21 and cond or dealer_score==21 and cond:
        if dealer_score>player_score:
            messagebox.showinfo("Result",'Dealer wins by BLACKJACK!!')
            cond=False
        if player_score>dealer_score:
            messagebox.showinfo("Result","You Win by BLACKJACK!!!")
            cond=False
        if player_score==dealer_score:
            messagebox.showinfo("Result","Draw")
            cond=False  
              
    if player_score<21 and dealer_score<21 and cond:
        if dealer_score>player_score:
            messagebox.showinfo("Result",'Dealer wins!!')
        if player_score>dealer_score:
            messagebox.showinfo("Result","You Win!!!")   
        if player_score==dealer_score:
            messagebox.showinfo("Result","Draw")         

#GUI screen
root=Tk()
root.title('Blackjack')
root.geometry("800x700")
root.configure(background='green')

title_text=Label(root,bg='green', text='Blackjack', font=("MS Serif", 35))
title_text.pack(padx=50, pady=20)

frame=Frame(root, bg='green')
frame.pack(pady=20)

dealer_frame=LabelFrame(frame , text='Dealer Cards:',font=("MS Serif", 12), bd=0 )
dealer_frame.pack()

player_frame=LabelFrame(frame, text='Player Cards:',font=("MS Serif", 12), bd=0)
player_frame.pack(pady=20 )

dealer_label=Label(dealer_frame , text="")
dealer_label.pack(padx=20)

player_label=Label(player_frame , text="")
player_label.pack(padx=20)

button_frame=Button(root, bg='green',bd=0)
button_frame.pack(pady=20)

hit_button=Button(button_frame, text="Hit" , font=17, command=hit  )
hit_button.grid(row=0 , column=0 , padx=10)

stand_button=Button(button_frame, text="Stand" , font=17 , command=dealer_hit)
stand_button.grid(row=0, column=1)

shuffle_button=Button(button_frame, text="New Game" ,font=17 , command=new_game)
shuffle_button.grid(row=0, column=2 , padx=10)

shuffle()
root.mainloop()

