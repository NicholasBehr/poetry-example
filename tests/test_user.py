from poetry_example.user import User


def test_user():
    """Check that User instance has the particular properties."""
    bob = User("Bob", 42)
    assert bob.name == "Bob"
    assert bob.age == 42


def test_get_introduction():
    """Check that user introduces herself properly."""
    alice = User("Alice", 21)
    intro = alice.get_introduction()
    assert alice.name in intro
    assert str(alice.age) in intro
