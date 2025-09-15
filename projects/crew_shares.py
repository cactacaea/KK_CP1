# KK 2nd Crew Shares Project

# 50000/30 + 10 shares for captain and first mate
story = "The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew $500 for the evening and then sat down with his first mate to properly divide the shares."
print(story)
crew_mems = input("How many crew members do you wish there were?:\n") # int
money = input("How much money was earned?:\n") # int
shares = crew_mems + 10
divided_shares = shares 
captain_money = 1
crew_money = 1
firstm_money = 1


modded_story = (f"The crew earned ${money} on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares.")
print(f"Money Earned: {money}\n# of Crew Members:{crew_mems}\nCaptain earns:{captain_money}\nFirst mate earns:{firstm_money}\nCrew still requires:{crew_money}")