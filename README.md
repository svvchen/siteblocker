# siteblocker
Block social media sites until I've reached my Duolingo french XP goal for the day.

**To Do:**
* Create add_site/remove_site methods.
  * Only available upon hitting daily xp. :)
* Write up a cron job to run this thing as soon as I open my laptop for maximum pain (uh I mean French learning motivation).

**In Progress:**
* Link up `check_goal_reached` and the `check_block`.
* Rename `check_block` &rightarrow; `action_block`. It's not really checking, so much as adding/removing the block.

**Done:**
* Created a `check_block` function that blocks websites based on the hosts file (let the pain begin).
* Create a blocker class that houses `check_block` and associated methods.
* Create function to check on my Duolingo xp progress via their API endpoints.

![Blocked_Facebook](https://github.com/svvchen/siteblocker/blob/master/PR_1_Ss.png)
