def share_story(sharestory):
    return{
       "tribe": sharestory.tribe,
       "story": sharestory.story,
       "title": sharestory.story_title
    }

def allstories(stories):
    return [share_story(story) for story in stories]