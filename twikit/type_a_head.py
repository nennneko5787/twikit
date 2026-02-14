class SuggestionUser:
    """
    {'id': 130447415, 'id_str': '130447415', 'verified': False, 'ext_is_blue_verified': True, 'badges': [], 'is_dm_able': False, 'is_secret_dm_able': False, 'is_persona_media_genable': False, 'is_blocked': False, 'can_media_tag': False, 'name': 'HIKAKIN😎ヒカキン 【YouTuber】', 'screen_name': 'hikakin', 'profile_image_url': 'http://pbs.twimg.com/profile_images/2006602716844535810/zaKv0MUS_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/2006602716844535810/zaKv0MUS_normal.jpg', 'location': 'Tokyo', 'is_protected': False, 'rounded_score': 0, 'social_proof': 0, 'connecting_user_count': 0, 'connecting_user_ids': [], 'social_proofs_ordered': [], 'social_context': {'following': False, 'followed_by': False}, 'tokens': [], 'inline': False}
    """

    def __init__(self, data: dict):
        self.id = data["id"]
        self.screen_name = data["screen_name"]
        self.name = data["name"]
        self.profile_image_url = data["profile_image_url_https"]
        self.location = data["location"]
        self.verified = data["verified"]
        self.is_blue_verified = data["ext_is_blue_verified"]
        self.can_media_tag = data["can_media_tag"]
        self.can_dm = data["is_dm_able"]
        self.protected = data["is_protected"]


class SuggestionResult:
    """
    Attributes
    ----------
    num_results : :class:`int`
        Number of search suggestions.
    topics : :class:`list`
        Topic search suggestions.
    users : :class:`list`
        User search suggestions.
    """

    def __init__(self, data: dict):
        self.num_results = data["num_results"]
        self.topics = [result["topic"] for result in data["topics"]]
        self.users = [SuggestionUser(result) for result in data["users"]]
