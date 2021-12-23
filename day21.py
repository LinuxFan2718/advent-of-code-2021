import math
winning_score = 21
position = [7, 6]
score = [0, 0]
game = {
  "position": position,
  "score": score,
  "player": 0,
  "universes": 1
}
wins = [0 ,0]
games = [game]
rolls = {
  3: 1, 
  4: 3,
  5: 6,
  6: 7,
  7: 6, 
  8: 3, 
  9: 1
}

while len(games) > 0:
  print(f"wins {sum(wins)} games {len(games)}")
  new_games = []
  for game in games:
    for roll in rolls:
      new_game = {
        "position": game["position"][:],
        "score": game["score"][:],
        "player": game["player"],
        "universes": game["universes"]
      }
      player = new_game["player"]
      num_occurances = rolls[roll]
      current_position = new_game["position"][player]
      current_position += roll
      if current_position > 10:
        current_position -= 10
      
      new_game["position"][player] = current_position
      new_game["score"][player] += current_position
      new_game["player"] = (player + 1) % 2
      new_game["universes"] *= num_occurances

      if new_game["score"][player] >= winning_score:
        wins[player] += new_game["universes"]
      else:
        new_games.append(new_game)
  games = new_games
print(wins)