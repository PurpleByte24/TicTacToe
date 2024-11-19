from guizero import App, Box, Text, PushButton, TextBox

app = App(title="TicTacToe", bg=(255,255,255), layout="grid", width="295", height="510")
app.text_color = (0, 0, 0)

question = "Fill in your names and press SUBMIT!"
question1 = "You want to play TicTacToe?"

box = Box(app, layout="grid", grid=[0,1],  align="left")
box1 = Box(app, layout="grid", grid=[0,0], align="top")
box2 = Box(app, layout="grid", grid=[0,2], align="left")
box3 = Box(app, layout="grid", grid=[0,4], align="left")

## Signs
sign1 = "X"
sign2 = "O"

##Spielernamen, -status und -turn
player_1 = ""
player_2 = ""
player_status = "not chosen"
players_turn = "not chosen"
winner = "nobody"

##Button-Werte
button1_wert = ""
button2_wert = ""
button3_wert = ""
button4_wert = ""
button5_wert = ""
button6_wert = ""
button7_wert = ""
button8_wert = ""
button9_wert = ""

##Spots
open_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

##Definition Button Command
def zeichen_setzen1():
    global button1_wert, question
    if players_turn == player_1:
        button1_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button1_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button1.text = button1_wert
    open_spots.remove(1)
    check_won()
    
def zeichen_setzen2():
    global button2_wert, question
    if players_turn == player_1:
        button2_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button2_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button2.text = button2_wert
    open_spots.remove(2)
    check_won()
    
def zeichen_setzen3():
    global button3_wert, question
    if players_turn == player_1:
        button3_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button3_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button3.text = button3_wert
    open_spots.remove(3)
    check_won()
    
def zeichen_setzen4():
    global button4_wert, question
    if players_turn == player_1:
        button4_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button4_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button4.text = button4_wert
    open_spots.remove(4)
    check_won()
    
def zeichen_setzen5():
    global button5_wert, question
    if players_turn == player_1:
        button5_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button5_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button5.text = button5_wert
    open_spots.remove(5)
    check_won()
    
def zeichen_setzen6():
    global button6_wert, question
    if players_turn == player_1:
        button6_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button6_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button6.text = button6_wert
    open_spots.remove(6)
    check_won()
    
def zeichen_setzen7():
    global button7_wert, question
    if players_turn == player_1:
        button7_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button7_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button7.text = button7_wert
    open_spots.remove(7)
    check_won()
    
def zeichen_setzen8():
    global button8_wert, question
    if players_turn == player_1:
        button8_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button8_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button8.text = button8_wert
    open_spots.remove(8)
    check_won()
    
def zeichen_setzen9():
    global button9_wert, question
    if players_turn == player_1:
        button9_wert = sign1
        question = player_2 + "(O), click the field you would like to choose."
        check_players_turn()
    elif players_turn == player_2:
        button9_wert = sign2
        question = player_1 + "(X), click the field you would like to choose."
        check_players_turn1()
    button9.text = button9_wert
    open_spots.remove(9)
    check_won()
    
##Widgets
instructions = Text(box1, bg=(255,255,255), text=question, color=(0, 0, 0), grid=[0,1], align="top", width="42", height="2")
first_question = Text(box1, bg=(255,255,255), text=question1, color=(0, 0, 0), grid=[0,0], align="top", width="42", height="2")

button1 = PushButton(box, text=button1_wert, grid=[0,1], align="left", width=5, height=5, visible = False, command=zeichen_setzen1)
button2 = PushButton(box, text=button2_wert, grid=[1,1], align="left", width=5, height=5, visible = False, command=zeichen_setzen2)
button3 = PushButton(box, text=button3_wert, grid=[2,1], align="left", width=5, height=5, visible = False, command=zeichen_setzen3)
button4 = PushButton(box, text=button4_wert, grid=[0,2], align="left", width=5, height=5, visible = False, command=zeichen_setzen4)
button5 = PushButton(box, text=button5_wert, grid=[1,2], align="left", width=5, height=5, visible = False, command=zeichen_setzen5)
button6 = PushButton(box, text=button6_wert, grid=[2,2], align="left", width=5, height=5, visible = False, command=zeichen_setzen6)
button7 = PushButton(box, text=button7_wert, grid=[0,3], align="left", width=5, height=5, visible = False, command=zeichen_setzen7)
button8 = PushButton(box, text=button8_wert, grid=[1,3], align="left", width=5, height=5, visible = False, command=zeichen_setzen8)
button9 = PushButton(box, text=button9_wert, grid=[2,3], align="left", width=5, height=5, visible = False, command=zeichen_setzen9)

name_player_1 = TextBox(box2, grid=[1,1])
name_player_2 = TextBox(box2, grid=[1,2])
titel_name_1 = Text(box2, text = "Player 1:", grid=[0, 1])
titel_name_2 = Text(box2, text = "Player 2:", grid=[0, 2])

##Gamesetting
game = "off"

##Definitionen
def set_spieler_names():
    global player_1, player_2, question, player_status, game
    player_1 = name_player_1.value
    player_2 = name_player_2.value
    submit_button.hide()
    titel_name_1.hide()
    titel_name_2.hide()
    name_player_1.hide()
    name_player_2.hide()
    app.height="364"
    first_question.destroy()
    button1.visible = True
    button2.visible = True
    button3.visible = True
    button4.visible = True
    button5.visible = True
    button6.visible = True
    button7.visible = True
    button8.visible = True
    button9.visible = True
    question = ""
    instructions.value = question
    player_status = "chosen"
    game = "on"
    check_player_status()

    
submit_button = PushButton(box3, text="SUBMIT", command=set_spieler_names, grid=[0,0])

def check_player_status():
    global players_turn
    players_turn = player_1
    if player_status == "chosen":
        if players_turn == player_1:
            global question
            question = player_1 + '(X), click the field you would like to choose.'
            instructions.value = question

def check_players_turn():
    global players_turn
    players_turn = player_2
    instructions.value = question
def check_players_turn1():
    global players_turn
    players_turn = player_1
    instructions.value = question
    
def change_colour():
    instructions.bg=(0, 255, 0)
    button1.disable()
    button2.disable()
    button3.disable()
    button4.disable()
    button5.disable()
    button6.disable()
    button7.disable()
    button8.disable()
    button9.disable()

def check_won():
    global winner, game, question
    if (button1_wert == button2_wert and button2_wert == button3_wert and button1_wert == sign1) or \
        (button4_wert == button5_wert and button5_wert == button6_wert and button4_wert == sign1) or \
        (button7_wert == button8_wert and button8_wert == button9_wert and button7_wert == sign1) or \
        (button1_wert == button4_wert and button4_wert == button7_wert and button1_wert == sign1) or \
        (button2_wert == button5_wert and button5_wert == button8_wert and button2_wert == sign1) or \
        (button3_wert == button6_wert and button6_wert == button9_wert and button3_wert == sign1) or \
        (button1_wert == button5_wert and button5_wert == button9_wert and button1_wert == sign1) or \
        button3_wert == button5_wert and button5_wert == button7_wert and button3_wert == sign1:
        winner = player_1
        game = "off"
        
    if (button1_wert == button2_wert and button2_wert == button3_wert and button1_wert == sign2) or \
        (button4_wert == button5_wert and button5_wert == button6_wert and button4_wert == sign2) or \
        (button7_wert == button8_wert and button8_wert == button9_wert and button7_wert == sign2) or \
        (button1_wert == button4_wert and button4_wert == button7_wert and button1_wert == sign2) or \
        (button2_wert == button5_wert and button5_wert == button8_wert and button2_wert == sign2) or \
        (button3_wert == button6_wert and button6_wert == button9_wert and button3_wert == sign2) or \
        (button1_wert == button5_wert and button5_wert == button9_wert and button1_wert == sign2) or \
        button3_wert == button5_wert and button5_wert == button7_wert and button3_wert == sign2:
        winner = player_2
        game = "off"
        
    if game == "off":
        question = ('Winner is ' + winner + '!')
        instructions.value = question
        change_colour()

app.display()