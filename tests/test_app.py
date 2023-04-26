from projectname.app import validate_name


def test_validate_name():
    assert validate_name("fuji44") is True
