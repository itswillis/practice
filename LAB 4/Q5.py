def sum_of_scores(scores):
    # try converting the scores to int first
    a_list = []
    for score in scores:
        try:
            score = int(score)
            if score > 0 and score < 10:
                a_list.append(score)
        except ValueError:
            return sum(a_list) # up to the point of ValueError - don't pass this 
    return sum(a_list)
    
my_list = [1, 2, 13, 4, "two", 2, 9]
print(sum_of_scores(my_list))

print(sum_of_scores(['NA']))