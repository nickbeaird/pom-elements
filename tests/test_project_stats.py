from pom_elements.__version__ import __version__ as project_version


def test_version():
    """Test that the current version of the project is set accurately."""
    assert project_version == "0.1.0"
