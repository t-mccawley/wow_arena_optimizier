# wow_arena_optimizier
A tool to predict rankings of WoW WoTLK 2v2 arena teams

Edit `setup.py` to configure the following assumptions:
- Tier ranking (S, A, B, C, D, F) for individual class specs
- Tier ranking (S, A, B, C, D, F) for individual teams (combination of two class specs)
  - By default, a team tier rank will be the minimum of the individual class spec ranks
- Frequency of occurrence of team tier rankins
  - i.e. assume that 35% of teams will be "S Tier", 25% will be "A Tier" etc.
 - Frequency of occurrence of individual teams
  - i.e. 50% of teams will be Holy Paladin + Arms Warrior
 - Probability of one team winning against another based on Tier and/or individual comps
   - i.e. Tier S teams have a 70% chance to win over Tier B teams or any team with a frost mage has 90% chance to win over a team with a warrior and no magic dispel

The tool predicts the expeted number of wins for a given team out of 100 and ranks them to determine the expected best team in aggregate. Example outputs:
![image](https://user-images.githubusercontent.com/29646748/155903790-a322f6be-9283-41b1-af8b-37a85c634aa6.png)
![image](https://user-images.githubusercontent.com/29646748/155903824-4f6ecae7-a3e8-4b00-a10d-4bcd18473ab4.png)
