from random import randrange
from typing import List, Dict


class WordGenerator:
    """Generate two random words from the word lists

    :param first_word_list: the first word list to generate the first word
    :type first_word_list: List
    :param second_word_list: the second word list use to generate the second word
    :type second_word_list: List
    """

    def __init__(self, first_word_list: List, second_word_list: List):
        self.fist_word_list = first_word_list
        self.second_word_list = second_word_list
        self.first_length = len(first_word_list)
        self.second_length = len(second_word_list)

    def generate(self) -> Dict[str, str]:
        """Get one random word per list

        :returns: the first and second word randomly selected
        :rtype: Dict[str, str]
        """

        rand_first = randrange(self.first_length)
        rand_second = randrange(self.second_length)

        first_word = self.fist_word_list[rand_first]
        second_word = self.second_word_list[rand_second]

        return {"first": first_word, "second": second_word}
