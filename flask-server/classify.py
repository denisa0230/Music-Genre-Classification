import tensorflow as tf
import librosa
import numpy as np
import math

# Preprocesses the file
def preprocess(file_path, num_mfcc=40, n_fft=2018, hop_length=512, num_segment=10):
    data = {"labels" : [], "mfcc" : []}
    sample_rate = 22050
    samples_per_segment = int(sample_rate*30/num_segment)

    print("Track Name ", file_path)
    
    try:
        y, sr = librosa.load(file_path, sr = sample_rate)
    except:
        return
    for n in range(num_segment):
        mfcc = librosa.feature.mfcc(y = y[samples_per_segment*n : samples_per_segment*(n+1)],
                                    sr = sample_rate, n_mfcc = num_mfcc, n_fft = n_fft,
                                    hop_length = hop_length)
        mfcc = mfcc.T
        if len(mfcc) == math.ceil(samples_per_segment / hop_length):
            data["mfcc"].append(mfcc.tolist())
            data["labels"].append(0)
    return data

# Finds the genre of the song found at file_path
def find_genre(file_path):
    # Load the trained model
    model = tf.keras.models.load_model("GTZAN_LSTM.h5")

    # Preprocess the new audio file
    preprocessed_data = preprocess(file_path)

    if preprocessed_data is not None:
        # Convert into array
        input_data = np.array(preprocessed_data["mfcc"])
        
        # Make prediction
        predictions = model.predict(input_data)

        # Get the predicted class
        predicted_class = np.argmax(predictions, axis=1)[0]
        
        class_names = ["disco", "reggae", "hiphop", "jazz", "rock", "country", "metal", "pop", "classical", "blues"]
        predicted_class_name = np.array(class_names)[predicted_class]

        return predicted_class_name

    else:
        return f"File: {file_path}, Prediction failed due to preprocessing error."