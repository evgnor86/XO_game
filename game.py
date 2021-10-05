# --- XO game for practical work on SkillFactory FPW-2.0 course
# --- Evgeniy Ivanov, flow FPW-42, Okt'2021

BOARD = {
    7: '_', 8: '_', 9: '_',
    4: '_', 5: '_', 6: '_',
    1: '_', 2: '_', 3: '_'
}

RULES = (
    {
        7: '*', 8: '*', 9: '*',
        4: '_', 5: '_', 6: '_',
        1: '_', 2: '_', 3: '_'
    },
    {
        7: '_', 8: '_', 9: '_',
        4: '*', 5: '*', 6: '*',
        1: '_', 2: '_', 3: '_'
    },
    {
        7: '_', 8: '_', 9: '_',
        4: '_', 5: '_', 6: '_',
        1: '*', 2: '*', 3: '*'
    },
    {
        7: '*', 8: '_', 9: '_',
        4: '*', 5: '_', 6: '_',
        1: '*', 2: '_', 3: '_'
    },
    {
        7: '_', 8: '*', 9: '_',
        4: '_', 5: '*', 6: '_',
        1: '_', 2: '*', 3: '_'
    },
    {
        7: '_', 8: '_', 9: '*',
        4: '_', 5: '_', 6: '*',
        1: '_', 2: '_', 3: '*'
    },
    {
        7: '*', 8: '_', 9: '_',
        4: '_', 5: '*', 6: '_',
        1: '_', 2: '_', 3: '*'
    },
    {
        7: '_', 8: '_', 9: '*',
        4: '_', 5: '*', 6: '_',
        1: '*', 2: '_', 3: '_'
    }
)


def print_board():
    print(f'{BOARD[7]} {BOARD[8]} {BOARD[9]}')
    print(f'{BOARD[4]} {BOARD[5]} {BOARD[6]}')
    print(f'{BOARD[1]} {BOARD[2]} {BOARD[3]}')


def win_check(sign):
    s = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    for i in range(1, 10):
        if BOARD[i] == sign:
            s[i-1] = '*'

    for rule in RULES:
        if s == list(rule.values()):
            return True
    return False


def start():
    sign = 'X'
    step = 1
    while True:
        print_board()
        cell = input(f'\nCurrent {sign}, Type cell [1-9] or 0 for exit game: ')
        if cell == '0':
            break

        elif cell in list(map(str, range(1, 10))):
            # ---
            if BOARD[int(cell)] == '_':
                BOARD[int(cell)] = sign
            else:
                print(f'\nCell is busy... repeat input')
                continue
            # ---
            if win_check(sign):
                print(f'\nSign {sign} winner!!!')
                print_board()
                break
            else:
                if step == 9:
                    print(f'\nOut of steps!!! GAME OVER')
                    print_board()
                    break
                else:
                    step += 1

            sign = 'O' if sign == 'X' else 'X'

        else:
            print('\nWrong input: Must be [1-9] for select cell, or 0 for exit game')
            continue


if __name__ == '__main__':
    start()
