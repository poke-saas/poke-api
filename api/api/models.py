"""
Since we are working with Google Firestore to handle information, and not a relational database, we
cannot leverage Django's models framework, as those migrations occur over relational databses.

Instead, we can make a dataclass to model each item, and then serialize the response from the google firestore into one of
these dataclasses for easy lookups.
"""

from typing import *
from dataclasses import dataclass

# First, start out with the users.
@dataclass
class PokeUser:
    full_name: str
    id: str
    org_id: str
    phone: str
    points: int
    profile_picture_link: str
    claimed_reward_ids: list
    complete_poke_ids: list
    user_credentials: map

# Next, the Rewards
@dataclass
class Reward:
    cost: int
    desc: str
    id: str
    img: str
    name: str

# Pokes
@dataclass
class Poke:
    cta: str
    data: map
    deadline: str
    desc: str
    id: int
    name: str
    pts: int

# Finally, orgs
@dataclass
class Org:
    icon: str
    id: str
    name: str
    poke_ids: list
    reward_ids: list
    user_ids: list
