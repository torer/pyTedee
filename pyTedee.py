import requests, json, argparse, config

parser = argparse.ArgumentParser()
parser.add_argument("--attr")
parser.add_argument("--action")
parser.add_argument("--name")
args = parser.parse_args()


def log_oauth() :
    url='https://tedee.b2clogin.com/tedee.onmicrosoft.com/oauth2/v2.0/token?p=B2C_1_SignIn_Ropc&grant_type=password&username=%s&password=%s&scope=openid 02106b82-0524-4fd3-ac57-af774f340979&client_id=02106b82-0524-4fd3-ac57-af774f340979'% (
    config.tedee_config['login'], config.tedee_config['password'])
    r = requests.post(url)
    token = json.loads(r.text)['access_token']
    return (token)


def get_all():
    headers = {"Authorization": "Bearer " + log_oauth()}
    r = requests.get('https://api.tedee.com/api/v1.14/my/lock', headers=headers)
    return ( json.loads(r.text))


def lock_status():
# state
# 2 = open
# 3 = half closed
# 4 = opening
# 5 = closing
# 6 = closed
    headers = {"Authorization": "Bearer " + log_oauth() }
    r = requests.get('https://api.tedee.com/api/v1.14/my/lock',headers=headers)
    return (json.dumps(json.loads(r.text)['result'][0]['lockProperties']))


def open(lock_id):
    post_data = {"deviceId": lock_id}
    headers = {"Authorization": "Bearer " + log_oauth(), 'Content-Type': 'application/json'}
    r = requests.post('https://api.tedee.com/api/v1.14/my/lock/open', json=post_data, headers=headers)
    print(r.text)


def close(lock_id):
    post_data = {"deviceId": lock_id}
    headers = {"Authorization": "Bearer " + log_oauth(), 'Content-Type': 'application/json'}
    r = requests.post('https://api.tedee.com/api/v1.14/my/lock/close', json=post_data, headers=headers)
    print(r.text)


def get_id_by_name(name):
    values = get_all()
    for k in values['result']:
        if k['name'] == name:
            return k['id']


if args.attr:
    print(json.loads(lock_status())[args.attr])

if args.action:
    if args.action == 'showAll':
        print(get_all())
    elif args.action == 'open':
        open(get_id_by_name(args.name))
    elif args.action == 'close':
        close(get_id_by_name(args.name))
    elif args.action == 'name':
        print (get_id_by_name(args.name))

