from tkinter import *
from Dungeon import *
from Fighter import *
from random import randint, shuffle

dungeon_maze_multi_dimensional_list = [[]]
pool_of_fighters = []
player = Fighter(None, None, None, None, None, None, None)
bad_guy_to_fight = Fighter(None, None, None, None, None, None, None)
dungeon_name = None
dungeon_description = None
current_row = int(randint(0, 3))
current_column = int(randint(0, 3))
current_location = [], []
maze_button_list = [[]]
start_dungeon_location = str(current_row) + str(current_column)


def initialize_maze_and_start_game():
    global dungeon_maze_multi_dimensional_list, player, bad_guy_to_fight, pool_of_fighters, \
        dungeon_name, dungeon_description

    player_hit_points = randint(300, 500)
    computer1_hit_points = randint(100, 500)
    computer2_hit_points = randint(100, 500)
    computer3_hit_points = randint(100, 500)
    computer4_hit_points = randint(100, 500)
    computer5_hit_points = randint(100, 500)
    computer6_hit_points = randint(100, 500)
    computer7_hit_points = randint(100, 500)
    computer8_hit_points = randint(100, 500)
    computer9_hit_points = randint(100, 500)
    computer10_hit_points = randint(100, 500)
    computer11_hit_points = randint(100, 500)
    computer12_hit_points = randint(100, 500)
    computer13_hit_points = randint(100, 500)
    computer14_hit_points = randint(100, 500)
    computer15_hit_points = randint(100, 500)
    computer16_hit_points = randint(100, 500)

    player_min_damage = randint(1, 50)
    computer1_min_damage = randint(1, 50)
    computer2_min_damage = randint(1, 50)
    computer3_min_damage = randint(1, 50)
    computer4_min_damage = randint(1, 50)
    computer5_min_damage = randint(1, 50)
    computer6_min_damage = randint(1, 50)
    computer7_min_damage = randint(1, 50)
    computer8_min_damage = randint(1, 50)
    computer9_min_damage = randint(1, 50)
    computer10_min_damage = randint(1, 50)
    computer11_min_damage = randint(1, 50)
    computer12_min_damage = randint(1, 50)
    computer13_min_damage = randint(1, 50)
    computer14_min_damage = randint(1, 50)
    computer15_min_damage = randint(1, 50)
    computer16_min_damage = randint(1, 50)

    player_max_damage = randint(50, 100)
    computer1_max_damage = randint(50, 100)
    computer2_max_damage = randint(50, 100)
    computer3_max_damage = randint(50, 100)
    computer4_max_damage = randint(50, 100)
    computer5_max_damage = randint(50, 100)
    computer6_max_damage = randint(50, 100)
    computer7_max_damage = randint(50, 100)
    computer8_max_damage = randint(50, 100)
    computer9_max_damage = randint(50, 100)
    computer10_max_damage = randint(50, 100)
    computer11_max_damage = randint(50, 100)
    computer12_max_damage = randint(50, 100)
    computer13_max_damage = randint(50, 100)
    computer14_max_damage = randint(50, 100)
    computer15_max_damage = randint(50, 100)
    computer16_max_damage = randint(50, 100)

    player = Fighter("Soulless Hero", "This will be too easy", player_hit_points, player_hit_points,
                     player_min_damage,
                     player_max_damage, "img/Little_Mac.png")

    Hulk_Hogan = Fighter("Hulk Hogan", "Holywood Hogan", computer1_hit_points, computer1_hit_points,
                         computer1_min_damage, computer1_max_damage, "img/Hulk_Hogan.png")

    The_Undertaker = Fighter("The Undertaker", "The Master of Pain", computer2_hit_points, computer2_hit_points,
                             computer2_min_damage, computer2_max_damage, "img/Undertaker.png")

    Steve_Austin = Fighter("Steve Austin", "Stone Cold Steve Austin", computer3_hit_points, computer3_hit_points,
                           computer3_min_damage, computer3_max_damage, "img/Steve_Austin.png")

    Randy_Savage = Fighter("Randy Savage", "Macho Man", computer4_hit_points, computer4_hit_points,
                           computer4_min_damage, computer4_max_damage, "img/Randy_Savage.png")

    Dwayne_Johnson = Fighter("Dwayne Johnson", "The Rock", computer5_hit_points, computer5_hit_points,
                             computer5_min_damage, computer5_max_damage, "img/Dwayne_Johnson.png")

    John_Cena = Fighter("John Cena", "The Prototype", computer6_hit_points, computer6_hit_points,
                        computer6_min_damage, computer6_max_damage, "img/John_Cena.png")

    Rey_Mysterio = Fighter("Rey Mysterio", "El Nino", computer7_hit_points, computer7_hit_points,
                           computer7_min_damage, computer7_max_damage, "img/Rey_Mysterio.png")

    Arnold_Schwarzenegger = Fighter("Arnold Schwarzenegger", "The Terminator", computer8_hit_points,
                                    computer8_hit_points, computer8_min_damage, computer8_max_damage,
                                    "img/Arnold_Schwarzenegger.png")

    Hugh_Jackman = Fighter("Hugh Jackman", "Wolverine", computer9_hit_points, computer9_hit_points,
                           computer9_min_damage, computer9_max_damage, "img/Hugh_Jackman.png")

    Bowser = Fighter("Bowser", "Mario's Nemesis", computer10_hit_points, computer10_hit_points,
                     computer10_min_damage, computer10_max_damage, "img/Bowser.png")

    King_Boo = Fighter("King Boo", "Evil Ghost", computer11_hit_points, computer11_hit_points,
                       computer11_min_damage, computer11_max_damage, "img/King_Boo.png")

    Bowser_Jr = Fighter("Bowser Jr.", "The Son of Mario's Nemesis", computer12_hit_points, computer12_hit_points,
                        computer12_min_damage, computer12_max_damage, "img/Bowser_Jr.png")

    The_Joker = Fighter("The Joker", "Batman's Nemesis", computer13_hit_points, computer13_hit_points,
                        computer13_min_damage, computer13_max_damage, "img/Joker.png")

    Thanos = Fighter("Thanos", "Destroyer of Worlds", computer14_hit_points, computer14_hit_points,
                     computer14_min_damage, computer14_max_damage, "img/Thanos.png")

    Dr_Evil = Fighter("Dr. Evil", "Mad Scientist", computer15_hit_points, computer15_hit_points,
                      computer15_min_damage, computer15_max_damage, "img/Dr_Evil.png")

    Pin_Head = Fighter("Pin Head", "Who you calling Pin Head?", computer16_hit_points, computer16_hit_points,
                       computer16_min_damage, computer16_max_damage, "img/Pinhead.png")

    pool_of_fighters = [Hulk_Hogan, The_Undertaker, Steve_Austin, Randy_Savage, Dwayne_Johnson, John_Cena,
                        Rey_Mysterio,
                        Arnold_Schwarzenegger, Hugh_Jackman, Bowser, King_Boo, Bowser_Jr, The_Joker, Thanos,
                        Dr_Evil,
                        Pin_Head]

    shuffle(pool_of_fighters)
    stole_soul_winner = randint(0, 15)
    pool_of_fighters[stole_soul_winner].stole_soul = True

    d1 = Dungeon('The Stinky Dungeon', 'This dungeon smells really, really bad!', pool_of_fighters[0])
    d2 = Dungeon('The Eyesore Dungeon', 'This dungeon looks terrible!', pool_of_fighters[1])
    d3 = Dungeon('The Painful Dungeon', 'This dungeon is painful. ow!', pool_of_fighters[2])
    d4 = Dungeon('The Hearing Impairment Dungeon', 'Why can\'t I hear anything?', pool_of_fighters[3])
    d5 = Dungeon('The Distasteful Dungeon', 'Idk, tastes pretty bad in here man...', pool_of_fighters[4])
    d6 = Dungeon('The Sad Dungeon', 'Do you want to cry yet?', pool_of_fighters[5])
    d7 = Dungeon('The Hateful Dungeon', 'This dungeon makes you angry >:(',
                 pool_of_fighters[6])
    d8 = Dungeon('The Hysterical Dungeon', 'Wait... why am I laughing hahahaha',
                 pool_of_fighters[7])
    d9 = Dungeon('The Scary Dungeon', 'Be Afraid, Be Very Afraid.', pool_of_fighters[8])
    d10 = Dungeon('The Powerless Dungeon', 'I\'m feeling a bit faint...',
                  pool_of_fighters[9])
    d11 = Dungeon('The False Hope Dungeon', 'Well, there\'s no hope for you here', pool_of_fighters[10])
    d12 = Dungeon('The Death Dungeon', 'Try not to die here ;)',
                  pool_of_fighters[11])
    d13 = Dungeon('The Doomed Dungeon', 'We\'re all dooooomed!!!', pool_of_fighters[12])
    d14 = Dungeon('The Doubtful Dungeon', 'Doubting yourself yet?',
                  pool_of_fighters[13])
    d15 = Dungeon('The Disturbed Dungeon', 'Let\'s get down with the sickness dude!', pool_of_fighters[14])
    d16 = Dungeon('The Happy Dungeon', 'Hey! Who said you can be happy, huh!?', pool_of_fighters[15])

    list_of_dungeons = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16]
    shuffle(list_of_dungeons)

    dungeon_maze_multi_dimensional_list = [
        [list_of_dungeons[0], list_of_dungeons[1], list_of_dungeons[2], list_of_dungeons[3]],
        [list_of_dungeons[4], list_of_dungeons[5], list_of_dungeons[6], list_of_dungeons[7]],
        [list_of_dungeons[8], list_of_dungeons[9], list_of_dungeons[10], list_of_dungeons[11]],
        [list_of_dungeons[12], list_of_dungeons[13], list_of_dungeons[14], list_of_dungeons[15]],
    ]

    dungeon_maze_multi_dimensional_list[0][0] = list_of_dungeons[0]
    dungeon_maze_multi_dimensional_list[0][1] = list_of_dungeons[1]
    dungeon_maze_multi_dimensional_list[0][2] = list_of_dungeons[2]
    dungeon_maze_multi_dimensional_list[0][3] = list_of_dungeons[3]
    dungeon_maze_multi_dimensional_list[1][0] = list_of_dungeons[4]
    dungeon_maze_multi_dimensional_list[1][1] = list_of_dungeons[5]
    dungeon_maze_multi_dimensional_list[1][2] = list_of_dungeons[6]
    dungeon_maze_multi_dimensional_list[1][3] = list_of_dungeons[7]
    dungeon_maze_multi_dimensional_list[2][0] = list_of_dungeons[8]
    dungeon_maze_multi_dimensional_list[2][1] = list_of_dungeons[9]
    dungeon_maze_multi_dimensional_list[2][2] = list_of_dungeons[10]
    dungeon_maze_multi_dimensional_list[2][3] = list_of_dungeons[11]
    dungeon_maze_multi_dimensional_list[3][0] = list_of_dungeons[12]
    dungeon_maze_multi_dimensional_list[3][1] = list_of_dungeons[13]
    dungeon_maze_multi_dimensional_list[3][2] = list_of_dungeons[14]
    dungeon_maze_multi_dimensional_list[3][3] = list_of_dungeons[15]

    dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
    dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description
    bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter


class FindMySoul:
    def __init__(self):

        global player, bad_guy_to_fight, dungeon_name, dungeon_description, current_row, \
            current_column, start_dungeon_location, maze_button_list, current_location

        self.root = Tk()
        self.root.title("Find My Soul Game")
        self.root.geometry('1600x800')

        # Title
        self.label_Title = Label(self.root, text="Find My Soul", font=('Arial', 30))
        self.label_Title.place(x=500, y=50)

        # Attack/Heal Buttons
        self.attack_button = Button(self.root, text="Attack", padx=20, pady=10, font=('Arial', 20),
                                    command=self.attack_button_pressed)
        self.attack_button.place(x=100, y=380)

        self.heal_button = Button(self.root, state=NORMAL, text="Heal", padx=27, pady=10, font=('Arial', 20),
                                  command=self.heal_button_pressed)
        self.heal_button.place(x=100, y=480)

        # Player Image
        self.player_image = PhotoImage(file=player.image)
        self.label_image = Label(self.root, image=self.player_image)
        self.label_image.place(x=300, y=300)

        # Player Titles
        self.label_player_name = Label(self.root, text="Player Name: {}".format(player.name))
        self.label_player_name.place(x=300, y=190)
        self.label_player_description = Label(self.root, text="Player Description: {}".format(player.description))
        self.label_player_description.place(x=300, y=210)
        self.label_current_hit_points = Label(self.root, font=('Arial', 14, 'bold'),
                                              text="Current Hitpoints: {}".format(player.current_hit_points))
        self.label_current_hit_points.place(x=300, y=570)
        self.label_min_damage = Label(self.root, text="Min Damage: {}".format(player.min_damage))
        self.label_min_damage.place(x=300, y=230)
        self.label_max_damage = Label(self.root, text="Max Damage: {}".format(player.max_damage))
        self.label_max_damage.place(x=300, y=250)

        # Opponent Image
        self.opponent_image = PhotoImage(file=bad_guy_to_fight.image)
        self.label_opponent_image = Label(self.root, image=self.opponent_image)
        self.label_opponent_image.place(x=700, y=300)

        # Opponent Titles
        self.label_opponent_name = Label(self.root, text="Opponent Name: {}".format(bad_guy_to_fight.name))
        self.label_opponent_name.place(x=700, y=190)
        self.label_opponent_description = Label(self.root, text="Opponent Description: {}".format(
            bad_guy_to_fight.description))
        self.label_opponent_description.place(x=700, y=210)
        self.label_opponent_hit_points = Label(self.root, font=('Arial', 14, 'bold'),
                                               text="Current Hitpoints: {}".format(
                                                   bad_guy_to_fight.current_hit_points))
        self.label_opponent_hit_points.place(x=700, y=570)
        self.label_opponent_min_damage = Label(self.root,
                                               text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
        self.label_opponent_min_damage.place(x=700, y=230)
        self.label_opponent_max_damage = Label(self.root,
                                               text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
        self.label_opponent_max_damage.place(x=700, y=250)

        # Fight Description
        self.label_fight_description1 = Label(self.root, text="Click either the Attack or Heal button")
        self.label_fight_description1.place(x=480, y=660)
        self.label_fight_description2 = Label(self.root, text="")
        self.label_fight_description2.place(x=480, y=680)

        # Maze Buttons / row 1
        self.button00 = Button(self.root, padx=15, pady=8, command=self.button00_Pressed, state=DISABLED)
        self.button00.place(x=1100, y=295)
        self.button01 = Button(self.root, padx=15, pady=8, command=self.button01_Pressed, state=DISABLED)
        self.button01.place(x=1140, y=295)
        self.button02 = Button(self.root, padx=15, pady=8, command=self.button02_Pressed, state=DISABLED)
        self.button02.place(x=1180, y=295)
        self.button03 = Button(self.root, padx=15, pady=8, command=self.button03_Pressed, state=DISABLED)
        self.button03.place(x=1220, y=295)

        # row 2
        self.button10 = Button(self.root, padx=15, pady=8, command=self.button10_Pressed, state=DISABLED)
        self.button10.place(x=1100, y=335)
        self.button11 = Button(self.root, padx=15, pady=8, command=self.button11_Pressed, state=DISABLED)
        self.button11.place(x=1140, y=335)
        self.button12 = Button(self.root, padx=15, pady=8, command=self.button12_Pressed, state=DISABLED)
        self.button12.place(x=1180, y=335)
        self.button13 = Button(self.root, padx=15, pady=8, command=self.button13_Pressed, state=DISABLED)
        self.button13.place(x=1220, y=335)

        # row 3
        self.button20 = Button(self.root, padx=15, pady=8, command=self.button20_Pressed, state=DISABLED)
        self.button20.place(x=1100, y=375)
        self.button21 = Button(self.root, padx=15, pady=8, command=self.button21_Pressed, state=DISABLED)
        self.button21.place(x=1140, y=375)
        self.button22 = Button(self.root, padx=15, pady=8, command=self.button22_Pressed, state=DISABLED)
        self.button22.place(x=1180, y=375)
        self.button23 = Button(self.root, padx=15, pady=8, command=self.button23_Pressed, state=DISABLED)
        self.button23.place(x=1220, y=375)

        # row 4
        self.button30 = Button(self.root, padx=15, pady=8, command=self.button30_Pressed, state=DISABLED)
        self.button30.place(x=1100, y=415)
        self.button31 = Button(self.root, padx=15, pady=8, command=self.button31_Pressed, state=DISABLED)
        self.button31.place(x=1140, y=415)
        self.button32 = Button(self.root, padx=15, pady=8, command=self.button32_Pressed, state=DISABLED)
        self.button32.place(x=1180, y=415)
        self.button33 = Button(self.root, padx=15, pady=8, command=self.button33_Pressed, state=DISABLED)
        self.button33.place(x=1220, y=415)

        # GUI MAZE BUTTON INITIALIZER LIST
        maze_button_list = [
            [self.button00, self.button01, self.button02, self.button03],
            [self.button10, self.button11, self.button12, self.button13],
            [self.button20, self.button21, self.button22, self.button23],
            [self.button30, self.button31, self.button32, self.button33]
        ]

        # Current Location
        current_location = maze_button_list[current_row][current_column]
        current_location.config(highlightbackground="black")

        # Dungeon Titles
        self.label_Dungeon = Label(self.root, text="Dungeon Maze Map", font=('Arial', 20, 'bold'))
        self.label_Dungeon.place(x=1080, y=250)
        self.label_Dungeon_name1 = Label(self.root, text="Dungeon Name:", font=('Arial', 14, 'bold'))
        self.label_Dungeon_name2 = Label(self.root, text="{}".format(dungeon_name))
        self.label_Dungeon_name1.place(x=1080, y=470)
        self.label_Dungeon_name2.place(x=1080, y=490)
        self.label_Dungeon_description1 = Label(self.root, text="Dungeon Description:", font=('Arial', 14, 'bold'))
        self.label_Dungeon_description2 = Label(self.root,
                                                text="{}".format(dungeon_description))
        self.label_Dungeon_description1.place(x=1080, y=510)
        self.label_Dungeon_description2.place(x=1080, y=530)

        # Rules
        self.label_rules_title = Label(self.root, text="Rules:", font=('Arial', 20, 'bold'))
        self.label_rules_title.place(x=1080, y=60)
        self.label_rule1 = Label(self.root, text="A fighter in this maze of dungeons has taken your soul")
        self.label_rule2 = Label(self.root, text="Find and defeat the fighter who has your soul to win")
        self.label_rule3 = Label(self.root, text="When fighting, you can either Punch or Heal")
        self.label_rule4 = Label(self.root, text="You only receive 1 heal per battle")
        self.label_rule5 = Label(self.root, text="After defeating a fighter, press one of the green")
        self.label_rule6 = Label(self.root, text="buttons to move to a new dungeon within the maze")

        # Placing Rules
        self.label_rule1.place(x=1080, y=100)
        self.label_rule2.place(x=1080, y=120)
        self.label_rule3.place(x=1080, y=140)
        self.label_rule4.place(x=1080, y=160)
        self.label_rule5.place(x=1080, y=180)
        self.label_rule6.place(x=1080, y=200)

        # Loop
        self.root.mainloop()

    def attack_button_pressed(self):
        global player, bad_guy_to_fight

        # player attack
        attack_strength = player.attack()
        bad_guy_to_fight.current_hit_points -= attack_strength

        # bad guy is alive after strike // Opponent attack
        if bad_guy_to_fight.is_alive():
            bad_guy_to_fight_attack = bad_guy_to_fight.attack()
            player.current_hit_points -= bad_guy_to_fight_attack

            # if player dies
            if not player.is_alive():
                self.attack_button.config(state=DISABLED)
                self.heal_button.config(state=DISABLED)
                self.label_current_hit_points.config(text="Current Hitpoints: 0")
                self.label_opponent_hit_points.config(
                    text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
                self.label_fight_description1.config(
                    text="Your opponent struck you with a strength of {}. YOU LOSE!".format(bad_guy_to_fight_attack))
                self.label_fight_description2.config(
                    text="To play again, application must be closed and then re-opened.")

            # if both player and opponent are still alive
            else:
                self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
                self.label_opponent_hit_points.config(
                    text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
                self.label_fight_description1.config(
                    text="You struck your opponent with a strength of {}".format(attack_strength))
                self.label_fight_description2.config(
                    text="Your opponent struck you with a strength of {}".format(bad_guy_to_fight_attack))

        # if opponent dies
        else:
            self.attack_button.config(state=DISABLED)
            self.heal_button.config(state=DISABLED)
            self.display_current_moves()
            self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
            self.label_opponent_hit_points.config(text="Current Hitpoints: 0")
            self.label_fight_description1.config(
                text="You struck your opponent with a strength of {}. Your opponent dies.".format(
                    attack_strength))

            # forgetting opponent labels
            self.label_opponent_image.place_forget()
            self.label_opponent_hit_points.place_forget()
            self.label_opponent_name.place_forget()
            self.label_opponent_description.place_forget()
            self.label_opponent_max_damage.place_forget()
            self.label_opponent_min_damage.place_forget()

            # opponent has soul
            if bad_guy_to_fight.stole_soul:
                self.label_fight_description2.config(text="You have found your Soul. YOU WIN!")
                self.reset_map()
            # opponent does not have soul
            else:
                self.label_fight_description2.config(text="Your soul isn't here. Try a different dungeon.")

    def heal_button_pressed(self):
        player.heal()
        bad_guy_to_fight_attack = bad_guy_to_fight.attack()
        player.current_hit_points -= bad_guy_to_fight_attack
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
        self.label_fight_description1.config(
            text="You chose to heal yourself and have 0 potions remaining")
        self.label_fight_description2.config(
            text="Your opponent struck you with a strength of {}".format(bad_guy_to_fight_attack))
        self.heal_button.config(state=DISABLED)

    def reset_map(self):
        self.button00.config(highlightbackground="white", state=DISABLED)
        self.button01.config(highlightbackground="white", state=DISABLED)
        self.button02.config(highlightbackground="white", state=DISABLED)
        self.button03.config(highlightbackground="white", state=DISABLED)

        # row 2
        self.button10.config(highlightbackground="white", state=DISABLED)
        self.button11.config(highlightbackground="white", state=DISABLED)
        self.button12.config(highlightbackground="white", state=DISABLED)
        self.button13.config(highlightbackground="white", state=DISABLED)

        # row 3
        self.button20.config(highlightbackground="white", state=DISABLED)
        self.button21.config(highlightbackground="white", state=DISABLED)
        self.button22.config(highlightbackground="white", state=DISABLED)
        self.button23.config(highlightbackground="white", state=DISABLED)

        # row 4
        self.button30.config(highlightbackground="white", state=DISABLED)
        self.button31.config(highlightbackground="white", state=DISABLED)
        self.button32.config(highlightbackground="white", state=DISABLED)
        self.button33.config(highlightbackground="white", state=DISABLED)

    def display_current_moves(self):
        global current_row, current_column, maze_button_list, current_location
        self.reset_map()

        if bad_guy_to_fight.is_alive():
            maze_button_list[current_row][current_column].config(highlightbackground="black")
        else:

            # column 1
            if current_row == 0 and current_column == 0:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
            elif current_row == 1 and current_column == 0:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
            elif current_row == 2 and current_column == 0:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
            elif current_row == 3 and current_column == 0:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)

            # col 2
            elif current_row == 0 and current_column == 1:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
            elif current_row == 1 and current_column == 1:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 2 and current_column == 1:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 3 and current_column == 1:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)

            # col 3
            elif current_row == 0 and current_column == 2:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
            elif current_row == 1 and current_column == 2:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 2 and current_column == 2:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 3 and current_column == 2:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row][current_column + 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)

            # col 4
            elif current_row == 0 and current_column == 3:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 1 and current_column == 3:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 2 and current_column == 3:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row + 1][current_column].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)
            elif current_row == 3 and current_column == 3:
                maze_button_list[current_row][current_column].config(highlightbackground="black")
                maze_button_list[current_row][current_column - 1].config(highlightbackground="green", state=NORMAL)
                maze_button_list[current_row - 1][current_column].config(highlightbackground="green", state=NORMAL)

    def button00_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 0
        current_column = 0
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()

        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button01_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 0
        current_column = 1
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button02_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 0
        current_column = 2
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button03_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 0
        current_column = 3
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button10_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 1
        current_column = 0
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button11_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 1
        current_column = 1
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button12_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 1
        current_column = 2
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button13_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 1
        current_column = 3
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))
        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button20_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 2
        current_column = 0
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description
        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button21_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 2
        current_column = 1
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button22_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 2
        current_column = 2
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button23_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 2
        current_column = 3
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button30_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 3
        current_column = 0
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description
        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button31_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 3
        current_column = 1
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button32_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 3
        current_column = 2
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")

    def button33_Pressed(self):
        global current_row, current_column, bad_guy_to_fight, dungeon_name, dungeon_description
        current_row = 3
        current_column = 3
        player.current_hit_points = player.max_hit_points
        bad_guy_to_fight = dungeon_maze_multi_dimensional_list[current_row][current_column].fighter
        dungeon_name = dungeon_maze_multi_dimensional_list[current_row][current_column].name
        dungeon_description = dungeon_maze_multi_dimensional_list[current_row][current_column].description

        self.display_current_moves()
        self.label_Dungeon_name2.config(text=dungeon_name)
        self.label_Dungeon_description2.config(text=dungeon_description)
        self.label_current_hit_points.config(text="Current Hitpoints: {}".format(player.current_hit_points))

        if bad_guy_to_fight.is_alive():
            self.opponent_image.config(file=bad_guy_to_fight.image)
            self.label_opponent_image.place(x=700, y=300)
            self.label_opponent_name.config(text="Opponent Name: {}".format(bad_guy_to_fight.name))
            self.label_opponent_name.place(x=700, y=190)
            self.label_opponent_description.config(text="Opponent Description: {}".format(bad_guy_to_fight.description))
            self.label_opponent_description.place(x=700, y=210)
            self.label_opponent_hit_points.config(
                text="Current Hitpoints: {}".format(bad_guy_to_fight.current_hit_points))
            self.label_opponent_hit_points.place(x=700, y=570)
            self.label_opponent_min_damage.config(text="Min Damage: {}".format(bad_guy_to_fight.min_damage))
            self.label_opponent_min_damage.place(x=700, y=230)
            self.label_opponent_max_damage.config(text="Max Damage: {}".format(bad_guy_to_fight.max_damage))
            self.label_opponent_max_damage.place(x=700, y=250)
            self.label_fight_description1.config(text="Click either the Attack or Heal button")
            self.label_fight_description2.config(text="")
            self.attack_button.config(state=NORMAL)
            self.heal_button.config(state=NORMAL)
        else:
            self.label_fight_description1.config(text="You have already defeated this fighter.")
            self.label_fight_description2.config(text="Please choose a different dungeon")


initialize_maze_and_start_game()
app = FindMySoul()
