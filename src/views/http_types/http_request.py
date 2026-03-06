class HttpRequest:
    def __init__(
        self, 
        headers: dict = None, 
        body: str = None, 
        params: dict = None, 
        token_infos: dict = None
    ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_infos = token_infos