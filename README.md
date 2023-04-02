# Face Recognition

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)

![cover](/img/cover.png)

## Table of Content

- [Introduction](#Introduction)
- [Dataset](#Dataset)
- [How To Use It](#How-To-Use-It)
- [Dashboard](#Dashboard)
- [Credits](#Credits)

## Introduction

This is my Bootcamp Final Project where I created a dashboard about face recognition 📹. It is my second real project since I jumped into data analytics field. You are going to find how I did it. I hope you like it 🤟

[Back to Table of Content](#table-of-content)

## Dataset

I used this dataset from Kaggle to get Obama images [Object Detection - Obama](https://www.kaggle.com/datasets/jipingsun/object-detection-obama). On the other hand, I took 45 photos of myself. However, I only used a photo of me and obama for the model and it worked fine.

[Back to Table of Content](#table-of-content)

## How To Use It

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)

### Installation Options:

#### Installing on Mac or Linux

First, make sure you have dlib already installed with Python bindings:

  * [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
  
Then, make sure you have cmake installed:  
 
```bash
brew install cmake
```

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

Then, you have to run streamlit. To do that you need to access dashboard folder and write this code in your terminal

```bash
streamlit run main.py
```

Follow the instructions to start face recognition. Remember, the model is only able to recognize Obama's face and my face. If you try showing your face, the model is not going to recognize you and show "Unknow".

If you want the model recognize your face, please add an image of you in data folder. Then, open recognition.py and change this code according to what you need.

```python
# Image path
jesus_image_path = "../data/train/Jesus/IMG_3462.jpg"
obama_image_path = "../data/train/Obama/Obama006.jpg"

# Load a sample picture and learn how to recognize it.
jesus_image = face_recognition.load_image_file(jesus_image_path)
jesus_face_encoding = face_recognition.face_encodings(jesus_image)[0]

# Load a second sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file(obama_image_path)
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Create list of known face encodings and their names
known_face_encodings = [jesus_face_encoding, obama_face_encoding]
known_face_names = ["Jesus Adraz", "Barak Obama"]
```
[Back to Table of Content](#table-of-content)

## Dashboard

When you run streamlit, this is the main page:

![image0](/img/image0.png)

Then, you need to clic the "Start" buttom to go to recognition page.

When you are in recognition page, please clic on "Start Camera" buttom and put in front of your camera:

![image1](/img/image1.png)

If you show the second known face name, Obama in this case, it will look like this:

![image2](/img/image2.png)


Finally, if you show an unknown face, it will look like this:

![image3](/img/image3.png)

[Back to Table of Content](#table-of-content)

## Credits

I would like to thanks to my teachers [Santino Lede](https://github.com/Luxor5k) and [Daniel Alvarado](https://github.com/DanielDls-exe) for support me in each step of this project. Also, I want to thank you to [Adam Geitgey](https://github.com/ageitgey) for his face recognition library. You can check his repo for more info doing [clic here](https://github.com/ageitgey/face_recognition).

[Back to Top](#face-recognition)