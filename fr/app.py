import tkinter as tk
from tkinter import filedialog
import tensorflow.keras as keras
import librosa
import numpy as np

# Load the model from the HDF5 file
model = keras.models.load_model('best_model1_weights (2).h5')

# Define a function to classify emotions
def classify_emotion(file_path):
    # Load audio file and extract features
    try:
        features = extract_features(file_path)
        # Predict emotion
        emotion = model.predict(features.reshape(1, -1))[0]
        result_label.config(text=f'Predicted Emotion: {emotion}')
    except Exception as e:
        result_label.config(text=f'Error: {str(e)}')

# Define a function to extract features from audio file
def extract_features(file_path):
    # Load audio file using librosa
    y, sr = librosa.load(file_path, sr=None)
    # Extract features (example: using MFCC)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    # Flatten the features array
    flat_features = np.ravel(mfccs)
    return flat_features

# Define a function to handle button click
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        classify_emotion(file_path)

# Create the main application window
root = tk.Tk()
root.title("Speech Emotion Recognition")

# Create and place widgets
label = tk.Label(root, text="Select an audio file:")
label.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
