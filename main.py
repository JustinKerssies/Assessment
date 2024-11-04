from pathlib import Path
from operator import itemgetter
from re import search, split
import os
import click
from baseclass import TextProcessor

@click.command()
@click.argument('filename', required= True)
@click.option('--load', help="load a file into the appended file, making it possible to make changes")
@click.option('--display',help='displays a new file within the terminal', required=False)
@click.option('--search', help='searches for given word and returns begin and end location of said words')
@click.option('--replace', help='replaces a given word with another words within the text')
@click.option('--wordfrequency', help='returns a list of the most used words')
@click.option('--palindromes', help='returns all palindromes appearing in the document')
@click.option('--emailsearch', help='returns all emails found in the document')
@click.option('--decoder',help='returns a decoded msg based on a Ceasers cypher')
@click.option('--save', help='saves any changes made to the document')
@click.option('--reset', help='resets all changes made back to its original version')


def cli(filename, load, display, replace, search, wordfrequency, palindromes, emailsearch, decoder, save, reset):
    app = MyTextProcessor()
    path = os.path.join(os.path.dirname(__file__), filename)
    app.load(path)
    if display:
        app.display()
    elif load:
        app.reset()
    elif search:
        app.search()
    elif replace:
        input = str(click.prompt('What word do u want to replace'))
        output = str(click.prompt('what should the word be replaced with'))
        app.replace(input, output)
    elif wordfrequency:
        wordcount = int(click.prompt("How many words do u want to see the frequency off"), type=int)
        app.common_words(wordcount)
    elif palindromes:
        app.palindromes()
    elif emailsearch:
        app.find_email_addresses()
    elif decoder:
        shift = int(click.prompt("What is the expected shift for the Ceasars Cypher"), type=int)
        app.find_cypher(shift)
    elif save:
        app.save()
    elif reset:
        app.reset()
    pass


class NoPalindromeException(Exception):
    pass

class MyTextProcessor(TextProcessor):

    def __init__(self):
        self.file = None
        self.appendedfile = None
        self.append_path = 'temp_file.txt'

    def load(self, path: Path) -> None:
        self.file = open(path, 'r')
        self.append_path = os.path.join(os.path.dirname(__file__), self.append_path)
        click.echo(f'Load {path} into cache')

    def display(self) -> None:
        click.echo(f'Display {self.append_path} into Terminal')
        with open(self.append_path, 'r') as f:
            for lines in f.readlines():
                click.echo(lines)
    
    def search(self) -> None:
        target_word = click.prompt('Please enter the search target', type=str)
        output = []
        temp_dict = []
        indicator = 0
        for x, letter in enumerate(self.file.read()):
            if letter == target_word[indicator]:
                temp_dict.append(x)
                if indicator == len(target_word) - 1:
                    location = (temp_dict[0], temp_dict[-1] + 1)
                    output.append(location)
                    temp_dict = []
                elif indicator < len(target_word) - 1:
                    indicator += 1
                else:
                    indicator = 0
            else:
                indicator = 0
                temp_dict = []
        click.echo(output)

    def replace(self, input, output) -> None:
        temp_dict = []
        self.appendedfile = open(self.append_path, 'w')
        for line in self.file.readlines():
            if input in line:
                text = line.replace(input, output)
            else:
                text = line
            temp_dict.append(text)

        for line in temp_dict:
            self.appendedfile.write(line)

        self.file = self.appendedfile

    def common_words(self, wordcount: int) -> None:
        output = []
        temp_dict = {}
        for lines in self.file.readlines():
            for char in '.,@#:-':
                lines = lines.replace(char, ' ')
            words = lines.strip().split(' ')
            for word in words:
                if word.lower() in temp_dict:
                    temp_dict[word.lower()] += 1
                else:
                    temp_dict[word.lower()] = 1
        for words in temp_dict:
            if words != '':
                name, amount = words, temp_dict[words]
                if len(output) < wordcount:
                    output.append((name, amount))
                else:
                    output.sort(key=itemgetter(1), reverse=True)
                    if amount > output[-1][1]:
                        output[-1] = (name, amount)
                    else:
                        pass

        click.echo(output)

    def palindromes(self) -> None:
        temp_dict = []
        for lines in self.file.readlines():
            for char in '.,@#:-':
                lines = lines.replace(char, ' ')
            words = lines.strip().split(' ')
            for word in words:
                if len(word) >= 3:
                    word_indicator = 0
                    palindrome = True
                    for letter in range(int(len(word) / 2)):
                        if word[word_indicator].lower() == word[-(word_indicator + 1)].lower():
                            word_indicator += 1
                        else:
                            palindrome = False
                            break
                    if palindrome:
                        temp_dict.append(word)

        if not temp_dict:
            raise NoPalindromeException("No palindromes in the text")
        else:
            click.echo(temp_dict)

    def find_email_addresses(self):
        for lines in self.file.readlines():
            if '@' in lines:
                words = lines.strip().split(' ')
                for word in words:
                    if search(r'^[a-zA-Z]+\.?[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z.]*$', word):
                        click.echo(word)

    def find_cypher(self, shift: int):
        for lines in self.file.readlines():
            words = split(r'(\W+)', lines)
            for word in words:
                for indic, letter in enumerate(word):
                    if letter.isupper() and indic != 0:
                        output = self._ceasar(letter.lower(), shift)
                        if output:
                            click.echo(output)

    def _ceasar(self, input_letter, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for indic, letter in enumerate(alphabet):
            if input_letter == letter:
                if indic + shift <= len(alphabet):
                    return alphabet[indic + shift]
                elif indic + shift > len(alphabet):
                    return alphabet[(indic + shift) - len(alphabet)]

    def save(self, path: Path) -> None:
        temp_dict = []
        self.appendedfile = open(self.append_path, 'r')
        for lines in self.appendedfile.readlines():
            temp_dict.append(lines)

        for lines in temp_dict:
            with open(path, 'w') as f:
                f.write(lines)

    def reset(self) -> None:
        temp_dict = []
        self.appendedfile = open(self.append_path, 'w')
        for lines in self.file.readlines():
            temp_dict.append(lines)

        for lines in temp_dict:
            self.appendedfile.write(lines)



if __name__ == '__main__':
    cli()
   
