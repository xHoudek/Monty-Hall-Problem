# Monty Hall Problem by Xander Houdek
### A Python script to model the Monty Hall Problem.

>"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"

### HYPOTHESIS AND GOAL:
Statistically speaking, you should always choose to switch doors, because the door you originally chose had a 33% chance of being right, whereas the door you switch to has a 50% chance of being right. So our hypothesis is that the player should switch doors if one door is revealed to be incorrect.

The goal of this script is to recreate the problem, run both scenarios (switch doors vs keep door), and show the probability of winning for each scenario.


### RESULTS:
The keep percentage aligns with the hypothesis, and is roughly 33%. However, the switch percentage is closer to 66%, rather than 50%. This may be a problem with the program, so I will look at other models and see how they perform differently.

After looking at some other implementations, it looks like results vary from 50% to 60-70%. Either way, this model shows that the hypothesis is true, and that you should switch doors if given the Monty Hall Problem.