class CommonLetters: 
    def __init__(self, first_word = "first", second_word = "second"):
        self.first_word = first_word
        self.second_word = second_word
        self.common_letters = []

        for letter in first_word: 
            if letter in second_word:
                if letter not in self.common_letters:
                    self.common_letters.append(letter)
        self.common_letters = sorted(self.common_letters)
    
    def __str__(self):
        common = ''.join(str(i) for i in self.common_letters)
        return (f"{self.first_word}, {self.second_word} ({common})")



object1 = CommonLetters('lessons', 'learn')
object2 = CommonLetters('experience', 'effort')
print(object1)
print(object2)