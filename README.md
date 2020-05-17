# siteblocker
Blocks social media sites until I've reached my Duolingo french XP goal for the day.

**To Do:**
* Create add_site/remove_site methods.
  * Only available upon hitting daily xp. :)

**In Progress:**
* Write up a cron job to run this thing as soon as I open my laptop and forever until I do my lessons.

**(Recently) Done:**
* Created a `action_block` function and associate class that blocks websites based on the hosts file (let the pain begin).
* Create function to check on my Duolingo xp progress via Duolingo API endpoints.
* Create a user/pass secrets file so I don't need to ever worry about pushing my user/pass to GH.
* Replace the Duoling API checker with a selenium web scraper. The Duo API gives me really inconsistent xp data.

## Progress screenshots
**Blocking FB via hosts file:**
<details>
 <summary>Success...</summary>

 ![Successful Block](https://github.com/svvchen/siteblocker/blob/master/images/PR_1_Ss.png)
</details>


**Blocking YT with Duolingo API**
<details>
 <summary>Blocked...</summary>

 ![Blocked](https://github.com/svvchen/siteblocker/blob/master/images/Blocked.png)
</details>

<details>
 <summary>Working...</summary>

 ![Work](https://github.com/svvchen/siteblocker/blob/master/images/Work.png)
</details>

<details>
 <summary>Play!</summary>

 ![Play](https://github.com/svvchen/siteblocker/blob/master/images/Play.png)
</details>
