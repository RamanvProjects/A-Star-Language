#! /usr/bin/python

import nltk, re, pprint
import urllib2

def ie_preprocess(doc):
	sentences = nltk.sent_tokenize(doc)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

# Example:

source = urllib2.urlopen("http://en.wikipedia.org")
source = source.read()
print ie_preprocess(unicode(source))
