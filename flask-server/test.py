import tensorflow as tf
import numpy as np
import librosa
import math
import sys

print("Hello")
#Preprocesses the file
def preprocess(file_path, num_mfcc=40, n_fft=2018, hop_length=512, num_segment=10):
    data = {"labels" : [], "mfcc" : []}
    sample_rate = 22050
    samples_per_segment = int(sample_rate30/num_segment)

    print("Track Name ", file_path)

    try:
        y, sr = librosa.load(file_path, sr = sample_rate)
    except:
        return
    for n in range(num_segment):
        mfcc = librosa.feature.mfcc(y = y[samples_per_segmentn : samples_per_segment*(n+1)],
                                    sr = sample_rate, n_mfcc = num_mfcc, n_fft = n_fft,
                                    hop_length = hop_length)
        mfcc = mfcc.T
        if len(mfcc) == math.ceil(samples_per_segment / hop_length):
            data["mfcc"].append(mfcc.tolist())
            data["labels"].append(0)
    return data

model = tf.keras.models.load_model("GTZAN_LSTM.h5")
file_path = sys.argv[1]
#Preprocess the new audio file
print(file_path)
preprocessed_data = preprocess(file_path)

if preprocessed_data is not None:
    # Convert into array
    input_data = np.array(preprocessed_data["mfcc"])

#Make prediction
    predictions = model.predict(input_data)

    # Get the predicted class
    predicted_class = np.argmax(predictions, axis=1)[0]

    class_names = ["disco", "reggae", "hiphop", "jazz", "rock", "country", "metal", "pop", "classical", "blues"]
    predicted_class_name = np.array(class_names)[predicted_class]

    print(predicted_class_name)

else:
    print(f"File: {file_path}, Prediction failed due to preprocessing error.")