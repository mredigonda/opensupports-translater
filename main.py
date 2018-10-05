from googletrans import Translator
import ast

class Translater:
    def __init__(self):
        self.data = self.get_language_data('en')
    
    def get_language_description(self, data):
        return data[15:len(data)-2];

    def get_dest_language(self, lang):
        if lang == 'br':
            return 'pt'
        if lang == 'cn':
            return 'zh-cn'
        if lang == 'gr':
            return 'el'
        if lang == 'in':
            return 'hi'
        if lang == 'jp':
            return 'ja'
        return lang
    
    def get_language_data(self, lang):
        with open(lang + '.js', encoding='utf-8') as f:
            language_description = self.get_language_description(f.read())
            data = ast.literal_eval(language_description)
            return data

    def main(self):
        translator = Translator()
        #~ language_list = ['br', 'cn', 'de', 'es', 'fr', 'gr', 'in', 'it', 
            #~ 'jp', 'nl', 'pt', 'ru', 'tr']
        language_list = ['br', 'cn']
            
        for language in language_list:
            print('Translating for language: ' + language)
            dest_language = self.get_dest_language(language)
            odata = self.get_language_data(language)
            
            for key in self.data.keys():
                if not key in odata:
                    value = translator.translate(self.data[key], src='en', 
                                                 dest=dest_language).text
                    print("'"+key+"': '"+value+"',")

if __name__ == "__main__":
    translater = Translater()
    translater.main()
