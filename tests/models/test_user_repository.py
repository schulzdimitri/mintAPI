from unittest.mock import Mock

from ...src.models.repositories.user_repository import UserRepository


class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()
 
        
class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_user():
    username = "test_user"
    password = "test_password"
    
    mock_conn = MockConnection()
    repo = UserRepository(mock_conn)
    
    repo.registry_user(username, password)
    
    cursor = mock_conn.cursor.return_value
    
    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)
    
    mock_conn.commit.assert_called_once()
    
    
def test_edit_balance():
    user_id = 234
    balance = 100.11
    
    mock_conn = MockConnection()
    repo = UserRepository(mock_conn)
    
    repo.edit_balance(user_id, balance)
    
    cursor = mock_conn.cursor.return_value
    
    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (balance, user_id)
   
    
def test_get_user_by_username():
    username = "test_user"
    password = "test_password"
        
    mock_conn = MockConnection()
    repo = UserRepository(mock_conn)
    
    repo.registry_user(username, password)
    repo.get_user_by_username(username)
    
    cursor = mock_conn.cursor.return_value
    
    assert "SELECT id, username, password, balance" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)
    
    cursor.fetchone.assert_called_once()
    assert cursor.fetchone.return_value == repo.get_user_by_username(username)