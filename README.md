## Tests for Programming Skill Assessment

These are the tests used to evaluate student submissions for quiz0.
Most of the test code is the same as the tests included in the starter code and given to students.

I modified two tests to also test for:

- each ScoreKeeper has its own collection of Players.  This collection should not be shared among scorekeepers. That is, it is an instance attribute not a class or static attribute.
- when you invoke `scorekeeper.get_player("player-name')` it always returns the same Player object for the same player name. It should not return a different Player object each time.
