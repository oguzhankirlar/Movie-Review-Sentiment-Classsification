import collections
import sys
from os import listdir
from os.path import isfile, join

first_input = sys.argv[1]  # Positive files for train
second_input = sys.argv[2]  # Negative files for train
third_input = sys.argv[3]  # Positive files for test
fourth_input = sys.argv[4]  # Negative files for test

pos_files = [f for f in listdir(first_input) if isfile(join(first_input, f))]  # holds txt files in pos train
neg_files = [f for f in listdir(second_input) if isfile(join(second_input, f))]  # holds txt files in neg train
positive_comments = []  # holds all positive lines
negative_comments = []  # holds all negative lines
positive_words = []  # holds all positive words
negative_words = []  # holds all negative words
all_words = []  # holds all words
all_unique_words = []  # holds all unique words
positive_comments_unique = []  # holds lines with unique words
negative_comments_unique = []  # holds lines with unique words
pos_cnt = collections.Counter()  # count of positive words
neg_cnt = collections.Counter()  # count of negative words
unq_cnt = collections.Counter()  # count of unique words
pos_unq_cnt = collections.Counter()
neg_unq_cnt = collections.Counter()

for f in pos_files:  # This part add all positive comments to one list
    file = open(first_input + '/' + f, 'r', errors='replace')
    all_lines = ""
    lines = file.readlines()
    for line in lines:
        l = line.split(" ")
        for word in l:
            if word.isalnum():
                positive_words.append(word)
                all_lines = all_lines+word+" "
    positive_comments.append(all_lines)

for f in neg_files:  # This part add all negative comments to one list
    file = open(second_input + '/' + f, 'r', errors='replace')
    all_lines = ""
    lines = file.readlines()
    for line in lines:
        l = line.split(" ")
        for word in l:
            if word.isalnum():
                negative_words.append(word)
                all_lines = all_lines+word+" "
    negative_comments.append(all_lines)

# This part creates all words list
for w in positive_words:
    if w is not all_words:
        all_words.append(w)
for w in negative_words:
    if w is not all_words:
        all_words.append(w)
# This part creates counter of words in positive, negative and total comments
for word in positive_words:
    pos_cnt[word] += 1
for word in negative_words:
    neg_cnt[word] += 1
for word in all_words:
    unq_cnt[word] += 1
# Create unique words list
for word in all_words:
    if word not in all_unique_words:
        all_unique_words.append(word)
# Make comments words to unique for positive comments (Words exist in different words still holds)
for comment in positive_comments:
    s = ""
    text = comment.split(" ")
    for w in text:
        if w not in s:
            s = s + w + " "
    positive_comments_unique.append(s)
# Make comments words to unique for negative comments (Words exist in different words still holds)
for comment in negative_comments:
    s = ""
    text = comment.split(" ")
    for w in text:
        if w not in s:
            s = s + w + " "
    negative_comments_unique.append(s)

# Create counter for unique comments words
for line in positive_comments_unique:
    text = line.split(" ")
    for word in text:
        pos_unq_cnt[word] += 1
for line in negative_comments_unique:
    text = line.split(" ")
    for word in text:
        neg_unq_cnt[word] += 1

# Sum of words in unique comments
pos_unq_counter = 0
neg_unq_counter = 0
for line in positive_comments_unique:
    t = line.split(" ")
    pos_unq_counter = pos_unq_counter + len(t)
for line in negative_comments_unique:
    t = line.split(" ")
    neg_unq_counter = neg_unq_counter + len(t)


