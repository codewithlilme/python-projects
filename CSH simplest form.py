#shows user the available operations.
print(f"WELCOME TO COMMUNITY STORY HUB.\n Operations available: \n1.Explore \n2.Share \nWARNING!!USE THE NUMBER ASSIGNED TO YOUR DESIRED OPERATION")
tribe_stories = {"Agikuyu":["Agikuyu stories"],"Luo":["Luo stories"]}#put story samples in the dict where tribe is key and story is values
while True:#continous program
    operation =input("Enter operation: ")
    operation = int(operation)
    if operation == 1:#exploring stories
        print("Explore page \nTRIBES AVAILABLE: \n 1.Agikuyu \n 2.Luo")
        tribe = input("Enter tribe: ").capitalize()#user enters name of tribe from list and the firsst letter of the word is made a captial letter while the rest remain as small letters to ensure the input resembles tribes(key) in the dict 
        if tribe in tribe_stories:#checks if the tribe user inputed is present in the stories dict.
            print(f"Stories from the {tribe} tribe")
            stories = tribe_stories[tribe] #retrieves the stories present in the chosen tribe
            print(f"{stories}")#prints stories present in the chosen tribe
        else:
            print(f"Sorry we dont have stories for the {tribe} tribe yet.Check if tribe is correct or misspelled.")
    elif operation == 2:#share
        print("SHARE PAGE.")
        share_tribe = input("Enter story's tribe:").capitalize()
        if share_tribe in tribe_stories: #checks if the tribe of the story exists in dictionary 
            share_story = input("Write story: ")
            tribe_stories[share_tribe].append(share_story)#adds stories instead of overrwriting
            print(tribe_stories)
        else:#if the story's tribe doesnt exist, you add the story's tribe to the dictionary as a key then tell the user to write the story and assign the story as the value to the tribe which is the key.
            share_newtribestory = input("Write story: ")
            tribe_stories[share_tribe] = share_newtribestory