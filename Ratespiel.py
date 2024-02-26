# Helferlein: Luggas 🐔

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
playCounter = 0
maxTries: int = 3


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

        self.memoryLabel.configure(text="Memo:\n")

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

        self.guessesCounterLabel.configure(text=str(len(self.guessesList)))
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

    def __checkProgressBar(self) -> bool:
        return self.progressBar.get() == 1

    def __check(self) -> None:
        global maxTries

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

        guessesAsString: str = "\n".join(map(str, self.guessesList))
        self.memoryLabel.configure(text=f"Memo:\n{guessesAsString}")

        self.guessesCounterLabel.configure(text=str(len(self.guessesList)))
        self.progressBar.set(len(self.guessesList) / (maxTries))

        if self.__checkProgressBar() == True:
            self.winningLabel.configure(text="You lost!")
            # player1Action.deactivate()
            # player2Action.deactivate()

        PlayerActionDisplayer.switchBetweenPlayers()

    @staticmethod
    def switchBetweenPlayers():
        global playCounter
        global player1Action
        global player2Action
        Progress = int(player1Action.progressBar.get())
        Progress02 = int(player2Action.progressBar.get())
        if (Progress < 1) or (Progress02 < 1):
            if (playCounter % 2) == 0:
                player1Action.activate()
                player2Action.deactivate()
            else:
                player1Action.deactivate()
                player2Action.activate()
        else:
            player1Action.deactivate()
            player2Action.deactivate()
        playCounter += 1


# FUNC: all stuff what should do before start
def start():
    global player1Action
    global player2Action

    player1Action.progressBar.set(0)
    player2Action.progressBar.set(0)
    PlayerActionDisplayer.switchBetweenPlayers()


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

memoLabel = ctk.CTkLabel(master=root)
memoLabel.grid(row=1, column=0, pady=5)

memoLabel2 = ctk.CTkLabel(master=root)
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
