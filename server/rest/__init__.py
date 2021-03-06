from flask.ext.restful import Api

from constants import HTTP_STATUS

from internal.exceptions import ServerAlreadyExistsError
from internal.exceptions import UserAlreadyExistsError


class VinzApi(Api):
    """
    Base Api class to override some error handling and return specific responses for certain
    exceptions specific to this application/api.
    """

    def handle_error(self, e):
        if isinstance(e, UserAlreadyExistsError):
            data = {'message': "User already exists."}
            return self.make_response(data, HTTP_STATUS.BAD_REQUEST)
        elif isinstance(e, ServerAlreadyExistsError):
            data = {'message': "Server already exists."}
            return self.make_response(data, HTTP_STATUS.BAD_REQUEST)
        else:
            return super(VinzApi, self).handle_error(e)
