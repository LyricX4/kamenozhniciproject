import random


def get_computer_choice():
    """Возвращает случайный выбор компьютера."""
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def determine_winner(player, computer):
    """Определяет победителя раунда.

    Возвращает:
        'player'   - если победил игрок
        'computer' - если победил компьютер
        'draw'     - если ничья
    """
    if player == computer:
        return "draw"

    wins = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень",
    }

    if wins[player] == computer:
        return "player"
    else:
        return "computer"


def main():
    print("=" * 40)
    print(" Камень — ножницы — бумага ")
    print("=" * 40)
    print("Правила:")
    print(" - Камень бьёт ножницы")
    print(" - Ножницы бьют бумагу")
    print(" - Бумага бьёт камень")
    print("Побеждает тот, кто первым наберёт 3 очка!\n")

    valid_choices = ["камень", "ножницы", "бумага"]
    player_score = 0
    computer_score = 0
    round_num = 0

    while player_score < 3 and computer_score < 3:
        round_num += 1
        print(f"\n--- Раунд {round_num} | Счёт: Вы {player_score} : {computer_score} Компьютер ---")

        while True:
            player_input = input("Ваш выбор (камень / ножницы / бумага): ").strip().lower()
            if player_input in valid_choices:
                break
            print("Неверный ввод. Введите: камень, ножницы или бумага.")

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        result = determine_winner(player_input, computer_choice)

        if result == "draw":
            print("Результат: Ничья! Очки не начисляются.")
        elif result == "player":
            player_score += 1
            print("Результат: Вы победили в этом раунде! (+1 очко)")
        else:
            computer_score += 1
            print("Результат: Компьютер победил в этом раунде! (+1 очко)")

    print("\n" + "=" * 40)
    print("Игра окончена!")
    print("=" * 40)
    print(f"Финальный счёт: Вы {player_score} : {computer_score} Компьютер")

    if player_score > computer_score:
        print("Поздравляем! Вы победили!")
    else:
        print("Компьютер победил! Попробуйте еще раз.")
    print("=" * 40)


if __name__ == "__main__":
    main()