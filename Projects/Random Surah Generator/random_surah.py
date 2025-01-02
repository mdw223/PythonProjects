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


from Surah import Surah # import Surah class from Surah.py file

from Juz import Juz # import Juz class from Juz.py

    

# List of Juz objects with flipped start and end Surah numbers and no Ayah numbers
juz_list = [
    Juz(1, "Alif Lam Meem", "الم", 2, 1),
    Juz(2, "Sayaqool", "سيقول", 2, 2),
    Juz(3, "Tilkal Rusul", "تلك الرسل", 3, 2),
    Juz(4, "Lan Tana Loo", "لن تنالوا", 4, 3),
    Juz(5, "Wal Mohsanat", "والمحصنات", 4, 4),
    Juz(6, "La Yuhibbullah", "لا يحب الله", 5, 4),
    Juz(7, "Wa Iza Samiu", "وإذا سمعوا", 6, 5),
    Juz(8, "Wa Lau Annana", "ولو أننا", 7, 6),
    Juz(9, "Qalal Malao", "قال الملأ", 8, 7),
    Juz(10, "Wa A'lamu", "واعلموا", 9, 8),
    Juz(11, "Yatazeroon", "يعتذرون", 11, 9),
    Juz(12, "Wa Mamin Da'abat", "وما من دابة", 12, 11),
    Juz(13, "Wa Ma Ubrioo", "وما أبرئ", 14, 12),
    Juz(14, "Rubama", "ربما", 16, 15),
    Juz(15, "Subhanallazi", "سبحان الذي", 18, 17),
    Juz(16, "Qal Alam", "قال ألم", 20, 18),
    Juz(17, "Aqtarabo", "اقتربت", 22, 21),
    Juz(18, "Qadd Aflaha", "قد أفلح", 25, 23),
    Juz(19, "Wa Qalallazina", "وقال الذين", 27, 25),
    Juz(20, "A'man Khalaq", "أمن خلق", 29, 27),
    Juz(21, "Utlu Ma Oohi", "اتل ما أوحي", 33, 29),
    Juz(22, "Wa Manyaqnut", "ومن يقنت", 36, 33),
    Juz(23, "Wa Mali", "وما لي", 39, 36),
    Juz(24, "Faman Azlam", "فمن أظلم", 41, 39),
    Juz(25, "Ilaahe Yuruddu", "إليه يرد", 45, 41),
    Juz(26, "Ha'a Meem", "حم", 51, 46),
    Juz(27, "Qala Fama Khatbukum", "قال فما خطبكم", 57, 51),
    Juz(28, "Qadd Aflaha", "قد أفلح", 66, 58),
    Juz(29, "Tabarakalladhi", "تبارك الذي", 77, 67),
    Juz(30, "Amma Yatasa'aloon", "عم يتساءلون", 114, 78)
]

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

# randomly select two surahs in order and display
import random
from tracemalloc import start

# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

from FormatException import FormatException # import my custom exception class
#using from... fixed the type error, it didn't recognize the class FormatException

''' start refers ot the smallest surah number and end refers to the largest surah number to choose from
split the range into two and choose a random surah from each half
it checks if the surahs are the same number
'''
def choose_surah_num(start, end):
    if start == end:
        return [start, end]
    elif start + 1 == end: # like if start == 1 and end == 2
        return [start, end]
    else: # like if start == 1 and end == 3, then 1 + 3 = 4 / 2 = 2 
        mid = int((start + end) / 2)
        return [random.randint(start, mid), random.randint(mid + 1, end)]

def choose_surahs(start_juz, end_juz):
    #gets the surah range based on given juz start and end 
    s = juz_list[start_juz].get_start_surah() 
    e = juz_list[end_juz].get_end_surah()

    if s > e: #put in order 
        temp = s
        s = e
        e = temp
    
    print(f"Look between: the start surah number: {s}. The end surah number: {e} ")

    surah_pair = choose_surah_num(s, e)
    surah_1 = surahs[surah_pair[0] - 1] # surah list is zero indexed 
    surah_2 = surahs[surah_pair[1] - 1]
    print(f"surah_1 is {surah_1.get_num()}")
    print(f"surah_2 is {surah_2.get_num()}")
    return [surah_1, surah_2]

    

def convert(surah):
    surah_num = surah.get_num()
    surah_eng = surah.get_name_eng()
    text_to_be_reshaped = surah.get_name_ar()
    reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
    surah = reshaped_text[::-1] # slice backwards  
    return f"{str(surah_num)} {surah_eng} {surah}"   

def user():
        cont = True
        while cont:
            #map iterates through the parts of the string and initializes them for us 
            start_juz = 1
            end_juz = 30
            try:
                user_input = input("Choose a range of juz to choose from (1-30) or 'q' to quit: ")
                if user_input == 'q':
                    cont = False
                    break
                elif user_input.isdigit() and int(user_input) >= 1 and int(user_input) <= 30:
                    # if they input a single number like 1 then only choose from juz 1  
                    start_juz = int(user_input)
                    end_juz = int(user_input)
                else:
                    start_juz, end_juz = map(int, user_input.split('-'))
                    if (start_juz > end_juz) or (start_juz < 1) or (start_juz > 30) or (end_juz < 1) or (end_juz > 30):
                        raise FormatException()
            
            except FormatException as e: # if in wrong format, will come here 
                print(e)
                continue
            except:
                print("Incorrect format. An example of a correct format is '5-10'.")
                # pass statement in Python does not skip to the next iteration of a loop. Instead, it is a null operation; when it is executed, nothing happens.
                continue # If you want to skip to the next iteration of a loop, you should use the continue statement.

            surah_pair = choose_surahs(start_juz - 1, end_juz - 1) # the list is 0 indexed
            
            if surah_pair[0] == surah_pair[1]:
                print(f'Read from surah {convert(surah_pair[0])}')  
            else:
                print(f'Read surahs {convert(surah_pair[0])} and {convert(surah_pair[1])}')  
        

        
user()


