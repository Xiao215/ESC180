'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math
import re
import timeit


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    common_key = []
    for key in vec1:
        if key in vec2:
            common_key.append(key)
    numerator = 0
    for item in common_key:
        numerator += vec1[item]*vec2[item]
    if numerator == 0:
        return 0
    denominator = 0
    vec1_sq = 0
    vec2_sq = 0
    for value in vec1.values():
        vec1_sq += (value)**2
    for value in vec2.values():
        vec2_sq += (value)**2
    sim = numerator/(math.sqrt(vec1_sq*vec2_sq))
    return sim


"""
def build_semantic_descriptors(sentences):
    d = {}
    # iterate all the words
    for sentence in sentences:
        for word in sentence:
            # check if the word is inside dictionary d
            if(word not in d):
                d_word = {}
                # check through the entire sentences again
                for checkSentence in sentences:
                    if word in checkSentence:
                        # this set will check to avoid duplicate word
                        avoid_dup = {word}
                        # if the word is inside the sentense
                        for other_word in checkSentence:
                            # for all the other words inside the sentense
                            if other_word not in avoid_dup:
                                # add to just avoid seeing a duplicate word again
                                avoid_dup.add(other_word)
                                if other_word not in d_word:
                                    d_word[other_word] = 1
                                else:
                                    d_word[other_word] += 1
                d[word] = d_word
    return d
"""  # OLD


def sentence_add_dict(d, sentence):
    if(len(sentence) <= 1):
        return
    word = sentence.pop(0)
    for other_word in sentence:
        if other_word not in d[word]:
            d[word][other_word] = 1
        else:
            d[word][other_word] += 1
        if word not in d[other_word]:
            d[other_word][word] = 1
        else:
            d[other_word][word] += 1
    sentence_add_dict(d, sentence)


def build_semantic_descriptors(sentences):
    d = {}
    # iterate all the words
    for sentence in sentences:
        for word in sentence:
            if word not in d.keys():
                d[word] = {}
        sentence_add_dict(d, sentence)
    return d
# check code for Q2


"""
print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
                                  ["i", "am", "a", "spiteful", "man"],
                                  ["i", "am", "an", "unattractive", "man"],
                                  ["i", "believe", "my", "liver", "is", "diseased"],
                                  ["however", "i", "know", "nothing", "at", "all", "about", "my",
                                   "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]])["man"])

"""


def split_string(filenames):
    f = open(filenames, "r")
    # convert all the end sentence punctuation into .\n
    str = f.read()
    sentences = re.split('[?!.]', str)
    for i in range(len(sentences)):
        sentences[i] = re.split('[^0-9a-zA-Z]', sentences[i])
        try:
            while True:
                sentences[i].remove("")
        except ValueError:
            pass
        for j in range(len(sentences[i])):
            sentences[i][j] = sentences[i][j].lower()
    return sentences


def build_semantic_descriptors_from_files(filenames):
    total = {}
    for file in filenames:
        sentences = split_string(file)
        for key, value in build_semantic_descriptors(sentences).items():
            if key not in total.keys():
                total[key] = value
            else:
                for subKey, subValue in value.items():
                    if subKey not in total[key].keys():
                        total[key][subKey] = subValue
                    else:
                        total[key][subKey] += subValue
    return total


#print(build_semantic_descriptors_from_files(["test.txt", "test1.txt"]))


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_choice_score = -1
    most_match_choice = -1
    for choice in choices:
        if(choice in semantic_descriptors.keys()) and (word in semantic_descriptors.keys()):
            simi = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
            if max_choice_score < simi:
                max_choice_score = simi
                most_match_choice = choice
    return most_match_choice == -1 and -1 or most_match_choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename, "r")
    #stringList = re.split('\s', f.read())
    stringList = f.readlines()
    right_num = 0
    total_num = 0
    for question in stringList:
        question = re.split('\s', question)
        word = question.pop(0)
        answer = question.pop(0)
        my_answer = most_similar_word(word, question, semantic_descriptors, similarity_fn)
        if my_answer == answer:
            right_num += 1
        total_num += 1
    return right_num*100/total_num


time = timeit.default_timer()
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
res = run_similarity_test("text.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
print("Time:", timeit.default_timer()-time)
