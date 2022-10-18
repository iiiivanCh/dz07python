

def get_search():
    user_search = input('Введите искомое: ')
    print('-' * 80)
    print('РЕЗУЛЬТАТЫ ПОИСКА')
    print('-' * 80)
    with open('data_tel.txt', 'r', encoding='utf-8') as f:
        sum_line = ''
        flag = False
        for line in f:
            if not line == '\n':
                line = line.replace('\n', '')
                sum_line += line
            else:
                if user_search not in sum_line:
                    sum_line = ''
                else:
                    flag = True
                    print(sum_line + '\n')
                    sum_line = ''
        if flag:
            print('-' * 80)
            redo = input(
                'Желаете повторить поиск? (дa - д, нет - любую клавишу): ')
            if redo == 'д':
                get_search()
            else:
                return
        else:
            print()
            redo = input(
                'Ничего не найдено :(\nЖелаете повторить поиск? (дa - д, нет - любую клавишу): ')
            if redo == 'д':
                get_search()
            else:
                return
