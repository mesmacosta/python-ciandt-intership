from services import start_game, gess_word, reset_game, new_id


def new():
    """Endpoint to create new game id"""
    return {'game_id': new_id()}, 200


def start(game_id: str):
    """Endpoint to create new game record"""
    return start_game(game_id)


def handle_guess(game_id: str, gess: str):
    """Endpoint handle the guess"""
    return gess_word(game_id, gess)


def reset(game_id: str):
    """Endpoint to reset"""
    return reset_game(game_id)
