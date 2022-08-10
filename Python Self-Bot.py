import os
import base64
import discord
from datetime import datetime
from discord.ext import commands

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

client = commands.Bot(command_prefix="Enter a prefix", self_bot=True, help_command=None) # Enter a good prefix like .
auth_token = "Your Authorization Token"

@client.event # event
async def on_ready(): # what to do when self-bot is online and connected to the authorization token
    os.system("cls")
    print("Self-Bot Is Online And Ready. (" + current_time + ")")
    

@client.command() # command
async def time(ctx):  # {prefix}time
    await ctx.send(f"```{current_time}```")
    
    
@client.command() # command
async def spam(ctx, *, args = None): # by adding "*, args" you can use more than 1 word as a parameter / input for the command
    await ctx.message.delete()
    if args is None:
        await ctx.send("```No Arguments Entered.```")
    else:
        while 1 == 1: #while loop
            await ctx.send(args)
    

@client.command()
async def b64(ctx, type = None, *, args = None): # usage: {prefix}b64 encode {message}  / {prefix}b64 decode {message}
    await ctx.message.delete()
    if type is None:
        await ctx.send("```No Type Entered. (encode / decode)```")
    if args is None:
        await ctx.send("```No Arguments Entered.```")
    else:
        if type == "encode" or type == "Encode":
            EB = base64.b64encode(args.encode("utf-8"))
            ESTR = str(EB, "utf-8")
            print(current_time + " b64:")
            print(f"Message: {args}")
            print(f"Encoded Message: {ESTR}")
            await ctx.send(f"""```
 == Base64 == 
Message: Check Python Terminal For Message!\n
Encoded Message: {ESTR}
```""", delete_after=10)
            
        if type == "decode" or type == "Decode":
            DB = base64.b64decode(args)
            DSTR = str(DB, "utf-8")
            print(current_time + " b64:")
            print(f"Encoded Message: {args}")
            print(f"Decoded Message: {DSTR}")
            await ctx.send(f"""```
Encoded Message: {args}
\nDecoded Message: {DSTR}```""", delete_after=10)

client.run(auth_token, bot=False)
