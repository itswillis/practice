while True: 
    input_score = int(input("Enter a score: "))

    if 0 <= input_score <= 100: 
        if input_score > 50: 
            print("PASSED")
        else: 
            print("FAILED")
        break