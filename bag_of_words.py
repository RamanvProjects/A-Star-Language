import nltk
import urllib
rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]

def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features

def bag_of_words(words):
	return dict([(word, True) for word in words.split()])

def histograms(words):
	hist = {}
	words = words.split()
	for word in words:
		if word in hist:
			hist[word] = hist[word] + 1
		else:
			hist[word] = 1

	return hist
#for i v in enumerate
print rte_features(rtepair)
print histograms("This is a sentence made up of multiple words")
print bag_of_words("This is a sentence made up of multiple words")

webpage = urllib.urlopen("http://en.wikipedia.org/wiki/Isaac_Newton")
source = webpage.read()

print bag_of_words(source)
