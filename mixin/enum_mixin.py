from enum import Enum
from typing import Callable, Optional, TypeVar, Type, List

E = TypeVar('E', bound=Enum)

class EnumLinqMixin:
    @classmethod
    def values(cls: Type[E]) -> List:
        return [e.value for e in cls]
    
    @classmethod
    def names(cls: Type[E]) -> List[str]:
        return [e.name for e in cls]
    
    @classmethod
    def map(cls: Type[E], func: Callable[[E], any]) -> List:
        """類似 Dart map，對每個 Enum 執行 func"""
        return [func(e) for e in cls]

    @classmethod
    def index_where(cls: Type[E], predicate: Callable[[E], bool]) -> int:
        for i, e in enumerate(cls):
            if predicate(e):
                return i
        return -1

    @classmethod
    def first_where(cls: Type[E], predicate: Callable[[E], bool], default: Optional[E]=None) -> Optional[E]:
        for e in cls:
            if predicate(e):
                return e
        return default
    
    @classmethod
    def where(cls: Type[E], predicate: Callable[[E], bool]) -> List[E]:
        """返回所有符合 predicate 的 Enum 成員列表"""
        return [e for e in cls if predicate(e)]