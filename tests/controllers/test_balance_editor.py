from src.controllers.balance_editor import BalanceEditor


class MockUserRepository:
    def __init__(self):
        self.edit_balance_called = False
        self.last_user_id = None
        self.last_balance = None
    
    def edit_balance(self, user_id: int, new_balance: float):
        self.edit_balance_called = True
        self.last_user_id = user_id
        self.last_balance = new_balance

def test_balance_editor():
    balance_editor = BalanceEditor(MockUserRepository())
    response = balance_editor.edit(1, 100.0)
    
    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["new_balance"] == 100.0

def test_balance_editor_calls_repository():
    mock_repo = MockUserRepository()
    balance_editor = BalanceEditor(mock_repo)
    balance_editor.edit(5, 250.50)
    
    assert mock_repo.edit_balance_called is True
    assert mock_repo.last_user_id == 5
    assert mock_repo.last_balance == 250.50

def test_balance_editor_multiple_edits():
    mock_repo = MockUserRepository()
    balance_editor = BalanceEditor(mock_repo)
    
    response1 = balance_editor.edit(1, 100.0)
    response2 = balance_editor.edit(2, 500.75)
    
    assert response1["new_balance"] == 100.0
    assert response2["new_balance"] == 500.75
    assert mock_repo.last_balance == 500.75

def test_balance_editor_zero_balance():
    balance_editor = BalanceEditor(MockUserRepository())
    response = balance_editor.edit(3, 0.0)
    
    assert response["new_balance"] == 0.0
    assert response["count"] == 1

def test_balance_editor_negative_balance():
    balance_editor = BalanceEditor(MockUserRepository())
    response = balance_editor.edit(4, -50.0)
    
    assert response["new_balance"] == -50.0
    assert response["type"] == "User"