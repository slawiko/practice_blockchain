from .block import Block


def is_valid_chain(chain):
    if chain[0] != Block.genesis():
        return False

    for i in range(1, len(chain)):
        previous = chain[i - 1]
        current = chain[i]
        if current.previousHash != previous.hash:
            return False

    return True


class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(Block.genesis())

    def mine_block(self, transactions):
        if len(transactions) == 0:
            return False

        block = Block(self.last_block_hash, transactions)

        self.chain.append(block)

        return block

    def replace_chain(self, chain):
        if len(chain) <= len(self.chain):
            raise ValueError('New chain must be longer than old one')

        self.chain = chain

    @property
    def last_block(self):
        return self.chain[-1]

    @property
    def last_block_hash(self):
        return self.last_block.hash
