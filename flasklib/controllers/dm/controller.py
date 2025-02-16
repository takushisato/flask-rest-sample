from flask_restful import reqparse
from flasklib.controllers.common.base_route import BaseRoute

parser: reqparse.RequestParser = reqparse.RequestParser()


class DmController(BaseRoute):
    @BaseRoute.base_exception_res
    def get(self, id: int):
        print('DMの取得')

    def post(self):
        print('DMの登録')

    def put(self, id: int):
        print('DMの編集')

    def delete(self, id: int):
        print('DMの削除')
