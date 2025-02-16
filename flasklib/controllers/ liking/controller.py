from flask_restful import reqparse
from flasklib.controllers.common.base_route import BaseRoute

parser: reqparse.RequestParser = reqparse.RequestParser()


class LikingController(BaseRoute):
    @BaseRoute.base_exception_res
    def get(self, id: int):
        print('likingの取得')

    def post(self):
        print('likingの登録')

    def put(self, id: int):
        print('likingの編集')

    def delete(self, id: int):
        print('likingの削除')
