import smtplib, ssl, getpass, twitter, json

my_api = twitter.Api(consumer_key='mgwDK6fgRv8V6J1ZFErk2fUI4',
                    consumer_secret='PMBJKxBWzmcjVYzkPAw1YnAZh9ExtxsSrft7ZR7vJndGg8ofaS',
                    access_token_key='1012650702-pDmAe9xJMeL2NgDcPf2kHLSzrUbtOxVWTxNtsgu',
                    access_token_secret='3XVTWPseYPkvzWhFUH9NWM8x6I7ygYlwehXz3aUIJLxyp')

id_file = open("last_id.txt", 'r')
last_id = id_file.read()
id_file.close()

new_last_id = last_id

timeline = my_api.GetUserTimeline(screen_name='dril', since_id=last_id)
email = ""
got_id = False

for tweet in timeline:
    if not(got_id):
        got_id = True
        new_last_id = str(tweet.id)
    email += json.dumps(tweet.text) + '\n\n'

id_file = open("last_id.txt", 'wt')
id_file.write(new_last_id)
id_file.close()

if len(email) != 0:
    password = getpass.getpass("pw: ")
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("samprattdev@gmail.com", password)
    server.sendmail("samprattdev@gmail.com", "sampratt6@gmail.com", email)
else:
    print("no new tweets")