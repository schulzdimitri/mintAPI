from src.controllers.interfaces.balance_editor import BalanceEditorInterface

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interfaces import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get('new_balance')
        user_id = http_request.body.params.get('user_id')
        self.__validate_inputs(new_balance, user_id)
        
        response = self.__controller.edit_balance(new_balance, user_id)
        return HttpResponse(body={ 'data': response }, status_code=200)
        
    def __validate_inputs(self, new_balance: any, user_id: any) -> None:
        if (
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
        ): raise ValueError('Invalid input data')