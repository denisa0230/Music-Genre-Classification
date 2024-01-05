# Second attempt #

Code from : https://www.projectpro.io/article/music-genre-classification-project-python-code/566#mcetoc_1fsm03988c

Accuracy of around 80%

**FILES**

**second_version.py**
   * The algorithm uses Mel Frequency Cepstral Coefficients (MFCC’s) with an LSTM Model.
   * Steps:
      * Use the preprocess function to load the audio files from the downloaded dataset and extract MFCC features (based on several sampling parameters) using Librosa.
      * Once the MFCC features are extracted, we can prepare the training, testing, and validating dataset using the train_test_split function from scikit-learn.
      * Train a simple LSTM classifier model using the GTZAN dataset.
      * Compile and fit the model using standard parameters: the Adam optimizer, sparse categorical cross-entropy loss (this performed better than categorical cross-entropy), and a 0.001 learning rate. Training the set on 60 epochs is enough for the classifier model to converge with 95% training and 85% validation accuracy.

**test_second_version.py**
   * Tests the model on the the files in the "../test_songs" directory

**USAGE**
  * To create GTZAN_LSTM.h5 dataset and get accuracy => *python3 second_version.py* (although I already included it in the repo, but do that 
  if you make changes to second_version.py)
  * To test the model => *python3 test_second_version.py*
  * You can view the results in out.txt
