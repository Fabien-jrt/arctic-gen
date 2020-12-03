import argparse
from typing import Dict

from util.str_fmt import StringFormatter
from generator.word_gen import WordGenerator
from handlers.config import ConfigHandler
from handlers.files import FilesHandler

CONFIG_FILE: str = "../config.ini"
DEFAULT_CASE: str = "camel"
CASES: set = {"camel", "pascal", "name", "insert", "none"}


def load_config(config_file) -> Dict[str, str]:
    configuration = ConfigHandler(config_file)
    return configuration.load()


def create_file_word_gen(paths: Dict[str, str]) -> WordGenerator:
    files = FilesHandler(paths["first_path"], paths["second_path"])
    word_lists = files.get_content()

    return WordGenerator(word_lists["first"], word_lists["second"])


def create_arg_parser(default_case: str) -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        description="Generate a word composed of two random words.")

    arg_parser.add_argument("-c", "--case", type=str,
                            help="change case. Default: " + default_case,
                            choices=CASES,
                            default=default_case)
    arg_parser.add_argument("--prefix", type=str,
                            help="add a prefix to the final word")
    arg_parser.add_argument("--suffix", type=str,
                            help="add a suffix to the final word")
    arg_parser.add_argument("-q", "--quiet", help="stay silent", action="store_true")

    return arg_parser.parse_args()


args = create_arg_parser(DEFAULT_CASE)
word_gen = create_file_word_gen(load_config(CONFIG_FILE))
words = word_gen.generate()
first_word = words["first"]

second_word = words["second"]

final_word: str = ""

if args.case:
    if args.case == "camel":
        final_word = StringFormatter.camel_case(first_word, second_word)
    if args.case == "name":
        final_word = StringFormatter.name_case(first_word, second_word)
    if args.case == "pascal":
        final_word = StringFormatter.pascal_case(first_word, second_word)
    if args.case == "insert":
        final_word = StringFormatter.insert_between(first_word, second_word)
    if args.case == "none":
        final_word = first_word + second_word

if args.prefix:
    final_word = args.prefix + final_word
if args.suffix:
    final_word = final_word + args.suffix

print(final_word)
