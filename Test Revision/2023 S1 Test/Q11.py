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

    def set_first_word(self, first_word):
        self.first_word = first_word

        self.common_letters = []

        for letter in first_word: 
            if letter in self.second_word:
                if letter not in self.common_letters:
                    self.common_letters.append(letter)
        self.common_letters = sorted(self.common_letters)

    def set_second_word(self, second_word):
        self.second_word = second_word

        self.common_letters = []
        for letter in self.first_word: 
            if letter in second_word:
                if letter not in self.common_letters:
                    self.common_letters.append(letter)
        self.common_letters = sorted(self.common_letters)

    def get_common_letters(self):
        return (''.join(str(i) for i in self.common_letters))
    
    def __str__(self):
        common = ''.join(str(i) for i in self.common_letters)
        return (f"{self.first_word}, {self.second_word} ({common})")
    
object1 = CommonLetters()
object2 = CommonLetters('hello', 'world')
print(object1)
print(object2)
object1.set_first_word('hello')
print(object1)
object2.set_second_word('bubble')
print(object2)
object3 = CommonLetters('cat', 'banana')
print(object3)
print(CommonLetters('cat', 'dog'))
data = object2.get_common_letters()
print(type(data))
print(data)