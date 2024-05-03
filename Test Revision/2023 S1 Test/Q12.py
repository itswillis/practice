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

class CommonLettersList:
    def __init__(self):
        self.items = []

    def add_item(self, common_letters):
        self.items.append(common_letters)

    def get_union(self):
        union_list = []
        for item in self.items:
            union = item.get_common_letters()
            for letter in union:
                if letter not in union_list:
                    union_list.append(letter)
        return sorted(union_list)

    def __str__(self):
        common = '\n'.join(str(item) for item in self.items)
        return (common) 


object1 = CommonLetters()
object2 = CommonLetters('hello', 'world')
data = CommonLettersList()
data.add_item(object1)
data.add_item(object2)
print(data)
print(data.get_union())