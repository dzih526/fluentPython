import collections
from random import choice,choices

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)] + list('JQKA')
    suits="hongTao heiTao fangPian meiHua".split()

    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return (self._cards[item])

if __name__ == '__main__':
    deck = FrenchDeck()
    