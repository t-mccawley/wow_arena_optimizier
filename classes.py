# imports
from logging import warning
from enum import Enum
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# define classes
class ClassSpec(Enum):
    DEATH_KNIGHT_BLOOD = 1
    DEATH_KNIGHT_FROST = 2
    DEATH_KNIGHT_UNHOLY = 3
    DRUID_FERAL = 4
    DRUID_RESTO = 5
    DRUID_BALANCE = 6
    HUNTER_BM = 7
    HUNTER_SURV = 8
    HUNTER_MARKS = 9
    MAGE_FROST = 10
    MAGE_FIRE = 11
    MAGE_ARCANE = 12
    PALADIN_RET = 13
    PALADIN_PROT = 14
    PALADIN_HOLY = 15
    PALADIN_PREG = 16
    PRIEST_HOLY = 17
    PRIEST_SHADOW = 18
    PRIEST_DISC = 19
    ROGUE_COMBAT = 20
    ROGUE_SUB = 21
    ROGUE_ASSASSIN = 22
    SHAMAN_ENH = 23
    SHAMAN_RESTO = 24
    SHAMAN_ELE = 25
    WARLOCK_DEMO = 26
    WARLOCK_AFF = 27
    WARLOCK_DESTRO = 28
    WARRIOR_ARMS = 29
    WARRIOR_FURY = 30
    WARRIOR_PROT = 31
    ANY = 32

class_spec_color_dict = {
    ClassSpec.DEATH_KNIGHT_BLOOD:(0.77,0.12,0.23,1.0),
    ClassSpec.DEATH_KNIGHT_FROST:(0.77,0.12,0.23,1.0),
    ClassSpec.DEATH_KNIGHT_UNHOLY:(0.77,0.12,0.23,1.0),
    ClassSpec.DRUID_FERAL:(1.00,0.49,0.04,1.0),
    ClassSpec.DRUID_RESTO:(1.00,0.49,0.04,1.0),
    ClassSpec.DRUID_BALANCE:(1.00,0.49,0.04,1.0),
    ClassSpec.HUNTER_BM:(0.67,0.83,0.45,1.0),
    ClassSpec.HUNTER_SURV:(0.67,0.83,0.45,1.0),
    ClassSpec.HUNTER_MARKS:(0.67,0.83,0.45,1.0),
    ClassSpec.MAGE_FROST:(0.25,0.78,0.92,1.0),
    ClassSpec.MAGE_FIRE:(0.25,0.78,0.92,1.0),
    ClassSpec.MAGE_ARCANE:(0.25,0.78,0.92,1.0),
    ClassSpec.PALADIN_RET:(0.96,0.55,0.73,1.0),
    ClassSpec.PALADIN_PROT:(0.96,0.55,0.73,1.0),
    ClassSpec.PALADIN_HOLY:(0.96,0.55,0.73,1.0),
    ClassSpec.PALADIN_PREG:(0.96,0.55,0.73,1.0),
    ClassSpec.PRIEST_HOLY:(1.0,1.0,1.0,1.0),
    ClassSpec.PRIEST_SHADOW:(1.0,1.0,1.0,1.0),
    ClassSpec.PRIEST_DISC:(1.0,1.0,1.0,1.0),
    ClassSpec.ROGUE_COMBAT:(1.00,0.96,0.41,1.0),
    ClassSpec.ROGUE_SUB:(1.00,0.96,0.41,1.0),
    ClassSpec.ROGUE_ASSASSIN:(1.00,0.96,0.41,1.0),
    ClassSpec.SHAMAN_ENH:(0.00,0.44,0.87,1.0),
    ClassSpec.SHAMAN_RESTO:(0.00,0.44,0.87,1.0),
    ClassSpec.SHAMAN_ELE:(0.00,0.44,0.87,1.0),
    ClassSpec.WARLOCK_DEMO:(0.53,0.53,0.93,1.0),
    ClassSpec.WARLOCK_AFF:(0.53,0.53,0.93,1.0),
    ClassSpec.WARLOCK_DESTRO:(0.53,0.53,0.93,1.0),
    ClassSpec.WARRIOR_ARMS:(0.78,0.61,0.43,1.0),
    ClassSpec.WARRIOR_FURY:(0.78,0.61,0.43,1.0),
    ClassSpec.WARRIOR_PROT:(0.78,0.61,0.43,1.0),
}

class ClassRole(Enum):
    DPS = 1
    HEALER = 2

class TierRank(Enum):
    F = 1 # 1st percentile
    D = 2 # 10th percentile
    C = 3 # 30th percentile
    B = 4 # 50th percentile
    A = 5 # 80th percentile
    S = 6 # 90th percentile
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

# dictionary that maps class specs to roles
ClassSpecToClassRoleMap = {
    ClassSpec.DEATH_KNIGHT_BLOOD:ClassRole.DPS,
    ClassSpec.DEATH_KNIGHT_FROST:ClassRole.DPS,
    ClassSpec.DEATH_KNIGHT_UNHOLY:ClassRole.DPS,
    ClassSpec.DRUID_FERAL:ClassRole.DPS,
    ClassSpec.DRUID_RESTO:ClassRole.HEALER,
    ClassSpec.DRUID_BALANCE:ClassRole.DPS,
    ClassSpec.HUNTER_BM:ClassRole.DPS,
    ClassSpec.HUNTER_SURV:ClassRole.DPS,
    ClassSpec.HUNTER_MARKS:ClassRole.DPS,
    ClassSpec.MAGE_FROST:ClassRole.DPS,
    ClassSpec.MAGE_FIRE:ClassRole.DPS,
    ClassSpec.MAGE_ARCANE:ClassRole.DPS,
    ClassSpec.PALADIN_RET:ClassRole.DPS,
    ClassSpec.PALADIN_PROT:ClassRole.DPS,
    ClassSpec.PALADIN_HOLY:ClassRole.HEALER,
    ClassSpec.PALADIN_PREG:ClassRole.DPS,
    ClassSpec.PRIEST_HOLY:ClassRole.HEALER,
    ClassSpec.PRIEST_SHADOW:ClassRole.DPS,
    ClassSpec.PRIEST_DISC:ClassRole.HEALER,
    ClassSpec.ROGUE_COMBAT:ClassRole.DPS,
    ClassSpec.ROGUE_SUB:ClassRole.DPS,
    ClassSpec.ROGUE_ASSASSIN:ClassRole.DPS,
    ClassSpec.SHAMAN_ENH:ClassRole.DPS,
    ClassSpec.SHAMAN_RESTO:ClassRole.HEALER,
    ClassSpec.SHAMAN_ELE:ClassRole.DPS,
    ClassSpec.WARLOCK_DEMO:ClassRole.DPS,
    ClassSpec.WARLOCK_AFF:ClassRole.DPS,
    ClassSpec.WARLOCK_DESTRO:ClassRole.DPS,
    ClassSpec.WARRIOR_ARMS:ClassRole.DPS,
    ClassSpec.WARRIOR_FURY:ClassRole.DPS,
    ClassSpec.WARRIOR_PROT:ClassRole.DPS,
}

def create_team_name_string(class_spec_1,class_spec_2):
    """Creates team name string given two class_specs enum"""
    sorted_names = sorted([class_spec_1.name,class_spec_2.name])
    return("{} + {}".format(sorted_names[0],sorted_names[1]))

class Team:
    """Class that defines a 2v2 arena team"""
    def __init__(
        self,
        class_spec_1,
        class_spec_2,
        class_spec_tier_rank,
        team_tier_rank_override_dict,
        ):
        # record composition
        self.class_spec_1 = class_spec_1
        self.class_spec_2 = class_spec_2
        self.name = create_team_name_string(self.class_spec_1,self.class_spec_2)
        # determine individual class tier ranks
        self.class_spec_tier_rank_1 = class_spec_tier_rank[class_spec_1]
        self.class_spec_tier_rank_2 = class_spec_tier_rank[class_spec_2]
        # determine team tier rank
        team_tier_rank = self.determine_default_team_tier_rank()
        if self.name in team_tier_rank_override_dict:
            team_tier_rank = team_tier_rank_override_dict[self.name]
        self.team_tier_rank = team_tier_rank
        # assign defaults
        self.freq_overall = 0.0
        self.score = 0.0

    def determine_default_team_tier_rank(self):
        """Determines the default team tier rank based on individual class ranks and roles"""
        team_tier_rank = min(self.class_spec_tier_rank_1,self.class_spec_tier_rank_2)
        if ClassSpecToClassRoleMap[self.class_spec_1] == ClassRole.HEALER and ClassSpecToClassRoleMap[self.class_spec_2] == ClassRole.HEALER:
            team_tier_rank = TierRank.F
        return(team_tier_rank)

    def fight(self,other_team,prob_to_win_by_tier,prob_to_win_by_team_dict):
        """Determines expected number of wins for self team against other team"""
        if self.name in prob_to_win_by_team_dict and other_team.name in prob_to_win_by_team_dict[self.name]:
            prob_to_win = prob_to_win_by_team_dict[self.name][other_team.name]
        elif self.team_tier_rank >= other_team.team_tier_rank:
            prob_to_win = prob_to_win_by_tier[self.team_tier_rank][other_team.team_tier_rank]
        else:
            prob_to_win = 1.0 - prob_to_win_by_tier[other_team.team_tier_rank][self.team_tier_rank]

        self.score += (other_team.freq_overall * prob_to_win)

    def print(self):
        print(self.name)
        print("\ttier rank: {}".format(self.team_tier_rank.name))
        print("\tfrequency: {:0.1f} teams out of 100".format(self.freq_overall))
        print("\texpected wins: {:0.1f} wins out of 100".format(self.score))

    def __lt__(self,other):
        return(self.score < other.score)

    def __le__(self,other):
        return(self.score <= other.score)
    
class TeamRoster:
    def __init__(self,class_spec_tier_rank,team_tier_rank_override_dict):
        self.teams = {}
        for class_spec_1 in ClassSpec:
            if class_spec_1 == ClassSpec.ANY:
                break
            for class_spec_2 in ClassSpec:
                if class_spec_2 == ClassSpec.ANY:
                    break
                team_name_string = create_team_name_string(class_spec_1,class_spec_2)
                self.teams[team_name_string] = Team(class_spec_1, class_spec_2, class_spec_tier_rank, team_tier_rank_override_dict)
    
    def compute_team_frequency(self,frequency_of_teams_by_tier,frequency_of_teams_override_dict):
        """
            returns the frequency of the given team
            units are number of teams of the given comp out of 100 total teams
        """
        # first check for overrides
        total_teams = 100
        for team_name in self.teams:
            if team_name in frequency_of_teams_override_dict:
                self.teams[team_name].freq_overall = frequency_of_teams_override_dict[team_name]*total_teams
                total_teams -= frequency_of_teams_override_dict[team_name]*total_teams
        # compute remaining teams by even distribution within tier
        for tier_rank in TierRank:
            # determine teams within tier and remove from total pool
            teams_within_tier = total_teams*frequency_of_teams_by_tier[tier_rank]
            # count number of remaining teams within tier
            count_of_rem_teams_in_tier = 0
            for team_name in self.teams:
                if (self.teams[team_name].team_tier_rank == tier_rank) and (self.teams[team_name].freq_overall == 0.0):
                    count_of_rem_teams_in_tier += 1
            # determine number of teams split evenly
            for team_name in self.teams:
                if (self.teams[team_name].team_tier_rank == tier_rank) and (self.teams[team_name].freq_overall == 0.0):
                    self.teams[team_name].freq_overall = teams_within_tier/count_of_rem_teams_in_tier
            
            # print stats to check
            print("tier_rank: {}".format(tier_rank))
            total_freq = 0.0
            for team_name in self.teams:
                if self.teams[team_name].team_tier_rank == tier_rank:
                    total_freq += self.teams[team_name].freq_overall
            print("total_freq: {:0.0f} out of 100 teams".format(total_freq))
    
    def print(self,sort=False,top=10):
        teams_to_print = self.teams
        if sort:
            teams_to_print = dict(sorted(teams_to_print.items(), key=lambda item: item[1]))
        cnt = 0
        print("=== TOP {} TEAMS ===".format(top))
        for team in reversed(teams_to_print):
            if cnt < top:
                teams_to_print[team].print()
                cnt += 1
        
    def opt(self,prob_to_win_by_tier,prob_to_win_by_team_dict):
        for team_self in self.teams:
            for team_other in self.teams:
                self.teams[team_self].fight(self.teams[team_other],prob_to_win_by_tier,prob_to_win_by_team_dict)
    
    def plot_score(self):
        # determine ranking of class_spec by average score in comps
        class_spec_avg_score = {}
        for class_spec_1 in ClassSpec:
            if class_spec_1 == ClassSpec.ANY:
                continue
            class_spec_avg_score[class_spec_1] = 0.0
            # scan all comps
            for class_spec_2 in ClassSpec:
                if class_spec_2 == ClassSpec.ANY:
                    continue
                class_spec_avg_score[class_spec_1] += self.teams[create_team_name_string(class_spec_1,class_spec_2)].score
            # compute average
            class_spec_avg_score[class_spec_1] /= (len(ClassSpec) - 1)
        # sort
        class_spec_avg_score_sorted = dict(sorted(class_spec_avg_score.items(), key=lambda item: item[1]))
        # format contour plot data
        x = [class_spec for class_spec in class_spec_avg_score_sorted]
        y = [class_spec for class_spec in class_spec_avg_score_sorted]
        # shape = (rows,cols)
        z = np.zeros(shape=(len(y),len(x)))
        for i_x in range(len(x)):
            for i_y in range(len(y)):
                z[i_y][i_x] = self.teams[create_team_name_string(x[i_x],y[i_y])].score
        

        x_label = [class_spec.name for class_spec in x]
        y_label = [class_spec.name for class_spec in y]

        fig, ax = plt.subplots(constrained_layout=True,facecolor='grey')
        cs = ax.contourf(z,cmap='RdYlGn')
        plt.grid(which='both')
        plt.xticks(ticks=range(len(x)),labels=x_label,rotation=90,weight='bold')
        plt.yticks(ticks=range(len(y)),labels=y_label,weight='bold')
        colors_x = [class_spec_color_dict[class_spec] for class_spec in x]
        for xtick, color in zip(ax.get_xticklabels(), colors_x):
            xtick.set_color(color)
        colors_y = [class_spec_color_dict[class_spec] for class_spec in y]
        for ytick, color in zip(ax.get_yticklabels(), colors_y):
            ytick.set_color(color)
        cbar = fig.colorbar(cs)
        cbar.ax.set_ylabel('expected wins out of 100')

        plt.show()