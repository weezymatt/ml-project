import argparse
import pdb

class Token:
	def __init__(self, word, pos, chunk, ner):
		self.word = word
		self.pos = pos
		self.chunk = chunk
		self.ner = ner

	def __str__(self):
		return f"{self.word} {self.pos} {self.chunk} {self.ner}"

class DeuToken:
	def __init__(self, word, lemma, pos, chunk, ner):
		self.word = word
		self.lemma = lemma
		self.pos = pos
		self.chunk = chunk
		self.ner = ner

	def __str__(self):
		return f"{self.word} {self.lemma} {self.pos} {self.chunk} {self.ner}"

def read_conll_data(file, encoding='utf-8', language='es'):
	""" Reads a BIO data."""
	collection = []
	document = []
	sentence = []
	
	with open(file, 'r', encoding=encoding, errors='ignore') as f:
		for line in f:
			line = line.strip()
			if line.startswith('-DOCSTART-'):
				if document:
					collection.append(document)
					document = []
			elif line:
				token_ = line
				parts = token_.split()
				if language == 'es':
					word, pos, chunk, ner = parts[0], parts[1], parts[2], parts[3]
					sentence.append(Token(word, pos, chunk, ner))
					# sentence.append(token_)
				elif language == 'deu':
					word, lemma, pos, chunk, ner = parts[0], parts[1], parts[2], parts[3], parts[4]
					sentence.append(DeuToken(word, lemma, pos, chunk, ner))
			else:
				if sentence:
					document.append(sentence)
					sentence = []

	if document:
		collection.append(document)

	return collection


# def preprocess


# python3 implementation/corpus.py corpora/conll2003/eng/train/eng.train

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Corpus preprocessing')

	parser.add_argument('PATH',
						help="Path to file with en NER annotations.")
	parser.add_argument('PATH_DEU',
						help="Path to file with deu NER annotations.")

	args = parser.parse_args()

	X = read_conll_data(args.PATH)
	# first en sentence 
	sent = X[0][0]
	for entity in sent:
		print(entity.__str__())

	X2 = read_conll_data(args.PATH_DEU, encoding='latin-1', language='deu')
	# first deu sentence
	sent = X2[0][0]
	for entity in sent:
		print(entity.__str__())

