from . import state

tiles_mjai: list[int] = [
    '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m',
    '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',
    '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s',
    'E', 'S', 'W', 'N', 'P', 'F', 'C'
]

tiles_tenhou: dict[str, int] = {
    '1m': 0, '2m': 1, '3m': 2, '4m': 3, '5m': 4, '5mr': 4, '6m': 5, '7m': 6, '8m': 7, '9m': 8,
    '1p': 9, '2p': 10, '3p': 11, '4p': 12, '5p': 13, '5pr': 13, '6p': 14, '7p': 15, '8p': 16, '9p': 17,
    '1s': 18, '2s': 19, '3s': 20, '4s': 21, '5s': 22, '5sr': 22, '6s': 23, '7s': 24, '8s': 25, '9s': 26,
    'E': 27, 'S': 28, 'W': 29, 'N': 30, 'P': 31, 'F': 32, 'C': 33
}


def tenhou_to_mjai_one(index: int) -> str:
    return tenhou_to_mjai([index])[0]


def mjai_to_tenhou_one(label: str, tsumogiri: bool = False) -> int:
    if tsumogiri:
        return state.hand[-1]
    else:
        return mjai_to_tenhou([label])[0]


def tenhou_to_mjai(indices: list[int]) -> list[str]:
    ret = []

    for index in indices:
        label = tiles_mjai[index // 4]
        ret.append(label + 'r' if index in [16, 52, 88] else label)

    return ret


def mjai_to_tenhou(labels: list[str]) -> list[int]:
    ret = []
    # 赤ドラを優先して残すために降順ソート
    hand = sorted(state.hand, reverse=True)

    for label in labels:
        is_red = label[-1] == 'r'
        index = tiles_tenhou[label]
        # 赤ドラが指定された場合インデックスの剰余は0
        index = [i for i in hand if i // 4 == index and (not is_red or i % 4 == 0)][0]
        ret.append(index)
        hand.remove(index)

    return ret


def to_34_array(indices: list[int]) -> list[int]:
    ret = [0] * 34

    for index in indices:
        ret[index // 4] += 1

    return ret
