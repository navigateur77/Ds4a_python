"""
For this project, you will have to build an English-to-Lolcat translation engine
It is able to read in a plain-text file in English (.txt extension), translate it,
and produce another text file in Lolcat, regardless of the length of the text.

Please replace the name of "english.txt" by your text name to translate.
Also you can choose and output file name.
"""
import json


with open('english.txt', 'r') as englishFile, open('tranzlashun.json', 'r') as jsonFile:

    with open('lolcat.txt', 'w') as lolcatFile:
        jsondata = json.load(jsonFile)
        for line in englishFile:
            words = line.lower().strip('"').split()
            for word in words:
                if word in jsondata:
                    lolcatFile.write(jsondata[word])
                elif word not in jsondata:
                    lolcatFile.write(word)
                elif word in "\"'.,:;?!' '":
                    lolcatFile.write(word)
                else:
                    lolcatFile.write(word)
                lolcatFile.write(' ')
            lolcatFile.write('\n')

