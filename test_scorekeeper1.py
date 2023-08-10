"""
Tests of ScoreKeeper using pytest.
"""
from player import Player
from scorekeeper import ScoreKeeper


# names of some players
name1 = "First"
name2 = "Second"
name3 = "Third"
name4 = "Fourth"

def test_create_and_get_player():
    """ScoreKeeper creates new players when name has not been seen before."""
    scorekeeper = ScoreKeeper()
    scorekeeper.add_score(name1, 1)
    scorekeeper.add_score(name2, 20)
    scorekeeper.add_score(name3, 300)
    player1 = scorekeeper.get_player(name1)
    assert isinstance(player1, Player)
    assert player1 is not None
    assert player1.name == name1
    assert player1.score == 1
    # if we get the same name again, it returns same Player
    playerX = scorekeeper.get_player(name1)
    assert player1 is playerX
    # we can get other players as well
    player2 = scorekeeper.get_player(name2)
    player3 = scorekeeper.get_player(name3)
    assert isinstance(player2, Player)
    assert isinstance(player3, Player)

	# Each ScoreKeeper has its own Players (not a class attribute)
    scorekeeper2 = ScoreKeeper()
    scorekeeper2.add_score(name4, 4000)
    # scorekeeper2 does not know about players in first scorekeeper
    assert scorekeeper2.get_player(name1) is None
    assert scorekeeper2.get_player(name2) is None
    # first scorekeeper does not know 2nd scorekeeper's player
    assert scorekeeper.get_player(name4) is None
    # second scorekeeper remembers its own player
    playerX = scorekeeper2.get_player(name4)
    assert playerX is not None
    assert playerX.name == name4
    assert playerX.score == 4000


def test_len():
    """len() returns the number of players known by the ScoreKeeper."""
    scorekeeper = ScoreKeeper()
    # no players yet
    assert len(scorekeeper) == 0
    scorekeeper.add_score(name1, 10)
    assert len(scorekeeper) == 1
    # add another player
    scorekeeper.add_score(name2, 5)
    assert len(scorekeeper) == 2
    # current player, not a new player
    scorekeeper.add_score(name1, 5)
    assert len(scorekeeper) == 2


def test_accumulate_score_many_players():
    """Correctly adds scores for many players."""
    scorekeeper = ScoreKeeper()
    scorekeeper.add_score(name1, 10)
    scorekeeper.add_score(name2, 20)
    scorekeeper.add_score(name3, 30)
    scorekeeper.add_score(name4, 100)
    # more scores for same players, in different order
    scorekeeper.add_score(name4, 5)
    scorekeeper.add_score(name2, 10)
    scorekeeper.add_score(name2, 10)
    scorekeeper.add_score(name2, 10)
    scorekeeper.add_score(name3, 10)
    scorekeeper.add_score(name3, 20)
    scorekeeper.add_score(name1, 10)
    scorekeeper.add_score(name4, 5)
    # totals:  [20, 50, 60, 110]
    # get all scores
    player1 = scorekeeper.get_player(name1)
    player2 = scorekeeper.get_player(name2)
    player3 = scorekeeper.get_player(name3)
    player4 = scorekeeper.get_player(name4)
    assert player1.score == 20
    assert player2.score == 50
    assert player3.score == 60
    assert player4.score == 110


def test_get_nonexisting_player():
    """get_player should return none if player name is not a Player"""
    scorekeeper = ScoreKeeper()
    scorekeeper.add_score(name1, 10)
    scorekeeper.add_score(name2, 20)
    # this name is not in the scorekeeper's player collection
    # should return None for unknown player. Don't raise exception.
    player = scorekeeper.get_player("Bogus")
    assert player is None


def test_top_n():
    """Returns highest scoring players."""
    scorekeeper = ScoreKeeper()
    scorekeeper.add_score(name1, 10)
    scorekeeper.add_score(name2, 20)
    scorekeeper.add_score(name3, 40)
    scorekeeper.add_score(name4, 30)
    # Top 2 scorers
    best = scorekeeper.top(2)
    assert len(best) == 2
    assert isinstance(best[0], Player), "top should return Player objects"
    assert isinstance(best[1], Player), "top should return Player objects"
    assert best[0].name == name3
    assert best[1].name == name4
    # players 1 and 2 fight back
    scorekeeper.add_score(name1, 40) # total 50
    scorekeeper.add_score(name2, 40) # total 60
    best = scorekeeper.top(3)
    assert len(best) == 3
    assert best[0].name == name2
    assert best[1].name == name1
    assert best[2].name == name3
    # border case: get the top 1 player
    best = scorekeeper.top(1)
    assert len(best) == 1
    assert best[0].name == name2
    # if n > number of players, return all the players
    best = scorekeeper.top(10)
    assert len(best) == 4
    assert best[0].name == name2
    assert best[3].name == name4
