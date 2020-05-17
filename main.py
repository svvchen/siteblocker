import duolingo_status
import media_blocker

if __name__ == "__main__":
    new_blocker = media_blocker.Blocker()

    # set daily goal
    daily_goal = 20

    # run the whole shebang
    new_blocker.action_block(duolingo_status.check_goal_reached(daily_goal))
