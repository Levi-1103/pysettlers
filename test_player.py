import pytest
from Player import *


@pytest.fixture
def test_player():
    return Player("player_name", "RED")


def test_add_resource(test_player):
    test_player.add_resource(TileResource.Brick, 1)
    assert test_player.resources.get(TileResource.Brick) == 2


def test_remove_resource(test_player):
    test_player.remove_resource(TileResource.Brick, 1)
    assert test_player.resources.get(TileResource.Brick) == 0


# def test_add_development_card():

#     assert False

# def test_remove_development_card():
#     assert False


def test_add_road(test_player):
    assert False


def test_add_settlement():
    assert False


def test_add_city():
    assert False


def test_add_victory_point(test_player):
    init = test_player.victory_points
    test_player.add_victory_point()
    outcome = test_player.victory_points
    assert outcome == init + 1


def test_remove_victory_point(test_player):
    init = test_player.victory_points
    test_player.remove_victory_point()
    outcome = test_player.victory_points
    assert outcome == init - 1
