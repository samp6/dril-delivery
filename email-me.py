import smtplib, ssl, getpass, twitter, json
import config

my_api = twitter.Api(config.consumer_key,
                    config.consumer_secret,
                    config.access_token_key,
                    config.access_token_secret)

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
    server.login(config.sending_email, password)
    server.sendmail(config.sending_email, config.receiving_email, email)
else:
    print("no new tweets")