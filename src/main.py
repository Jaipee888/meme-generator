import meme
import argparse
import os

if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str,
                        help="path to an image file")
    parser.add_argument('--body', type=str,
                        help="quote body to add to the image.")
    parser.add_argument('--author', type=str,
                        help="quote author to add to the image.")
    args = parser.parse_args()
    print(meme.generate_meme(args.path, args.body, args.author))
