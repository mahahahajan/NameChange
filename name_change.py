import os


#Step 1: Get the right directory
print("This was built originally only to change files within /Documents/Videos/")
print("Which show would you like to rename? ")
show = input("Enter Show:   ")
#show = "HIMYM"

path = "/Users/pulkitmahajan/Documents/Videos/" + show




seasons = 0
keywords = []
entries = os.scandir(path)
for entry in entries:
    if entry.is_dir():
        seasons+=1
        episodes = os.scandir(path +  "/" + entry.name )
        counter = 0
        for episode in episodes:
            if counter == 0:
                print("Episodes in this season are formatted as such: ")
                print(episode.name)
                counter+=1
                badwords = input("Enter key words to be removed:   ")
                keywords = badwords.split(" ")
            episodeName = episode.name
            for words in keywords:
                cleanName = episodeName.replace(words, "")
                episodeName = cleanName
            os.rename(path + "/" + entry.name + "/" + episode.name, path + "/" + entry.name + "/" + episodeName) 

        

print("There are " + str(seasons) + " seasons in this show")