import kenlm
import sys
import nltk


if __name__ == '__main__':
    model = sys.argv[1]
    input_file = sys.argv[2]
    sentence_num = 0
    score = 0
    model = kenlm.LanguageModel(model)
    with open(input_file, encoding='utf-8') as file:
        sentence = file.readline()
        # sentence = ' '.join(nltk.word_tokenize(sentence)).lower()
        score += model.score(sentence)
        sentence_num += 1

    print("average score:", score/sentence_num)