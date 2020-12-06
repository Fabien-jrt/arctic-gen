# Arctic-gen
Arctic-gen is a username generator written in Python.

By default, it allows you to generate a username from 2 distinct lists.  
The first contains adjectives and the second contains nouns. This helps create meaningful usernames.

Feel free to modify the content of the lists or to create new ones. 
As an example, you could use a list of verbs instead of adjectives.

**Please, do not use this program to automate the account creation process.**

## Install 
At the moment, you need to clone this repository 
or download the source code.

## Usage
`arctic.py` generate a username with the default values and print it in the console.

Use `arctic.py --case <case>` to change the case.  
The available cases are as follows: 
- `camel` is the default case. Output: `camelCased`
- `pascal`, output: `PascalCased`
- `name`, output: `Name Cased`
- `insert` is used to insert a sequence between the two words. By default: `_`, output: `insert_case`
- `none`, output: `nonecased`

In addition, you can add a custom prefix and a custom suffix.  
Simply add `--prefix <prefix>` and/or `--suffix <suffix>`. Output: `<prefix><username><suffix>`.

See `arctic.py --help` to print the usage in the console.

## Config 
You can change the word lists paths in `config.ini`.

### Word lists
You can modifiy, add and remove word lists.
By default, word lists are stored under `words/`.

For the moment, you **must** have at least two word lists and reference their path in `config.ini` before running the program.

## License
Under GNU GPL v2.0. See [`LICENSE`](./LICENSE).

## The whys 
### Why did you create Arctic?
It was created because I was tired of looking for username
 with each registration that asked for a new one.
 
 It was also an opportunity to create a side project to show and improve my development skills.
 
 ### Why Arctic?
 Why not? It was created in winter.
