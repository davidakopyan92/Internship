# logic() wrapper for other functions. Recursion makes the game continuous.
#         If command doesn't repeat -> if it exists -> do stuff
# is_repeat() makes sure user commands do not repeat, i.e. endless loop of silent contempt :)
# for_correct() for commands that exist prints the msg, takes new user input and restarts logic() with it
# for_wrong() shows disrespect and restarts logic()
# MAY BE it's possible to use less variables, passing then prom function to function... I have to read about the scope
# just decided to use everything we learned so far

import sys
def logic(user_command, values, prev=''):

    def is_repeat(user_com, prev_command=''):
        prev_command = prev
        if user_com == prev_command:
            print('Aye aye, sir!')  # can't do twice
            while user_com == prev_command: # loop until different command given
                user_com = input(' ')
            else:
                return user_com
        else:
            return user_com

    def for_correct():
        print(values[x])
        previous = x
        command = input(' ')
        logic(command, values, previous)

    def for_wrong():
        user_com = input('Mess with the best, die like the rest')
        logic(user_com, values)


    com = is_repeat(user_command)
    if com == 'quit':
        sys.exit('Game ended')   # return didn't work for me
    for x in values:
        if com == x:
            for_correct()

    for_wrong()

scenarios = {'help': ' Enter start - to start the ride\n Enter stop - to stop the ride\n Enter quit - to quit the ride',
            'start': "Car started, ready to go\n",
            'stop': 'Car stopped\n',
            'quit': 'Game ended\n'}

answer = input(' Imagine you have a car. Tell me what to do with it. '
               'If you are a new user, enter “help”\n ')

logic(answer, scenarios)

