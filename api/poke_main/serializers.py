"""
To serialize our models, we'll make use of dictionary unpacking.
Currently, we are working with our firestore documents as pure dictionaries, which
has its limitations and drawbacks. By serializing them into our dataclasses, it's much
easier to return a valid json response this way.

These serializers will just me functions that returns our data as a model (dataclass) from a dictionary.
"""
from .models import *


# Methods convert a dict of that object into the corresponding model
def to_poke_user(poke_user_dict):
    return PokeUser(**poke_user_dict)


def to_reward(reward_dict):
    return Reward(**reward_dict)


def to_poke(poke_dict):
    return Poke(**poke_dict)


def to_org(org_dict):
    return Org(**org_dict)