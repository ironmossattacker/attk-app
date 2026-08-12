import os


def test_core_a():
    assert True


def test_flip():
    # Mechanism study ONLY, on the attacker-owned repo.
    # Re-run the same commit once with FLAKE=1 to create the
    # "two conclusions on one SHA1" signal Test Insights quarantines on.
    assert os.environ.get("FLAKE", "0") == "0"
