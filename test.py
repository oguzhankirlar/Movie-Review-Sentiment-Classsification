from os import listdir
from os.path import isfile, join
from tabulate import tabulate
from calculations import third_input, fourth_input
from naivebayes import multi_naive_bayes, bernoulli_naive_bayes, binary_naive_bayes

test_pos_files = [f for f in listdir(third_input) if isfile(join(third_input, f))]  # holds txt files in pos test
tes_neg_files = [f for f in listdir(fourth_input) if isfile(join(fourth_input, f))]  # holds txt files in neg test
test_pos_comments = []  # holds all positive lines
test_neg_comments = []  # holds all negative lines
# This part add all positive comments to one list
for f in test_pos_files:
    file = open(third_input + '/' + f, 'r', errors='replace')
    all_lines = ""
    lines = file.readlines()
    for line in lines:
        l = line.split(" ")
        for word in l:
            if word.isalnum():
                all_lines = all_lines+word+" "
    test_pos_comments.append(all_lines)
# This part add all negative comments to one list
for f in tes_neg_files:
    file = open(fourth_input + '/' + f, 'r', errors='replace')
    all_lines = ""
    lines = file.readlines()
    for line in lines:
        l = line.split(" ")
        for word in l:
            if word.isalnum():
                all_lines = all_lines+word+" "
    test_neg_comments.append(all_lines)

# In this part 3 algorithm works, precision, recall and f-scores calculate for micro and macro average in all NB's
naive_bayes_list = [multi_naive_bayes, bernoulli_naive_bayes, binary_naive_bayes]
name_list = ["Multinomial NB", "Bernoulli NB  ", "Binary NB     "]
for nb in naive_bayes_list:
    index = naive_bayes_list.index(nb)
    pos_counter, neg_counter = 0, 0
    sec_pos_counter, sec_neg_counter = 0, 0
    tp1, tp2 = 0, 0
    fn1, fn2 = 0, 0
    fp1, fp2 = 0, 0
    for comments in test_pos_comments:
        pos_calc = nb(comments, 1)
        neg_calc = nb(comments, 0)
        if pos_calc > neg_calc:
            pos_counter = pos_counter + 1
        elif neg_calc > pos_calc:
            neg_counter = neg_counter + 1
    for c in test_neg_comments:
        pos_calc = nb(c, 1)
        neg_calc = nb(c, 0)
        if pos_calc > neg_calc:
            sec_pos_counter = sec_pos_counter + 1
        elif neg_calc > pos_calc:
            sec_neg_counter = sec_neg_counter + 1
    tp1 = pos_counter
    fn1 = neg_counter
    fp1 = sec_pos_counter
    tp2 = sec_neg_counter
    fn2 = sec_pos_counter
    fp2 = neg_counter
    p1 = tp1 / (tp1+fp1)
    r1 = tp1 / (tp1+fn1)
    f1 = 2 * (p1*r1)/(p1+r1)
    p2 = tp2 / (tp2+fp2)
    r2 = tp2 / (tp2+fn2)
    f2 = 2 * (p2*r2)/(p2+r2)
    micro_precision = (tp1+tp2) / (tp1+tp2+fp1+fp2)
    micro_recall = (tp1+tp2) / (tp1+tp2+fn1+fn2)
    micro_f = 2 * (micro_recall*micro_precision) / (micro_recall+micro_precision)
    macro_precision = (p1+p2)/2
    macro_recall = (r1+r2)/2
    macro_f = 2 * (macro_recall*macro_precision) / (macro_recall+macro_precision)
    print(tabulate([['Micro average', micro_precision, micro_recall, micro_f], ['Macro average', macro_precision, macro_recall, macro_f]], headers=[name_list[index], 'Precision', 'Recall', 'F-scores']))
    print("\n")
    print(tabulate([['Positive', pos_counter, neg_counter], ['Negative', sec_pos_counter, sec_neg_counter]], headers=[name_list[index], 'Positive Data Set', 'Negative Data Set']))
    print("\n")
