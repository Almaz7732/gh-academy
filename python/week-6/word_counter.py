class WordCounter:
    def __init__(self):
        self.wordCounter = {}

    def inputWord(self, sentence):
        words = sentence.split()

        for word in words:
            if word.lower() not in self.wordCounter:
                self.wordCounter[word.lower()] = 1
            else:
                self.wordCounter[word.lower()] += 1

    def printCount(self):
        print(self.wordCounter)



def main():
    sentence = input('Enter a sentence: ')
    wordCounter = WordCounter()
    wordCounter.inputWord(sentence)
    wordCounter.printCount()

if __name__ == "__main__":
    main()