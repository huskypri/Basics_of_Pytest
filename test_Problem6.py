import pytest
from unittest.mock import Mock
from Problem6 import Database


@pytest.fixture
def database_connection():
    db = Database()
    db.connect = Mock()
    db.disconnect = Mock()

    db.connect()
    yield db
    db.disconnect()

    db.connect.assert_called_once()
    db.disconnect.assert_called_once()


def test_database_connection_fixture(database_connection):
    assert isinstance(database_connection, Database)
    database_connection.connect.assert_called_once()


def test_database_connection_fixture_without_isinstance(database_connection):
    assert type(database_connection) is Database
    database_connection.connect.assert_called_once()