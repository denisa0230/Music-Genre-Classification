import math
import librosa
import os
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import keras
from keras import layers

def preprocess(dataset_path, num_mfcc=40, n_fft=2018, hop_length=512, num_segment=10):
    data = {"labels" : [], "mfcc" : []}
    sample_rate = 22050
    samples_per_segment = int(sample_rate*30/num_segment)
    
    for label_idx, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
        if dirpath == dataset_path:
            continue
        for f in sorted(filenames):
            if not f.endswith(".wav"):
                continue
            file_path = str(str(dirpath).split('\\')[-1]) + "/" + str(f)
            print("Track Name ", file_path)
            
            try:
                y, sr = librosa.load(file_path, sr = sample_rate)
            except:
                continue
            for n in range(num_segment):
                mfcc = librosa.feature.mfcc(y = y[samples_per_segment*n : samples_per_segment*(n+1)],
                                            sr = sample_rate, n_mfcc = num_mfcc, n_fft = n_fft,
                                            hop_length = hop_length)
                mfcc = mfcc.T
                if len(mfcc) == math.ceil(samples_per_segment / hop_length):
                    data["mfcc"].append(mfcc.tolist())
                    data["labels"].append(label_idx-1)
    return data

mfcc_data = preprocess("../Data/genres_original")
x = np.array(mfcc_data["mfcc"])
y = np.array(mfcc_data["labels"])

x = x.reshape(x.shape[0], x.shape[1], x.shape[2], 1)
y = keras.utils.to_categorical(y, num_classes = 10)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = 0.2)

# Adjust labels
y_train[y_train==10] = 9
y_val[y_val==10] = 9
y_test[y_test==10] = 9

input_shape = x_train.shape[1:]

# Define CNN model
cnn_model = keras.Sequential([
                layers.Conv2D(32, (3,3), activation = 'relu', padding = 'valid',
                              input_shape = input_shape),
                layers.MaxPooling2D(2, padding = 'same'),
                layers.Conv2D(128, (3,3), activation = 'relu', padding = 'valid'),
                layers.MaxPooling2D(2, padding = 'same'),
                layers.Dropout(0.3),
                
                layers.Conv2D(128, (3,3), activation = 'relu', padding = 'valid'),
                layers.MaxPooling2D(2, padding = 'same'),
                layers.Dropout(0.3),
                
                layers.GlobalAveragePooling2D(),
                layers.Dense(512, activation = 'relu'),
                layers.Dense(10, activation = 'softmax')
])

cnn_model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = 'accuracy')
cnn_model.summary()

history = cnn_model.fit(x_train, y_train,
                        validation_data=(x_val, y_val),
                        epochs=40,
                        verbose=2,
                        batch_size=32)

cnn_model.save("GTZAN_LSTM.h5")

y_pred = cnn_model.predict(x_test)
y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)

print(np.sum(y_pred==y_test)/len(y_pred))