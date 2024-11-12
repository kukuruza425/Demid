import random


def get_user_input(stones):
    while True:
        try:
            user_input = int(input(f"Выберите количество камней (1, 2 или 3) из {stones} оставшихся: "))
            if user_input not in [1, 2, 3]:
                print("Ошибка: Выберите 1, 2 или 3 камня.")
            elif user_input > stones:
                print(f"Ошибка: Нельзя взять больше камней, чем осталось ({stones}).")
            else:
                return user_input
        except ValueError:
            print("Ошибка: Пожалуйста, введите число.")


def computer_move(stones):
    return random.randint(1, min(3, stones))

#sfgsgsfg
stones = random.randint(4, 30)
print(f"Игра началась! У вас есть {stones} камней.")

while stones > 0:
    user_choice = get_user_input(stones)
    stones -= user_choice
    print(f"Вы взяли {user_choice} камня(ей). Оставшиеся камни: {stones}")
    if stones <= 0:
        print("Вы выиграли!")
        break

    computer_choice = computer_move(stones)
    stones -= computer_choice
    print(f"Компьютер взял {computer_choice} камня(ей). Оставшиеся камни: {stones}")
    if stones <= 0:
        print("Компьютер выиграл!")
####3