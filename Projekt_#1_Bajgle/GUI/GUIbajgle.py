import tkinter as tk
import random
from tkinter import BOTH

#Define start game value
NUM_DIGITS = 3
MAX_GUESSES = 10
num_guesses = 1
empty_answer = []

#Define window
root = tk.Tk()
root.iconbitmap("bagels.ico")
root.title("Bajgle - Gra logiczna")
root.geometry("450x450")
root.resizable(0,0)

# Define fonts and colors
rule_font = ("Cambria", 10)
rule_font_big = ("Cambria", 11)
bg_color = "#FFC971"
button_color = "#CC5803"
button_color_active = "#E2711D"
root.config(bg = bg_color)




def start_game():
    global secret_num

    secret_num = get_secret_num()
    #print(secret_num)
    rule_frame.destroy()
    start_frame.destroy()
    

    AI_frame.pack(padx = 5, pady= 5,ipady=5, ipadx =70)
    PL_frame.pack(fill=BOTH, expand = True, padx = 5, pady= 5)

    
    answer_info.grid(padx=100,pady=3,ipadx =4,ipady=1,row=0,column=0,columnspan=2)
    answer_entry.grid(pady=3,ipadx =4,ipady=1,row=1,column=0,sticky="E")
    answer_button.grid(pady=3,ipadx =4,ipady=1,row=1,column=1,sticky="W")
    restart_button.grid(row=0,column=1)
    for i in range(MAX_GUESSES+1):
        empty_answer[i].grid(row=i+1,ipadx= 70, padx=5,pady=1,sticky="WE")
        print(i)

    AI_label.grid(row=0,ipadx= 70, padx=5,pady=5,sticky="WE")

def ok_click():
    global guess, num_guesses,answer_entry,secret_num,empty_answer11
    while num_guesses <= MAX_GUESSES:
        guess = str(answer_entry.get())
        while len(guess) == NUM_DIGITS or not guess.isdecimal():
            #print(num_guesses)
            clues = getClues(guess, secret_num)   
            empty_answer = tk.Label(AI_frame, text="Próba #{}: {}".format(num_guesses,clues),background=bg_color)
            empty_answer.grid(row=num_guesses,ipadx= 70, padx=5,pady=1,sticky="WE")
            num_guesses +=1
            break
        break
    if num_guesses > MAX_GUESSES:
        tries_answer = tk.Label(AI_frame, text="Szanse się skończyły! Odpowiedź to: {}".format(secret_num),background=bg_color)
        tries_answer.grid(row=11,ipadx= 70, padx=5,pady=1,sticky="WE")
        answer_button.config(state="disabled")

def getClues(guess, secret_num):
    global num_guesses,answer_button
    if guess == secret_num:
        answer_button.config(state="disabled")
        return "Brawo!!! udało się!"
        
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append('Piko')
    if len(clues) == 0:
        return "Bajgle"
    else:
        clues.sort()
        return " ".join(clues)
    
def restart_game():
    global secret_num,num_guesses,empty_answer
    for i in range(MAX_GUESSES+1):
        empty_answer[i] = tk.Label(AI_frame, text="",background=bg_color)
        empty_answer[i].grid(row=i+1,ipadx= 70, padx=5,pady=1,sticky="WE")
        answer_button.config(state="active")
        num_guesses = 1
        get_secret_num()

def get_secret_num():
    global secret_num
    numbers = list('0123456789')
    random.shuffle(numbers)


    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num
    
# Define layouts
rule_frame = tk.LabelFrame(root, padx = 5, pady = 5,background=bg_color)
start_frame = tk.LabelFrame(root, padx = 5, pady = 5,background=bg_color)
rule_frame.pack( padx = 5, pady= 5)
start_frame.pack(fill=BOTH, expand = True, padx = 5, pady= 5)

#Define start window labels
rules_label = tk.Label(rule_frame, text = '''Bajgle, to logiczna gra na dedukcję. Mam na mysli {}-cyfrową
 liczbę, w której nie powtarza się żadna z cyfr. Spróbuj ją odgadnąć. \n
    Oto wskazówki:'''.format(NUM_DIGITS),background=bg_color,font=rule_font,justify="center")
rules_label2 = tk.Label(rule_frame, text = '''
    Gdy mówię:\n                                                                
    Piko - Jedna cyfra jest poprawna, ale jest na złej pozycji\n        
    Fermi - Jedna cyfra jest poprawna i znajduje sie w
                     odpowiednim miejscu\n    
    Bajgle - Żadna cyfra nie jest poprawna\n''',justify='left',background=bg_color,font=rule_font_big)    

rules_label3 = tk.Label(rule_frame, text = '''Na przykład, jeśli tajna liczba to248, a Ty podasz liczbe 843, 
    wskazówka będzie brzmieć Fermi Piko.''',background=bg_color,font=rule_font)  

start_button = tk.Button(start_frame,text = "START",background=button_color,activebackground=button_color_active,command=start_game)
start_button.grid(padx=150,pady=30,ipadx =40,ipady=15)
rules_label.grid(row=0,column=0,sticky='E')
rules_label2.grid(row=1,column=0,sticky='W')
rules_label3.grid(row=2,column=0,sticky='WE')

#Define after Start click layouts
AI_frame = tk.LabelFrame(root, padx = 5, pady = 5,background=bg_color)
PL_frame = tk.LabelFrame(root, padx = 5, pady = 5,background=bg_color)
AI_label = tk.Label(AI_frame, text = '''Mam na myśli liczbę. 
Masz {} prób, by odgadnąć, jaka to liczba. \n
Oto wskazówki:'''.format(MAX_GUESSES),background=bg_color,font=rule_font,justify="center")
answer_info = tk.Label(PL_frame,text = "Tutaj wpisz odpowiedź i kliknij 'OK' ",font = rule_font_big,background=bg_color)
answer_entry = tk.Entry(PL_frame,width=5,font=rule_font_big)
answer_button = tk.Button(PL_frame,text = "OK",background=button_color,activebackground=button_color_active,command=ok_click)
restart_button = tk.Button(PL_frame,text = "Restart",background=button_color,activebackground=button_color_active,command=restart_game)
for i in range(MAX_GUESSES+1):
    empty_answer.append(tk.Label(AI_frame, text="",background=bg_color))


    
#Run the root mainloop
root.mainloop()