from enum import Enum

from mixin.base_enum import BaseEnum #基底
from mixin.enum_mixin import EnumLinqMixin #基底

# class RouterEnum(Enum, EnumLinqMixin):
class RouterEnum(BaseEnum):
    home = ('首頁')
    analyze = ('分析')
    setting = ('設定')
    
    def __init__(self, val):
        self.val = val