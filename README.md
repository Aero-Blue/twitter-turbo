# twitter-turbo
Proof of concept twitter username turbo using Tweepy, the idea of a turbo is to instantly take a username once it is available. This is an extremely fast and simple concept which can definitely be improved. Ideally you would only run this when you knew the name was becoming available because you will hit ratelimits

## Get your API keys: 

[Apply for Access](https://developer.twitter.com/en/apply-for-access)

[Access Tokens Guide](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)

## Config.py:

In order to have read/write access to a twitter account, all keys and tokens must be provided by the user.

Copy and paste the appropriate keys/tokens into the file:

- api_key

- api_secret_key

- access_token

- access_token_secret

## Running twitter.py

Once you run the program it will continue attempting the name change until it is closed.

## Logging

Logs will be stored in twitter.log for debugging issues.
