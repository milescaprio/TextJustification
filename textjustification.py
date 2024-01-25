def justify(words, maxWidth):
    strings = []
    while len(words) != 0:
        currentlineremaining = maxWidth
        lettersinuse = 0
        wordstouse = []
        string = ""
        while len(words) != 0 and currentlineremaining >= len(words[0]):
            wordstouse.append(words[0])
            currentlineremaining -= len(words[0]) + 1
            lettersinuse += len(words[0])
            words.pop(0)
        spaces = maxWidth - lettersinuse
        sections = len(wordstouse) - 1
        if sections == 0:
            sections = 1
        spacearray = [spaces // sections] * sections
        spaces = spaces % sections
        spacearray.append(0)
        for i in range(spaces):
            spacearray[i] += 1
        j = 0
        while len(wordstouse) != 0:
            string += wordstouse[0] + " " * spacearray[0]
            spacearray.pop(0)
            wordstouse.pop(0)
        strings.append(string)
    print(strings)


justify(["This", "is", "an", "example", "1234789000123" "of", "text", "justification."], 16)

        

        