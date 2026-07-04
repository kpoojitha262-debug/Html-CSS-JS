{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOHeeJYk1A0jCRFn5H81sf0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kpoojitha262-debug/Html-CSS-JS/blob/main/Tfidf.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jzw12n8JOiy1",
        "outputId": "06e6c1e0-4ef4-4946-9ebb-80c46c87c061"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Vocabulary: ['1285732' 'is' 'subject' 'this' 'useful' 'very']\n",
            "TF-IDF Matrix :\n",
            " [[0.        0.4472136 0.4472136 0.4472136 0.4472136 0.4472136]\n",
            " [1.        0.        0.        0.        0.        0.       ]]\n",
            "Cosine Similarity between doc1 and doc2: 0.0\n"
          ]
        }
      ],
      "source": [
        "doc1 = \"This is very useful subject\"\n",
        "doc2 = \"1285732\"\n",
        "documents = (doc1,doc2)\n",
        "\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "\n",
        "Vectorizer = TfidfVectorizer()\n",
        "\n",
        "tfidf_matrix = Vectorizer.fit_transform(documents)\n",
        "\n",
        "print(\"Vocabulary:\",Vectorizer.get_feature_names_out())\n",
        "print(\"TF-IDF Matrix :\\n\",tfidf_matrix.toarray())\n",
        "\n",
        "similarity = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])\n",
        "print(\"Cosine Similarity between doc1 and doc2:\", similarity[0][0])"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "4oUEsAFqOpEH"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}