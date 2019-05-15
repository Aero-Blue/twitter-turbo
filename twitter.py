import tweepy
import logging
import config


class TwitterTurbo:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        """
        Create an app @ https://developer.twitter.com/en/apps/create
        Authentication info is found under YOURAPP > Details > Keys and tokens
        You can always regenerate your keys if something isn't working
        All logs are kept in the turbo.log file (current dir)
        """
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        # Logging settings
        self.logger = logging.getLogger("Turbo")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s: %(message)s", datefmt="%m/%d %I:%M %p"
        )
        file_handler = logging.FileHandler(filename="turbo.log")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.info("Initializing script...")
        # Functions
        self.authenticate()
        self.change_screen_name()

    def authenticate(self):
        """
        Authenticates user via api tokens and keys
        If auth fails
        """
        self.logger.info("Attempting authentication...")
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
        try:
            self.api.me()
            self.logger.info("Authentication was successful!")
        except tweepy.error.TweepError as error:
            resp = error.response.json()["errors"][0]
            self.logger.info("Authentication failed.")
            logger.error("{} ({})".format(resp["message"], resp["code"]))
        finally:
            return

    def change_screen_name(self):
        self.logger.info("Attempting namechange...")
        try:
            status = self.api.update_profile(screen_name="treeboy")
            self.logger.info("Name change successful!")
        except tweepy.TweepError as error:
            resp = error.response.json()["errors"][0]
            self.logger.info("Name change unsuccessful.")
            self.logger.error("{} ({})".format(resp["message"], resp["code"]))
        finally:
            return self


if __name__ == "__main__":
    TwitterTurbo(
        config.api_key,
        config.api_secret_key,
        config.access_token,
        config.access_token_secret,
    )
