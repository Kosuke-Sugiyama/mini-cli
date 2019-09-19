def main():
    total = int(input('合計金額 : '))
    number_of_people = int(input('人数 : '))

    payment, amari = divmod(total, number_of_people)
    print(f'一人当たり{payment}円です。端数は{amari}円です。')


if __name__ == '__main__':
    main()
