# RYM Random Genre Picker

A simple web app that displays a random music genre with a direct link to its RateYourMusic (RYM) page.

## Description

RYM Genre Picker is a small Python project built with Streamlit. It loads a list of music genres from a local text file and allows users to generate a random genre at the click of a button. Each genre shown includes a link to its corresponding page on RateYourMusic.com.

## Live Version

You can try the app directly in your browser: [RYM Genre Picker (Web)](https://rym-genre-picker.streamlit.app/)

## Getting Started

### Dependencies

* Python 3.8 or later
* Streamlit

### Installing

1. Clone or download this repository:
```
git clone https://github.com/andrea441/rym-genre-picker
cd rym-genre-picker
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Make sure you have a `genres.txt` file in the root folder with one genre per line.

### Executing program

To run the Streamlit app:

```
streamlit run app.py
```

Once running, your browser will open a local server where you can use the app.

## Help

If you encounter issues related to the file not being found, make sure:
* `genres.txt` exists in the same directory as `app.py`
* It uses UTF-8 encoding and is not empty

## Authors

[@andrea441](https://github.com/andrea441)
