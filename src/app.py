import os
import random

import requests
from flask import Flask, render_template, request

from MemeGenerator.meme_engine import MemeEngine
from Ingestor import Ingestor

app = Flask(__name__, static_folder='./tmp')

meme = MemeEngine('./tmp/static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []

    for values in quote_files:
        quotes = Ingestor.parse(values)

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = os.listdir(images_path)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = os.getcwd() + "\\_data\\photos\\dog\\" + random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    r = requests.get(image_url, allow_redirects=True)
    tmp = f'./tmp/{random.randint(0, 100000000)}.png'
    imz = open(tmp, 'wb').write(r.content)

    path = meme.make_meme(tmp, body, author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
