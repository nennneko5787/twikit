from enum import Enum
from typing import Union


class ReportCategoryOption(str, Enum):
    HATEFUL_CONDUCT = "HatefulConductOption"
    ABUSIVE_BEHAVIOR = "AbusiveBehaviorOption"
    VIOLENT_SPEECH = "ViolentSpeechOption"
    CHILD_SAFETY = "ZazuChildSafetyOption"
    PRIVACY = "PrivacyOption"
    ILLEGAL_AND_REGULATED = "IllegalAndRegulatedBehaviorsOption"
    SPAMMED = "SpammedOption"
    SUICIDE_SELF_HARM = "SuicideSelfHarmOption"
    SENSITIVE_DISTURBING_MEDIA = "ShownSensitiveDisturbingMediaOption"
    DECEPTIVE_IDENTITIES = "DeceptiveIdentitiesOption"
    VIOLENT_AND_HATEFUL_ENTITIES = "ViolentAndHatefulEntitiesOption"
    CIVIC_INTEGRITY = "CivicIntegrityOption"


class HateDetailOption(str, Enum):
    USING_SLURS = "UsingSlursOption"
    HATEFUL_REFERENCE = "HatefulReferenceOption"
    DEHUMANIZING = "DehumanizingOption"
    SENDING_UNWANTED_IMAGERY = "SendingUnwantedImageryOption"
    ENCOURAGING_DENYING_FINANCIAL_SUPPORT = (
        "EncouragingDenyingFinancialSupportOnIdentityOption"
    )


class AbusiveBehaviorDetailOption(str, Enum):
    SENDING_ADULT_CONTENT = "SendingAdultContent"
    TARGETED_HARASSMENT = "TargetedHarassmentOption"
    INSULTING = "InsultingOption"
    UNWANTED_SEXUAL_CONTENT = "UnwantedSexualContentOption"
    DENYING_VIOLENT_EVENT = "DenyingViolentEventOption"
    INCITING_HARASSMENT = "IncitingHarassmentOption"


class ViolentSpeechDetailOption(str, Enum):
    THREATENING_WITH_VIOLENCE = "ThreateningWithViolence"
    CELEBRATING_VIOLENT_ACTS = "CelebratingViolentActs"
    INCITEMENT_OF_VIOLENCE = "IncitementOfViolenceOption"
    WISH_OF_HARM = "WishOfHarmOption"
    CODED_INCITEMENT_OF_VIOLENCE = "CodedIncitementOfViolenceOption"


class ChildSafetyDetailOption(str, Enum):
    SEXUAL_CONTENT_INVOLVING_MINOR = "SexualContentInvolvingMinor"
    SEXUALISING_MINOR = "SexualisingMinor"
    GROOMING_MINOR = "GroomingMinor"
    CHILD_SEX_TRAFFICKING = "ChildSexTrafficking"
    PHYSICAL_CHILD_ABUSE = "PhysicalChildAbuse"
    MINOR_AT_RISK = "MinorAtRisk"
    DEPICTING_MINOR_IN_SEXUAL_ACT = "DepictingMinorInSexualAct"
    UNDERAGE_USER = "UnderageUserOption"
    NORMALIZING_CHILD_EXPLOITATION = "NormalizingChildExploitationOption"


class PrivacyDetailOption(str, Enum):
    THREATENING_TO_EXPOSE = "ThreateningToExposeOption"
    SHARE_INTIMATE_PHOTO = "ShareIntimatePhoto"
    SHARE_PERSONAL_PHOTO = "SharePersonalPhoto"


class IllegalAndRegulatedDetailOption(str, Enum):
    HUMAN_EXPLOITATION = "HumanExploitation"
    SEXUAL_SERVICES = "SexualServices"
    DRUGS = "Drugs"
    WEAPONS = "Weapons"
    ENDANGERED_SPECIES = "EndangeredSpecies"
    FACILITATING_ILLEGAL_ACTIVITY = "FacilitatingIllegalActivity"


ReportSubCategoryOption = Union[
    HateDetailOption,
    AbusiveBehaviorDetailOption,
    ViolentSpeechDetailOption,
    ChildSafetyDetailOption,
    PrivacyDetailOption,
    IllegalAndRegulatedDetailOption,
]
