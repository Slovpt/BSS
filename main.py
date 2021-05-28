import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = ";")

@client.event
async def on_member_join(person):
  print("h")
  MemberRole = discord.utils.get(person.guild.roles, name='Member')
  await person.add_roles(MemberRole)


@client.event
async def on_ready():
  print("Bot is ready to be used.")


@client.command(help="(Shows your current ping)")
async def ping(ctx):
  await ctx.send(f' Pong! Oh look at that, {round(client.latency * 1000)}ms')

@client.command(pass_context=True, help="(Kicks the named user)")
async def kick_member(ctx, member : discord.Member, *, reason=None):
  if ctx.message.author.guild_permissions.administrator:
    await ctx.send(f' User has been kicked for {reason}!')
    await member.kick(reason=reason)
  else:
    await ctx.send("You don't have permission to use this.")
    return

@client.command(pass_context=True, help="(Bans the named user)")
async def ban_member(ctx, member : discord.Member, *, reason=None):
  if ctx.message.author.guild_permissions.administrator:
    await ctx.send(f' User has been permanently banned from the server for {reason}!')
    await member.ban(reason=reason)
  else:
    await ctx.send("You don't have permission to use this.")
    return

@client.command(pass_context=True, help="(Mutes the named user)")
async def mute_member(ctx, member : discord.Member):
  if ctx.message.author.guild_permissions.administrator:
    MutedRole = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(MutedRole)
    await ctx.send("User has been muted")
    return
  else:
    await ctx.send("You don't have permission to use this.")
    return

@client.command(pass_context=True, help="(Unmutes the named user)")
async def unmute_member(ctx, member : discord.Member):
  if ctx.message.author.guild_permissions.administrator:
    MutedRole = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(MutedRole)
    await ctx.send("User has been unmuted")
  else:
    await ctx.send("You don't have permission to use this.")
    return


client.run('ODQ2MjA5NDY0NzAwMzcwOTU1.YKsL-g.N_wsuAdRe-Vr37IrR9lkx9_kV9w')
