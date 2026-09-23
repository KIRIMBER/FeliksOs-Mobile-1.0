#!/usr/bin/env python3
# ============================================================
#  🐱 FELIKSOS Mobile v1.0
#  📱 Terminal Edition for UserLAnd
#  🖤 Created by Kernel
# ============================================================

import os
import sys
import time
import random

# ============================================================
#  🎨 ЦВЕТА
# ============================================================
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

# ============================================================
#  🐱 ASCII-КОТ
# ============================================================
CAT = r"""
      /\_/\
     ( o.o )
      > ^ <
"""

# ============================================================
#  🌌 КОСМИЧЕСКИЕ ОБОИ
# ============================================================
def show_wallpaper():
    os.system('clear')
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════════╗
║{PURPLE}                    🌌 КОСМОС FELIKSOS  🌌                    {CYAN}║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║{YELLOW}        *        .        ✦        .        *                {CYAN}║
║{WHITE}     .        *        .        🌟        .        *          {CYAN}║
║{PURPLE}         ✦        🌌        .        ✦        .               {CYAN}║
║                                                              ║
║{BLUE}              🪐  ПЛАНЕТЫ  🪐  ЗВЁЗДЫ  🪐  КОСМОС              {CYAN}║
║                                                              ║
║{YELLOW}        .        *        ✦        .        *                {CYAN}║
║{WHITE}     *        .        🌟        .        *        .          {CYAN}║
║{PURPLE}         .        ✦        .        🌌        ✦               {CYAN}║
║                                                              ║
║{CYAN}                   🐱 FELIKSOS ULTIMATE 🐱                   {CYAN}║
║                                                              ║
║{YELLOW}              Добро пожаловать, Kernel!                       {CYAN}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")

# ============================================================
#  🧮 КАЛЬКУЛЯТОР
# ============================================================
def calculator():
    print(f"{YELLOW}🧮 Калькулятор FeliksOS{RESET}")
    print("Введи выражение (например: 2 + 2)")
    print("Или 'back' для возврата.")

    while True:
        expr = input(f"{CYAN}calc> {RESET}").strip()
        if expr.lower() == 'back':
            break
        try:
            result = eval(expr)
            print(f"{GREEN}Результат: {result}{RESET}")
        except:
            print(f"{RED}Ошибка! Попробуй снова.{RESET}")

# ============================================================
#  🎮 ИГРА: УГАДАЙ ЧИСЛО
# ============================================================
def guess_game():
    print(f"{YELLOW}🎮 Угадай число!{RESET}")
    print("Я загадал число от 1 до 100.")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input(f"{CYAN}Твой вариант: {RESET}"))
            attempts += 1

            if guess < secret:
                print(f"{BLUE}Больше!{RESET}")
            elif guess > secret:
                print(f"{BLUE}Меньше!{RESET}")
            else:
                print(f"{GREEN}🎉 Угадал! С {attempts} попыток!{RESET}")
                break
        except:
            print(f"{RED}Введи число!{RESET}")

# ============================================================
#  🔐 ШИФР ЦЕЗАРЯ
# ============================================================
def ceasar_cipher():
    print(f"{YELLOW}🔐 Шифр Цезаря{RESET}")
    print("1. Зашифровать")
    print("2. Расшифровать")
    print("3. Назад")

    choice = input(f"{CYAN}Выбор: {RESET}")

    if choice == '1':
        text = input("Текст: ")
        shift = int(input("Сдвиг: "))
        result = ''.join(chr((ord(c) + shift) % 256) for c in text)
        print(f"{GREEN}Зашифровано: {result}{RESET}")
    elif choice == '2':
        text = input("Текст: ")
        shift = int(input("Сдвиг: "))
        result = ''.join(chr((ord(c) - shift) % 256) for c in text)
        print(f"{GREEN}Расшифровано: {result}{RESET}")

# ============================================================
#  🌌 КОСМОС (АНИМАЦИЯ)
# ============================================================
def cosmos_animation():
    stars = ['*', '.', '✦', '🌟', '✨', '·']
    for i in range(30):
        os.system('clear')
        print(f"{CYAN}🌌 КОСМОС FELIKSOS 🌌{RESET}\n")
        for _ in range(15):
            line = ''.join(random.choice(stars) if random.random() > 0.7 else ' ' for _ in range(60))
            print(f"{random.choice([CYAN, BLUE, PURPLE, WHITE])}{line}{RESET}")
        time.sleep(0.3)

# ============================================================
#  🛒 МАГАЗИН
# ============================================================
def market():
    balance = 0

    print(f"{YELLOW}🛒 FELIKSOS MARKET{RESET}")
    print(f"💰 Баланс: {balance} BTC")
    print("\n1. ⛏️ Майнить (+5 BTC)")
    print("2. ⌨️ Купить клавиатуру (5 BTC)")
    print("3. 🪑 Купить кресло (5 BTC)")
    print("4. 💣 Купить бомбу (5 BTC)")
    print("5. Назад")

    while True:
        choice = input(f"{CYAN}market> {RESET}")

        if choice == '1':
            balance += 5
            print(f"{GREEN}⛏️ Намайнено! Баланс: {balance} BTC{RESET}")
        elif choice == '2':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплена клавиатура!{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '3':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплено кресло!{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '4':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплена бомба! 💣{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '5':
            break

# ============================================================
#  📋 СПРАВКА
# ============================================================
def show_help():
    print(f"""{YELLOW}
📋 ДОСТУПНЫЕ КОМАНДЫ:

  help      — этот список
  version   — версия FeliksOS
  meow      — Феликс мяукает
  cat       — ASCII-кот
  calc      — калькулятор
  game      — игра "Угадай число"
  ceasar    — шифр Цезаря
  cosmos    — анимация космоса
  market    — магазин FeliksOS
  clear     — очистить экран
  exit      — выход
{RESET}""")

# ============================================================
#  🚀 ГЛАВНАЯ ФУНКЦИЯ
# ============================================================
def main():
    show_wallpaper()
    print(f"{GREEN}Добро пожаловать в FeliksOS Ultimate!{RESET}")
    print(f"{GREEN}Введи 'help' для списка команд.{RESET}\n")

    while True:
        try:
            cmd = input(f"{CYAN}feliksos> {RESET}").strip().lower()

            if cmd == "help":
                show_help()
            elif cmd == "version":
                print(f"{GREEN}FeliksOS Mobile v1.0{RESET}")
            elif cmd == "meow":
                print(f"{YELLOW}🐱 Мяу!{RESET}")
            elif cmd == "cat":
                print(f"{CYAN}{CAT}{RESET}")
            elif cmd == "calc":
                calculator()
            elif cmd == "game":
                guess_game()
            elif cmd == "ceasar":
                ceasar_cipher()
            elif cmd == "cosmos":
                cosmos_animation()
            elif cmd == "market":
                market()
            elif cmd == "clear":
                show_wallpaper()
            elif cmd == "exit":
                print(f"{YELLOW}🐱 Феликс: Пока, Kernel!{RESET}")
                break
            else:
                print(f"{RED}Неизвестная команда. Введи 'help'.{RESET}")
        except KeyboardInterrupt:
            print(f"\n{YELLOW}🐱 Феликс: Пока!{RESET}")
            break

# ============================================================
if __name__ == "__main__":
    main()
