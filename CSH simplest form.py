#shows user the available operations.
print(f"WELCOME TO COMMUNITY STORY HUB.\n Operations available: \n1.Explore \n2.Share \n3.Delete \nWARNING!!USE THE NUMBER ASSIGNED TO YOUR DESIRED OPERATION")
tribe_stories = {"Agikuyu": ["Agikuyu stories"], "Luo": ["Luo stories"]}  # each tribe must store a list of stories

while True:  # continuous program
    operation = input("Enter operation: ")
    try:
        operation = int(operation)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if operation == 1:  # exploring stories
        print("Explore page")
        print("TRIBES AVAILABLE:")
        for i, tribe in enumerate(tribe_stories, start=1):
            print(f"{i}.{tribe}")

        tribe = input("Enter tribe: ").strip().capitalize()
        if tribe in tribe_stories:  # checks if the tribe user inputed is present in the stories dict.
            print(f"Stories from the {tribe} tribe")
            stories = tribe_stories[tribe]  # retrieves the stories present in the chosen tribe
            for story in stories:
                print(f"- {story}")
        else:
            print(f"Sorry we dont have stories for the {tribe} tribe yet. Check if tribe is correct or misspelled.")

    elif operation == 2:  # share
        print("SHARE PAGE.")
        share_tribe = input("Enter story's tribe: ").strip().capitalize()
        share_story = input("Write story: ").strip()

        if share_story == "":
            print("Story cannot be empty.")
            continue

        if share_tribe not in tribe_stories:
            tribe_stories[share_tribe] = []

        tribe_stories[share_tribe].append(share_story)  # adds stories instead of overwriting
        print(f"Story added to {share_tribe}.")
        print(tribe_stories)

    elif operation == 3:  # delete
        delete_story = input("Enter story to delete: ").strip()
        if delete_story == "":
            print("Story cannot be empty.")
            continue

        for tribe, stories in tribe_stories.items():
            if delete_story in stories:
                stories.remove(delete_story)
                print(f"Story deleted from {tribe}.")
                break
        else:
            print("The story is not available.")

    else:
        print("Invalid operation. Please choose 1, 2, or 3.")