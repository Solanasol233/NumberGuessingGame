import customtkinter as ctk
import random

# configurations for the whole root and overlay
ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("green")


# root = ability to create windows and GUI
root = ctk.CTk()
# size of window
root.geometry("500x350")
root.resizable(False, False)

random.seed()
rangeG = 1000
randomNumber = random.randint(0, rangeG)
randomNumber02 = random.randint(0, rangeG)
guesses = 0
guesses02 = 0
playCounter = 0
# playChecker = False  # True => Player 1 | False => Player 2
Player = 1
tries = 3
# Memo = ["Memo:\n"]
# Memo2 = ["Memo:\n"]


class PlayerActionDisplayer:
    def __init__(
        self,
        frame: ctk.CTkFrame,
        playerNameLabel: ctk.CTkLabel,
        guessesCounterLabel: ctk.CTkLabel,
        indicatorLabel: ctk.CTkLabel,
        memoryLabel: ctk.CTkLabel,
        winningLabel: ctk.CTkLabel,
        numberEntry: ctk.CTkEntry,
        checkButton: ctk.CTkButton,
        newRandomValueButton: ctk.CTkButton,
        progressBar: ctk.CTkProgressBar,
    ) -> None:
        self.frame = frame
        self.playerNameLabel = playerNameLabel
        self.guessesCounterLabel = guessesCounterLabel
        self.indicatorLabel = indicatorLabel
        self.memoryLabel = memoryLabel
        self.numberEntry = numberEntry
        self.checkButton = checkButton
        self.newRandomValueButton = newRandomValueButton
        self.progressBar = progressBar
        self.winningLabel = winningLabel

        self.randomNumber: int = self.__generateRandomNumber()
        self.guessesList: list = []

        self.memoryLabel = "Memo:\n"

        self.newRandomValueButton.configure(command=self.__generateNewRandomValue)
        self.checkButton.configure(command=self.__check)

    def activate(self):
        self.frame.configure(fg_color="lightgreen")
        self.numberEntry.configure(state="normal")
        self.checkButton.configure(state="normal")
        self.newRandomValueButton.configure(state="normal")

    def deactivate(self):
        self.frame.configure(fg_color="red")
        self.numberEntry.configure(state="disabled")
        self.checkButton.configure(state="disabled")
        self.newRandomValueButton.configure(state="disabled")

    def __generateNewRandomValue(self):
        self.randomNumber = self.__generateRandomNumber()
        self.guessesList.clear()
        self.guessesCounterLabel.configure(text=str(self.guessesList.count()))
        self.indicatorLabel.configure(text="your Number")
        self.numberEntry.delete(-1, "end")
        self.progressBar.set(0)

    def __guessIsTooLow(self, guess: int) -> bool:
        return guess < self.randomNumber

    def __guessIsTooHigh(self, guess: int) -> bool:
        return guess > self.randomNumber

    def __guessIsCorrect(self, guess: int) -> bool:
        return guess == self.randomNumber

    def __generateRandomNumber(self) -> int:
        global rangeG
        return random.randint(0, rangeG)

    def __check(self) -> None:
        global tries

        guessInput: int = int(self.numberEntry.get())
        if self.__guessIsTooLow(guessInput):
            self.indicatorLabel.configure(text="Your number is too low!")
        elif self.__guessIsTooHigh(guessInput):
            self.indicatorLabel.configure(text="Your number is too high!")
        elif self.__guessIsCorrect(guessInput):
            self.indicatorLabel.configure(text="Your number is correct!")
        else:
            print("Something weird happened.")
            return

        self.guessesList.append(guessInput)
        self.guessesCounterLabel.configure(text=str(self.guessesList.count()))
        self.progressBar.set(self.guessesList.count() / tries)

        if self.progressBar.get() == 1:
            self.winningLabel.configure(text="You lost!")


##//FUNCTIONS\\##


# FUNC: all stuff what should do before start
def start():
    global player1Action
    global player2Action

    playCheck()
    player1Action.progressBar.set(0)
    player2Action.progressBar.set(0)

    global Player
    Player = 1


# FUNC: switch between Player 1 and 2
def playCheck():
    global Player
    global playCounter
    global player1Action
    global player2Action

    if (playCounter % 2) == 0:
        Player = 1
        player1Action.activate()
        player2Action.deactivate()
    else:
        Player = 2
        player1Action.deactivate()
        player2Action.activate()

    playCounter += 1


# FUNC: check function for Button to check if higher or lower
def mainCheck():
    if Player == 1:  # Stuff for Player 1
        try:
            global guesses  # acces to global variable
            i = entry1.get()
            if int(i) < randomNumber:
                label2.configure(text="Your number is too low!")
            elif int(i) > randomNumber:
                label2.configure(text="Your number is too high!")
            else:
                label2.configure(text="Congrats! You found the right number!")
                winLabel.configure(text="You won!")
            guesses += 1  # Versuchszähler erhöhen
            Labelguesses.configure(text=str(guesses))
        except ValueError:
            Labelguesses.configure(text="Invalid input!")
        if int(i) > rangeG:
            Labelguesses.configure(text="Invalid input!")
        elif int(i) < 0:
            Labelguesses.configure(text="Invalid input!")
        progressBar.set(guesses / tries)
        if progressBar.get() == 1:
            winLabel.configure(text="You lost!")
        Memo.append(str(i) + "\n")
        memoLabel.configure(text="".join(Memo))
    if Player == 2:  # Stuff for Player 2
        try:
            global guesses02  # access to global variable
            i02 = entry102.get()
            if int(i02) < randomNumber02:
                label202.configure(text="Your number is too low!")
            elif int(i02) > randomNumber02:
                label202.configure(text="Your number is too high!")
            else:
                label202.configure(text="Congrats! You found the right number!")
                winLabel02.configure(text="You won!")
            guesses02 += 1  # increase guesses
            Labelguesses02.configure(text=str(guesses02))
        except ValueError:
            Labelguesses02.configure(text="Invalid input!")
        if int(i02) > rangeG:
            Labelguesses02.configure(text="Invalid input!")
        elif int(i02) < 0:
            Labelguesses02.configure(text="Invalid input!")
        progressBar02.set(guesses / tries)
        if progressBar02.get() == 1:
            winLabel02.configure(text="You lost!")
        Memo2.append(str(i02) + "\n")
        memoLabel2.configure(text="".join(Memo2))
    playCheck()


# # FUNC: generate new, independence random value and reset entry1, guesses and guesses label
# def newRandom():
#     global randomNumber
#     global randomNumber02
#     global player1Action
#     random.seed()
#     randomNumber = random.randint(0, rangeG)
#     randomNumber02 = random.randint(0, rangeG)
#     global guesses
#     global guesses02
#     guesses = 0
#     guesses02 = 0
#     Labelguesses.configure(text=str(guesses))
#     Labelguesses02.configure(text=str(guesses02))
#     label2.configure(text="your number")
#     label202.configure(text="your number")
#     entry1.delete(-1, "end")
#     entry102.delete(-1, "end")
#     player1Action.progressBar.set(0)


##//GRAPHICAL USER INTERFACE (GUI) PARTS\\##

progressBar = ctk.CTkProgressBar(master=root)
progressBar.grid(row=0, column=1)

progressBar02 = ctk.CTkProgressBar(master=root)
progressBar02.grid(row=0, column=2)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# create frame, is basicly a colored box with round vertices LOL


frame = ctk.CTkFrame(master=root)
frame.grid(row=1, column=1)
frame.configure(fg_color="lightgreen")

frame2 = ctk.CTkFrame(master=root)
frame2.grid(row=1, column=2)
frame2.configure(fg_color="red")

label = ctk.CTkLabel(master=frame, text="Player 1")
label.pack(pady=12, padx=10)

label2 = ctk.CTkLabel(master=frame, text="your number")
label2.pack(pady=12, padx=10)

Labelguesses = ctk.CTkLabel(master=frame, text="")
Labelguesses.place(x=87, y=38)

Labelguesses2 = ctk.CTkLabel(master=frame, text="Your guesses:")
Labelguesses2.place(x=5, y=38)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Your number")
entry1.pack(pady=12, padx=10)

button_Check = ctk.CTkButton(master=frame, text="check!")
button_Check.pack(padx=10, pady=10)

button_NewRandom = ctk.CTkButton(master=frame, text="New Value!")
button_NewRandom.pack(padx=10, pady=10)

winLabel = ctk.CTkLabel(master=frame, text="")
winLabel.pack(pady=12, padx=10)

label02 = ctk.CTkLabel(master=frame2, text="Player 2")
label02.pack(pady=12, padx=10)

label202 = ctk.CTkLabel(master=frame2, text="your number")
label202.pack(pady=12, padx=10)

Labelguesses02 = ctk.CTkLabel(master=frame2, text="")
Labelguesses02.place(x=87, y=38)

Labelguesses202 = ctk.CTkLabel(master=frame2, text="Your guesses:")
Labelguesses202.place(x=5, y=38)

entry102 = ctk.CTkEntry(master=frame2, placeholder_text="Your number")
entry102.pack(pady=12, padx=10)

button_Check02 = ctk.CTkButton(master=frame2, text="check!")
button_Check02.pack(padx=10, pady=10)

button_NewRandom02 = ctk.CTkButton(master=frame2, text="New Value!")
button_NewRandom02.pack(padx=10, pady=10)

winLabel02 = ctk.CTkLabel(master=frame2, text="")
winLabel02.pack(pady=12, padx=10)

memoLabel = ctk.CTkLabel(master=root, text="".join(Memo))
memoLabel.grid(row=1, column=0, pady=5)

memoLabel2 = ctk.CTkLabel(master=root, text="".join(Memo2))
memoLabel2.grid(row=1, column=3)

player1Action = PlayerActionDisplayer(
    frame=frame,
    playerNameLabel=label,
    guessesCounterLabel=Labelguesses,
    indicatorLabel=label2,
    memoryLabel=memoLabel,
    numberEntry=entry1,
    checkButton=button_Check,
    newRandomValueButton=button_NewRandom,
    progressBar=progressBar,
    winningLabel=winLabel,
)

player2Action = PlayerActionDisplayer(
    frame=frame2,
    playerNameLabel=label02,
    guessesCounterLabel=Labelguesses02,
    indicatorLabel=label202,
    memoryLabel=memoLabel2,
    numberEntry=entry102,
    checkButton=button_Check02,
    newRandomValueButton=button_NewRandom02,
    progressBar=progressBar02,
    winningLabel=winLabel02,
)

start()
# repeat mainloop until window is closed
root.mainloop()
