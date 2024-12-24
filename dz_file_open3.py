
# DZ 29
class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.args = 'args.txt'
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        slova = []
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line.lower()
                    for pp in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        if pp in line:
                            line = line.replace(pp, '')
                    for st in line.split():
                        slova.append(st.lower())
                    all_words.update({i:slova})
            return all_words

    def find(self, word):
        find_list = {}
        x = 1
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() == i.lower():
                    find_list = {name:x}
                    return find_list
                else:
                    x += 1

    def count(self, word):
        count_list = {}
        x = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() == i.lower():
                    x += 1
            count_list = {name:x}
            return count_list


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего