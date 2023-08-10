"""
Tests of the Player class.
These tests require pytest be installed.
Run these tests using 'pytest -v test_player.py' 
(-v is optional)
"""
from player import Player
import pytest


def test_constructor_and_readonly_properties():
    """Constructor correctly initializes arguments."""
    p = Player("Fred")
    q = Player("Bill Gates")
    assert p.name == "Fred"
    assert p.score == 0
    assert q.name == "Bill Gates"

    """Score and name should be read-only properties."""
    p = Player("Foo")
    with pytest.raises(AttributeError):
        p.score = 1
    with pytest.raises(AttributeError):
        p.name = "Bar"

def test_add_score():
    """Add score accumulates scores."""
    p = Player("Shakar")
    q = Player("Jabaar")
    p.add_score(5)
    assert p.score == 5
    p.add_score(20)
    assert p.score == 25
    p.add_score(25)
    assert p.score == 50
    # other player's score is still 0
    assert q.score == 0

def test_score_raises_exception():
    """Should raise ValueError if score is invalid."""
    p = Player("Bogus")
    p.add_score(20)
    with pytest.raises(ValueError):
        p.add_score(-1)
    # Only NEGATIVE values raise an exception
    p.add_score(0)   # useless, but valid


def test_str():
    """String value is player's name in title case."""
    # This is easy. Python str class has a method to do this.
    p = Player("Numero UNO")
    q = Player("niban")      # Japanese for #2
    assert str(p) == "Numero Uno"
    assert str(q) == "Niban"


def test_less_than():
    """Less than compares players by total score."""
    p = Player("First")
    q = Player("Second")
    p.add_score(10)
    q.add_score(1)
    # Player p has larger score, so p > q
    assert q < p
    assert not p < q
    assert not p < p
    q.add_score(5)
    q.add_score(5)
    # Now q has larger score than p.
    assert p < q
    assert not q < p
