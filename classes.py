# imports
from logging import warning
from enum import Enum

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
    return("{} / {}".format(sorted_names[0],sorted_names[1]))

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
        self.overall_freq = 0.0
        self.win_rank = 0.0

    def determine_default_team_tier_rank(self):
        """Determines the default team tier rank based on individual class ranks and roles"""
        team_tier_rank = min(self.class_spec_tier_rank_1,self.class_spec_tier_rank_2)
        if ClassSpecToClassRoleMap[self.class_spec_1] == ClassRole.HEALER and ClassSpecToClassRoleMap[self.class_spec_2] == ClassRole.HEALER:
            team_tier_rank = TierRank.F
        return(team_tier_rank)

    def fight(self,other_team,prob_to_win_by_tier,prob_to_win_by_team_dict):
        """Determines win rank for self team against other team"""
        if self.name in prob_to_win_by_team_dict and other_team.name in prob_to_win_by_team_dict[self.name]:
            prob_to_win = prob_to_win_by_team_dict[self.name][other_team.name]
        elif self.team_tier_rank >= other_team.team_tier_rank:
            prob_to_win = prob_to_win_by_tier[self.team_tier_rank][other_team.team_tier_rank]
        else:
            prob_to_win = 1.0 - prob_to_win_by_tier[other_team.team_tier_rank][self.team_tier_rank]

        self.win_rank += (other_team.overall_freq * prob_to_win)*100

    def print(self):
        print(self.name)
        print("\t{}".format(self.team_tier_rank))
        print("\tfrequency: {:0.1f}%".format(self.overall_freq*100))
        print("\twin_rank: {:0.0f}".format(self.win_rank))

    def __lt__(self,other):
        return(self.win_rank < other.win_rank)

    def __le__(self,other):
        return(self.win_rank <= other.win_rank)
    
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
    
    def compute_team_frequency(self,frequency_of_teams_by_tier,frequency_of_teams_within_tier_by_team_dict):
        """returns the frequency of the given team within their tier"""
        for tier_rank in TierRank:
            tier_even_dist_cnt = 0
            total_tier_freq = frequency_of_teams_by_tier[tier_rank]
            team_within_tier_freq = 1.0
            team_freq_dict = {}
            for team_name in self.teams:
                if self.teams[team_name].team_tier_rank == tier_rank:
                    if team_name in frequency_of_teams_within_tier_by_team_dict:
                        # team has overriden frequency within tier
                        team_freq_dict[team_name] = frequency_of_teams_within_tier_by_team_dict[team_name]*total_tier_freq
                        team_within_tier_freq -= frequency_of_teams_within_tier_by_team_dict[team_name]
                        if team_within_tier_freq < 0.0:
                            warning("tier {} has individual team overrides that are greater than 1.0".format(tier_rank))
                    else:
                        # team is evenly distributed in remainder of tier
                        tier_even_dist_cnt += 1
                        team_freq_dict[team_name] = None
            for team_name in team_freq_dict:
                if not team_freq_dict[team_name]:
                    self.teams[team_name].overall_freq = team_within_tier_freq / tier_even_dist_cnt
                else:
                    self.teams[team_name].overall_freq = team_freq_dict[team_name]
    
    def print(self,sort=False):
        teams_to_print = self.teams
        if sort:
            teams_to_print = dict(sorted(teams_to_print.items(), key=lambda item: item[1]))
        for team in teams_to_print:
            teams_to_print[team].print()
        
    def opt(self,prob_to_win_by_tier,prob_to_win_by_team_dict):
        for team_self in self.teams:
            for team_other in self.teams:
                self.teams[team_self].fight(self.teams[team_other],prob_to_win_by_tier,prob_to_win_by_team_dict)