from random import choice
from collections import Counter
import nltk

class ELN(object):

	def __init__(self):
		self.word_list = {}
		self.rules = []

	def log(self, label, msg):
		print "[%s]: %s" % (label, msg)

	def generate(self):
		sentence = ""
		rules = choice(self.rules)[1:]
		for part in rules.split("|"):
			try:
				word = 
choice(self.word_list[part]).strip()
				sentence += "%s " % word
			except Exception as e:
				print "%s not defined" % part
		return sentence.replace(" 's", "'s")

	def loadFile(self, file_name):
		f = open(file_name, "r") #DO NOT REUSE ARTICLES
		texts = f.read()
		f.close()
		return texts.split("\n")	

	def generateRules(self):
		texts = self.loadFile("article.txt")
		for text in texts: #Generate sentence rules
			text_ = nltk.word_tokenize(text)
			text_ = nltk.pos_tag(text_)
			i, x = 0, 0
			while i < len(text_):
				rule = ""
				x = ""
				while x != ".":
					try:
						x = text_[i][1]
						rule += "|%s" % x
						i += 1
					except Exception as e:
						break
				self.rules.append(rule)

	def addWords(self):
		texts = self.loadFile("article.txt")
		for text in texts: #Add words to word_list
			raw = nltk.word_tokenize(text)
			raw = nltk.pos_tag(raw)
			for word in raw:
				print word
				try:
					typ = word[1]
					if self.word_list.has_key(typ):
						if word[0] in 
self.word_list[typ]:
							pass
						else:
							
self.word_list[typ].append(word[0])
					else:
						self.word_list[typ] = []
						
self.word_list[typ].append(word[0])
				except Exception as e:
					pass
		print "Task completed"

	def extractTopic(self, text):
		self.log("INPUT", text)
		rules = ["NN|NN", "JJ|JJ", "VBP|NNS", "VBG|NN", 
"VBG|NNS", "JJ|NN", "JJS|NN", "NNP|NNP"]
		text = nltk.pos_tag(nltk.word_tokenize(text))
		topics = []
		nnp = False
		nns = False
		print text
		for i, part in enumerate(text):
			if part[1] == "IN":
				del text[i]
		for i, part in enumerate(text):
			try:
				if part[1] == "NNS" and nns == False:
					topics.append(' %s' % part[0])
				if part[1] == "NNP" and nnp == False:
					nnp = True
					print part[1]
					topics.append(' %s' % part[0])				
				if '|'.join([part[1], text[i+1][1]]) in 
rules:
					topic = ' '.join([part[0], 
text[i+1][0]])
					if topic not in topics and "." 
not in topic:
						topics.append(topic)
			except Exception as e:
				pass
		self.log("EXTRACTED", str(topics))
		#Let's narrow down the topic
		narrowed = []
		if len(topics) > 1:
			for topic in topics:
				if " " in topic:
					narrowed.append(topic)
			topics = narrowed
		#Let's now clean chained NN|NN and JJ|JJ
		for i, topic in enumerate(topics):
			try:
				if topic.split(' ')[1] == 
topics[i+1].split(' ')[0]:
					topics[i] = ' 
'.join([topic.split(' ')[0], topics[i+1]])
					del topics[i+1]
			except Exception as e:
				pass
		topics = [x.strip() for x in topics]
		self.log("NARROWED TOPIC", str(topics))
		return topics



#Example with dark poem
"""
Task completed
on how it see hoping to Of 
in how you lie turning to dust, 
about all day As my fear 
the me look yet turn to come now 
that once thou , My parents do closed ? 
now so one demon 
it gets to Thou 
but keeps me do hiding off Thou . 
The Wicked Of Path Destiny 
The it do rust quench to burn there 
he are that chance of lurk, room, tilt 
So how me do turning to Destiny 
weeping to Path 
My lie hiding 
that soul thou , my dreams walk torn ? 
thirst, And now ? 
My parents shall have in, 
that room, smirk , my bones look lie . 
that bad mans , that old back 
n't off one back 
""" 






