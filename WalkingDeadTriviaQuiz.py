### This code outputs a Trivia Quiz based on the AMC's Walking Dead TV show. For each question, there are 5 options. Only one option is correct.
### This code uses classes, loops, if and else statements as well as the random function to run the Trivia Quiz. 

import sys
import random

def Greet(hello):
    name = raw_input("What\'s your name?: ")  # function greets the Trivia master before asking questions.
    return hello + name + "!"
print Greet("Welcome to the Walking Dead Trivia Quiz, ")
                    
class Question(object):
    def __init__(self, question, answer, options):   # function takes the parameters (objects) and constructs a class out of them.
        self.question = question
        self.answer = answer
        self.options = options

    def ask(self):                                    # function will ask the Trivia master the question and print the following options to choose from.
        print self.question + "?"
        for n, option in enumerate(self.options):
            print "%d) %s" % (n + 1, option)

        response = int(sys.stdin.readline().strip())   # the integers next to each question is the input for the answer. The correct integer will print 
        if response == self.answer:                    # "CORRECT!" or "INCORRECT" if the integer inputed by the Trivia master does not match the answer in the class. 
            print "CORRECT!"
        else:
            print "INCORRECT!"
    
questions = [
    Question("What was the name of Carol's daughter", 3, ["Sydney", "Sarah", "Sophia", "Sophie", "Sherry"]),
    Question("Who did Carl shoot to prevent him/her from turning into a walker", 1, ["Lori", "Daryl", "T-Dog", "Hershel", "Carol"]),
    Question("Who was handcuffed to the roof of a building", 5, ["Rick", "Glenn", "Daryl", "No one", "Merle"]),
    Question("What was the name of the community Nolan's family lived in", 5, ["The Shire", "Shirewilt Estates", "Stark Estates", "Nolan and his family didn't live in a community", "Trick question! Nolan doesn't exist!"]),
    Question("What kind of drunk is Beth", 3, ["A happy drunk", "A angry drunk", "An unhappy drunk", "A scary drunk", "A funny drunk"]),
    Question("What occupation did Hershel have before the inevitable zombie apocalypse", 3, ["A southern mall Santa Clause", "A horse doctor", "A veterinarian", "Didn't have one", "Love Doctor"]),
    Question("What was the number on Shane's chain", 2, ["23", "22", "13", "15", "46"]),
    Question("Who manages to sucessfully escape Grady Memorial Hospital", 2, ["Beth and Noah", "Noah", "Beth", "No one manages to escape", "Dawn"]),
    Question("Who said, 'I lied, I am not a scientist.'", 1, ["Eugene Porter", "Milton Mamet", "Edwin Jenner", "Negan", "Hershel"]),
    Question("Who is Lucille", 1, ["Negan's bitchin' baseball bat", "Negan's wife", "One of Negan's wives", "A figament of Negan's imagination", "Negan's girlfriend"]),
    Question("Who kills Otis", 2, ["Rick", "Shane", "Daryl", "Carl", "Dale"]),
    Question("Who evolves from being a coward to a fearless team player?", 4, ["Nicolas", "Father Gaberiel", "Fat Joey", "Eugene", "Merle"]),
    Question("What was the name of Michonne's son?", 3, ["Andy", "Andrew", "Andre", "Aiden", "Anthony"]),
    Question("Does Noah die and if so, how and by who", 1, ["He is eaten alive by Walkers and it's Nicolas's fault", "He doesn't die", "Crushed by a revolving door", "He's shot by Dawn", "He's shot by Beth"]),
    Question("Beth is kidnapped; where is she held hostage", 2, ["Grady Hospital", "Grady Memorial Hospital", "Georgia's Bestest Hospital", "Northside Hospital", "St. Sarah Church"]),
    Question("Who is the Jesus Archtype in the show", 3, ["Rick", "Daryl", "Glenn", "Merle", "Dale"]),
    Question("Why do Rick and friends refer to the undead as Walkers instead of Zombies", 3, ["The word zombie is stupid", "Walker is a better term to define the undead", "Rick and friends live in a parallel universe of ours where Zombie pop culture never existed", "They do refer to them as zombies", "They use both Walker and Zombies to refer to the undead"])
    ]

random.shuffle(questions)    # Outputs the questions randomly, each time the quiz is taken.

for question in questions:   #loops through the question for the options and the answer to the question.
    question.ask()

