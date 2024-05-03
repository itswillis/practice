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

word_score1 = WordScore("bleats")
word_score2 = WordScore("stable")
word_score3 = WordScore("tables")
word_score4 = WordScore("beat")
print(word_score1, word_score2, word_score3, word_score4)
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score1 == word_score4)
print(word_score1 < word_score2)
print(word_score1 < word_score3)
print(word_score1 < word_score4)
print(word_score2 < word_score3)
print(word_score2 < word_score4)
print(word_score3 < word_score4)
