

def ask_question(question, function_to_handle_question):
   return function_to_handle_question(question) 

def now_handle_the_question(question_asked):
    options = {
        "name_of_person": "John Doe"
    }
    return f"Q: {question_asked}? || R: Your name is {options["name_of_person"]}."