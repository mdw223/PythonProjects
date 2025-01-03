class Juz:
    def __init__(self, number, name_eng, name_ar, end_surah, start_surah):
        self.number = number
        self.name_eng = name_eng
        self.name_ar = name_ar
        self.start_surah = start_surah
        self.end_surah = end_surah

    # Getter methods
    def get_number(self):
        return self.number

    def get_name_eng(self):
        return self.name_eng

    def get_name_ar(self):
        return self.name_ar

    def get_start_surah(self):
        return self.start_surah

    def get_end_surah(self):
        return self.end_surah