# First attempt #

Code from : https://data-flair.training/blogs/python-project-music-genre-classification/
Last tested accuracy : 0.689119170984456 (68.91%)

**music_genre.py**
    * The algorithm uses K-Nearest Neighbors, which is a popular machine learning algorithm for regression and classification. It makes predictions on data points based on their similarity measures i.e distance between them.
    * Steps:
      * Extract features from the dataset and dump these features into a binary .dat file “my.dat”.
      * Train and test split on the dataset
      * Make prediction using KNN and get the accuracy on test data

**test.py**
    * Tests the model on the the files in the "../test_songs" directory

**USAGE**
  * To create my.dat dataset and get accuracy => *python3 music_genre.py* (although I already included it in the repo, but do that 
  if you make changes to music_genre.py)
  * To test the model => *python3 music_genre.py*