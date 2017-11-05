import nltk
from nltk.corpus import stopwords
from itertools import product
from nltk.corpus import wordnet as wn
# import timeit

def main():
    # temp sentence
    temp_s = "why am running new york city marathon as guide for disabled runner"

    # timer
    #start = timeit.default_timer()
    # tokenize
    token_s = nltk.word_tokenize(temp_s)

    # remove stopwords
    stopWords = set(stopwords.words('english'))
    filtered_tokens = [word for word in token_s if word not in stopWords]
    filtered_tokens = []
    for word in token_s:
        if word not in stopWords:
            filtered_tokens.append(word)

    # ini print
    print('tokens:', token_s)
    print('filtered:', filtered_tokens)

    # dummy var
    prob_list = []
    comp_list = []
    top_3 = []

    # loops through for comparisons
    filtered_iter = iter(filtered_tokens)
    for i in range(len(filtered_tokens)):
        total = 0
        elem = next(filtered_iter)

        # loops through phrase with each keyword
        allsyns1 = set(ss for word in token_s for ss in wn.synsets(word))
        allsyns2 = set(ss for word in elem for ss in wn.synsets(word))
        full_list = [(wn.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in product(allsyns1, allsyns2)]
        score_list = iter(full_list)

        # get avg score
        for j in range(len(full_list)):
            total += float(next(score_list)[0])
        print('word:', elem, '| weighted avg:', total/len(full_list))

        # store dummy
        prob_list.append(float(total/len(full_list)))
        comp_list.append(elem)

    # grab min(3, #of elements)
    for i in range(min(3, len(prob_list))):
        curr_max = prob_list.index(max(prob_list))
        top_3.append(comp_list[curr_max])

        prob_list.pop(curr_max)
        comp_list.pop(curr_max)

    # prints top 3
    print('TOP:', top_3)

    queryKeys(top_3)

# accepts list of top keywords, returns url targets for summary.py
def queryKeys(key_list):
    # search param
    main_url = "https://en.wikipedia.org/wiki/"

    url_list = []
    # generate url targets
    for keys in key_list:
        url_list.append(main_url + str(keys))

    # return url_list
    for link in url_list:
        print(link)

main()
