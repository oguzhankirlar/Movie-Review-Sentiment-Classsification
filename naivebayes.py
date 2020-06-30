from calculations import negative_comments, positive_comments, positive_words, negative_words, \
    pos_cnt, neg_cnt, unq_cnt, pos_unq_cnt, neg_unq_cnt, all_unique_words, pos_unq_counter, neg_unq_counter

total_positive_ratio_for_bern = 8.90711325678439e-21
total_negative_ratio_for_bern = 2.410093311436033e-10
# These 2 methods compute ratio in all unique words for (1-x)
def compute_positive_ratio_bern():
    R = 1
    for word in all_unique_words:
        x = (pos_unq_cnt[word]+1)/(len(positive_comments)+2)
        R = R*(1-x)
    return R

def compute_negative_ratio_bern():
    R = 1
    for word in all_unique_words:
        x = (neg_unq_cnt[word]+1)/(len(negative_comments)+2)
        R = R*(1-x)
    return R

def convert(text):
    s = ""
    li = text.split(" ")
    for word in li:
        if word.isalnum():
            s = s + word + " "
    return s
# Multinomial Naive Bayes Algorithm
def multi_naive_bayes(text, id):
    calc = 1
    t = convert(text)
    li = t.split(" ")
    ratio = len(positive_comments)/(len(positive_comments)+len(negative_comments))
    for word in li:
        if id == 1:
            calc = calc * 1400 * (pos_cnt[word] + 1) / (len(positive_words) + len(unq_cnt))
        elif id == 0:
            calc = calc * 1400 * (neg_cnt[word] + 1) / (len(negative_words) + len(unq_cnt))
    return calc*ratio
# Bernoulli Naive Bayes Algorithm
def bernoulli_naive_bayes(text, id):
    a = convert(text)
    li = a.split(" ")
    unique_text = []
    for w in li:
        if w not in unique_text:
            unique_text.append(w)
    calc = 1
    if id == 1:
        ratio = len(positive_comments) / (len(positive_comments) + len(negative_comments))
        calc = calc * ratio
        for word in unique_text:
            x = (pos_unq_cnt[word]+1)/(len(positive_comments)+2)
            calc = calc * 10 * x / (1 - x)
        calc = calc * total_positive_ratio_for_bern
    elif id == 0:
        ratio = len(negative_comments) / (len(positive_comments) + len(negative_comments))
        calc = calc * ratio
        for word in unique_text:
            x = (neg_unq_cnt[word]+1)/(len(negative_comments)+2)
            calc = calc * 10 * x / (1 - x)
        calc = calc * total_negative_ratio_for_bern
    return calc
# Binary Naive Bayes Algorithm
def binary_naive_bayes(text, id):
    a = convert(text)
    li = a.split(" ")
    unique_text = []
    for w in li:
        if w not in unique_text:
            unique_text.append(w)
    calc = 1
    if id == 1:
        ratio = len(positive_comments) / (len(positive_comments) + len(negative_comments))
        calc = calc * ratio
        for word in unique_text:
            calc = calc * (pos_unq_cnt[word]+1)/(pos_unq_counter + len(unq_cnt)) * 3000
    elif id == 0:
        ratio = len(negative_comments) / (len(positive_comments) + len(negative_comments))
        calc = calc * ratio
        for word in unique_text:
            calc = calc * (neg_unq_cnt[word]+1)/(neg_unq_counter + len(unq_cnt)) * 3000
    return calc


