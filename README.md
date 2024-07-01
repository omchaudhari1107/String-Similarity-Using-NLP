# 📚 Text Similarity Analysis using Spacy and Sklearn

This project demonstrates how to preprocess text and calculate text similarity using Spacy and Sklearn libraries. The process involves lemmatizing the text and using the `CountVectorizer` to transform the text data into vectors. Cosine similarity is then calculated to determine the similarity between different texts.

## Notebook Contents

1. 📦 Importing Libraries
2. 📝 Text Preprocessing
3. 🔢 Vectorization
4. 📊 Similarity Calculation
5. 📈 Visualization

## 📦 Importing Libraries

The necessary libraries are imported, including Spacy for natural language processing, Sklearn for vectorization and similarity calculation, and Matplotlib for visualization.

## 📝 Text Preprocessing

The text is first lemmatized using Spacy to reduce words to their base forms.

## 🔢 Vectorization

Using `CountVectorizer`, the lemmatized text is transformed into vectors.

## 📊 Similarity Calculation

Cosine similarity is calculated to determine the similarity between the two text vectors.

## 📈 Visualization

You can visualize the similarity matrix using Matplotlib.

## Example Output

When comparing the two example texts:

1. **Text 1**: "Thor is eating Pizza."
2. **Text 2**: "Loki is eating pizza."

The cosine similarity matrix will look like this:

![Similarity Matrix](https://github.com/omchaudhari1107/String-Similarity-Using-NLP/assets/90174038/2beef417-5e90-4979-a93e-49e0a4f84e25)

When comparing the two example of **Non-similar** texts:

1. **Text 1**: "Thor is eating Pizza."
2. **Text 2**: "Loki is Traveling."

The cosine similarity matrix will look like this:

![Non-Similarity Matrix](https://github.com/omchaudhari1107/String-Similarity-Using-NLP/assets/90174038/80618a50-8bcd-45b0-b380-408f11afb49b)


## How to Run

1. Clone this repository:

   ```
   git clone https://github.com/omchaudhari1107/String-Similarity-Using-NLP.git
   ```
