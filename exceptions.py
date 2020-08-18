class DigitOutOfRange(Exception):

    def __init__(self, msg, overflow=None):
        self.msg = msg
        self.overflow = overflow
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.overflow} -> {self.msg}'