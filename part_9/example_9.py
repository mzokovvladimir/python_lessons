class CardDeck:
    """
    Реалізація ітератора колоди карток (52 штуки) CardDeck. Кожна карта представлена у вигляді рядка типу "2 Пік".
    При виклику функції next() буде представлено наступну картку. Після закінчення перебору всіх елементів з'явиться
    помилка StopIteration.
    """

    def __init__(self):
        self.__length = 52
        self._index = 0
        self.__SUITS = ['П', 'Б', 'Ч', 'К']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']

    def __len__(self):
        return self.__length

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self.__length:
            raise StopIteration
        else:
            suit = self.__SUITS[self._index // len(self.__RANKS)]
            rank = self.__RANKS[self._index % len(self.__RANKS)]
            self._index += 1
            return f'{rank} {suit}'


deck = CardDeck()
while True:
    try:
        print(next(deck))
    except StopIteration:
        break
