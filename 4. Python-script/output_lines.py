
def output_lines(filename, word):
    with open(filename) as file:
        lines = list(map(str.strip, file.readlines()))

    for line in lines:
        if line.find(word) != -1:
            print(line)

filename = input()
target_word = input()
output_lines(filename, target_word)
    