import yaml
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)

class Game(Base):
    __tablename__ = 'games'
    id = Column(String, primary_key=True)
    date = Column(String)
    find = Column(String)
    result = Column(String)
    time_sec = Column(Float)
    tries = Column(Integer)
    word = Column(String)




__all__ = ['get_game', 'save_game', 'new_game']


def get_game(_id):
    Session = sessionmaker(engine)
    session = Session()
    current_game_query = session.query(Game).filter(Game.id == _id)
    current_game = current_game_query.one()
    return current_game, session


def save_game(_id, game, session):
    session.add(game)
    session.commit()
    return game


def delete_game(_id):
    Session = sessionmaker(engine)
    session = Session()
    session.query(Game).filter(Game.id == _id).delete()
    session.commit()


def new_game(new_game):
    Session = sessionmaker(engine)
    session = Session()
    new_game_create = Game(id=str(new_game['id']), date=new_game['date'], word=new_game['word'],
                           find=new_game['find'], tries=new_game['tries'], result=new_game['result'],
                           time_sec=new_game['time_sec'],
                           )

    session.add(new_game_create)
    # Base.metadata.create_all(engine)
    session.commit()

    return new_game


