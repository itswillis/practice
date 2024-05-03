class WordScore:
    def __init__(self, word=""): #assume lowercase letters
        valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        score = 0
        for letter in word:
            score += valid_letters.index(letter)
        self.score = score
        self.word = word

    def __str__(self):
        return f"{self.word}({self.score})"
    
    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.score == other.score and self.word == other.word
    
    def __lt__(self, other):
        if self.score == other.score:
            if self.word < other.word:
                return True
        return self.score < other.score
    
def selection_sort(word_scores):
    for pass_num in range(len(word_scores)-1, 0, -1):
        position_largest = 0
        for i in range(1, pass_num):
            if word_scores[i].score > word_scores[position_largest].score:
                position_largest = i
        if word_scores[position_largest].score > word_scores[pass_num].score:
            word_scores[position_largest], word_scores[pass_num] = word_scores[pass_num], word_scores[position_largest]
        print_wordscores(word_scores)

def print_wordscores(word_scores):
    print_str = ""
    for word_score in word_scores:
        print_str += str(word_score) + " "
    print(print_str.strip())

import math 

def binary_search(word_scores, search_score):
    low = 0
    high = len(word_scores) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_score = word_scores[mid].score

        if mid_score == search_score:
            return word_scores[mid].score
        elif mid_score < search_score:
            low = mid + 1
        else:
            high = mid - 1
    return None




a_list = [WordScore('code'), WordScore('rain'), WordScore('days'), WordScore('object'), WordScore('score'), WordScore('trees'), WordScore('everything')]
for element in a_list:
    print(element, end=' ')
print()
print(binary_search(a_list, 15))
print(binary_search(a_list, 68))
print(binary_search(a_list, 55))
print(binary_search(a_list, 38))
result = binary_search(a_list, 45)
print(result, type(result))