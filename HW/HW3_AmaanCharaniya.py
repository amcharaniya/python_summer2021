#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:52:37 2021

@author: amaancharaniya
"""

import os
import operator
os.chdir('/Users/amaancharaniya/Documents/Keys')

#---------- Twitter API ----------#

import tweepy
twitter = importlib.import_module('start_twitter')
api = twitter.client

# Create user objects
wustl = api.get_user('@WUSTLPoliSci')

    
#First Degree of Separation

follow_dic = {} #creating a dictionary to store the handles and follower counts of Wustl's followers
tweet_dic = {} #creating a dictionary to store the handles and tweet counts of Wustl's followers
for follower_id in wustl.followers_ids():
        user = api.get_user(follower_id)
        handle = user.screen_name
        tweets = user.statuses_count
        count = user.followers_count
        tweet_dic[handle] = tweets
        follow_dic[handle] = count 
print(tweet_dic.values)
max_follow = max(follow_dic, key = follow_dic.get) #getting the maximum followers or most popular
max_tweets = max(tweet_dic, key = tweet_dic.get) #getting the maximum tweets or most active

print("Q1: \nOf WUSTLPoliSci's followers, the account who is most popular is {}.".format(max_follow)) #printing answer   
#Q1: Of WUSTLPoliSci's followers, the account who is most popular is BrendanNyhan.
print("Q2: \nOf WUSTLPoliSci's followers, the account who is most active is {}.".format(max_tweets)) #printing answer  
#Q2: Of WUSTLPoliSci's followers, the account who is most active is TheNjoroge.

friend_dic = {} #creating a dictionary to store the handles and tweets of wustl's friends
friend_tweet_dic = {} #creating a dictionary to store the handles and followers of wustl's friends
# Get followers geo location
for friend_id in api.friends_ids('@WUSTLPoliSci'):
    try:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        count = user.followers_count
        tweet = user.statuses_count
        friend_tweet_dic[handle] = tweet
        friend_dic[handle] = count      
    except:
    	time.sleep(15*60)
max_friend = max(friend_dic, key = friend_dic.get) #getting the maximum tweets or most active
max_active = max(friend_tweet_dic, key = friend_tweet_dic.get) #getting the maximum follwoers or most popular

print("Q3: \nOf WUSTLPoliSci's friends, the account who is most popular is {}.".format(max_friend)) #printing answer
#Q3: Of WUSTLPoliSci's friends, the account who is most popular is BarackObama.
print("Q4: \nOf WUSTLPoliSci's friends, the account who is the most active is {}.".format(max_active)) #printing answer
#Q4: Of WUSTLPoliSci's friends, the account who is the most active is nytimes.


        
#Two Degrees of Separation

followers = [] #creating list to store ids of wustl's followers
followeroffollower_tweet_dic1 = {} #creating dictionary to store layman handles and tweets
followeroffollower_tweet_dic2 = {} #creating dictionary to store expert handles and tweets
followeroffollower_tweet_dic3 = {} #creating dictionary to store celebrity handles and tweets

#Using 3 if/else statements to store all followers in appropriate category
for follower_id in api.followers_ids('@WUSTLPoliSci'):
    if api.get_user(follower_id).followers_count <= 100:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweet = user.statuses_count
        followeroffollower_tweet_dic1[handle] = tweet
        followers += api.followers_ids(follower_id)
    else:
        pass
    if 100 < api.get_user(follower_id).followers_count <= 1000:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweet = user.statuses_count
        followeroffollower_tweet_dic2[handle] = tweet
        followers += api.followers_ids(follower_id)
    else:
        pass
    if api.get_user(follower_id).followers_count > 1000:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweet = user.statuses_count
        followeroffollower_tweet_dic3[handle] = tweet
        followers += api.followers_ids(follower_id)
    else:
        pass

#Using same 3 statements to put followers of followers in appropriate category 
for follower_id in followers[0:3]:
    if api.get_user(follower_id).followers_count <= 100:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweet = user.statuses_count
        followeroffollower_tweet_dic1[handle] = tweet
    else:
        pass
    if 100 < api.get_user(follower_id).followers_count <= 1000:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweet = user.statuses_count
        followeroffollower_tweet_dic2[handle] = tweet
    else: 
        pass
    if api.get_user(follower_id).followers_count > 1000:
        user = api.get_user(follower_id)
        handle = api.get_user(follower_id).screen_name
        tweet = user.statuses_count
        followeroffollower_tweet_dic3[handle] = tweet
    else: 
        pass

#Maximizing activity in each category
maxfollow_tweet1 = max(followeroffollower_tweet_dic1, key = followeroffollower_tweet_dic1.get)
maxfollow_tweet2 = max(followeroffollower_tweet_dic2, key = followeroffollower_tweet_dic2.get)
maxfollow_tweet3= max(followeroffollower_tweet_dic3, key = followeroffollower_tweet_dic3.get)


#printing all 3 answers
print("Q5: \nOf WUSTLPoliSci's friends with less than 100 followers, the account who is the most active is {}.\nOf WUSTLPoliSci's friends with more than 100 followers but less than 1000 followers, the account who is the most active is {}.\nOf WUSTLPoliSci's friends with more than 1000 followers, the account who is the most active is {}." .format(maxfollow_tweet1, maxfollow_tweet2, maxfollow_tweet3))


#Repeating the process but with friends instead of followers
friends = []
friendoffriend_tweet_dic1 = {}
friendoffriend_tweet_dic2 = {}
friendoffriend_tweet_dic3 = {}
for friend_id in api.friends_ids('@WUSTLPoliSci')[0:3]:
    if api.get_user(friend_id).followers_count <= 100:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        tweet = user.statuses_count
        friendoffriend_tweet_dic1[handle] = tweet
        friends += api.friends_ids(friend_id)
    else:
        pass
    if 100 < api.get_user(friend_id).followers_count <= 1000:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        tweet = user.statuses_count
        friendoffriend_tweet_dic2[handle] = tweet
        friends += api.friends_ids(friend_id)
    else:
        pass
    if api.get_user(friend_id).followers_count > 1000:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        tweet = user.statuses_count
        friendoffriend_tweet_dic3[handle] = tweet
        friends += api.friends_ids(friend_id)
    else:
        pass
        
for friend_id in friends[0:3]:
    if api.get_user(friend_id).followers_count <= 100:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        tweet = user.statuses_count
        friendoffriend_tweet_dic1[handle] = tweet
    else:
        pass
    if 100 < api.get_user(friend_id).followers_count <= 1000:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        tweet = user.statuses_count
        friendoffriend_tweet_dic2[handle] = tweet
    else: 
        pass
    if api.get_user(friend_id).followers_count > 1000:
        user = api.get_user(friend_id)
        handle = api.get_user(friend_id).screen_name
        tweet = user.statuses_count
        friendoffriend_tweet_dic3[handle] = tweet
    else: 
        pass


maxfriend_tweets1 = max(friendoffriend_tweet_dic1, key = friendoffriend_tweet_dic1.get)
maxfriend_tweets2 = max(friendoffriend_tweet_dic2, key = friendoffriend_tweet_dic2.get)
maxfriend_tweets3 = max(friendoffriend_tweet_dic3, key = friendoffriend_tweet_dic3.get)


print("Q6: \nOf WUSTLPoliSci's friends with less than 100 followers, the account who is the most active is {}.\nOf WUSTLPoliSci's friends with more than 100 followers but less than 1000 followers, the account who is the most active is {}.\nOf WUSTLPoliSci's friends with more than 1000 followers, the account who is the most active is {}." .format(maxfriend_tweets1, maxfriend_tweets2, maxfriend_tweets3))

