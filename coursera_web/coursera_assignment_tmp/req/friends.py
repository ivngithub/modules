import json
from datetime import datetime
import requests

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

"""
https://api.vk.com/method/users.get?v=5.71&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_ids=id90437796
"""

"""
https://api.vk.com/method/friends.get?v=5.71&access_token=17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711&user_id=90437796&fields=bdate
"""

def loader(request):
    response = requests.get(request)
    response = json.loads(response.content)

    return response['response']

def get_bdate_friends(user):
    users_get = 'https://api.vk.com/method/users.get?v=5.71' \
                '&access_token={token}' \
                '&user_ids={user}'.format(token=ACCESS_TOKEN, user=user)

    users = loader(users_get)
    user_id = users[0]['id']

    bdate_friends_get = 'https://api.vk.com/method/friends.get?v=5.71' \
                        '&access_token={token}' \
                        '&user_id={user_id}&fields=bdate'.format(token=ACCESS_TOKEN, user_id=user_id)

    bdate_friends = loader(bdate_friends_get)

    return bdate_friends['items']

def calc_age(uid):

    bdate_friends = get_bdate_friends(uid)
    # {'id': 556114716, 'first_name': 'Alexander', 'last_name': 'Lobanov', 'bdate': '17.7.1990'}

    def _filter_date(date):

        try:
            _ = datetime.strptime(date.get('bdate'), '%d.%m.%Y').date()
        except (ValueError, TypeError):
            return False
        else:
            return True

    def _set_date(item):

        item['bdate'] = datetime.strptime(item.get('bdate'), '%d.%m.%Y').date()

        return item

    bdate_friends = filter(_filter_date, bdate_friends)
    bdate_friends = map(_set_date, bdate_friends)

    today = datetime.now()
    resume_age = dict()

    for bdate_friend in bdate_friends:

        age = today.year - bdate_friend['bdate'].year
        resume_age[age] = resume_age.get(age, 0) + 1

    return [(age, count) for age, count in resume_age.items()]


if __name__ == '__main__':
    res = calc_age('id90437796')
    print(res)
