
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points={
  key:value
  for key,value in zip(letters,points)
}
letter_to_points[" "]=0

#the following function shall calculate the points scored by a player
def score_word (word):
  point_total=0
  for letter in word:
    point_total= point_total+letter_to_points.get(letter,0)
  return point_total

brownie_points= score_word("BROWNIE")
print(brownie_points)

players_to_words={"player1":["BLUE","TENNIS","EXIT"], "wordNerd":["EARTH,EYES,MACHINE"], "Lexi Con":["ERSER", "BELLY","HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
players_to_points={}

for players, words in players_to_words.items():
  player_points=0
  for word in words:
    player_points= player_points+ score_word(word)
  players_to_points[players]=player_points

print(players_to_points)

#the following function will add new words to the list of words that belongs to a player
def play_word(player,word):
  players_to_words[player].append(word)

#the following function shall update the scoreboard whenever called.
def update_point_totals():
   for players, words in players_to_words.items():
    player_points = 0
   for word in words:
     player_points= player_points+ score_word(word)
     players_to_points[players]=player_points
