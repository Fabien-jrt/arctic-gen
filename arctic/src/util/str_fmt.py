class StringFormatter:
    """Utility class to format and concatenate two words in a given case"""

    @staticmethod
    def camel_case(first: str, second: str) -> str:
        """Concatenate fist and second in camelCase style

        :param first: a word
        :type first: str
        :param second: a second word
        :type second: str
        :return: first concatenated to second with second capitalized
        :rtype: str
        """
        return first + second.capitalize()

    @staticmethod
    def pascal_case(first: str, second: str) -> str:
        """Concatenate fist and second in PascalCase style

        :param first: a word
        :type first: str
        :param second: a second word
        :type second: str
        :return: first concatenated with second with both of them capitalized
        :rtype: str
        """
        return first.capitalize() + second.capitalize()

    @staticmethod
    def name_case(first: str, second: str) -> str:
        return first.capitalize() + " " + second.capitalize()

    @staticmethod
    def insert_between(first: str, second: str, sequence: str = "_") -> str:
        """Concatenate fist and second with a sequence between them

        :param first: a word
        :type first: str
        :param second: a second word
        :type second: str
        :param sequence: a string to separate the first and second word
        :type sequence: str
        :return: first concatenated with sequence and second
        :rtype: str
        """
        return first + sequence + second
