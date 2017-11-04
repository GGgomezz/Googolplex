from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Lsa
from sumy.summarizers.edmundson import EdmundsonSummarizer as Edmundson
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRank
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.models.dom._sentence import Sentence

LANGUAGE = "english"
SENTENCES_COUNT = 4

if __name__ == "__main__":
    url = "http://www.encyclopedia.com/plants-and-animals/plants/plants/potato"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    #define summarizers for the summarizing methods being used
    summarizer_Lsa = Lsa(stemmer)
    summarizer_Lsa.stop_words = get_stop_words(LANGUAGE)
    summary_Lsa = summarizer_Lsa(parser.document, SENTENCES_COUNT)

    summarizer_LexRank = LexRank()
    summary_LexRank = summarizer_LexRank(parser.document, SENTENCES_COUNT)

    summarizer_Edmundson = Edmundson(stemmer)
    summarizer_Edmundson.null_words = get_stop_words(LANGUAGE)
    summarizer_Edmundson.bonus_words = parser.significant_words
    summarizer_Edmundson.stigma_words = parser.stigma_words
    summary_Edmundson = summarizer_Edmundson(parser.document, SENTENCES_COUNT)

    #store summaries in a text  file
    #list_of_sums = [summary_Lsa, summary_LexRank, summary_Edmundson]
    #f = open('summarized.txt', 'w')
    #for t in list_of_sums:
    #    line = ' '.join(str(x) for x in t)
    #    f.write(line + '\n')
    #f.close()

    #create new shorter summaries
    #parser = PlaintextParser.from_file("summarized.txt", Tokenizer(LANGUAGE))
    #SENTENCES_COUNT = 3

    #define summarizers for the summarizing methods being used
    #summarizer_Lsa = Lsa(stemmer)
    #summarizer_Lsa.stop_words = get_stop_words(LANGUAGE)
    #summary_Lsa = summarizer_Lsa(parser.document, SENTENCES_COUNT)

    #summarizer_LexRank = LexRank()
    #summary_LexRank = summarizer_LexRank(parser.document, SENTENCES_COUNT)

    #summarizer_Edmundson = Edmundson(stemmer)
    #summarizer_Edmundson.null_words = get_stop_words(LANGUAGE)
    #summarizer_Edmundson.bonus_words = parser.significant_words
    #summarizer_Edmundson.stigma_words = parser.stigma_words
    #summary_Edmundson = summarizer_Edmundson(parser.document, SENTENCES_COUNT)

    #print summaries
    summary_Lsa_trim = []
    for sentence in summary_Lsa:
        #trim off super short - likely a few word sentences
        if len(sentence._text)>20:
            print(sentence)
            summary_Lsa_trim.append(sentence)

    print('\n')
    summary_LexRank_trim = []
    for sentence in summary_LexRank:
        #trim off super short - likely a few word sentences
        if len(sentence._text)>20:
            print(sentence)
            summary_LexRank_trim.append(sentence)

    print('\n')
    summary_Edmundson_trim = []
    for sentence in summary_Edmundson:
        #trim off super short - likely a few word sentences
        if len(sentence._text)>20:
            print(sentence)
            summary_Edmundson_trim.append(sentence)