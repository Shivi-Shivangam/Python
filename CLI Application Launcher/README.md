# CLI Based Windows App Launcher

This is a Python Program for executing certain Programs/Application as per the Commands given.

## Package Used

NLTK Natural Language Toolkit for [Tokenization](https://www.nltk.org/#some-simple-things-you-can-do-with-nltk) of Words.

```cmd
pip install nltk
```

## Usage of Work Token
#### Disadvantage of using ```in``` with String:
Using ```in``` Operator for understanding commands is erroneous. Since, ```in``` doesn't perform a thorough Check.
Below Code Evaluates to True and will Execute Chrome, even though the String doesn't make any Sense. Because ```varun``` have the substring ```run```.
```python
string = "Varun Chrome"
print('run' in string.lower()) # True
```
#### Using NLTK Tokenize to overcome Disadvantage of ```in```:
To overcome this problem I tried to use NLP Package nltk. Using ```nltk.tokenize``` the search is a lot more Sensible. I haven't used any Grammar Check.
```python
from nltk.tokenize import word_tokenize
string = "Varun Chrome"
tokens = word_tokenize(string.lower())
print('run' in tokens) # False
```