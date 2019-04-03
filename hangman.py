def hangman(word):
    wrong = 0
    stages = ["",
              "__________       ",
              "|         |      ",
              "|         |      ",
              "|         o      ",
              "|       | | |    ",
              "|         人     ",
              "|                "
              ]
    rletters = list(word);
    board = ["_"] * len(word)
    win = False
    print("welcome.")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字いれてね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print ("\n".join(stages[0:wrong+1]))
        if "_" not in board:
            print ("you win")
            print (" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose.")

    print("aaa")
