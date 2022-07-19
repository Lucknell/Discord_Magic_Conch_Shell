from discord.ext import commands
import random

class Magic(commands.Cog):#class declaration for the command %magic
    def __init__(self, bot):#a default init function where we can pass the client variable made in the conch.py file
        self.bot = bot#setting a local copy of the bot variable(This is the client variable from the main function)

    @commands.command()
    async def magic(self, ctx, name, *, args):#an function to define the command %magic with the params
	#self for local class variables. ctx which is the discord context for the trigger message. name which will be the first word of a message. args which will be everything else after that
        if not name.lower() == "conch":#only trigger if the command started like "%magic conch" 
            return#leave if the above was not met
        choices = ["https://tenor.com/view/conch-spongebob-squarepants-magic-conch-no-nope-gif-17942465",#3 magic conch answer shell gifs 
        "https://tenor.com/view/spongebob-conch-gif-4612648",
        "https://tenor.com/view/magic-conch-shell-spongebob-yes-gif-7322577"]
        finisher = ["https://tenor.com/view/the-shell-has-spoken-magic-gif-19450862",#2 more generic gifs 
        "https://tenor.com/view/spongebob-patrick-magic-conch-shell-gif-5486197"]
        await ctx.send(choices[random.randint(0,len(choices) - 1)])#send a random answer gif after the question was asked
        await ctx.send(finisher[random.randint(0, len(finisher) - 1)])#send a random follow up after the answer like the shell has spoken

def setup(bot):#setup function to add a command from a class to a bot
    bot.add_cog(Magic(bot))#add the class Magic to the bot variable that was passed from the conch.py file