from classes import ClassSpec, TierRank

# define the tier rank for each class
class_spec_tier_rank = {
    # S
    ClassSpec.WARRIOR_ARMS:TierRank.S,
    ClassSpec.PALADIN_HOLY:TierRank.S,
    # A
    ClassSpec.HUNTER_MARKS:TierRank.A,
    ClassSpec.DEATH_KNIGHT_UNHOLY:TierRank.A,
    ClassSpec.DRUID_FERAL:TierRank.A,
    # B
    ClassSpec.SHAMAN_ELE:TierRank.B, # note, actual video puts at S, but for 2s ele suffers from very low CC and not super viable comps
    ClassSpec.WARLOCK_AFF:TierRank.B,
    ClassSpec.MAGE_FROST:TierRank.B,
    ClassSpec.PRIEST_DISC:TierRank.B,
    ClassSpec.PALADIN_RET:TierRank.B,
    ClassSpec.PRIEST_SHADOW:TierRank.B,
    ClassSpec.ROGUE_SUB:TierRank.B,
    ClassSpec.SHAMAN_RESTO:TierRank.B,
    ClassSpec.SHAMAN_ENH:TierRank.B,
    ClassSpec.DRUID_RESTO:TierRank.B,
    ClassSpec.PALADIN_PREG:TierRank.B,
    ClassSpec.WARLOCK_DESTRO:TierRank.B,
    # C
    ClassSpec.MAGE_FIRE:TierRank.C,
    ClassSpec.DRUID_BALANCE:TierRank.C,
    ClassSpec.HUNTER_BM:TierRank.C,
    ClassSpec.WARRIOR_PROT:TierRank.C,
    ClassSpec.DEATH_KNIGHT_FROST:TierRank.C,
    ClassSpec.ROGUE_ASSASSIN:TierRank.C,
    # D
    ClassSpec.MAGE_ARCANE:TierRank.D,
    ClassSpec.PALADIN_PROT:TierRank.D,
    ClassSpec.HUNTER_SURV:TierRank.D,
    # F
    ClassSpec.DEATH_KNIGHT_BLOOD:TierRank.D,
    ClassSpec.WARLOCK_DEMO:TierRank.D,
    ClassSpec.WARRIOR_FURY:TierRank.D,
    ClassSpec.PRIEST_HOLY:TierRank.D,
    ClassSpec.ROGUE_COMBAT:TierRank.D,
}

# specify team tiers to override default logic
team_tier_rank_override = [
    # Tier Video Sourced
    # S
    [ClassSpec.WARLOCK_AFF,ClassSpec.SHAMAN_RESTO,TierRank.S],
    [ClassSpec.WARRIOR_ARMS,ClassSpec.PALADIN_HOLY,TierRank.S],
    [ClassSpec.DRUID_FERAL,ClassSpec.PRIEST_DISC,TierRank.S],
    [ClassSpec.MAGE_FROST,ClassSpec.PRIEST_SHADOW,TierRank.S],
    [ClassSpec.HUNTER_MARKS,ClassSpec.PALADIN_RET,TierRank.S],
    [ClassSpec.PRIEST_SHADOW,ClassSpec.ROGUE_SUB,TierRank.S],
    # A
    [ClassSpec.WARLOCK_DESTRO,ClassSpec.DRUID_RESTO,TierRank.A],
    [ClassSpec.DRUID_FERAL,ClassSpec.ROGUE_SUB,TierRank.A],
    [ClassSpec.MAGE_FROST,ClassSpec.PRIEST_DISC,TierRank.A],
    [ClassSpec.HUNTER_MARKS,ClassSpec.PRIEST_DISC,TierRank.A],
    [ClassSpec.PALADIN_RET,ClassSpec.SHAMAN_ENH,TierRank.A],
    # B
    [ClassSpec.WARRIOR_ARMS,ClassSpec.SHAMAN_RESTO,TierRank.B],
    [ClassSpec.WARRIOR_ARMS,ClassSpec.DRUID_RESTO,TierRank.B],
    [ClassSpec.DRUID_BALANCE,ClassSpec.ROGUE_SUB,TierRank.B],
    [ClassSpec.SHAMAN_ELE,ClassSpec.WARLOCK_DESTRO,TierRank.B],
    [ClassSpec.MAGE_FROST,ClassSpec.ROGUE_SUB,TierRank.B],
    [ClassSpec.PALADIN_RET,ClassSpec.PRIEST_DISC,TierRank.B],
    [ClassSpec.PALADIN_RET,ClassSpec.ROGUE_SUB,TierRank.B],
    [ClassSpec.PALADIN_RET,ClassSpec.WARRIOR_ARMS,TierRank.B],
    [ClassSpec.ROGUE_SUB,ClassSpec.PRIEST_DISC,TierRank.B],
    [ClassSpec.DEATH_KNIGHT_UNHOLY,ClassSpec.PALADIN_HOLY,TierRank.B],
    [ClassSpec.DEATH_KNIGHT_UNHOLY,ClassSpec.PALADIN_RET,TierRank.B],
    # C
    [ClassSpec.ROGUE_SUB,ClassSpec.WARLOCK_DESTRO,TierRank.C],
    [ClassSpec.ROGUE_SUB,ClassSpec.DRUID_RESTO,TierRank.C],
    [ClassSpec.DEATH_KNIGHT_UNHOLY,ClassSpec.SHAMAN_ENH,TierRank.C],
    [ClassSpec.DEATH_KNIGHT_UNHOLY,ClassSpec.PRIEST_DISC,TierRank.C],
    # D
    [ClassSpec.SHAMAN_ELE,ClassSpec.PRIEST_DISC,TierRank.D],

    # Assumed
    # S
    # A
    # B
    # C
    # D
    # F
]

# frequency of occurrence of team by tier
frequency_of_teams_by_tier = {
    TierRank.S:0.35,
    TierRank.A:0.25,
    TierRank.B:0.25,
    TierRank.C:0.09,
    TierRank.D:0.05,
    TierRank.F:0.01,
}

# frequency of occurrence of team within a tier by team comp
frequency_of_teams_within_tier_by_team = [
    [ClassSpec.PALADIN_HOLY,ClassSpec.WARRIOR_ARMS,0.5],
]

# probability to win based on team tier rank (win prob w.r.t. team associated with first key)
prob_to_win_by_tier = {
    TierRank.S:{
        TierRank.S:0.5,
        TierRank.A:0.6,
        TierRank.B:0.7,
        TierRank.C:0.8,
        TierRank.D:0.9,
        TierRank.F:0.99,
    },
    TierRank.A:{
        TierRank.A:0.5,
        TierRank.B:0.6,
        TierRank.C:0.7,
        TierRank.D:0.8,
        TierRank.F:0.9,
    },
    TierRank.B:{
        TierRank.B:0.5,
        TierRank.C:0.6,
        TierRank.D:0.7,
        TierRank.F:0.8,
    },
    TierRank.C:{
        TierRank.C:0.5,
        TierRank.D:0.6,
        TierRank.F:0.7,
    },
    TierRank.D:{
        TierRank.D:0.5,
        TierRank.F:0.6,
    },
    TierRank.F:{
        TierRank.F:0.5,
    }
}

# probability to win based on team composition (win prob w.r.t. team associated with first element)
prob_to_win_by_team = [
    # burst comps counter hpal + war
    [
        [ClassSpec.PRIEST_SHADOW,ClassSpec.ROGUE_SUB],
        [ClassSpec.PALADIN_HOLY,ClassSpec.WARRIOR_ARMS],
        [0.8],
    ],
    [
        [ClassSpec.SHAMAN_ELE,ClassSpec.WARLOCK_DESTRO],
        [ClassSpec.PALADIN_HOLY,ClassSpec.WARRIOR_ARMS],
        [0.65],
    ],
    # holy paladin counters insane melee burst from feral + rogue
    [
        [ClassSpec.PALADIN_HOLY,ClassSpec.ANY],
        [ClassSpec.DRUID_FERAL,ClassSpec.ROGUE_SUB],
        [0.7],
    ],
    # disarm counters marks hunters (cannot use deterrence without melee weapon)
    [
        [ClassSpec.PRIEST_SHADOW,ClassSpec.ANY],
        [ClassSpec.HUNTER_MARKS,ClassSpec.PRIEST_DISC],
        [0.7],
    ],
    [
        [ClassSpec.WARRIOR_ARMS,ClassSpec.ANY],
        [ClassSpec.HUNTER_MARKS,ClassSpec.PRIEST_DISC],
        [0.7],
    ],
    # frost mage counters arms warror without dispel for slows from warrior
    [
        [ClassSpec.MAGE_FROST,ClassSpec.ANY],
        [ClassSpec.WARRIOR_ARMS,ClassSpec.SHAMAN_RESTO],
        [0.9],
    ],
    [
        [ClassSpec.MAGE_FROST,ClassSpec.ANY],
        [ClassSpec.WARRIOR_ARMS,ClassSpec.DRUID_RESTO],
        [0.9],
    ],
]