import random 

def RPS():
    print('Welcome to the rock,paper, and scissor game!')
    print('')
    while True:
        ques1 = str(input('Would you like to play? Yes/No ')).lower()
        if ques1 == 'yes':
            options = 'rock', 'paper', 'scissor'
            rock = 'rock wins!'
            paper = 'paper wins!'
            scissor = 'scissor wins!'
            draw = 'draw!'
            robot = random.choice(options)
            ques2 = str(input('please pick either rock/paper/scissor: ')).lower()
            fight = f'{ques2} VS {robot}'.lower()
            print(fight)
            if fight == 'rock vs paper':
                print(paper)
            elif fight == 'rock vs scissor':
                print(rock)
            elif fight == 'rock vs rock':
                print(draw)
            elif fight == 'paper vs rock':
                print(paper)
            elif fight == 'paper vs scissor':
                print(paper)
            elif fight == 'paper vs paper':
                print(draw)
            elif fight == 'scissor vs rock':
                print(scissor)
            elif fight == 'scissor vs paper':
                print(scissor)
            elif fight == 'scissor vs scissor':
                print(draw)
            else:
                print('wrong choice!')
        elif ques1 == 'no':
            print('thank you for playing!')
            break
        else:
            print('Invalid response. Please answer Yes or No.')
RPS()