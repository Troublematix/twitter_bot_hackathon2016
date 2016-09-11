#!/usr/local/virtualenvs/ds-py3/bin/python
import json
import tweepy
from time import sleep

SECRETS_FILE = "secrets.json"
CHECK_INTERVAL = 5


def main():
    # Twitter API setup
    with open(SECRETS_FILE) as f:
        secrets = json.load(f)
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])
    api = tweepy.API(auth)

    while(True):
        search = api.search("#motivaSparta")
        for x in range(0, len(search)):
            print search[x].text
            try:
                api.update_status("@{} This is SPARTA, GRRRR!!!!!!!!!!".format(search[x].user.screen_name),
                                  search[x].id)

            except tweepy.error.TweepError as e:
                print(repr(e))
                continue
        sleep(CHECK_INTERVAL)

    # search = api.search("#xmotivaSparta")
    # for x in range(0, len(search)):
    #     try:
    #         # api.update_status("This is SPARTA, GRRRR!!!!!!!!!!", search[x].id, IMG)
    #         h = api.media_upload("sparta.jpg")
    #         print h
    #     except tweepy.error.TweepError as e:
    #         print(repr(e))
    #         next

if __name__ == '__main__':
    main()
