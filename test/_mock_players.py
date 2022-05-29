from player import Player
names = [
    "john",
    "paul",
    "rachel",
    "han",
    "zeckler",
    "lucia",
    "balutria",
    "rossin",
    "martha",
    "philip",
    "tyler"
]

mock_players=[]
for i,x in enumerate(names):
    mock_players.append(Player(x))
    if i%2==0:
        mock_players[len(mock_players)-1].health=50
        mock_players[len(mock_players)-1].dreams=50
        mock_players[len(mock_players)-1].happy=50
        mock_players[len(mock_players)-1].confidence=50
        mock_players[len(mock_players)-1].hate=50
        mock_players[len(mock_players)-1].curiosity=50
        mock_players[len(mock_players)-1].respawn=50
        mock_players[len(mock_players)-1].delerium=50
        mock_players[len(mock_players)-1].sad=50
        mock_players[len(mock_players)-1].loathing=50
    if i%3==0:
        mock_players[len(mock_players)-1].fear=50
        mock_players[len(mock_players)-1].love=50
        mock_players[len(mock_players)-1].speed=50
        mock_players[len(mock_players)-1].risk=50
        mock_players[len(mock_players)-1].respawn=50
        mock_players[len(mock_players)-1].vision=50