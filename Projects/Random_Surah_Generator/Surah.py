class Surah:
    def __init__(self, num, name_eng, name_ar):
        self.num = num
        self.name_eng = name_eng
        self.name_ar = name_ar

    def __eq__(self, other):
        if isinstance(other, Surah):
            return self.num == other.num and self.name_eng == other.name_eng and self.name_ar == other.name_ar
        return False
    
    # Getter for number
    def get_num(self):
        return self.num

    # Getter for English name
    def get_name_eng(self):
        return self.name_eng

    # Getter for Arabic name
    def get_name_ar(self):
        return self.name_ar
    
    def __gt__(self, other):
        if isinstance(other, Surah):
            if self.num > other.get_num():
                return True
            else:
                return False
        else:
            return None
        
    def to_dict(self):
        return {
            "num": self.num,
            "name_eng": self.name_eng,
            "name_ar": self.name_ar
        }

    # Class method to create an object from a dictionary
    def from_dict(data):
        return Surah(data["num"], data["name_eng"], data["name_ar"])