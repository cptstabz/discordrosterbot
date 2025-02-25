import discord
import random
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)  


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  


bot = commands.Bot(command_prefix="!", intents=intents)

# tier tokens
classes = {
    "Evoker": "Zenith, Mail",
    "Monk": "Zenith, Leather",
    "Rogue": "Zenith, Leather",
    "Warrior": "Zenith, Plate",
    "Death Knight": "Dreadful, Plate",
    "Demon Hunter": "Dreadful, Leather",
    "Warlock": "Dreadful, Cloth",
    "Druid": "Mystic, Leather",
    "Boomkin Druid": "Mystic, Leather",
    "Feral Druid": "Mystic, Leather",
    "Hunter": "Mystic, Mail",
    "Mage": "Mystic, Cloth",
    "Paladin": "Venerated, Plate",
    "Priest": "Venerated, Cloth",
    "Shaman": "Venerated, Mail",
    "Elemental Shaman": "Venerated, Mail"
}

# required raid buffs
required_classes = {"Druid", "Paladin", "Monk", "Demon Hunter", "Rogue", "Mage", "Shaman", "Warrior", "Priest", "Evoker"}

# roles
roles = {
    "Tank": ["Druid", "Paladin", "Warrior", "Demon Hunter", "Death Knight"],
    "Healer": ["Priest", "Paladin", "Druid", "Monk", "Shaman", "Evoker"],
    "Melee DPS": ["Rogue", "Warrior", "Monk", "Demon Hunter", "Paladin", "Death Knight", "Feral Druid"],
    "Range DPS": ["Mage", "Elemental Shaman", "Evoker", "Priest", "Boomkin Druid", "Hunter", "Warlock"]
}

# main characters
mains = [
    ("Scurro - M", "Tank", "Death Knight"),
    ("Karp - M", "Tank", "Druid"),
    ("Magshock - M", "Healer", "Paladin"),
    ("Holybazoo - M", "Healer", "Paladin"),
    ("Kovah - M", "Healer", "Monk"),
    ("Tehkthyr - M", "Healer", "Shaman"),
    ("Bloodblain - M", "Healer", "Priest"),
    ("Tamikochan - M", "Healer", "Priest"),
    ("Akylix - M", "Melee DPS", "Demon Hunter"),
    ("Skëlly - M", "Melee DPS", "Demon Hunter"),
    ("Charley - M", "Melee DPS", "Monk"),
    ("Cptstabz - M", "Melee DPS", "Rogue"),
    ("Vynstabz - M", "Melee DPS", "Rogue"),
    ("Koby - M", "Melee DPS", "Paladin"),
    ("Urusa - M", "Melee DPS", "Warrior"),
    ("Chocksticks - M", "Melee DPS", "Warrior"),
    ("Mamichan - M", "Range DPS", "Mage"),
    ("Meekaroo - M", "Range DPS", "Mage"),
    ("Impquisition - M", "Range DPS", "Warlock"),
    ("Zing - M", "Range DPS", "Warlock"),
    ("Nezzyz - M", "Range DPS", "Boomkin Druid"),
    ("Alcadeus - M", "Range DPS", "Evoker"),
    ("Liz - M", "Range DPS", "Evoker"),
    ("Ampered - M", "Range DPS", "Hunter"),
    ("Buttadog - M", "Range DPS", "Hunter"),
    ("Nexrax - M", "Range DPS", "Hunter"),
    ("Kinmai - M", "Range DPS", "Shaman")
]

# spilt characters
splits = [
    ("Scoom - S", "Tank", "Paladin"),
    ("Karp - S", "Tank", "Death Knight"),
    ("Warbazoo - S", "Melee DPS", "Warrior"),
    ("Kovah - S", "Healer", "Priest"),
    ("Tekyer - S", "Healer", "Evoker"),
    ("Bloodblain - S", "Healer", "Druid"),
    ("Tamikochan - S", "Healer", "Priest"),
    ("Akylix - S", "Melee DPS", "Demon Hunter"),
    ("Skëlly - S", "Melee DPS", "Paladin"),
    ("Charley - S", "Melee DPS", "Death Knight"),
    ("Cptstabz - S", "Melee DPS", "Death Knight"),
    ("Vynstabz - S", "Melee DPS", "Feral Druid"),
    ("Koby - S", "Melee DPS", "Paladin"),
    ("Urusa - S", "Melee DPS", "Rogue"),
    ("Chocksticks - S", "Range DPS", "Elemental Shaman"),
    ("Mamichan - S", "Melee DPS", "Paladin"),
    ("Meekaroo - S", "Range DPS", "Evoker"),
    ("Impquisition - S", "Range DPS", "Mage"),
    ("Zing - S", "Range DPS", "Mage"),
    ("Nezzyz - S", "Range DPS", "Priest"),
    ("Liz - S", "Range DPS", "Boomkin Druid"),
    ("Ampered - S", "Range DPS", "Hunter"),
    ("Buttadog - S", "Range DPS", "Mage"),
    ("Nexrax - S", "Range DPS", "Hunter"),
    ("Kinmai - S", "Range DPS", "Evoker")
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def roster(ctx):
    tanks = random.sample([char for char in mains + splits if char[1] == "Tank"], 2)  
    non_tanks = [char for char in mains + splits if char[1] != "Tank"]
    selected_roster = random.sample(non_tanks, 28)  
    response = "**Raid Roster:**\n" + "\n".join(
        f"**{name} ({role}, {char_class}, {classes.get(char_class, 'Unknown')})**" for name, role, char_class in tanks
    ) + "\n" + "\n".join(
        f"{name} ({role}, {char_class}, {classes.get(char_class, 'Unknown')})" for name, role, char_class in selected_roster
    )
    await ctx.send(response)


bot.run(os.getenv("DISCORD_BOT_TOKEN"))  
