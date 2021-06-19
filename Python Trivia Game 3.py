#Below I am importing the random shuffle function so that I can use it later to make the questions randomised.
from random import shuffle 

#I have printed what I want to initially appear when you first run the game to give you information on it. 
print('Code Author: Kelvin Adzigbli.'
'\n'
'This is an interactive quiz game called Python Trivia :).'
'\n'
'It was created for the event demo for entertainment purposes.'
'\n'
'Copyright© belongs to Kelvin Adzigbli. Copyright infringments will be legally handled.'
'\n'
'Version 3.0'
'\n')

#I'm asking the user to input their name so I can provide them with a greeting message. 
name = input('Please enter your name in the shell: ')

print('\n''Welcome to the world of Python Trivia, '+ name + '!! :)\n')

#These are the rules of the game       
print('The rules are:'
      '\n'
      ' 1). This is a multiple choice game in which you must choose one of either a, b or c.'
      '\n'
      ' 2). There are 9 questions in total.'
      '\n'
      ' 3). You get 10 points for the right answer and 0 points for the wrong one.') 

#below is a list of all 9 questions.
question_prompts = [
    'From which US city do the band The Killers originate? \na. California \nb. Las Vegas \nc. New York \n\n',
    'Name the Coffee shop in US sitcom Friends? \na. Zoo Park \nb. Park Royal \nc. Central Perk \n\n',
    'How many human players are there on each side in a polo match? \na. Eight \nb. Four \nc. Five \n\n',
    'In what year did Tony Blair become British Prime Minister? \na. 1998 \nb. 1997 \nc. 1995 \n\n',
    'How many times has England won the men’s football World Cup? \na. Twice \nb. Once \nc. Five times \n\n',
    'What is the capital of New Zealand? \na. Wellington \nb. Sydney \nc. Brisbane \n\n',
    'Street artist Banksy is originally associated with which British city? \na. Bristol \nb. Manchester \nc. London \n\n',
    'From what grain is the Japanese spirit Sake made? \na. Flour \nb. Wheat \nc. Rice \n\n', 
    'In which part of your body would you find the cruciate ligament? \na. Ankle \nb. Knee \nc. Elbow \n\n',
]

#this is a list of the 9 questions indexed next to the correct answers. 
question_answer = [
    (question_prompts[0], 'b'),
    (question_prompts[1], 'c'),
    (question_prompts[2], 'b'),
    (question_prompts[3], 'c'),
    (question_prompts[4], 'b'),
    (question_prompts[5], 'a'),
    (question_prompts[6], 'a'),
    (question_prompts[7], 'c'),
    (question_prompts[8], 'b'),
]

#this is what i used to call the random shuffle function that imported earlier. 
shuffle(question_answer)

#this function is what I am using to run the game and the variable named score is increasing by 10 if the answer is correct or staying the same if the answer is wrong via the if statement. 
def run_game(question_answer):
    score = 0
    for result in question_answer:
        answer = input(result[0])
        if answer == result[1]:
            score+=10
            print('Congrats, + You got 10 points!!')
        else:
            print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
        print('Current Score =', score)
        print('\n') 

#while loop with if, elif and else introuduced to make sure you only answer yes or no to being ready to play the game. 
while True:
    Prompt1 = input('\n''Are you happy to play the game with those rules? Please Enter yes or no: ')
    if Prompt1 == 'yes':
        run_game(question_answer)
        break
    elif Prompt1 == 'no':
        print('Sorry to see you go ' + name + '! We hope to see you next time!!')
        break
    else:
        print('sorry, you can only answer yes or no... please try again by answering yes or no') #for an answer that wouldn't be yes or no

#same loop and if statement but this time to ask the user if they would like to play again 
while True:
    Prompt2 = input('\n''Would you like to play again? Please Enter yes or no: ') 
    if Prompt2 == 'yes':
        run_game(question_answer)
        break
    elif Prompt2 == 'no':
        print('Sorry to see you go ' + name + '! We hope to see you next time!!')
        break
    else:
        print('Sorry, you can only answer yes or no... please try again by answering yes or no') #for an answer that wouldn't be yes or no

#tried to use sample quiz example to catch errors with this code but can't figure out the indentation issue

'''elif question_answer != 'a','b','c':
        print('You must enter only a, b or c to answer the questions.')'''
