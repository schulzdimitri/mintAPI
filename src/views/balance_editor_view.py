from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.errors.types.http_bad_request import HttpBadRequestError

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interfaces import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get('new_balance')
        user_id = http_request.params.get('user_id')
        header_user_id = http_request.headers.get('uid')
        self.__validate_inputs(new_balance, user_id, header_user_id)
        
        response = self.__controller.edit(user_id, new_balance)
        return HttpResponse(body={ 'data': response }, status_code=200)
        
    def __validate_inputs(self, new_balance: any, user_id: any, header_user_id: any) -> None:
        if (
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
            or int(header_user_id) != int(user_id)
        ): raise HttpBadRequestError('Invalid Input')