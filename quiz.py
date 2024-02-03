from pyscript import input

questions = [
    {
        "question": "strint is a sequence of ______ ?",
        "option": ["character", "element","list", "none of above" ],
        "answer": "character"
    },
    
    {
        "question": "these are example of arithmetic operation exept?",
        "option": ["Addition", "Subtraction","All of the above", "Multiplication" ],
        "answer": "All of the above"
    },
     {
        "question": "python was first develope in what year?",
        "option": ["1954", "1997","1991", "1967" ],
        "answer": "1991"
    },
    {
        "question": "what is the sum of a and b of the program bellow a = 2; b = 3?",
        "option": ["5", "7","2", "3" ],
        "answer": "5"
    },
    {
        "question": "what is use to display or output code?",
        "option": ["Print()", "wrtie()","send()", "cout" ],
        "answer": "Print()"
    },
    {
        "question": "python is ____ programming language?",
        "option": ["low lovel", "High Level","Assembly", "machine code" ],
        "answer": "High Level"
    },
    {
        "question": "which of the following is not example translator?",
        "option": ["Interpreter", "Compiler","Assembler", "All of the above" ],
        "answer": "All of the above"
    },
    {
        "question": "____ interprete code line by line?",
        "option": ["Interpreter", "Compiler","Assembler", "Non of the above" ],
        "answer": "Interpreter"
    },
    {
        "question": "____ interprete code once at a time?",
        "option": ["Interpreter", "Compiler","Assembler", "Non of the above" ],
        "answer": "Compiler"
    },
    {
        "question": "who is your python lecturer?",
        "option": ["Steve", "John","Emeka", "Konwe" ],
        "answer": "Steve"
    } 
]

score = 0
print("python quiz program")
print("welcome to young prof python programming quiz \n")

for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']} \n")
    
    for j, option in enumerate(question['option']):
        print(f"{j+1}. {option} ")
  
    user_answer = input("Enter the anser (1-4):  ")
    if user_answer == question['answer'].lower():
        
        print(f"\n Correct answer \n")
        score += 1
    else:
        print(f"incorrect answer \n")
    
print(f"\nQuiz Completed\n score: {score}/{len(questions)}")
    
    