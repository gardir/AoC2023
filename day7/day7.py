from queue import PriorityQueue
import re

real = 'input'
example = 'example'
test = 'test'

ranks = [
    (re.compile(r"(\w)\1{4}"),  "five-of-a-kind"),
    (re.compile(r"\w*?(\w)\1{3}\w*?"),  "four-of-a-kind"),
    (re.compile(r"(?:(\w)\1\1(\w)\2|(\w)\3(\w)\4\4)"),  "Full house"),
    (re.compile(r"\w*?(\w)\1{2}\w*?"),  "Three of a kind"),
    (re.compile(r"\w*?(\w)\1\w*?(\w)\2\w*?"),  "Two pair"),
    (re.compile(r"\w*?(\w)\1\w*?"),  "One pair"),
    (re.compile(r"(\w{5})"), "High card"),
]

card_ranks = [c.strip() for c in "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(",")]


class Hand:
    def __init__(self, hand, value):
        self.hand = hand
        self.value = value
        self.sorted_hand = ''.join(sorted(hand, key=lambda v: card_ranks.index(v.upper())))
        self.rank, self.rank_description = self.estimate_rank(hand)

    def estimate_rank(self, hand):
        for rank, (rank_check, rank_description) in enumerate(ranks):
            matched_rank = re.match(rank_check, self.sorted_hand)
            if matched_rank:
                return rank, rank_description
        raise Exception(f"Invalid rank: {hand}")

    def __lt__(self, other):
        if isinstance(other, Hand):
            if self.rank < other.rank:
                return True
            elif self.rank == other.rank:
                for i, u in zip(self.hand, other.hand):
                    iv = card_ranks.index(i.upper())
                    uv = card_ranks.index(u.upper())
                    if iv < uv:
                        return True
                    if uv < iv:
                        return False
        return False

    def __repr__(self):
        return f"Hand<{self.hand} ({self.sorted_hand}) has {self.rank_description} ({self.rank})>"


class Hands:

    def __init__(self, handlines):
        self.all_hands = {}
        for i, hand in enumerate(handlines):
            self.all_hands[i] = Hand(*hand.split())


n = 0
hands = PriorityQueue()
with open(real) as f:
    for line in f.readlines():
        hands.put(Hand(*line.split()))
        n += 1

total_winnings = 0
while not hands.empty():
    hand = hands.get()
    winnings = n * int(hand.value)
    print(f"{hand} achieved {winnings} winnings")
    total_winnings += winnings
    n -= 1
print(total_winnings)
