"""
Creates a file with all the data in a format similar to a diary
version 1.0
        Standard functionality, only able to write to the file,
                prints count across everything in a separate file
Marc (NessInMorse)
10 november 2020
"""
from time import time, localtime, asctime


def makeFile(filename = "diary.txt"):
        """
        Makes a count.txt and diary.txt file
        in: (optional) name for diary file
        out: a diary file and a count.txt file
        """
        try:
                infile = open("count.txt","x")
                infile.write("Your diary has 0 words")
                infile.close()
                infile = open(f"{filename}","x")
                infile.write(f"> {asctime(localtime(time()))}"+"\n\n")
                infile.close()
        except:
                print(f"{filename} will be re-used")
                infile = open(f"{filename}","a")
                infile.write(f"> {asctime(localtime(time()))}"+"\n\n")
                infile.close()


def getPage():
        """
        Gets the information to be written in the diary
        in: nothing
        out: information to write
        """
        p_text = input("What would you like to write in your "+
                     "diary today?\n")
        return p_text


def getCount(filename = "count.txt"):
        """
        Gets the current count of all the words in the current diary
        in: (optional): filename
        out: the amount of words in the diary file
        """
        infile = open(f"{filename}","r")
        data = infile.readlines()
        infile.close()
        elements = data[0].split(" ")
        print(elements[3])
        c = elements[3]
        return int(c)


def writePage(w_text = "", filename = "diary.txt",  c = 0):
        """
        Writes the information given similarly to a diary
        in: a string to be added to the diary
        out: an altered diary page
        """
        words = w_text.split(" ")
        infile = open(f"{filename}","a")
        for i in range(len(words)):
                reading_sign_volgend = findReadingSigns(words[i])
                if (c+1)%10==0 and reading_sign_volgend==False:
                        infile.write(f"{words[i]}"+"\n")
                        c = 0
                elif findReadingSigns(words[i]):
                        infile.write(f"{words[i]}"+"\n")
                        c = 0
                else:
                        infile.write(f"{words[i]} ")
                c += 1
        infile.write("\n\n"+
                     f"word count: {len(words)}"+
                     "\n\n")
        infile.close()


def writeCount(word_count, writings):
        """
        Writes the count of all the words in the coun.txt file
        in: amount of words already in the file,
                length of all the newly typed words
        out: a file containing the new amount of words in the file

        """
        c = word_count+len(writings)
        infile = open("count.txt","w")
        infile.write(f"Your diary has {c} words")
        infile.close()


def findReadingSigns(r_word):
        """
        Searches whether a reading sign is in the word
        in: a "word", perhaps with reading signs in them
        out: whether or not the word has a reading sign
        """
        items = ("," in r_word,
                 "." in r_word,
                 "!" in r_word,
                 "?" in r_word,
                 ":" in r_word,
                 ";" in r_word)
        return any(items)


def main():
        makeFile()
        writings = getPage()
        c = getCount()
        writePage(writings)
        writeCount(c,writings.split(" "))
        

main()
