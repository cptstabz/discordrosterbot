import discord
import random
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Define bot with command prefix
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)  # ✅ Ensure bot is defined BEFORE calling bot.run()

# Define armor types
armor_types = {
    "Death Knight": "Plate",
    "Paladin": "Plate",
    "Warrior": "Plate",
    "Hunter": "Mail",
    "Shaman": "Mail",
    "Evoker": "Mail",
    "Mage": "Cloth",
    "Priest": "Cloth",
    "Warlock": "Cloth",
    "Rogue": "Leather",
    "Druid": "Leather",
    "Monk": "Leather",
    "Demon Hunter": "Leather"
}

# Define classes and their tier tokens
classes = {
    "Evoker": "Zenith",
    "Monk": "Zenith",
    "Rogue": "Zenith",
    "Warrior": "Zenith",
    "Death Knight": "Dreadful",
    "Demon Hunter": "Dreadful",
    "Warlock": "Dreadful",
    "Druid": "Mystic",
    "Boomkin Druid": "Mystic",
    "Hunter": "Mystic",
    "Mage": "Mystic",
    "Paladin": "Venerated",
    "Priest": "Venerated",
    "Shaman": "Venerated",
    "Elemental Shaman": "Venerated"
}

# Define required classes for raid buffs
required_classes = {"Druid", "Paladin", "Monk", "Demon Hunter", "Rogue", "Mage", "Shaman", "Warrior", "Priest", "Evoker"}

# Define character roles
roles = {
    "Tank": ["Druid", "Paladin", "Warrior", "Demon Hunter", "Death Knight"],
    "Healer": ["Priest", "Paladin", "Druid", "Monk", "Shaman", "Evoker"],
    "Melee DPS": ["Rogue", "Warrior", "Monk", "Demon Hunter", "Paladin", "Death Knight", "Feral Druid"],
    "Range DPS": ["Mage", "Elemental Shaman", "Evoker", "Priest", "Boomkin Druid", "Hunter", "Warlock"]
}

# List of split characters
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
    tanks = random.sample([char for char in splits if char[1] == "Tank"], 2)  # Ensure exactly 2 tanks from splits
    non_tanks = [char for char in splits if char[1] != "Tank"]
    selected_roster = random.sample(non_tanks, 28)  # Select exactly 28 non-tank characters
    response = "**Raid Roster:**\n" + "\n".join(
        f"**{name} ({role}, {char_class}, {classes.get(char_class, 'Unknown')}, {armor_types.get(char_class, 'Unknown')})**" for name, role, char_class in tanks
    ) + "\n" + "\n".join(
        f"{name} ({role}, {char_class}, {classes.get(char_class, 'Unknown')}, {armor_types.get(char_class, 'Unknown')})" for name, role, char_class in selected_roster
    )
    await ctx.send(response)

# Run the bot securely
bot.run(os.getenv("DISCORD_BOT_TOKEN"))  # ✅ Securely loads the token from the .env file
