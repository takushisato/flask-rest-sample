from flask_restful import reqparse
from flasklib.controllers.common.base_route import BaseRoute


class UserController(BaseRoute):
    @BaseRoute.base_exception_res
    def get(self, id: int):
        print('Userの取得')

    def post(self):
        print('Userの登録')

    def put(self, id: int):
        print('Userの編集')

    def delete(self, id: int):
        print('Userの削除')
