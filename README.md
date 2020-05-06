# dril-delivery
A very simple, bare-bones Python script that pulls Twitter user Dril's most recent Tweets and emails them to you. 

It's a bit rough, and you need a couple of things to make it work. 

In a config.py file in the same directory, you need:
- the API keys from a Twitter dev account (I have mine stored privately)
- the email you're sending from
- the email you're sending too

It also creates a file called last_id.txt that stores the id of the most recent Tweet when running the script, so next time it will pick up where it left off. 

This project is more an example than a functioning public script, so I don't feel bad about publishing an "unfinished" project. 
