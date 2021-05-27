def split_words(string):
    words = []
    word_start_index = 0
    word_length = 0
    for i, char in enumerate(string):
        if char.isalpha():
            if word_length == 0:
                word_start_index = i
            word_length += 1
        else:
            word = string[word_start_index: word_start_index + word_length]
            words.append(word)
            word_length = 0

    return words


def word_cloud(string):
    cloud = dict()
    string = string.lower()
    word_list = split_words(string)
    for word in word_list:
        if word in cloud:
            cloud[word] += cloud[word]
        else:
            cloud[word] = 1
    return cloud


# print((word_cloud("After beating the eggs, Dana read the next step:"
#                   "Add milk and eggs, then add flour and sugar.")))


class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        current_word_index = 0
        current_word_length = 0

        for i, char in enumerate(input_string):
            if i == len(input_string) - 1:
                if char.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_index:current_word_length + current_word_index]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            elif char == " " or char == "\u2014":
                if current_word_length > 0:
                    current_word = input_string[current_word_index:current_word_length + current_word_index]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            elif char == ".":
                if i < len(input_string) - 1 and input_string[i + 1] == ".":
                    if current_word_length > 0:
                        current_word = input_string[current_word_index:current_word_length + current_word_index]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            elif char.isalpha() or char == "'":
                if current_word_length == 0:
                    current_word_index = i
                current_word_length += 1

            elif char == "-":
                if 0 < i and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    if current_word_length == 0:
                        current_word_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_index:current_word_length + current_word_index]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0
            elif char == ":":
                if current_word_length > 0:
                    current_word = input_string[current_word_index:current_word_length + current_word_index]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

    def add_word_to_dictionary(self, word):
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]
        else:
            self.words_to_counts[word] = 1


_words = WordCloudData("After beating the eggs, Dana read the next step:"
                       "Add milk and eggs, then add flour and sugar.")
print(_words.words_to_counts)
