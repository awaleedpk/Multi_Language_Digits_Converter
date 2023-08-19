

class conDigits:

    def __init__(self):
        self.__languages = ['Bangla', 'Hindi', 'Urdu', 'Malayalam', 'Thai', 'Arabic', 'Farsi', 'Japanese', 'Korean', 'Telugu', 'Tamil', 'Greek', 'Hebrew']


        self.__banglaDigits = {
            '0': '০',
            '1': '১',
            '2': '২',
            '3': '৩',
            '4': '৪',
            '5': '৫',
            '6': '৬',
            '7': '৭',
            '8': '৮',
            '9': '৯',
        }

        self.__hindiDigits = {
            '0': '०',
            '1': '१',
            '2': '२',
            '3': '३',
            '4': '४',
            '5': '५',
            '6': '६',
            '7': '७',
            '8': '८',
            '9': '९',
        }

        self.__urduDigits = {
            '0': '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹',
        }

        self.__arabicDigits = {
            '0': '٠',
            '1': '١',
            '2': '٢',
            '3': '٣',
            '4': '٤',
            '5': '٥',
            '6': '٦',
            '7': '٧',
            '8': '٨',
            '9': '٩',
        }

        self.__farsiDigits = {
            '0': '۰',
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹',
        }
        self.__malayalamDigits = {
            '0': '൦',
            '1': '൧',
            '2': '൨',
            '3': '൩',
            '4': '൪',
            '5': '൫',
            '6': '൬',
            '7': '൭',
            '8': '൮',
            '9': '൯',
        }

        self.__thaiDigits = {
            '0': '๐',
            '1': '๑',
            '2': '๒',
            '3': '๓',
            '4': '๔',
            '5': '๕',
            '6': '๖',
            '7': '๗',
            '8': '๘',
            '9': '๙',
        }
        # Add Japanese digits
        self.__japaneseDigits = {
            '0': '〇',
            '1': '一',
            '2': '二',
            '3': '三',
            '4': '四',
            '5': '五',
            '6': '六',
            '7': '七',
            '8': '八',
            '9': '九',
        }

        # Add Korean digits
        self.__koreanDigits = {
            '0': '영',
            '1': '일',
            '2': '이',
            '3': '삼',
            '4': '사',
            '5': '오',
            '6': '육',
            '7': '칠',
            '8': '팔',
            '9': '구',
        }

        # Add Telugu digits
        self.__teluguDigits = {
            '0': '౦',
            '1': '౧',
            '2': '౨',
            '3': '౩',
            '4': '౪',
            '5': '౫',
            '6': '౬',
            '7': '౭',
            '8': '౮',
            '9': '౯',
        }

        # Add Tamil digits
        self.__tamilDigits = {
            '0': '௦',
            '1': '௧',
            '2': '௨',
            '3': '௩',
            '4': '௪',
            '5': '௫',
            '6': '௬',
            '7': '௭',
            '8': '௮',
            '9': '௯',
        }
        # Add Greek digits
        self.__greekDigits = {
            '0': '0',
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
        }

        # Add Hebrew digits
        self.__hebrewDigits = {
            '0': 'ְ',
            '1': 'ֱ',
            '2': 'ֲ',
            '3': 'ֳ',
            '4': 'ִ',
            '5': 'ֵ',
            '6': 'ֶ',
            '7': 'ַ',
            '8': 'ָ',
            '9': 'ֹ',
        }

    def to_japanese(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__japaneseDigits[q]
        return self.convertDigits

    def to_korean(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__koreanDigits[q]
        return self.convertDigits

    def to_telugu(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__teluguDigits[q]
        return self.convertDigits

    def to_tamil(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__tamilDigits[q]
        return self.convertDigits


    def to_greek(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__greekDigits[q]
        return self.convertDigits

    def to_hebrew(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__hebrewDigits[q]
        return self.convertDigits

    def to_bangla(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__banglaDigits[q]
        return self.convertDigits

    def to_hindi(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__hindiDigits[q]
        return self.convertDigits

    def to_urdu(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__urduDigits[q]
        return self.convertDigits

    def to_malayalam(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__malayalamDigits[q]
        return self.convertDigits

    def to_thai(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__thaiDigits[q]
        return self.convertDigits

    def to_arabic(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__arabicDigits[q]
        return self.convertDigits

    def to_farsi(self, digits:int):
        self.currentDigits = str(digits)
        self.convertDigits = ''
        for q in self.currentDigits:
            self.convertDigits += self.__farsiDigits[q]
        return self.convertDigits




    def available(self):
        return self.__languages

if __name__ == "__main__":
    numbers = conDigits()

    available = numbers.available() #available languages
    print(available)




    convertedBangla = numbers.to_bangla(1234567890) #convert from English to Bangla
    print(convertedBangla)

    convertedHindi = numbers.to_hindi(1234567890) #convert from English to Hindi
    print(convertedHindi)

    convertedUrdu = numbers.to_urdu(1234567890) #convert from English to Urdu
    print(convertedUrdu)

    convertedMalayalam = numbers.to_malayalam(1234567890) #convert from English to Urdu
    print(convertedMalayalam)

    convertedThai = numbers.to_thai(1234567890) #convert from English to Urdu
    print(convertedThai)

    convertedArabic = numbers.to_arabic(1234567890) # convert to Arabic
    print(convertedArabic)

    convertedFarsi = numbers.to_farsi(1234567890) # convert to Farsi
    print(convertedFarsi)
    
    convertedJapanese = numbers.to_japanese(1234567890)  # Convert to Japanese
    print(convertedJapanese)

    convertedKorean = numbers.to_korean(1234567890)  # Convert to Korean
    print(convertedKorean)

    convertedTelugu = numbers.to_telugu(1234567890)  # Convert to Telugu
    print(convertedTelugu)

    convertedTamil = numbers.to_tamil(1234567890)  # Convert to Tamil
    print(convertedTamil)

    convertedGreek = numbers.to_greek(1234567890)  # Convert to Greek
    print(convertedGreek)

    convertedHebrew = numbers.to_hebrew(1234567890)  # Convert to Hebrew
    print(convertedHebrew)