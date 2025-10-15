from main import exchange_coins


def test_exchange():
    assert exchange_coins(cash=50) == {50: 1}
