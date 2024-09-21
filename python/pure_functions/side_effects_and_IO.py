
def get_file():
    with open('resources/file.txt') as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_lines(text):
    return len(text.split('\n'))