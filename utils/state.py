from .decoder import Meld

# 手牌(天鳳インデックス)
hand: list[int] = []
# 立直をかけているか
in_riichi: bool = False
# 壁牌の枚数
live_wall: int | None = None
# 副露のリスト
melds: list[Meld] = []
# 待ち
wait: set[int] = set()
