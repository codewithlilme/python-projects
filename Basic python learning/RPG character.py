def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"
    elif any(stat < 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"
    elif any(stat > 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"
    elif (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"
    else:
        return (
        f"{name}\n"
        f"STR {'●' * strength}{'○' * (10 - strength)}\n"
        f"INT {'●' * intelligence}{'○' * (10 - intelligence)}\n"
        f"CHA {'●' * charisma}{'○' * (10 - charisma)}"
    )