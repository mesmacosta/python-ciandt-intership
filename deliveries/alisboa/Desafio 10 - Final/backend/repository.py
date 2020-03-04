import yaml

__all__ = ['get_game', 'save_game', 'new_game']

def _load():
    with open('data.yaml', 'r') as file:
        save = yaml.safe_load(file)
        if not save['games']:
            save['games'] = {}
    return save


def _save(data):
    if data:
        with open('data.yaml', 'w') as file:
            return yaml.safe_dump(data, file)


def get_game(_id):
    data = _load()
    return data['games'].get(_id, {})


def save_game(_id, game):
    data = _load()
    data['games'][_id] = game
    _save(data)
    return game


def delete_game(_id):
    data = _load()
    del data['games'][_id]
    _save(data)


def new_game(new_game):
    data = _load()  
    data['games'].update(new_game)
    _save(data)
    return new_game
