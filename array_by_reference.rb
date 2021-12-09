def mutate(players)
  new_players = players
  new_players.append("daniel")
  players.replace(new_players)
  return
end

players = ['Lawrence', 'Dennis']
res = mutate(players)
puts("players = #{players} res = #{res}")