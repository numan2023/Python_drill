# カード：5枚
# 1<= x <= 13 (int)
# 役：カードの組み合わせ

# 例）
# FULL HOUSE：1 1 1 2 2（ある数をちょうど3つと、別の数をちょうど2つ含む。）
# THREE CARD：1 1 1 2 3（ある数をちょうど3つ含む。）
# TWO PAIR：1 1 2 2 3（ある数をちょうど2つと、別の数をちょうど2つ含む。）
# ONE PAIR：1 1 2 3 4（ある数をちょうど2つ含む。）
# NO HAND：役なし


from collections import Counter

# 役を判定する関数
def determine_hand(cards):
    """
    Determine the poker hand from a list of 5 cards.

    :param cards: A list of integers representing the card (1 to 13).
    return: The name of the hand.
    """

    counts = Counter(cards)
    unique_counts = set(counts.values())

    if 3 in unique_counts and 2 in unique_counts:
        return "Full House"
    
    if 3 in unique_counts:
        return "Three Card"
    
    if list(counts.values()).count(2) == 2:
        return "Two Pair"
    
    if 2 in unique_counts:
        return "One Pair"
    
    return "No Hand"

example_hands = [
    [1, 1, 1, 2, 2], # Full House
    [1, 1, 1, 2, 3], # Three Card
    [1, 1, 2, 2, 3], # Two Pair
    [1, 1, 2, 3, 4], # One Pair
    [1, 2, 3, 4, 5], # No Hand
]

for hand in example_hands:
    print(f"Hand {hand}: {determine_hand(hand)}")