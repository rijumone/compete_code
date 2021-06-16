'''
Ref:
https://www.hackerrank.com/challenges/crossword-puzzle/problem
'''


def crossword_puzzle(crossword, words):
    pass


if __name__ == '__main__':
    crossword = [
        '+-++++++++',
        '+-++++++++',
        '+-++++++++',
        '+-----++++',
        '+-+++-++++',
        '+-+++-++++',
        '+++++-++++',
        '++------++',
        '+++++-++++',
        '+++++-++++',
    ]
    words = 'LONDON;DELHI;ICELAND;ANKARA'

    crossword_puzzle(crossword, words)
    '''
    expected output:

    +L++++++++
    +O++++++++
    +N++++++++
    +DELHI++++
    +O+++C++++
    +N+++E++++
    +++++L++++
    ++ANKARA++
    +++++N++++
    +++++D++++
    
    '''
