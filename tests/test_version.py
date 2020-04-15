from pom_elements.__version__ import __version__


def test_version():
    """Test that the current version of the project is set accurately."""
    assert __version__ == "0.1.0"
