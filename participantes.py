from TwitterSearch import *

consumer_key = 'pO2AZzVpZqg0JLphPfBbAYLfF'
consumer_secret = 'qERo7rHc4YmO4u3LySeh7rVEdUSbW4C5d3MkmGg23MRuOwx50r'
access_token = '237497963-5fcUBCDgDEArEJk3w2A2dNmI1lovytFrdyXFhlCw'
access_secret = 'ZDYNX5ULWEQtpXWBdldRZMjZjhjsgKK7T0MoMrbLQx2iW'

users = []

def get ():
  participantes = []

  try:
      tso = TwitterSearchOrder() # create a TwitterSearchOrder object
      tso.set_keywords(['#potilivreoeste']) # let's define all words we would like to have a look for
      tso.set_include_entities(False) # and don't give us all those entity information

      # it's about time to create a TwitterSearch object with our secret tokens
      ts = TwitterSearch(
          consumer_key = consumer_key,
          consumer_secret = consumer_secret,
          access_token = access_token,
          access_token_secret = access_secret
      )

      # this is where the fun actually starts :)
      for tweet in ts.search_tweets_iterable(tso):
          if not tweet['user']['screen_name'] in users:
            users.append(tweet['user']['screen_name'])

      for user in users:
        if not user == 'potilivre':
          participantes.append(user)

  except TwitterSearchException as e: # take care of all those ugly errors if there are some
      print(e)

  return participantes
