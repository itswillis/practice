def sum_of_scores_continue(scores):
    a_list = []
    for score in scores: 
        try: 
            score = int(score)
            if score > 0 and score < 10:
                a_list.append(score)
        except ValueError:
            pass 
    return sum(a_list)

my_list = [-1, 0, 5, 2, 'ten', 35, 45, 9, 20]
print(sum_of_scores_continue(my_list))
print(sum_of_scores_continue([-1, 0, 10, 20, 'ten', 35, 45, 105, 20]))

my_list = [1, 2, 3, 4, "two", 2]
print(sum_of_scores_continue(my_list))