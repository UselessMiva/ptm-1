from yahtzee import Yahtzee

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores():
    """
    function that test scores
    """
    expected_scores = 15
    actual_scores = Yahtzee.chance(2, 3, 4, 5, 1)
    assert expected_scores == actual_scores
    assert 16 == Yahtzee.chance(3, 3, 4, 5, 1)
  

def test_yahtzee():
    """
    function that test the five identical dice
    """
    expected_scores = 50
    actual_scores = Yahtzee.yahtzee([4, 4, 4, 4, 4])
    assert expected_scores == actual_scores
    assert 50 == Yahtzee.yahtzee([6, 6, 6, 6, 6])
    assert 0 == Yahtzee.yahtzee([6, 6, 6, 6, 3])
  

def test_ones():
    """
    function that test the ones function
    """
    assert Yahtzee.ones(1, 2, 3, 4, 5) == 1
    assert 2 == Yahtzee.ones(1, 2, 1, 4, 5)
    assert 0 == Yahtzee.ones(6, 2, 2, 4, 5)
    assert 4 == Yahtzee.ones(1 ,2, 1, 1, 1)
  

def test_twos():
    """
    function that test the twos function
    """
    assert 4 == Yahtzee.twos(1, 2, 3, 2, 6)
    assert 10 == Yahtzee.twos(2, 2, 2, 2, 2)
  

def test_threes():
    """
    function that test the threes function
    """
    assert 6 == Yahtzee.threes(1, 2, 3, 2, 3)
    assert 12 == Yahtzee.threes(2, 3, 3, 3, 3)
  

def test_fours():
    """
    function that test the fours function
    """
    assert 12 == Yahtzee(4, 4, 4, 5, 5).fours()
    assert 8 == Yahtzee(4, 4, 5, 5, 5).fours()
    assert 4 == Yahtzee(4, 5, 5, 5, 5).fours()
  

def test_fives():
    """
    function that test the fives function
    """
    assert 10 == Yahtzee(4, 4, 4, 5, 5).fives()
    assert 15 == Yahtzee(4, 4, 5, 5, 5).fives()
    assert 20 == Yahtzee(4, 5, 5, 5, 5).fives()
  

def test_sixes():
    """
    function that test the sixs function
    """
    assert 0 == Yahtzee(4, 4, 4, 5, 5).sixes()
    assert 6 == Yahtzee(4, 4, 6, 5, 5).sixes()
    assert 18 == Yahtzee(6, 5, 6, 6, 5).sixes()
  

def test_one_pair():
    """
    function that test the score_pair function
    """
    assert 6 == Yahtzee.score_pair(3, 4, 3, 5, 6)
    assert 10 == Yahtzee.score_pair(5, 3, 3, 3, 5)
    assert 12 == Yahtzee.score_pair(5, 3, 6, 6, 5)
  

def test_two_pair():
    """
    function that test the two_pair function
    """
    assert 16 == Yahtzee.two_pair(3, 3, 5, 4, 5)
    assert 0 == Yahtzee.two_pair(3, 3, 5, 5, 5)


def test_three_of_a_kind():
    """
    function that test the three_of_a_kind function
    """
    assert 9 == Yahtzee.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yahtzee.three_of_a_kind(5, 3, 5, 4, 5)
    assert 0 == Yahtzee.three_of_a_kind(3, 3, 3, 3, 5)
  

def test_four_of_a_kind():
    """
    function that test the four_of_a_kind function
    """
    assert 12 == Yahtzee.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yahtzee.four_of_a_kind(5, 5, 5, 4, 5)
    assert 0 == Yahtzee.four_of_a_kind(3, 3, 3, 3, 3)
  

def test_small_straight():
    """
    function that test the small_straight function
    """
    assert 15 == Yahtzee.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yahtzee.small_straight(2, 3, 4, 5, 1)
    assert 0 == Yahtzee.small_straight(1, 2, 2, 4, 5)
  

def test_large_straight():  
    """
    function that test the large_straight function
    """
    assert 20 == Yahtzee.large_straight(6, 2, 3, 4, 5)
    assert 20 == Yahtzee.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yahtzee.large_straight(1, 2, 2, 4, 5)
  

def test_full_house():
    """
    function that test the full_house function
    """
    assert 18 == Yahtzee.full_house(6, 2, 2, 2, 6)
    assert 0 == Yahtzee.full_house(2, 3, 4, 5, 6)
