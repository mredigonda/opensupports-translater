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
        data = {}
        with open(lang + '.js', encoding='utf-8') as f:
            lineno = 0
            for l in f:
                lineno += 1
                if l[0] == 'e':
                    continue # export default line
                if l[0] == '}':
                    continue # last line
                line_data = ast.literal_eval('{'+l+'}')
                if line_data.keys():
                    key = list(line_data.keys())[0]
                    data[key] = {
                        'value': line_data[key], 
                        'lineno': lineno,
                    }
        return data

    def add_property(self, lang, key, value, line):
        """Adds a property to a lang.js file.
        """
        f = open(lang + '.js', 'r')
        contents = f.readlines()
        f.close()
        
        new_line = "    '{0}': '{1}',\n".format(key, value)
        #~ print(new_line)
        contents.insert(line - 1, new_line)
        
        f = open(lang + '.js', 'w')
        contents = "".join(contents)
        f.write(contents)
        f.close()

    def main(self):
        translator = Translator()
        #~ language_list = ['br', 'cn', 'de', 'es', 'fr', 'gr', 'in', 'it', 
            #~ 'jp', 'nl', 'pt', 'ru', 'tr']
        language_list = ['br']
            
        for language in language_list:
            print('Translating for language: ' + language)
            dest_language = self.get_dest_language(language)
            odata = self.get_language_data(language)
            
            for key in self.data.keys():
                if not key in odata:
                    value = translator.translate(self.data[key]['value'], 
                        src='en', dest=dest_language).text
                    self.add_property(language, key, value, self.data[key]['lineno'])
                    print("'"+key+"': '"+value+"',")

if __name__ == "__main__":
    translater = Translater()
    translater.main()
