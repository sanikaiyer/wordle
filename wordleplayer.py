#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from sys import maxsize
from player import Player

# TODO - make WordlePlayer

class WordlePlayer(Player):
	def __init__(self, name, maxTry):
		super().__init__(name)
		self.maxTry = maxTry # max number of guesses
		self.wins = 0 # current number of wins/current streak
		self.numGames =  0 # number of games,
		self.maxS = -1 # number of wins in a row (maximum) # determine max win streak
		self.totalWins = 0 # total number of wins regardless of the streak 
		self.distribution = [0 for i in range(self.maxTry + 1)] #[0 for i in range(maxTry + 1)] # !!!!!!! how to loop through a list... like with the range being range(maxTry + 1)
		#i could do  ????? not sure
		# or we could do 
		#for i in range(maxTry + 1)
	
	def updateStats(self, won, tries):
		if won == True:
			self.wins += 1
			self.totalWins += 1
			if self.wins >= 2 and self.wins >= self.maxS:
				self.maxS += 1
		    #if you did not win last time, max streak remains
			self.distribution[tries] += 1
		else:
			self.wins = 0
		self.numGames += 1
	def winPercentage(self):
		return (self.totalWins / self.numGames)*100
	def gamesPlayed(self):
		return self.numGames
	def currentStreak(self):
		return self.wins
	def maxStreak(self):
		return self.maxS	
	def displayStats(self):
		#print(self.wins, self.maxS)
		#numHashes = self.wins // self.maxS
		maxGuessNum = max(self.distribution)
		print("Games Played:", self.numGames)
		print("Win %: {}%".format(round(self.winPercentage(), 1)))
		print("Current Streak:", self.wins)
		print("Max Streak:", self.maxS)
		print("Guess Distribution")
		#print("#" * numHashes)
		for i in range(1, len(self.distribution)):
			print("  {}: #".format(i), "end = ")
			count = self.distribution[i]
			#for in range(count):
			numHashes = round((count / maxGuessNum) * 20)
				#print(numHashes)
			print("#" * numHashes, end = "")
			print("", count)
			#print("1: #" + ("#" * numHashes))
			#print("2: #" + ("#" * (numHashes)))
			#print("3: #" + ("#" * numHashes))
			#print("4: #" + ("#" * (numHashes)))
			#print("5: #" + ("#" * (numHashes)))
			#print("6: #" + ("#" * (numHashes)))