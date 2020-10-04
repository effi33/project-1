import tweepy

import random

from authorization_tokens import *


word_list = ["grind", "blind", "wind"]
word_list = ["politics", "bricks", "ticks"]

template_list = ["In waking numb and bleeding {}, Gears and chains in systems {}, We wade and break and build and {}. Lungs and lakes filled with {}, Feasts and grounds for fragrant {}, Just simulacra of strong {}."]

random_number = random.randrange( len (template_list))
template = template_list[random_number]

random_number = random.randrange( len(word_list))
word1 = word_list[random_number]

random_number = random.randrange( len(word_list))
word2 = word_list[random_number]

random_number = random.randrange( len(word_list))
word3 = word_list[random_number]

random_number = random.randrange( len(word_list))
word4 = word_list[random_number]

random_number = random.randrange( len(word_list))
word5 = word_list[random_number]

random_number = random.randrange( len(word_list))
word6 = word_list[random_number]

message = template.format(word1, word2, word3, word4, word5, word6)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
