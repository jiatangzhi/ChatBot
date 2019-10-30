""" This is the dictionary for the chatbot"""

keywords = dict()

keywords['you'] = 1
keywords['you?'] = 1
keywords['yourself?'] = 1
keywords['yourself'] = 1
keywords['u'] = 1

convo_words = dict()

convo_words['okay'] = 1
convo_words['good'] = 2
convo_words['great'] = 3
convo_words['not'] = -4
convo_words['brilliant'] = 3
convo_words['sad'] = -1
convo_words['tired'] = 0
convo_words['bored'] = 0
convo_words['fine'] = 1
convo_words['upset'] = -1
convo_words['alright'] = 1
convo_words['not bad'] = 1
