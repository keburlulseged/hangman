

def hangman():
  stage = 0
  word = "lover"
  wrong_guesses = ["", "__________", "|    |", "|    O", "|   /|\\", "|   / \\", "|    "]
  letters_left = list(word)
  score_board = ["_"] * len(word)
  win = False
  print("Welcome to Hang Man")

  while stage < len(wrong_guesses) - 1:
    print('\n')
    guess = input("Guess a letter")
    if guess in word:
      score_board[word.index(guess)] = guess
      letters_left[word.index(guess)] = '$'
    else:
      stage += 1
    print("".join(score_board))
    print('\n'.join(wrong_guesses[0:stage+1]))
    if '_' not in score_board:
      print('You win! The word was:')
      print(''.join(score_board))
      win = True
      break
  if not win:
    print('\n'.join(wrong_guesses[0:stange]))
    print('You lose!')



hangman()



#test =  ["", "__________", "|    |", "|    O", "|   /|\\", "|   / \\", "|    "]

