from string import ascii_uppercase



class Alphabet():
    def __init__(self, lang, letters):
        self.lang = lang 
        self.letters = letters 
    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', list(ascii_uppercase))
    __letters_num = 26
    def is_en_letters(self, let):
        if let.upper() in self.letters:
            return True
        else:
            return False
    def get_letter_num(self):
        return EngAlphabet.__letters_num
    @staticmethod
    def get_text():
        return "HELLO WORLD"
    

a = EngAlphabet()
print(a.lang)
print(a.letters) 
print(a.get_letter_num())
print(a.is_en_letters('а'))
print(EngAlphabet.get_text())