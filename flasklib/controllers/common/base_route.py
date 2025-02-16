import logging
from abc import ABCMeta

logger = logging.getLogger(__name__)


class BaseRoute(metaclass=ABCMeta):
    @staticmethod
    def base_exception_res(func: Callable[..., Any]):
        def wrapper(*args: Any, **kwargs: Any):
            print('レスポンスの成功と例外処理を統括しておこなう')

        return wrapper
