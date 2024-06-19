def read_questions(filename):
    input_file = None
    try:
        input_file = open(filename, 'r')
        contents = input_file.read()

    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []

    else:
        contents = contents.split("\n")
        question_answers = []
        for line in contents:
            parts = line.split("?")
            question = parts[0] + "?"
            answer = parts[1]
            question_answers.append((question,answer))           

    finally:
        if input_file:
            input_file.close()

    return question_answers 

print(read_questions('questions3.txt'))
