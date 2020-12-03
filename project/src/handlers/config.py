import configparser
from sys import exit
from typing import Dict


class ConfigHandler:
    """Handel the configuration file

    :param filename: the name of the configuration file
    :type filename: str
    """

    def __init__(self, filename: str):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def load(self) -> Dict[str, str]:
        """Load the configuration file

        :returns: the path of the first and second word list
        :rtype: Dict[str,str]
        """
        try:
            first = self.config["paths"]["first"]
            second = self.config["paths"]["second"]
        except KeyError as error:
            print(str(error) + " is missing in config.ini")
            exit(1)

        return {"first_path": first, "second_path": second}
