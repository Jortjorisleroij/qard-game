class Player:
    def __init__(self, id: int):
        self.id = id
        self.hand = []

    def get_hand(self) -> list:
        return list(self.hand)


def get_player(players: list, player_id: int) -> Player:
    if not isinstance(players, (list, tuple)):
        raise ValueError("players must be a list or tuple of Player objects")
    if not isinstance(player_id, int):
        raise ValueError("player_id must be an int")
    if player_id < 1 or player_id > len(players):
        raise ValueError(f"player_id must be between 1 and {len(players)}")
    return players[player_id - 1]


def get_player_hand(players: list, player_id: int) -> list:
    player = get_player(players, player_id)
    return player.get_hand()
