# --- XO game for practical work on SkillFactory FPW-2.0 course
# --- Evgeniy Ivanov, flow FPW-42, Okt'2021

BOARDS = {
    'main': {7: '_', 8: '_', 9: '_', 4: '_', 5: '_', 6: '_', 1: '_', 2: '_', 3: '_'},  # - Game board for print
    'X': {7: '_', 8: '_', 9: '_', 4: '_', 5: '_', 6: '_', 1: '_', 2: '_', 3: '_'},     # - Mask board for X-sign
    'O': {7: '_', 8: '_', 9: '_', 4: '_', 5: '_', 6: '_', 1: '_', 2: '_', 3: '_'}      # - Mask board for O-sign
}

WIN_RULES = [
    [7, 8, 9],  # - top horizontal line
    [4, 5, 6],  # - middle  horizontal line
    [1, 2, 3],  # - bottom horizontal line
    [1, 4, 7],  # - left vertical line
    [2, 5, 8],  # - middle vertical line
    [3, 6, 9],  # - right vertical line
    [3, 5, 7],  # - \ line
    [1, 5, 9]   # - / line
]


def print_board():
    board = BOARDS['main']
    print(f'{board[7]} {board[8]} {board[9]}')
    print(f'{board[4]} {board[5]} {board[6]}')
    print(f'{board[1]} {board[2]} {board[3]}')


def win_check(sign):
    board_mask = sorted([cell for cell in BOARDS[sign] if BOARDS[sign][cell] == '*'])
    winner = bool([True for rule in WIN_RULES if len(set(board_mask).intersection(set(rule))) == 3])
    return winner


def set_cell(cell, sign):
    BOARDS['main'][cell] = sign
    BOARDS[sign][cell] = '*'


def start():
    sign = 'X'  # - current sign
    step = 1    # - current step
    while True:
        # - print current game board
        print_board()

        # - wait & check user input
        cell = input(f'\nCurrent {sign}, Type cell [1-9] or 0 for exit game: ')

        # - if 0 - exit
        if cell == '0':
            break

        # - if in range [1-9] proceed game process
        elif cell in list(map(str, range(1, 10))):
            # - If cell is not busy then set current sign to it
            if BOARDS['main'][int(cell)] == '_':
                set_cell(int(cell), sign)
            else:
                print(f'\nCell is busy... repeat input')
                continue
            # - Winner check
            if win_check(sign):
                print(f'\nSign {sign} winner!!!')
                print_board()
                break
            else:
                # - If no winner, check steps
                if step == 9:
                    print(f'\nNo more steps!!! GAME OVER')
                    print_board()
                    break
                else:
                    step += 1
            # - Replace current sign
            sign = 'O' if sign == 'X' else 'X'

        # - if otherwise print a warning and continue
        else:
            print('\nWrong input: Must be [1-9] for select cell, or 0 for exit game')
            continue


if __name__ == '__main__':
    print(f'\nWelcome to XO-game. Game play step by step, from X to O sign.')
    print(f'Use Numpad for select cell. Good luck!!!\n')
    start()
