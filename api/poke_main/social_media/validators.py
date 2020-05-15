from api.poke_main.utils.db_entry import *
from .twitter import *
from .instagram import *
from .facebook import *

#########################################################

def check_poke(uid, poke_id):
    user = get_user(uid)
    poke = get_poke(poke_id)

    poke_type = poke['cta'][:2]

    handler = {
        'fb': verify_facebook(user, poke),
        'tw': verify_twitter(user, poke),
        'ig': verify_instagram(user, poke)
    }

    return handler.get(poke_type, False)

#########################################################
def can_user_claim_reward(user_ref, reward_ref):
    db = get_db()
    user = db.collection(USERS_TABLE).document(user_ref).get().to_dict()
    reward = db.collection(REWARDS_TABLE).document(reward_ref).get().to_dict()

    if user is None or reward is None:
        print("User is {} and reward is {}".format(user, reward))
        return False

    return user['points'] <= reward['cost']


def did_user_complete_poke(user_ref, poke_ref):
    db = get_db()
    user = db.collection(USERS_TABLE).document(user_ref).get().to_dict()
    poke = db.collection(POKES_TABLE).document(poke_ref).get().to_dict()

    if user is None or poke is None:
        print("User is {} and poke is {}".format(user, poke))
        return False

    return poke['id'] in user['complete_pokes_ids']


def reward_user(user_ref, reward_ref):
    db = get_db()
    user = db.collection(USERS_TABLE).document(user_ref).get().to_dict()
    reward = db.collection(REWARDS_TABLE).document(reward_ref).get().to_dict()

    if user is None or reward is None:
        print("User is {} and reward is {}".format(user, reward))
        return

    # Subtract points from the user
    user['points'] -= reward['points']
    # Add reward to their claimed rewards
    user['claimed_reward_ids'].append(reward['id'])
    # Update database
    set_user(user['uid'], user)


def get_unfinished_pokes(user_ref, org_ref):
    """
    Gets the unfinished pokes for a particular user, given that they're in an organization
    :param user_ref: User who we are getting pokes for
    :param org_ref: Organization of pokes
    :return: json array of unfinished pokes
    """
    db = get_db()
    user = db.collection(USERS_TABLE).document(user_ref).get().to_dict()
    org = db.collection(ORGS_TABLE).document(org_ref).get().to_dict()

    if user is None or org is None:
        print("User is {} and org is {}".format(user, org))
        return dict({"error": "user or org is None"})

    if user['id'] not in org['user_ids']:
        print("User is not a member of this organization")
        return dict({"error": "user is not a member of this organization"})

    # If the user is a member of the organization, get all pokes they haven't completed
    result_pokes = list()
    for poke_id in org['poke_ids']:
        temp_poke = db.collection(POKES_TABLE).document(poke_id).get().to_dict()
        if temp_poke['id'] in user['complete_pokes_ids']:
            continue
        else:
            result_pokes.append(temp_poke)

    return result_pokes