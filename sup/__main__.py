"""MIT License

Copyright (c) 2021-present EnokiUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from .story import Story
from .onlinestory import OnlineStory
from .storyerror import StoryError
from argparse import ArgumentParser


def main():
    # CLI handling
    parser = ArgumentParser(description='Runs a story directly from the terminal')
    parser.add_argument('Story', 'S', type=str, help='Name of the story')
    parser.add_argument('--online-story', dest='online', action='store_const', const=True, default=False,
                        help="(Optional) Tries to fetch the story from the github page")

    print(parser.parse_args())
    input()

if __name__ == '__main__':
    main()
    
    
