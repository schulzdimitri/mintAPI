import pytest

from ...src.views.http_types.http_request import HttpRequest
from ...src.views.http_types.http_response import HttpResponse
from ...src.views.user_register_view import UserRegisterView


class MockController:
    def registry(self, username: str, password: str) -> dict:
        return {
            'id': 1,
            'username': username
        }

def test_handle_user_register():
    body = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    
    request = HttpRequest(body=body)
    
    mock_controller = MockController()
    user_register_view = UserRegisterView(controller=mock_controller)
    
    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body['data']['id'] == 1
    assert response.body['data']['username'] == 'testuser'
    
def test_handle_user_register_validation_error():
    body = {
        'password': 'testpassword'
    }
    
    request = HttpRequest(body=body)
    
    mock_controller = MockController()
    user_register_view = UserRegisterView(controller=mock_controller)
    
    with pytest.raises(ValueError):
        user_register_view.handle(request)
    