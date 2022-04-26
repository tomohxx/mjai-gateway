from .decoder import Meld


class State:
    def __init__(self, name: str = 'NoName', room: str = '0_0'):
        self.name: str = name
        self.room: str = room.replace('_', ',')
        # 手牌(天鳳インデックス)
        self.hand: list[int] = []
        # 立直をかけているか
        self.in_riichi: bool = False
        # 壁牌の枚数
        self.live_wall: int | None = None
        # 副露のリスト
        self.melds: list[Meld] = []
        # 待ち
        self.wait: set[int] = set()
