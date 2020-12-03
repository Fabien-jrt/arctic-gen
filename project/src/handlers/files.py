from sys import exit
from typing import List, Dict


class FilesHandler:
    """Handel the word lists

    :param first_path: the path of the first word list
    :type first_path: str
    :param second_path: the path of the second word list
    :type second_path: str
    """

    def __init__(self, first_path: str, second_path: str):
        self.first_path = first_path
        self.second_path = second_path

    def get_content(self) -> Dict[str, str]:
        """Get the content of the word lists

        :returns: the content of the first and second word list
        :rtype: Dict[str,str]
        """
        try:
            first_content = self.get_word_list_content(self.first_path)
            second_content = self.get_word_list_content(self.second_path)
        except FileNotFoundError as error:
            print(str(error))
            print("A word list is missing or a path is misspelled in 'config.ini'")
            exit(error.errno)

        return {"first": first_content, "second": second_content}

    @staticmethod
    def get_word_list_content(file_path: str) -> List:
        """Get the content of the given word list

        :param file_path: the path to the word list
        :type file_path: str
        :returns: the content of the word list
        :rtype: List
        """
        FIRST_ITEM: int = 0
        content: List = []

        with open(file_path) as file:
            for line in file:
                if line.startswith('#'):
                    pass
                elif line.startswith('\n'):
                    pass
                else:
                    content.append(line.split().pop(FIRST_ITEM))
        return content
