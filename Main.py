from Kite import KiteApi
import discord


class App:
    def __init__(self):
        #  API token for discord bot.
        with open("API keys/discord_app.txt", "r") as myfile:
            Token = myfile.readlines()[0]

        Kiteapp = KiteApi()
        client = discord.Client()

        @client.event
        async def on_ready():
            print("Bot running")
            # initialise exchange apis
            # start markets
            # log current portfolio
            pass

        @client.event
        async def on_message(message):
            pass

        client.run(Token)


if __name__ == '__main__':
    app = App()
