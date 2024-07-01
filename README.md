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

![08fbb3035a87088e73235d5e6a3c89bd941f8cbfdc963c2518744a2e](https://github.com/omchaudhari1107/String-Similarity-Using-NLP/assets/90174038/986eda29-fb91-436d-bab3-0ccc23e53eaa)


When comparing the two example of **Non-similar** texts:

1. **Text 1**: "Thor is eating Pizza."
2. **Text 2**: "Loki is Traveling."

The cosine similarity matrix will look like this:

![407d9805166c440098e5c28b177f52c908cfb79ad2bd859d26d53a8a](https://github.com/omchaudhari1107/String-Similarity-Using-NLP/assets/90174038/4b4bc5ce-795d-4df6-8669-8dbeba0cdab3)


## How to Run

1. Clone this repository:

   ```
   git clone https://github.com/omchaudhari1107/String-Similarity-Using-NLP.git
   ```
