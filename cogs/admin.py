import os
import discord
import json

from discord.ext import commands
from funs import assignation, date

with open('config.json') as f:
    config = json.load(f)
owner = config.get('owners')


class Admin:
    def __init__(self, bot):
        self.bot = bot


    #Group Rotation (Tuesday & Wednesday)
    @commands.command(pass_context=True)
    async def roll(self, ctx):
        listG1 = []
        listG2 = []
        listG3 = []
        listG1A = []
        listG2A = []
        listG3A = []
        channel = ctx.message.channel

        if(ctx.message.author.id == owner):
            #Groups recovery
            for member in self.bot.get_all_members(): 
                try:
                    print("This is: " + member.display_name + " " + member.id + " " + str(member.roles[2]) + " & " + str(member.roles[1]))

                    if(str(member.roles[2]) == "G1"):
                        listG1.append(member.display_name)
                        
                    if(str(member.roles[2]) == "G2"):
                        listG2.append(member.display_name)

                    if(str(member.roles[2]) == "G3"):
                        listG3.append(member.display_name)

                    if(str(member.roles[1]) == "G1A"):
                        listG1A.append(member.display_name)
                        
                    if(str(member.roles[1]) == "G2A"):
                        listG2A.append(member.display_name)

                    if(str(member.roles[1]) == "G3A"):
                        listG3A.append(member.display_name)
                except Exception as e:
                    print("{} : [{}]".format(member.display_name,e))

            print(listG1) 
            print(listG2)
            print(listG3)

    #         #Calling assignation function
            assigner = assignation.Assignation_roles_random(0, 1, len(listG1)-1)
    #        logger.info("G1 : {}".format(assigner))
            tirLeader1 = listG1[assigner['leader']]
            tirSecret1 = listG1[assigner['secretaire']]
            tirScrib1 = listG1[assigner['scribe']]
            tirTkeeper1 = listG1[assigner['gestionnaire']]
            
            #Calling assignation function
            assigner = assignation.Assignation_roles_random(0, 2, len(listG2)-1)
    #        logger.info("G2 : {}".format(assigner))
            tirLeader2 = listG2[assigner['leader']]
            tirSecret2 = listG2[assigner['secretaire']]
            tirScrib2 = listG2[assigner['scribe']]
            tirTkeeper2 = listG2[assigner['gestionnaire']]       

            #Calling assignation function
    #         assigner = assignation.Assignation_roles_random(0, 3, len(listG3)-1)
    # #        logger.info("G3 : {}".format(assigner))
    #         tirLeader3 = listG3[assigner['leader']]
    #         tirSecret3 = listG3[assigner['secretaire']]
    #         tirScrib3 = listG3[assigner['scribe']]
    #         tirTkeeper3 = listG3[assigner['gestionnaire']]
            day = " ".join(date.getDateInList())

            await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n```fix\n{0}\n```".format(day))
            await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629943918985237>:```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'\n```".format(tirLeader1, tirSecret1, tirScrib1, tirTkeeper1))
            await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629942371287043>:```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'\n```".format(tirLeader2, tirSecret2, tirScrib2, tirTkeeper2))
    #         # await bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629949572907028>:\n ```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'```\n".format(tirLeader3, tirSecret3, tirScrib3, tirTkeeper3))
        else:
            messages = []
            await self.bot.send_message(channel,"`\nYou're not allowed to\n`")
            async for message in self.bot.logs_from(channel, 1):
                messages.append(message)
            await self.bot.delete_messages(message)
            

    #Clear function
    @commands.command(pass_context = True)
    async def clear(self, ctx, amount=99):
        if(ctx.message.author.id == owner):
            channel = ctx.message.channel
            messages = []
            async for message in self.bot.logs_from(channel, limit=int(amount+1)):
                messages.append(message)
            numberOfMessages = len(messages)-1
            await self.bot.delete_messages(messages)
            await self.bot.send_message(channel,'` {} messages deleted`'.format(numberOfMessages))
            
            async for message in self.bot.logs_from(channel, 1):
                messages.append(message)
            await self.bot.delete_messages(messages)
        else:
            await self.bot.send_message(channel,"`\nYou're not allowed to\n`")
            async for message in self.bot.logs_from(channel, 1):
                messages.append(message)
            await self.bot.delete_messages(messages)

    @commands.command(pass_context = True)
    async def s(self, ctx):
        if(ctx.message.author.id == owner or ctx.message.author.id == '124598335230312448' or ctx.message.author.id == '360765827294953472'):
            message = ctx.message.content
            try:
                temp = message.split(' ', 2)
                toTry = temp[1]
            except Exception:
                toTry = 0

            if(toTry == "-a"):
                id = '375268017011163157'
                await self.bot.send_message(discord.Object(id=id), temp[2])
            elif(toTry == '-g'):
                id = '499165605790875658'
                await self.bot.send_message(discord.Object(id=id), temp[2])
                id = '499165797038555146'
                await self.bot.send_message(discord.Object(id=id), temp[2])
            elif(toTry == '-g1'):
                id = '499165605790875658'
                await self.bot.send_message(discord.Object(id=id), temp[2])
            elif(toTry == '-g2'):
                id = '499165797038555146'
                await self.bot.send_message(discord.Object(id=id), temp[2])
            else:
                await self.bot.send_message(ctx.message.channel, "```fix\n-a  : annonce\n-g  : groupes\n-g1 : groupe 1\n-g2 : groupe 2\n```")
                
            


def setup(bot):
    bot.add_cog(Admin(bot))