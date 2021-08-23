#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:52:37 2021

@author: amaancharaniya
"""

import os
os.chdir('/Users/amaancharaniya/Documents/Keys')

#---------- Twitter API ----------#

import tweepy
twitter = importlib.import_module('start_twitter')
api = twitter.client

# See rate limit
limit = api.rate_limit_status()
limit.keys() ##look at dictionary's keys
# prepare for dictionaries all the way down

limit["resources"] ## another dictionary
limit["resources"].keys()
limit["resources"]["tweets"] ## another dictionary!!

for i in limit["resources"]["tweets"].keys():
    print(limit["resources"]["tweets"][i]) ## another dictionary!

# Create user objects
wustl = api.get_user('@WUSTLPoliSci')
wustl # biiiig object 

# Check type and methods
type(wustl)
dir(wustl)

# Trying some of these methods
print(wustl.id)
print(wustl.name)
print(wustl.screen_name)
print(wustl.location)

# Check his tweets
joe.status # last tweet
joe.status.text # text
joe.status._json # .json file
joe.statuses_count # tweet ID
# a list of tweepy methods https://www.geeksforgeeks.org/python-user-object-in-tweepy/

# Check his number of followers
wustl.followers_count
wustl.friends_count
wustl.friends
wustl.followers(ids)

api.get_user(3314329218).followers_count


# Screen names
[f.screen_name for f in joe_20]

# up to 200 (limit)
joe_200 = api.followers(joe.id, count = 200) ## up to 200
[f.screen_name for f in joe_200]
len(joe_200)

# A more round-about way, look up each user
joe_5000 = joe.followers_ids() #creates a list of user ids - up to 5000
len(joe_5000)
joe_5000[0]

api.get_user(2695008333).screen_name
    
follow_dic = {}
# Get followers geo location
for follower_id in wustl.followers_ids()[0:2]:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        count = user.followers_count
        follow_dic[handle] = count
        

max_follow = max(follow_dic, key = follow_dic.get)
#Answer is @BrendanNyhan

print("Q1: \nOf WUSTLPoliSci's followers, the account who is most popular is {}.".format(max_follow))


tweet_dic = {}
for follower_id in wustl.followers_ids()[1:10]:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweets = api.get_user(follower_id).statuses_count
        tweet_dic[handle] = tweets

max_tweets = max(tweet_dic, key = tweet_dic.get)
        
print("Q2: \nOf WUSTLPoliSci's followers, the account who is most active is {}.".format(max_tweets))


friend_dic = {}
# Get followers geo location
for friend_id in wustl.friends_ids()[0:3]:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        count = user.followers_count
        friend_dic[handle] = count

max_friend = max(friend_dic, key = friend_dic.get))


print("Q3: \nOf WUSTLPoliSci's friends, the account who is most popular is {}.".format(max_friend))


# Normally count = 200 is limit, let's go around that.

# By default, each method returns the first page, 
# which usually contains a few dozen items.
# We can define the pagination manually to get more results
# joe_statuses = []
# for p in range(0, 10):
# 	# extend gets the entire tweet
# 	joe_statuses.extend(api.user_timeline(id = 'JoeBiden', page = i, count = 20))

# joe_statuses[0].text
# joe_statuses[len(joe_statuses)-1].text

# # How was it tweeted?
# source = [x.source for x in joe_statuses]
# source

# # Print tweets with source equal to iPhone
# [x.text for x in joe_statuses if x.source == "Twitter for iPhone"]


# Cursor performs pagination easily for you
# iterate through the first 20 statuses in the timeline
histweets20 = [] ## tweet objects
for status in tweepy.Cursor(api.user_timeline, id = 'JoeBiden').items(20):
    histweets20.append(status)    
len(histweets20)
histweets20[0].text

histweets50 = [] ## tweet objects
for status in tweepy.Cursor(api.user_timeline, id = 'JoeBiden').items(50):
    histweets50.append(status)    
len(histweets50)
set(zip([i.text for i in histweets50],[j.created_at for j in histweets50]))

# iterate through all of the status...although this is a little sketchy and unrealiable
histweets = [] ## tweet objects
for status in tweepy.Cursor(api.user_timeline, id = 'JoeBiden').items():
    histweets.append(status)
len(histweets) # for some weird reason, it is returning a random number of status

# You should definitely hit the rate limit here.....
hisfollowers = []
for item in tweepy.Cursor(api.followers, 'JoeBiden').items():
	hisfollowers.append(item)
len(hisfollowers)