import requests
import datetime


def calc_age(uid):
    # age frequency calculation for friends of uid through vk api
    a_t = "17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711" #access token from test

    # id from input by vk api
    url_01 = "https://api.vk.com/method/users.get"
    payload = {'v': 5.71, 'access_token': a_t, 'user_ids': uid}
    r = requests.get(url_01, params=payload).json()
    id = r["response"][0]['id']

    # friends age from vk fpi
    url_02 = "https://api.vk.com/method/friends.get"
    payload = {'v': 5.71, 'access_token': a_t, 'user_id': id, 'fields': 'bdate'}
    r = requests.get(url_02, params=payload).json()

    # get delta yy for all existing dates in right format: dd.mm.yyyy
    sorted_list = []
    for i in r["response"]['items']:
        if 'bdate' in i:
            dd = i["bdate"].split(".")
            if len(dd) == 3:
                dd = datetime.datetime.now().year - int(dd[-1])
                sorted_list.append(dd)
    # calculating & sorting by frequency
    dic_bd = {}
    for i in sorted_list:
        if i not in dic_bd:
            dic_bd[i] = 0
        dic_bd[i] += 1

    sorted_list = sorted(dic_bd.items(), key=lambda x: (-x[1], x[0]))

    return sorted_list


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
