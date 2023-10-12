# GroupChatTp
A bot program to help you transfer group chats into a server channel

## Requirements
[Discord History Tracker](https://github.com/chylex/Discord-History-Tracker)

[Sqlite or anything similar](https://www.sqlite.org/download.html)

[DiscordPy](https://pypi.org/project/discord.py/)

## How to use
This program works along with Discord History Tracker.

You will have to extract the chat data using Discord History Tracker. After you have successfully extracted the chat,
you need to extract the following databases as csv using sqlite from the data file created with the name "archive" and store them in the same folder as reader.py :
- embeds
- replied_to
- reactions
- attachments
- users
- messages


When you have added your bot's token id in the transfer.py program, you need to run transfer.py.

There is also usericon which is basically a dictionary of the username and link to an image which will be used for that user. Add users as per you choice and the link to the image and make sure the link is hosted on a safe & reliable site so it doesn't get deleted later on. If a user has not been added to the dictionary, a default image will be used for the image of that user.

Now use the command ".transferstart" in the channel where you want the chat.

This can take some time if you have a lot of messages but it is pretty fast.


## How does it look?

<p><img src="https://github.com/fischpo/Group-Chat-Transfer/blob/main/howitlooks.png?raw=true"></p>

## Issues
If you face any issues please raise it [here](https://github.com/fischpo/Group-Chat-Transfer/issues).
