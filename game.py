#Sanika Iyer, Chitrini Anand
#SNAPSHOT 1:
    #finished all of wordleWord
    #finished all but one method of wordlePlayer (displayStats)
    #began working on game.py (initialized word bank and settings, got player name)
 	
 #SNAPSHOT 2:
    #finished displayStats in wordlePlayer
    #set all greens in alphabet and guess (markGuess)
    # #started working on yellows (not corner cases, just the basics)

from itertools import count
import string
from player import Player
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer

#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    # TO DO
    for idx in range(len(word)):
        if guess.charAt(idx) == word[idx]: #setting guess green
            guess.setCorrect(idx)
        elif guess.charAt(idx) in word and guess.charAt(idx) != word[idx]: #very basic guess yellow//needs fix!!
            guess.setMisplaced(idx)
        elif guess.charAt(idx) not in word: #guess setUnused
            guess.setUnused(idx)
    for idx in range(len(word)):
        if guess.charAt(idx) == word[idx]: #setting alphabet green
            ch = guess.charAt(idx)
            pos = alphabet.find(ch)
            alphabet.setCorrect(pos)
        elif guess.charAt(idx) in word and guess.charAt(idx) != word[idx]: #very basic alphabet yellow//needs fix!!
            ch = guess.charAt(idx)
            pos = alphabet.find(ch)
            alphabet.setMisplaced(pos)
        elif guess.charAt(idx) not in word: #alphabet setUnused
            ch = guess.charAt(idx)
            pos = alphabet.find(ch)
            alphabet.setUnused(pos)
guess = WordleWord("poppy")
#guess2 = WordleWord("aspen")
alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
markGuess("apple", guess, alphabet)
#markGuess("awake", guess2, alphabet)     
print(guess)
#print(guess2)
print(alphabet)

#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======
def playRound(players, words, all_words, settings):
    wordle = words.getRandom()
    tries = 0
    while tries < 6:
        guess = input("What is your guess?")
        while all_words.contains(guess) == False:
            guess = input("Your guess was invalid. Please enter another guess.")
        tries += 1
        wordle = WordleWord(wordle)
        guess = WordleWord(guess)
        alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
        markGuess(wordle, guess, alphabet)
        print(guess)
        print(alphabet)
        if guess == wordle:
            print("You have guessed the word!")
            players.updateStats(True, tries)
            break
    players.updateStats(False, tries)
    



def playWordle():
    print("Let's play the game of Wordle!")

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    common_words = WordBank("common5letter.txt")

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # make the player
    player = input("Enter your name: ")
    # start playing rounds of Wordle
    print("Welcome " + player + "!")
    print("\nOK, let's play Wordle!!\n")
    p = Player(player)
    playRound(p, common_words, all_words, settings)
    # end game by displaying player stats
    WordlePlayer.displayStats()

    # end game by displaying player stats
    #print(WordlePlayer.displayStats())

def main():
    playWordle()
    #pass

if __name__ == "__main__":
    main()