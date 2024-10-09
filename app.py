from flask import Flask, render_template, request, jsonify
import pickle
import re
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


def remove_mentions(text):
    """
    Supprime tous les mots commençant par un @ dans un texte.
    """
    return ' '.join(word for word in text.split() if not word.startswith('@'))


def clean_text_fct(text):
    """
    Nettoie le texte en supprimant les liens et les caractères spéciaux, sauf les smileys.
    """
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    pattern = re.compile(r'([^\w\s]|_)+', re.UNICODE)
    smileys = r'(:\)|:\(|:D|:P|:\*|;\)|;D|:\'-\(|<3|:\^])'
    text = re.sub(pattern, lambda x: x.group(
        0) if re.match(smileys, x.group(0)) else ' ', text)
    return text.strip()


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
