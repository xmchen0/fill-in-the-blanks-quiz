# Udacity IPNP Code Your Own Quiz

# Blanks
blanks = ["__1__", "__2__", "__3__", "__4__"]

# Quizes 
easy_quiz = """\nThe paragraph reads:\n__1__ (1412-1431) is a __2__ heroine and Roman Catholic saint. Born in obscurity to a peasant family, she travelled to the uncrowned Dauphin of __3__, advising him to reclaim his __2__ throne and defeat the __4__."""
medium_quiz = """\nThe paragraph reads:\nUnder __1__ de Ponthieu, the French were without direction and without a real __2__. When Joan of Arc came to the court she made a strong impression on __1__ with her passion and conviction. It is quite remarkable that this __3__-year-old peasant girl was, as a consequence, given control over an __4__ and allowed to lead them into battle."""
hard_quiz = """\nThe paragraph reads:\nIt is said that over 10,000 people came to see her execution by __1__. Afterwards, her ashes were scattered in the Seine. One legend tells how her __2__ remained unaffected by the __3__. \nTwenty-six years later the English were finally driven from Rouen and in a later inquest she was declared to be officially innocent and was officially designated to be a martyr. She was canonised a __4__ in 1920 and remains the patron __4__ of France."""

# Answers
easy_answers = ["Joan of Arc", "French", "France", "English"]
medium_answers = ["Charles", "leader", "17", "army"]
hard_answers = ["burning", "heart", "fire", "saint"]

# Greetings
name = input("\nHello, please enter your name: ")
print ("\nWelcome, " + name + "!" + " Take this quiz to learn about Joan of Arc's biography! \n**excerpts from biographyonline.net** ")
print ("\nGood luck and have fun!")

# Functions
def choose_level(user_prompt):
    """Purpose: to prompt user to select level of difficulty
        Input: user's choice of level
        Output: the quiz and answers corresponding to the level chosen"""
    if user_prompt == "easy":
        return easy_quiz, easy_answers
    elif user_prompt == "medium":
        return medium_quiz, medium_answers
    elif user_prompt == "hard":
        return hard_quiz, hard_answers
        
    choose_level(user_prompt)

def check_answer(choice, answer, answer_index):
    """Purpose: to check whether user's answer is correct or not
        Input: user's answer and correct answers 
        Output: return correct answer if matches with the answer index in the quiz and displays message""" 
    if choice == answer[answer_index]:
        return "Correct"
    else:
        print ("That's incorrect. Try again.")

def game_repeat():
    """Purpose: to prompt user to retake the quiz
        Input: user's decision to play on by typing in Y for 'yes' or N for 'no'
        Output: depending on the input, game will restart from the beginning to pick a level of difficulty or exit the game"""
    user_answer = input("\nWell done, " + name + "!" + " Do you want to play again? (Y/N): ")
    while user_answer not in ["Y", "N"]:
        user_answer = input("\nOps! That is not a proper option. Please choose from Y/N: ")
    if user_answer == "Y":
        play_game()
    else:
        print ("\nThanks for playing! Goodbye.")

def play_game():
    """Purpose: to execute the whole game 
        Input: None
        Output: displays the whole game"""
    user_prompt = input("\nWhen you're ready select the level of difficulty \nPossible choices include easy/medium/hard \nType here: ")
    while user_prompt not in ["easy", "medium", "hard"]:
        user_prompt = input("\nOps! That is not a proper option. Please choose from easy/medium/hard \nType here: ")
    quiz, answer_list = choose_level(user_prompt)
    print (quiz)
    blanks_index = 0
    answer_index = 0
    while blanks_index < len(blanks):
        user_input = input("\nWhat's your answer for: " + blanks[blanks_index] + "? \nType here: ")
        if check_answer(user_input, answer_list, answer_index) == "Correct":
            print ("That's CORRECT!")
            quiz = quiz.replace(blanks[blanks_index],user_input)
            print (quiz)
            blanks_index = blanks_index+1
            answer_index = answer_index+1
    game_repeat()
            
# Run Quiz
play_game()

