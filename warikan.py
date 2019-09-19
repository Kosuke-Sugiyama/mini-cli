def main():
    total = int(input('合計金額 : '))
    number_of_people = int(input('人数 : '))

    print(f'一人当たり{total // number_of_people}円です。端数は{total % number_of_people}円です。')


if __name__ == '__main__':
    main()