#!/usr/bin/env python3
from typing import Final


ICONS: Final[dict[int, str]] = {
    1: "<:antimage_icon:1274867157041414165>",
    2: "<:axe_icon:1274867174221152387>",
    3: "<:bane_icon:1274867183364603934>",
    4: "<:bloodseeker_icon:1274867208639615121>",
    5: "<:crystal_maiden_icon:1274867315565006859>",
    6: "<:drow_ranger_icon:1274867409055907881>",
    7: "<:earthshaker_icon:1274867420854485073>",
    8: "<:juggernaut_icon:1274867675419381800>",
    9: "<:mirana_icon:1274868004127117483>",
    10: "<:morphling_icon:1274868047479439410>",
    11: "<:nevermore_icon:1274868125904535574>",
    12: "<:phantom_lancer_icon:1274868358923157697>",
    13: "<:puck_icon:1274868454918455326>",
    14: "<:pudge_icon:1274868487587758090>",
    15: "<:razor_icon:1274868600473260032>",
    16: "<:sand_king_icon:1274868694690041938>",
    17: "<:storm_spirit_icon:1274869131233067090>",
    18: "<:sven_icon:1274869148530380906>",
    19: "<:tiny_icon:1274869265174106225>",
    20: "<:vengefulspirit_icon:1274869374565748736>",
    21: "<:windrunner_icon:1274869507386511401>",
    22: "<:zuus_icon:1274869575011401831>",
    23: "<:kunkka_icon:1274867704167141386>",
    25: "<:lina_icon:1274867791651930122>",
    26: "<:lion_icon:1274867808202788987>",
    27: "<:shadow_shaman_icon:1274868757478772766>",
    28: "<:slardar_icon:1274868966589861958>",
    29: "<:tidehunter_icon:1274869230160056320>",
    30: "<:witch_doctor_icon:1274869557571358734>",
    31: "<:lich_icon:1274867756948389928>",
    32: "<:riki_icon:1274868632001843321>",
    33: "<:enigma_icon:1274867501515411527>",
    34: "<:tinker_icon:1274869247662620776>",
    35: "<:sniper_icon:1274869074567888981>",
    36: "<:necrolyte_icon:1274868098880507987>",
    37: "<:warlock_icon:1274869463635857431>",
    38: "<:beastmaster_icon:1274867200448135270>",
    39: "<:queenofpain_icon:1274868540620668928>",
    40: "<:venomancer_icon:1274869389425905768>",
    41: "<:faceless_void_icon:1274867515331317802>",
    42: "<:skeleton_king_icon:1274868899837382809>",
    43: "<:death_prophet_icon:1274867367880429568>",
    44: "<:phantom_assassin_icon:1274868330569662525>",
    45: "<:pugna_icon:1274868515538468936>",
    46: "<:templar_assassin_icon:1274869189189963776>",
    47: "<:viper_icon:1274869406794514463>",
    48: "<:luna_icon:1274867843569160284>",
    49: "<:dragon_knight_icon:1274867399664865350>",
    50: "<:dazzle_icon:1274867358736973916>",
    51: "<:rattletrap_icon:1274868566730080287>",
    52: "<:leshrac_icon:1274867737562189994>",
    53: "<:furion_icon:1274867548667641998>",
    54: "<:life_stealer_icon:1274867774232985610>",
    55: "<:dark_seer_icon:1274867325199454319>",
    56: "<:clinkz_icon:1274867307528716420>",
    57: "<:omniknight_icon:1274868247849730078>",
    58: "<:enchantress_icon:1274867486193614920>",
    59: "<:huskar_icon:1274867614140600473>",
    60: "<:night_stalker_icon:1274868151338930239>",
    61: "<:broodmother_icon:1274867250230198294>",
    62: "<:bounty_hunter_icon:1274867219431690371>",
    63: "<:weaver_icon:1274869481847394424>",
    64: "<:jakiro_icon:1274867656968769546>",
    65: "<:batrider_icon:1274867190948171837>",
    66: "<:chen_icon:1274867299530182801>",
    67: "<:spectre_icon:1274869095036096542>",
    68: "<:ancient_apparition_icon:1274867147348119663>",
    69: "<:doom_bringer_icon:1274867389380690054>",
    70: "<:ursa_icon:1274869352616689696>",
    71: "<:spirit_breaker_icon:1274869112341921855>",
    72: "<:gyrocopter_icon:1274867579348848673>",
    73: "<:alchemist_icon:1274867138540339201>",
    74: "<:invoker_icon:1274867637956116490>",
    75: "<:silencer_icon:1274868846326583338>",
    76: "<:obsidian_destroyer_icon:1274868194430943253>",
    77: "<:lycan_icon:1274867859373297767>",
    78: "<:brewmaster_icon:1274867229032189973>",
    79: "<:shadow_demon_icon:1274868730203213896>",
    80: "<:lone_druid_icon:1274867825537978380>",
    81: "<:chaos_knight_icon:1274867270199283734>",
    82: "<:meepo_icon:1274867955942817954>",
    83: "<:treant_icon:1274869284010594400>",
    84: "<:ogre_magi_icon:1274868222511943741>",
    85: "<:undying_icon:1274869335625695262>",
    86: "<:rubick_icon:1274868670023335977>",
    87: "<:disruptor_icon:1274867379746111619>",
    88: "<:nyx_assassin_icon:1274868177737875591>",
    89: "<:naga_siren_icon:1274868079683309628>",
    90: "<:keeper_of_the_light_icon:1274867689361244160>",
    91: "<:wisp_icon:1274869541897502810>",
    92: "<:visage_icon:1274869426822320241>",
    93: "<:slark_icon:1274868999938773143>",
    94: "<:medusa_icon:1274867932366770246>",
    95: "<:troll_warlord_icon:1274869300506787840>",
    96: "<:centaur_icon:1274867259747205241>",
    97: "<:magnataur_icon:1274867874548416654>",
    98: "<:shredder_icon:1274868808128925800>",
    99: "<:bristleback_icon:1274867240436498616>",
    100: "<:tusk_icon:1274869318672322581>",
    101: "<:skywrath_mage_icon:1274868938777559050>",
    102: "<:abaddon_icon:1274867103689867364>",
    103: "<:elder_titan_icon:1274867450038583306>",
    104: "<:legion_commander_icon:1274867716435738726>",
    105: "<:techies_icon:1274869170021859338>",
    106: "<:ember_spirit_icon:1274867461451157676>",
    107: "<:earth_spirit_icon:1274867436595970139>",
    108: "<:abyssal_underlord_icon:1274867128511496294>",
    109: "<:terrorblade_icon:1274869213323857961>",
    110: "<:phoenix_icon:1274868384235913257>",
    111: "<:oracle_icon:1274868273250570342>",
    112: "<:winter_wyvern_icon:1274869527452319794>",
    113: "<:arc_warden_icon:1274867165698326549>",
    114: "<:monkey_king_icon:1274868026625364021>",
    119: "<:dark_willow_icon:1274867337761263728>",
    120: "<:pangolier_icon:1274868290950402153>",
    121: "<:grimstroke_icon:1274867563746299944>",
    123: "<:hoodwink_icon:1274867596776181892>",
    126: "<:void_spirit_icon:1274869445109743709>",
    128: "<:snapfire_icon:1274869050278809671>",
    129: "<:mars_icon:1274867910329892979>",
    135: "<:dawnbreaker_icon:1274867350251765780>",
    136: "<:marci_icon:1274867889081548840>",
    137: "<:primal_beast_icon:1274868421988978802>",
    138: "<:muerta_icon:1274868062012706816>"
}

dota_plus = "<:dotaplus:1275400946234425375>"
