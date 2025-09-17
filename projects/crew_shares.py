# KK 2nd Crew Shares Project

start = '\033[1m'
end = '\033[0m'

story = "The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port.\nHe gave each member of the crew $500 for the evening and then sat down with his first mate to properly divide the shares."
# prints the story above for details
print(story)
# amount of money and crew
crew_mems = int(input("\nHow many crew members do you wish there were?:\n"))
money = float(input("How much money was earned?:\n"))
# the number of shares is the amount of crew members + 7 and 3 for captain/first mate
shares = crew_mems + 10
# splits up the shares evenly 
divided_share = money/shares
# each share is added up accordingly to how much everyone needs
captain_money = divided_share*7
crew_money = divided_share-500 # subtract 500 from a divided share because crew already got 500
firstm_money = divided_share*3


modded_story = (f"\nThe crew earned ${money:,} on the last outing, but the captain didn't have time to divvy it all up before release everyone to port.\nHe gave each member of the crew $500 for the evening and then sat down with his first mate to properly divide the shares.")
print(modded_story)
print(f"\n{start}These were the final calculations.{end}\nMoney Earned: {money:,}\n# of Crew Members: {crew_mems}\nCaptain earns: {captain_money:.2f}\nFirst mate earns: {firstm_money:.2f}\nCrew still requires: {crew_money:.2f}")