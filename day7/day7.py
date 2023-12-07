from queue import PriorityQueue
import re

real = 'input'
example = 'example'
test = 'test'

ranks = [
    (re.compile(r"(\w)(?:\1|J){4}"),  "Five of a kind"),
    (re.compile(r"\w*?(\w)\w*(?:\1|J)\w*?(?:\1|J)\w*?(?:\1|J)\w*?"),  "Four of a kind"),
    (re.compile(r"(\w)(?:\1|J)(?:\1|J)(\w)(?:\2|J)|(\w)(?:\3|J)(\w)(?:\4|J)(?:\4|J)"),  "Full house"),
    (re.compile(r"\w*?(\w)\w*?(?:\1|J)\w*?(?:\1|J)\w*?"),  "Three of a kind"),
    (re.compile(r"\w*?(\w)\w*?(?:\1|J)\w*?(\w)\w*?(\2|J)\w*?"),  "Two pair"),
    (re.compile(r"\w*?(\w)\w*?(?:\1|J)\w*?"),  "One pair"),
    (re.compile(r"(\w{5})"), "High card"),
]

card_ranks = [c.strip() for c in "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(",")]


class Hand:
    def __init__(self, hand, value):
        self.hand = hand
        self.value = int(value)
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
            elif other.rank < self.rank:
                return False
        raise Exception(f"Invalid comparison: {self} < {other}")

    def __repr__(self):
        return f"Hand<{self.hand}('{self.sorted_hand}'=>{self.rank_description}, {self.rank})>"


n = 0
hands = PriorityQueue()
with open(real) as f:
    for line in f.readlines():
        hands.put(Hand(*line.split()))
        n += 1

total_winnings = 0
while not hands.empty():
    hand = hands.get()
    winnings = n * hand.value
    print(f"{hand} achieved ({n} * {hand.value} =) {winnings} winnings")
    total_winnings += winnings
    n -= 1
print(total_winnings)

# 249456356 too high on first attempt
# 249400220  something in between
# 249243143  still too low
# 249232528 too low on second attempt