
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Member, TextChannel

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {bot.user}')

#LOCK UNLOCK CHANNELS

@bot.slash_command(name="lock", description="Կողպել տեքստային ալիքը.")
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: nextcord.TextChannel):
    embed = nextcord.Embed(color=nextcord.Color.red())
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed.add_field(name='Հաջողությամբ փակվեց ✅', value=f'{channel.mention} Զրուցարանը փակվեց. 🔒')
    await ctx.send(embed=embed)

@bot.slash_command(name="unlock", description="Բացել տեքստային ալիքը.")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: nextcord.TextChannel):
    embed = nextcord.Embed(color=nextcord.Color.green())
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed.add_field(name='Հաջողությամբ բացվեց ✅', value=f'{channel.mention} Զրուցարանը բացվեց. 🔓')
    await ctx.send(embed=embed)

bot.run('YOUR_TOKEN')
