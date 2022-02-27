# import
from logging import warning
from classes import ClassSpec, create_team_name_string, TeamRoster
from setup import (
    class_spec_tier_rank,
    team_tier_rank_override,
    frequency_of_teams_by_tier,
    frequency_of_teams_within_tier_by_team,
    prob_to_win_by_tier,
    prob_to_win_by_team,
)

# parse team_tier_rank_override
team_tier_rank_override_dict = {}
for data in team_tier_rank_override:
    class_spec_1 = data[0]
    class_spec_2 = data[1]
    rank = data[2]
    team_name_string = create_team_name_string(class_spec_1,class_spec_2)
    if team_name_string in team_tier_rank_override_dict:
        print()
        warning("{} is found in team_tier_rank_override multiple times".format(team_name_string))
        print()
    team_tier_rank_override_dict[team_name_string] = rank

# parse frequency_of_teams_within_tier_by_team
frequency_of_teams_within_tier_by_team_dict = {}
for data in frequency_of_teams_within_tier_by_team:
    class_spec_1 = data[0]
    class_spec_2 = data[1]
    freq = data[2]
    team_name_string = create_team_name_string(class_spec_1,class_spec_2)
    if team_name_string in frequency_of_teams_within_tier_by_team_dict:
        print()
        warning("{} is found in frequency_of_teams_within_tier_by_team multiple times".format(team_name_string))
        print()
    frequency_of_teams_within_tier_by_team_dict[team_name_string] = freq

# parse prob_to_win_by_team
prob_to_win_by_team_dict = {}
for data in prob_to_win_by_team:
    self_team_names = []
    self_class_spec_1 = data[0][0]
    self_class_spec_2 = data[0][1]
    if self_class_spec_1 == ClassSpec.ANY and self_class_spec_2 == ClassSpec.ANY:
        for class_spec_1 in ClassSpec:
            for class_spec_2 in ClassSpec:
                self_team_names.append(create_team_name_string(class_spec_1,class_spec_2))
    elif self_class_spec_1 == ClassSpec.ANY:
        for class_spec in ClassSpec:
            self_team_names.append(create_team_name_string(self_class_spec_2,class_spec))
    elif self_class_spec_2 == ClassSpec.ANY:
        for class_spec in ClassSpec:
            self_team_names.append(create_team_name_string(self_class_spec_1,class_spec))
    else:
        self_team_names.append(create_team_name_string(self_class_spec_1,self_class_spec_2))

    other_team_names = []
    other_class_spec_1 = data[1][0]
    other_class_spec_2 = data[1][1]
    if other_class_spec_1 == ClassSpec.ANY and other_class_spec_2 == ClassSpec.ANY:
        for class_spec_1 in ClassSpec:
            for class_spec_2 in ClassSpec:
                other_team_names.append(create_team_name_string(class_spec_1,class_spec_2))
    elif other_class_spec_1 == ClassSpec.ANY:
        for class_spec in ClassSpec:
            other_team_names.append(create_team_name_string(other_class_spec_2,class_spec))
    elif other_class_spec_2 == ClassSpec.ANY:
        for class_spec in ClassSpec:
            other_team_names.append(create_team_name_string(other_class_spec_1,class_spec))
    else:
        other_team_names.append(create_team_name_string(other_class_spec_1,other_class_spec_2))

    prob = data[2][0]

    for self_team_name in self_team_names:
        if self_team_name not in prob_to_win_by_team_dict:
            prob_to_win_by_team_dict[self_team_name] = {}
        for other_team_name in other_team_names:
            if self_team_name in prob_to_win_by_team_dict and other_team_name in prob_to_win_by_team_dict[self_team_name]:
                print()
                warning("self: {} other: {} is found in prob_to_win_by_team multiple times".format(self_team_name,other_team_name))
                print()

            # ensure mirror is always 50%
            if self_team_name == other_team_name:
                prob = 0.5
                
            prob_to_win_by_team_dict[self_team_name][other_team_name] = prob    

# print("=== prob_to_win_by_team_dict ===")
# for self_team_name in prob_to_win_by_team_dict:
#     print(self_team_name)
#     for other_team_name in prob_to_win_by_team_dict[self_team_name]:
#         print("\t{}".format(other_team_name))
#         print("\twin_prob: {}".format(prob_to_win_by_team_dict[self_team_name][other_team_name]))

# construct teams
team_roster = TeamRoster(class_spec_tier_rank,team_tier_rank_override_dict)

# determine win rank
team_roster.compute_team_frequency(frequency_of_teams_by_tier,frequency_of_teams_within_tier_by_team_dict)
team_roster.opt(prob_to_win_by_tier,prob_to_win_by_team_dict)
print("=== RESULTS ===")
team_roster.print(sort=True)