MISSION
=======

**Data**: You will provide at least 100 twitter accounts with at least 50 accounts that are bots. This is the most important part of this milestone and you will be graded in how you harvest the accounts. If you have many of the same accounts as another group you will get no credit! See the papers a

**Data Sources**: 
---
* List of members for Bots - [https://twitter.com/ckolderup/lists/the-fall-of-humanity/members](https://twitter.com/ckolderup/lists/the-fall-of-humanity/members) `got reference from` [this](https://twitter.com/shiffman/lists/bots)

       -  __REST API call__ - [https://api.twitter.com/1.1/lists/members.json?owner_screen_name=ckolderup&slug=the-fall-of-humanity&count=500](https://api.twitter.com/1.1/lists/members.json?owner_screen_name=ckolderup&slug=the-fall-of-humanity&count=500)


* Twitter List of Members for verified Humans - [https://twitter.com/verified/lists/verified-accounts?lang=en](https://twitter.com/verified/lists/verified-accounts?lang=en)

       -  __REST API call__ - [https://api.twitter.com/1.1/lists/members.json?owner_screen_name=verified&slug=verified-accounts&count=500](https://api.twitter.com/1.1/lists/members.json?owner_screen_name=verified&slug=verified-accounts&count=500)
       
       
The CSV structure is as follow.
	
| #             | Name          |
| ------------- |:-------------:|
|1|id|
|2|Id_str|
|3|Screen_name|
|4|Location|
|5|Description|
|6|Url|
|7|Followers_count|
|8|Friends_count|
|9|Listed_count|
|10|Created_at|
|11|Favourites_count|
|12|Verified|
|13|Statuses_count|
|14|Lang|
|15|Status|
|16|Default_profile|
|17|Default_profile_image|
|18|Has_extended_profile|
|19|name|
|20|Bot|

The json file are converted using `jsonToCsv.py` to create the csv with the above structure.