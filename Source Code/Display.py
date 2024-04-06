import tkinter
import customtkinter
import pygame
import GameFunc
import time

from threading import Thread
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


# Sets up root window
root = Tk()
root.geometry("1280x720")
root.resizable(False, False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# Function to move pages
def move_page(page):
    page()


def sound(sound_name):
    # Finds sound from sounds folder based on name provided
    my_sound = pygame.mixer.Sound("Sounds/" + sound_name + ".wav")

    # Retrieves effect volume from GameFunc and sets it on scale from 0 to 1
    my_sound.set_volume(float(GameFunc.effect_volume) / 100)

    my_sound.play()


def game_music(song):
    # Finds song from sounds folder based on name provided
    pygame.mixer.music.load("Sounds/" + song)

    # Retrieves music volume from GameFunc and sets it on scale from 0 to 1
    pygame.mixer.music.set_volume(float(GameFunc.music_volume) / 100)

    pygame.mixer.music.play()


def home_page():
    home_frame = Frame(root, padx=0, pady=0)
    home_frame.grid(row=0, column=0, sticky=N + S + E + W)

    # Makes grid sizes equal
    for i in range(4):
        home_frame.rowconfigure(i, weight=1)
    home_frame.columnconfigure(0, weight=1)

    # Goes to level select page
    start_button = customtkinter.CTkButton(home_frame, text="Start",
                                           command=lambda: [move_page(level_select), sound("move")])
    start_button.grid(row=0, column=0, sticky=N + S + E + W)

    # Goes to options page
    option_button = customtkinter.CTkButton(home_frame, text="Options",
                                            command=lambda: [move_page(option_page), sound("move")])
    option_button.grid(row=1, column=0, sticky=N + S + E + W)

    # Goes to score select page
    scores_button = customtkinter.CTkButton(home_frame, text="Scores",
                                            command=lambda: [move_page(score_select), sound("move")])
    scores_button.grid(row=2, column=0, sticky=N + S + E + W)

    # Destroys window
    exit_button = customtkinter.CTkButton(home_frame, text="Exit", command=root.destroy)
    exit_button.grid(row=3, column=0, sticky=N + S + E + W)

    # If music isn't being played, play menu music
    if not pygame.mixer.music.get_busy():
        game_music("MenuMusic.mp3")


def level_select():
    level_select_frame = Frame(root, padx=0, pady=0)
    level_select_frame.grid(row=0, column=0, sticky=N + S + E + W)

    # Makes grid sizes equal
    for i in range(4):
        level_select_frame.rowconfigure(i, weight=1)
    level_select_frame.columnconfigure(0, weight=1)

    # All level buttons change level number variable using command in GameFunc and then moves to game page
    level1_button = customtkinter.CTkButton(level_select_frame, text="Level 1",
                                            command=lambda: [GameFunc.change_level_num(1), move_page(game_page),
                                                             sound("move")])
    level1_button.grid(row=0, column=0, sticky=N + S + E + W)

    level2_button = customtkinter.CTkButton(level_select_frame, text="Level 2",
                                            command=lambda: [GameFunc.change_level_num(2), move_page(game_page),
                                                             sound("move")])
    level2_button.grid(row=1, column=0, sticky=N + S + E + W)

    level3_button = customtkinter.CTkButton(level_select_frame, text="Level 3",
                                            command=lambda: [GameFunc.change_level_num(3), move_page(game_page),
                                                             sound("move")])
    level3_button.grid(row=2, column=0, sticky=N + S + E + W)

    # Goes to home_page
    back_button = customtkinter.CTkButton(level_select_frame, text="Back",
                                          command=lambda: [move_page(home_page), sound("move")])
    back_button.grid(row=3, column=0, sticky=N + S + E + W)


def score_select():
    def score_screen():
        score_frame = Frame(root, padx=0, pady=0)
        score_frame.grid(row=0, column=0, sticky=N + S + E + W)

        # Makes grid size for score text larger than grid size for back button
        score_frame.rowconfigure(0, weight=2)
        score_frame.rowconfigure(1, weight=1)
        score_frame.columnconfigure(0, weight=1)

        # Holds formatted text for score display
        score_text = ""
        place = ""
        score = ""

        # Goes through lines in data folder based on the level number set beforehand
        for line in open("Data/Data" + str(GameFunc.level_number) + ".txt", "r").readlines():
            place, score = line.split(":", 1)

            # If the score is empty, format it normally
            if score == " NO SCORE\n" or score == " NO SCORE":
                score_text = score_text + "{: <9}".format(place) + "{: >8}".format(score)
            # If the score is not empty convert the text to a number, round the number, turn it back to a string,
            # then format it.
            else:
                score_text = (score_text + "{: <9}".format(place) +
                              "{: >8}".format(str(round(float(score), 1))) + "\n")

        # Display scores using font with fixed size
        win_text = Label(score_frame, text="PLACE        SCORE\n" + score_text, font='TkFixedFont')
        win_text.grid(row=0, column=0, sticky=N + S + E + W)

        # Goes back to score select instead of home page
        win_button = Button(score_frame, text="Back", command=lambda: move_page(score_select))
        win_button.grid(row=1, column=0, sticky=N + S + E + W)

    score_select_frame = Frame(root, padx=0, pady=0)
    score_select_frame.grid(row=0, column=0, sticky=N + S + E + W)

    # Makes grid sizes equal
    for i in range(4):
        score_select_frame.rowconfigure(i, weight=1)
    score_select_frame.columnconfigure(0, weight=1)

    # All level buttons change level number variable using command in GameFunc and then moves to score screen above
    level1_button = customtkinter.CTkButton(score_select_frame, text="Level 1",
                                            command=lambda: [GameFunc.change_level_num(1), move_page(score_screen),
                                                             sound("move")])
    level1_button.grid(row=0, column=0, sticky=N + S + E + W)

    level2_button = customtkinter.CTkButton(score_select_frame, text="Level 2",
                                            command=lambda: [GameFunc.change_level_num(2), move_page(score_screen),
                                                             sound("move")])
    level2_button.grid(row=1, column=0, sticky=N + S + E + W)

    level3_button = customtkinter.CTkButton(score_select_frame, text="Level 3",
                                            command=lambda: [GameFunc.change_level_num(3), move_page(score_screen),
                                                             sound("move")])
    level3_button.grid(row=2, column=0, sticky=N + S + E + W)

    # Moves back to home page
    back_button = customtkinter.CTkButton(score_select_frame, text="Back",
                                          command=lambda: [move_page(home_page), sound("move")])
    back_button.grid(row=3, column=0, sticky=N + S + E + W)


def option_page():
    def reset_data():
        # Create boolean to store result of Yes or No message box
        ru_sure = messagebox.askyesno(title="Delete all data?",
                                      message="Are you sure?\nThis will delete all time data.")
        if ru_sure:
            # Go through each data document (1, 2, and 3) then replace their lines with the empty example data document
            for x in range(1, 4):
                with open("Data/DataExample.txt", "r") as example, open("Data/Data" + str(x) + ".txt", "w") as data:
                    for line in example:
                        data.write(line)

    def resolution_sel(*args):
        # Makes window resizable, sets it to the resolution you clicked, then makes window non-resizable
        root.resizable(True, True)
        root.geometry(clicked.get())
        root.resizable(False, False)

    def update_music_value(value):
        # Sets volume in GameFunc to received value, then sets music currently playing to that volume
        GameFunc.music_volume = value
        pygame.mixer.music.set_volume(float(GameFunc.music_volume) / 100)

    def update_effect_value(value):
        # Sets effect in GameFunc to received value
        GameFunc.effect_volume = value

    option_frame = Frame(root, padx=50, pady=50)
    option_frame.grid(row=0, column=0, sticky=N + S + E + W)

    # Makes grid sizes equal
    for i in range(1, 5):
        option_frame.rowconfigure(i, weight=1)
    for i in range(2):
        option_frame.columnconfigure(i, weight=1)

    option_label = tkinter.Label(option_frame, text="OPTIONS MENU")
    option_label.grid(row=0, column=0)

    res_label = Label(option_frame, text="Resolution")
    res_label.grid(row=1, column=0, sticky=N + S + E + W)

    resolutions = ["1280x720", "1366x768", "1920x1080", "2560x1440"]

    # Stores value of selected resolution and change based on current resolution
    clicked = StringVar(master=option_frame)
    clicked.set(str(root.winfo_width()) + "x" + str(root.winfo_height()))
    clicked.trace("w", resolution_sel)

    # Makes drop down of resolutions
    res_drop = OptionMenu(option_frame, clicked, *resolutions)
    res_drop.grid(row=1, column=1, sticky=E + W)

    music_label = Label(option_frame, text="Music Volume")
    music_label.grid(row=2, column=0, sticky=N + S + E + W)

    effect_label = Label(option_frame, text="Effect Volume")
    effect_label.grid(row=3, column=0, sticky=N + S + E + W)

    # Scale for music that calls function whenever its changed
    music_scale = Scale(option_frame, command=lambda value: update_music_value(value),
                        orient="horizontal")
    music_scale.grid(row=2, column=1, sticky=N + S + E + W)

    # Scale for effect that calls function whenever its changed
    effect_scale = Scale(option_frame, command=lambda value: update_effect_value(value),
                         orient="horizontal")
    effect_scale.grid(row=3, column=1, sticky=N + S + E + W)

    # Sets value of scale based on current volume
    music_scale.set(GameFunc.music_volume)
    effect_scale.set(GameFunc.effect_volume)

    # Button to call reset data function
    reset_data_button = Button(option_frame, text="Reset Data", command=lambda: reset_data())
    reset_data_button.grid(row=4, column=0)

    # Moves back to home page
    back_button = Button(option_frame, text="Back", command=lambda: [move_page(home_page), sound("move")])
    back_button.grid(row=5, column=0)


def game_page():
    # Unbinds keys, clears displayed images, and uses reset function in GameFunc
    def clear(event):
        global function_running, resize_list, image_placed
        function_running = False
        root.unbind("<Left>")
        root.unbind("<Right>")
        root.unbind("<Up>")
        root.unbind("<Down>")
        root.unbind("<Return>")
        resize_list.clear()
        image_placed.clear()

        # If the game is not complete continue the game loop, otherwise, just reset the level
        if not GameFunc.check_complete():
            GameFunc.reset(GameFunc.level_number)
            root.update()
            sound("reset")
            game_loop()

        GameFunc.reset(GameFunc.level_number)

    def leave_game():
        # Unbinds reset button for puzzle since the player is leaving the game screen
        root.unbind("<Delete>")
        clear(None)
        pygame.mixer.music.unload()
        move_page(home_page)

    def timer(state):
        # Changes value of timer label to current time elapsed, then sets itself to be called in 0.1 seconds
        def timer_label_counter():
            global time_job
            time_label.config(text=str(round(time.time() - float(timer_time), 1)))
            time_job = root.after(100, timer_label_counter)

        global timer_time, time_job

        # Store start time and put it in timer_time, create label for the time, then start thread for updating the label
        if state:
            timer_time = time.time()

            time_label = Label(game_canvas, text=timer_time, width=8, height=2)
            time_label.place(x=20, y=20, anchor='nw')

            timer_thread = Thread(target=timer_label_counter)
            timer_thread.start()

        # Stops timer and updates data folder
        elif not state:
            # If the timer label is going to be updated, cancel that task
            if time_job is not None:
                root.after_cancel(time_job)

            # Set final time
            timer_time = str(time.time() - float(timer_time))

            # open data file, store its data in a new file, then start reading from the beginning of the file again
            file = open("Data/Data" + str(GameFunc.level_number) + ".txt", "r+")
            new_file = file.read()
            file.seek(0)

            # Go through each line in the file and update it in the new file
            for line in file.readlines():
                place, score = line.split(":", 1)

                try:
                    # If there is no score, put the currently held time in that location
                    if score == " NO SCORE\n" or score == " NO SCORE":
                        new_file = new_file.replace(line, place + ": " + timer_time.strip() + "\n")
                        # Store NO SCORE into timer_time to be written into the new file
                        timer_time = score
                    # If there is a score, and it's faster than the current score, overwrite the old score
                    elif float(score) > float(timer_time):
                        new_file = new_file.replace(line, place + ": " + timer_time.strip() + "\n")
                        # Store the old score to be written at lower place in new file
                        timer_time = score
                except ValueError:
                    print("Something is wrong with writing to the data file")

            # Go back to the beginning of the original file and overwrite it with the new file contents
            file.seek(0)
            file.truncate(0)
            file.write(new_file)

    # Frame for displaying updated score and then allowing player to go back to home page
    def win_screen():
        # Stops timer and update data folder before continuing
        timer(False)

        win_frame = Frame(root, padx=0, pady=0)
        win_frame.grid(row=0, column=0, sticky=N + S + E + W)

        win_frame.rowconfigure(0, weight=2)
        win_frame.rowconfigure(1, weight=1)
        win_frame.columnconfigure(0, weight=1)

        score_text = ""
        place = ""
        score = ""

        # Goes through lines in data folder based on the current level
        for line in open("Data/Data" + str(GameFunc.level_number) + ".txt", "r").readlines():
            place, score = line.split(":", 1)
            # If the score is empty, format it normally
            if score == " NO SCORE\n" or score == " NO SCORE":
                score_text = score_text + "{: <9}".format(place) + "{: >8}".format(score)
            # If the score is not empty convert the text to a number, round the number, turn it back to a string,
            # then format it.
            else:
                score_text = (score_text + "{: <9}".format(place) +
                              "{: >8}".format(str(round(float(score), 1))) + "\n")

        # Display scores using font with fixed size font
        win_text = Label(win_frame, text="PLACE        SCORE\n" + score_text, font='TkFixedFont')
        win_text.grid(row=0, column=0, sticky=N + S + E + W)

        # Goes back to the home page
        win_button = Button(win_frame, text="Go to Menu", command=lambda: move_page(home_page))
        win_button.grid(row=1, column=0, sticky=N + S + E + W)

    # Used for displaying item when placing as well as handling its placement point
    def display_placement():

        def down(event):
            # Move image and placement point only if the item won't extend beyond the borders of the case array
            if (int(GameFunc.placement_point / 100) < (len(GameFunc.case_arr[0]) - 1)
                    - (len(GameFunc.item_list_actual[GameFunc.item_point].arr) - 1)):
                GameFunc.placement_point = GameFunc.placement_point + 100
                x = 0
                y = (64 / 1080) * game_canvas.winfo_height()
                game_canvas.move(image_placed[len(image_placed) - 1], x, y)
                sound("move")

        def up(event):
            # Move image and placement point only if the item won't extend beyond the borders of the case array
            if int(GameFunc.placement_point / 100) > 0:
                GameFunc.placement_point = GameFunc.placement_point - 100
                x = 0
                y = -(64 / 1080) * game_canvas.winfo_height()
                game_canvas.move(image_placed[len(image_placed) - 1], x, y)
                sound("move")

        def left(event):
            # Move image and placement point only if the item won't extend beyond the borders of the case array
            if (GameFunc.placement_point % 100) > 0:
                GameFunc.placement_point = GameFunc.placement_point - 1
                x = -(64 / 851) * (0.78796296296 * game_canvas.winfo_height())
                y = 0
                game_canvas.move(image_placed[len(image_placed) - 1], x, y)
                sound("move")

        def right(event):
            # Move image and placement point only if the item won't extend beyond the borders of the case array
            if (GameFunc.placement_point % 100) < ((len(GameFunc.case_arr) - 1) -
                                                   (len(GameFunc.item_list_actual[GameFunc.item_point].arr[0]) - 1)):
                GameFunc.placement_point = GameFunc.placement_point + 1
                x = (64 / 851) * (0.78796296296 * game_canvas.winfo_height())
                y = 0
                game_canvas.move(image_placed[len(image_placed) - 1], x, y)
                sound("move")

        def enter(event):
            global function_running
            function_running = False

            # Place item using GameFunc and reset placement point to 0
            GameFunc.fit_item(GameFunc.item_list_actual[GameFunc.item_point])
            GameFunc.placement_point = 0

            # Unbind keys for placing item
            root.unbind("<Left>")
            root.unbind("<Right>")
            root.unbind("<Up>")
            root.unbind("<Down>")
            root.unbind("<Return>")
            root.unbind("<BackSpace>")
            sound("pick")

            # Compare current item list length with recorded value to determine if the item was successfully placed
            if item_list_length == len(GameFunc.item_list_actual):
                # If no items were placed, remove the displayed images from the lists
                resize_list.pop()
                image_placed.pop()

            # Restart the game loop
            game_loop()

        def backspace(event):
            global function_running
            function_running = False
            GameFunc.placement_point = 0

            # Unbind keys for placing item
            root.unbind("<Left>")
            root.unbind("<Right>")
            root.unbind("<Up>")
            root.unbind("<Down>")
            root.unbind("<Return>")
            root.unbind("<BackSpace>")
            sound("reset")

            # Remove displayed item from lists
            resize_list.pop()
            image_placed.pop()

            # Restart the game loop
            game_loop()

        # Set resize_list and image_placed list to global so python doesn't automatically remove images
        global resize_list, image_placed

        # Get size of current item list
        item_list_length = len(GameFunc.item_list_actual)

        # Resize image for the current item to be correct size for resolution
        resize_list.append(
            ImageTk.PhotoImage(temp_image.resize((int(temp_image.width * (root.winfo_width() / 1980)),
                                                  int(temp_image.height * (root.winfo_height() / 1110))))))

        # Place resized image in correct location
        image_placed.append(game_canvas.create_image(int(game_canvas.winfo_width() / 6 +
                                                         ((0.78796296296 * game_canvas.winfo_height()) * 0.12573443008))
                                                     , int(game_canvas.winfo_height() * 0.35833333333),
                                                     image=resize_list[len(resize_list) - 1], anchor="nw"))

        # Bind keys to functions
        root.bind("<BackSpace>", backspace)
        root.bind("<Left>", left)
        root.bind("<Right>", right)
        root.bind("<Up>", up)
        root.bind("<Down>", down)
        root.bind("<Return>", enter)

    # Used for selecting which item to place
    def item_display():
        # Make these variables global so Python doesn't stop them from being displayed
        global temp_image, resize, item_image

        def item_change():
            # Make these variables global so Python doesn't stop them from being displayed
            global temp_image, resize, item_image

            # Delete image if it is set as 'deletable' so that only one item is displayed at a time
            item_canvas.delete("deletable&&token")

            # Get the name of the current item on the list, then open that image
            c_item = GameFunc.item_list_actual[GameFunc.item_point].name
            temp_image = Image.open("Images/" + c_item + ".png")

            # Resize the image and then create the image on the display with the token 'deletable'
            resize = ImageTk.PhotoImage(temp_image.resize((int(temp_image.width * (root.winfo_width() / 1980)),
                                                           int(temp_image.height * (root.winfo_height() / 1110)))))
            item_image = item_canvas.create_image(item_canvas.winfo_width() / 2, item_canvas.winfo_height() / 2,
                                                  image=resize, tags="deletable", anchor="center")

        def left(event):
            # Go to end of list if you want to go back an item, but are at the first item in the list
            if GameFunc.item_point == 0:
                GameFunc.item_point = len(GameFunc.item_list_actual) - 1
            # Otherwise go back 1 item on the list
            else:
                GameFunc.item_point -= 1

            # Display the new item
            item_change()
            sound("move")

        def right(event):
            # Go to front of list if you want to go forward an item, but are at the last item in the list
            if GameFunc.item_point == len(GameFunc.item_list_actual) - 1:
                GameFunc.item_point = 0
            # Otherwise go forward 1 item on the list
            else:
                GameFunc.item_point += 1

            # Display the new item
            item_change()
            sound("move")

        def leave(event):
            # Unbind keys except Delete which should still be able to be used while using display_placement
            root.unbind("<Left>")
            root.unbind("<Right>")
            root.unbind("<Return>")

            # Move to display_placement, having selected the current item
            sound("pick")
            display_placement()

        # Start at beginning of the list and display the item
        GameFunc.item_point = 0
        item_change()

        root.bind("<Left>", left)
        root.bind("<Right>", right)
        root.bind("<Return>", leave)
        root.bind("<Delete>", clear)

    def game_loop():
        global function_running

        # If the item list has items remaining and the game_loop function isn't already running start the item_display
        if len(GameFunc.item_list_actual) != 0:
            if not function_running and len(GameFunc.item_list_actual) > 0:
                function_running = True
                item_display()
        # If there are no items left, check if the game is complete then clear everything and go to the win screen
        elif GameFunc.check_complete():
            # Unbind Delete, as the game has ended
            root.unbind("<Delete>")
            clear(None)
            pygame.mixer.music.unload()
            move_page(win_screen)
        else:
            print("Some error has occurred and the list is empty, but the case is not complete.")

    # START OF GAME CODE HERE

    # Set these images to global so Python doesn't destroy them in a clean-up routine
    global case1, background_1, background_items, function_running, image_placed, resize_list

    # Unload menu music
    pygame.mixer.music.unload()

    game_frame = LabelFrame(root, text="Level 1", padx=0, pady=0)
    game_frame.grid(row=0, column=0, sticky=N + S + E + W)

    # Set grid size for the puzzle to be larger than that for the item selection
    game_frame.columnconfigure(1, weight=2)
    game_frame.rowconfigure(0, weight=1)

    # Canvas for picking item
    item_canvas = Canvas(game_frame)
    item_canvas.grid(row=0, column=0, sticky=N + S + E + W, )

    # Canvas for placing item
    game_canvas = Canvas(game_frame)
    game_canvas.grid(row=0, column=1, sticky=N + S + E + W)

    # Update idle tasks so Python displays everything it should
    root.update_idletasks()

    # Resize and place background on right screen
    background_1 = ImageTk.PhotoImage(Image.open("Images/Background1.png").resize(
        (game_canvas.winfo_width(), game_canvas.winfo_height())))
    game_canvas.create_image(0, 0, image=background_1, anchor="nw")

    # Resize and place background on left screen
    background_items = ImageTk.PhotoImage(Image.open("Images/BackgroundItems.png").resize(
        (item_canvas.winfo_width(), item_canvas.winfo_height())))
    item_canvas.create_image(0, 0, image=background_items, anchor="nw")

    # Resize and place case image with grid
    case1 = ImageTk.PhotoImage(Image.open("Images/AttacheCase1.png").resize(
        (int(0.78796296296 * game_canvas.winfo_height()), game_canvas.winfo_height())))
    game_canvas.create_image(game_canvas.winfo_width() / 6, 0, image=case1, anchor="nw")

    # Create small back button for leaving game without completing it
    back_button = Button(item_canvas, text="Back", width=8, height=2, command=leave_game)
    back_button.place(x=2, y=2, anchor='nw')

    # Create a resize list to hold resized images
    resize_list = []
    # Create image placed list to store images that will be moved
    image_placed = []

    # Create boolean to tell if game_loop is running
    function_running = False

    # Start music that plays for the game
    game_music("backgroundMusic.wav")

    # Start the timer
    timer(True)

    # Start the game loop
    game_loop()

# Main() CODE STARTS HERE

# Initialize the sound mixer
pygame.mixer.init()

# Start at the home page
home_page()

# Main loop so tkinter works
root.mainloop()
