# Movie-Review-Sentiment-Classification
Implement three Naive Bayes (NB) classifiers, Multinomial NB, Bernoulli NB, and Binary NB, for identifying the sentiment (positive/negative) of a given movie review.

Use the Cornell Movie Review Data Set (polarity dataset v2.0)(https://www.cs.cornell.edu/people/pabo/movie-review-data/) to train and test your classifiers.
The training and test sets are provided in the data.zip file. The positive reviews are in the pos
folder and the negative reviews are in the neg folder. The training set contains 700 positive and
700 negative movie reviews. The test set contains 300 positive and 300 negative movie reviews.
Each review is provided as a separate file. The tokens have already been lower-cased.


1- I used python programming language.

2- My program need 4 input folder. (train positive comments, train negative comments, test positive comments, test negative comments)

3- I have 3 different class but we need to run only test.py file.

4- If you open the terminal, you can write for run the program: `python3 test.py pos neg test_pos test_neg`

5- ```from tabulate import tabulate``` I import tabulate and draw tables for output. If you do not import, you cannot take any output. 

6- You can download tabulate like that : ```pip install tabulate```

Example Output: 


![alt text](https://github.com/Oguzhan09/Movie-Review-Sentiment-Classsification/blob/master/naivebayes.png?raw=true)
