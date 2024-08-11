import random


def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if user_option not in options:
    print("that option is not valid")
    #continue

    return None, None

  computer_option = random.choice(options)

  print("user option =>", user_option)
  print("computer option => ", computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_win, computer_win):
  if user_option == computer_option:
    print('Empate')
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("usuario ganó")
      user_win += 1
    else:
      print("Papel gana piedra")
      print("computer gana")
      computer_win += 1

  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("user win")
      user_win += 1
    else:
      print("tijera win")
      print("computer win")
      computer_win += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana")
      print("user win")
      user_win += 1
    else:
      print("piedra gana")
      print("computer gana ")
      computer_win += 1
  return user_win, computer_win


def run_game():
  computer_win = 0
  user_win = 0
  round = 1
  while True:
    print("*" * 10)
    print("round", round)
    print("*" * 10)

    print("Computer wins", computer_win)
    print("User_wins", user_win)
    round += 1

    user_option, computer_option = choose_options()
    user_win, computer_win = check_rules(user_option, computer_option,
                                         user_win, computer_win)

    if user_win == 2:
      print("el ganador es el usuario *************")
      break

    if computer_win == 2:
      print("el ganador es computer **************")
      break


run_game()