# using task extracts and adding my own word to test
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 =  nlp("animal")

print("Word 1 and Word 2: ")
print(word1.similarity(word2))
print("Word 3 and Word 2: ")
print(word3.similarity(word2))
print("Word 3 and Word 1: ")
print(word3.similarity(word1))
print("Word 4 and Word 1: ")
print(word4.similarity(word1))
print("Word 4 and Word 2: ")
print(word4.similarity(word2))
print("Word 4 and Word 3: ")
print(word4.similarity(word3))