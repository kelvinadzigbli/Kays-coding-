#I have printed the introduction into the game and whitespaces just to improve the readability.
print('Code Author: Kelvin Adzigbli.')
print('This is an interactive quiz game called Python Trivia :). It was created for the event demo for entertainment purposes.')
print('Copyright© ownership belongs to Kelvin Adzigbli. Copyright infringments will be legally handled.')
print('')
print('Please enter your name in the shell as follows: name(your name). <<< Please make sure your name is inbetween apostrophies')
print('')
#I created a function for the user to enter their name and told them to input it in the shell 
def name(name):

    print('Welcome to the world of Python Trivia, '+ name + '! :)')
#These are the rules of the game       
print('The rules are:'
      ' 1). This is a multiple choice game in which you must choose one of either a, b or c.'
      ' 2). There are 9 questions in total.'
      ' 3). You get 10 points for the right answer and 0 points for the wrong one.')
  
#This is for the user to conform they are happy to go ahead with the rules, I have created an if, else and elif statement for the various possible responses. 
Prompt1 = input('Are you happy to play the game with those rules? Please Enter yes or no: ')

if prompt1 == 'yes':
    print('What was the Turkish city of Istanbul called before 1930? Answer A B or C')
if prompt1 == 'no':
    print('Sorry to see you go!' + name)
else:
    print(input('sorry, you can only answer yes or no... please try again by answering yes or no')) #for an answer that wouldn't be yes or 
#below is the import random function so that the questions are randomised. 
import random

question2 = input('From which US city do the band The Killers originate? /na. California /nb. Las Vegas /nc. New York /nAnswer: ')
if answer2 == 'b' or answer2 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)
    
question3 = input('Name the Coffee shop in US sitcom Friends? /na. Zoo Park /nb. Park Royal /nc. Central Perk /nAnswer: ')
if answer3 == 'c' or answer3 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)
    
question4 = input('How many human players are there on each side in a polo match? /na. Eight /nb. Four /nc. Five /nAnswer: ')
if answer4 == 'b' or answer4 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)

question5 = input('In what year did Tony Blair become British Prime Minister? /na. 1998 /nb. 1997 /nc. 1995 /nAnswer: ')
if answer5 == 'c' or answer5 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)
    
question6 = input('How many times has England won the men’s football World Cup? /na. Twice /nb. Once /nc. Five times /nAnswer: ')
if answer6 == 'b' or answer6 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)

question7 = input('What is the capital of New Zealand? /na. Wellington /nb. Sydney /nc. Brisbane /nAnswer: ')
if answer7 == 'a' or answer7 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)


question8 = input('Street artist Banksy is originally associated with which British city? /na. Bristol /nb. Manchester /nc. Birmingham /nAnswer: ')
if answer8 == 'a' or answer8 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)


question9 = input('From what grain is the Japanese spirit Sake made? /na. Flour /nb. Wheat /nc. Rice /nAnswer: ')
if answer9 == 'c' or answer9 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)


question10 = input('In which part of your body would you find the cruciate ligament? /na. Ankle /nb. Knee /nc. Elbow /nAnswer: ')
if answer10 == 'b' or answer10 == 'Las Vegas':
    Score+=10
    print('Congrats, + 'name' + You got 10 points!!')
else
    print('Aww, what a shame. That wasn’t the correct answer. You got 0 points.')
    print('score', score)
