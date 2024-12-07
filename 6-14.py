# An influencer is a person who can influence other people's behaviour. 
# An influencer communicates with other people using social networking sites. 
# Write a program that checks whether a given person is a good influencer, that is, 
# whether the person has at least two of the following accounts: Facebook, Twitter or Instagram.
# Use logical type variables: facebook, twitter, instagram, the value of which indicates whether
#  the person has an account on the social networking site.

# Sample result:
# facebook = True
# twitter = False
# instagram = True
# You are a good influencer!

print("Do you have...")
s_facebook = input("Facebook? (Y/N): ")
s_instagram = input("Instagram? (Y/N): ")
s_twitter = input("Twitter? (Y/N): ")

if s_facebook.upper() == "Y":
    facebook = True
else:
    facebook = False

if s_instagram.upper() == "Y":
    instagram = True
else:
    instagram = False

if s_twitter.upper() == "Y":
    twitter = True
else:
    twitter = False

# facebook = True
# twitter = False
# instagram = True

apps = [facebook, twitter, instagram]
apps_count = 0


for app in apps:
    if app == True:
        apps_count += 1 


if apps_count >= 2:
    print("You are a good influencer!")
else:
    print("You are not so good at influencing... ")


