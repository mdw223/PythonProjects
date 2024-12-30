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
        if self.num > other.get_num():
            return True
        else:
            return False

# List of Surah objects
surahs = [
    Surah(1, "Al-Fatiha", "الفاتحة"),
    Surah(2, "Al-Baqarah", "البقرة"),
    Surah(3, "Aal-E-Imran", "آل عمران"),
    Surah(4, "An-Nisa", "النساء"),
    Surah(5, "Al-Maidah", "المائدة"),
    Surah(6, "Al-An'am", "الأنعام"),
    Surah(7, "Al-A'raf", "الأعراف"),
    Surah(8, "Al-Anfal", "الأنفال"),
    Surah(9, "At-Tawbah", "التوبة"),
    Surah(10, "Yunus", "يونس"),
    Surah(11, "Hud", "هود"),
    Surah(12, "Yusuf", "يوسف"),
    Surah(13, "Ar-Ra'd", "الرعد"),
    Surah(14, "Ibrahim", "إبراهيم"),
    Surah(15, "Al-Hijr", "الحجر"),
    Surah(16, "An-Nahl", "النحل"),
    Surah(17, "Al-Isra", "الإسراء"),
    Surah(18, "Al-Kahf", "الكهف"),
    Surah(19, "Maryam", "مريم"),
    Surah(20, "Ta-Ha", "طه"),
    Surah(21, "Al-Anbiya", "الأنبياء"),
    Surah(22, "Al-Hajj", "الحج"),
    Surah(23, "Al-Mu'minun", "المؤمنون"),
    Surah(24, "An-Nur", "النور"),
    Surah(25, "Al-Furqan", "الفرقان"),
    Surah(26, "Ash-Shu'ara", "الشعراء"),
    Surah(27, "An-Naml", "النمل"),
    Surah(28, "Al-Qasas", "القصص"),
    Surah(29, "Al-Ankabut", "العنكبوت"),
    Surah(30, "Ar-Rum", "الروم"),
    Surah(31, "Luqman", "لقمان"),
    Surah(32, "As-Sajda", "السجدة"),
    Surah(33, "Al-Ahzab", "الأحزاب"),
    Surah(34, "Saba", "سبإ"),
    Surah(35, "Fatir", "فاطر"),
    Surah(36, "Ya-Sin", "يس"),
    Surah(37, "As-Saffat", "الصافات"),
    Surah(38, "Sad", "ص"),
    Surah(39, "Az-Zumar", "الزمر"),
    Surah(40, "Ghafir", "غافر"),
    Surah(41, "Fussilat", "فصلت"),
    Surah(42, "Ash-Shura", "الشورى"),
    Surah(43, "Az-Zukhruf", "الزخرف"),
    Surah(44, "Ad-Dukhan", "الدخان"),
    Surah(45, "Al-Jathiya", "الجاثية"),
    Surah(46, "Al-Ahqaf", "الأحقاف"),
    Surah(47, "Muhammad", "محمد"),
    Surah(48, "Al-Fath", "الفتح"),
    Surah(49, "Al-Hujurat", "الحجرات"),
    Surah(50, "Qaf", "ق"),
    Surah(51, "Adh-Dhariyat", "الذاريات"),
    Surah(52, "At-Tur", "الطور"),
    Surah(53, "An-Najm", "النجم"),
    Surah(54, "Al-Qamar", "القمر"),
    Surah(55, "Ar-Rahman", "الرحمن"),
    Surah(56, "Al-Waqia", "الواقعة"),
    Surah(57, "Al-Hadid", "الحديد"),
    Surah(58, "Al-Mujadila", "المجادلة"),
    Surah(59, "Al-Hashr", "الحشر"),
    Surah(60, "Al-Mumtahina", "الممتحنة"),
    Surah(61, "As-Saff", "الصف"),
    Surah(62, "Al-Jumu'a", "الجمعة"),
    Surah(63, "Al-Munafiqun", "المنافقون"),
    Surah(64, "At-Taghabun", "التغابن"),
    Surah(65, "At-Talaq", "الطلاق"),
    Surah(66, "At-Tahrim", "التحريم"),
    Surah(67, "Al-Mulk", "الملك"),
    Surah(68, "Al-Qalam", "القلم"),
    Surah(69, "Al-Haqqah", "الحاقة"),
    Surah(70, "Al-Ma'arij", "المعارج"),
    Surah(71, "Nuh", "نوح"),
    Surah(72, "Al-Jinn", "الجن"),
    Surah(73, "Al-Muzzammil", "المزمل"),
    Surah(74, "Al-Muddaththir", "المدثر"),
    Surah(75, "Al-Qiyama", "القيامة"),
    Surah(76, "Al-Insan", "الإنسان"),
    Surah(77, "Al-Mursalat", "المرسلات"),
    Surah(78, "An-Naba", "النبأ"),
    Surah(79, "An-Nazi'at", "النازعات"),
    Surah(80, "Abasa", "عبس"),
    Surah(81, "At-Takwir", "التكوير"),
    Surah(82, "Al-Infitar", "الإنفطار"),
    Surah(83, "Al-Mutaffifin", "المطففين"),
    Surah(84, "Al-Inshiqaq", "الإنشقاق"),
    Surah(85, "Al-Buruj", "البروج"),
    Surah(86, "At-Tariq", "الطارق"),
    Surah(87, "Al-Ala", "الأعلى"),
    Surah(88, "Al-Ghashiya", "الغاشية"),
    Surah(89, "Al-Fajr", "الفجر"),
    Surah(90, "Al-Balad", "البلد"),
    Surah(91, "Ash-Shams", "الشمس"),
    Surah(92, "Al-Lail", "الليل"),
    Surah(93, "Ad-Duha", "الضحى"),
    Surah(94, "Ash-Sharh", "الشرح"),
    Surah(95, "At-Tin", "التين"),
    Surah(96, "Al-Alaq", "العلق"),
    Surah(97, "Al-Qadr", "القدر"),
    Surah(98, "Al-Bayyina", "البينة"),
    Surah(99, "Az-Zalzala", "الزلزلة"),
    Surah(100, "Al-Adiyat", "العاديات"),
    Surah(101, "Al-Qaria", "القارعة"),
    Surah(102, "At-Takathur", "التكاثر"),
    Surah(103, "Al-Asr", "العصر"),
    Surah(104, "Al-Humaza", "الهمزة"),
    Surah(105, "Al-Fil", "الفيل"),
    Surah(106, "Quraish", "قريش"),
    Surah(107, "Al-Ma'un", "الماعون"),
    Surah(108, "Al-Kawthar", "الكوثر"),
    Surah(109, "Al-Kafiroon", "الكافرون"),
    Surah(110, "An-Nasr", "النصر"),
    Surah(111, "Al-Masad", "المسد"),
    Surah(112, "Al-Ikhlas", "الإخلاص"),
    Surah(113, "Al-Falaq", "الفلق"),
    Surah(114, "An-Nas", "الناس")
]


# ask user whether he wants to select only from a certain juz

''' or anywhere in the Quran...

make it so the surah with smaller number is displayed to be read first

can have favorites folder of surahs to randomly pick from 


make the UI to make it look nice and interactive

also allow for a certain ayah in that surah like kursee 

can upload it to app store

a person can have an account to save their favs

can have a recently read folder of surahs.

Can also make a salah couter app for make ups'''

# randomly select two surahs in order and display
import random

# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

def choose_surah_num():
    return random.randint(0, len(surahs))

def choose_surahs():
    surah_1 = surahs[choose_surah_num()]
    surah_2 = surahs[choose_surah_num()]
    
    return ensure(surah_1, surah_2)

''' make sure the two surahs aren't the same and order them in ascending order '''
def ensure(surah_1, surah_2):
    while surah_1.__eq__(surah_2):
        surah_2 = choose_surah_num()
    
    if surah_1.__gt__(surah_2):
        return [surah_2, surah_1]
    else:
        return [surah_1, surah_2]

def convert(surah):
    surah_num = surah.get_num()
    surah_eng = surah.get_name_eng()
    text_to_be_reshaped = surah.get_name_ar()
    reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
    surah = reshaped_text[::-1] # slice backwards  
    return f"{str(surah_num)} {surah_eng} {surah}"

def output():
    surah_pair = choose_surahs()
    
    print(f'Read surahs {convert(surah_pair[0])} and {convert(surah_pair[1])}')

output()

