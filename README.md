# Instagram Python Bot

> A simple python bot built with selenium that allows you to generate a list with instagram accounts that you follow but don't follow you back!

> Automatic Unfollow Python Bot for Instagram!

> python, bot, instagram, unfollow

**Version 0.1**

- Initial project commit!

## Usage

- Clone the project and then edit the variables called `username` and `password` with your own username and password.
- Save the file and run it!

### Methods

- `get_unfollowers()` : this method will generate a list with the accounts that you follow but don't follow you back.

- `clean_log() : this method will clean up your log file that contains the last updated list of accounts.

-`unfollow(names)` : this method will begin to unfollow the accounts in the `names` list, where it will be executed as the following:

	- Unfollow 20 accounts (apparently that is the new limit imposed by Instagram)
	- Wait 20 minutes.
	- Unfollow 20 more accounts.
	- Repeat the cycle until all accouns in the `name` list are unfollowed.















