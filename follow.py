import requests, string,random,time

def genString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def data1():
    try:
        data = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query=%s&rank_token=0&include_reel=true"%(genString(random.randint(1,3)))).json()
        randData = random.randint(0, len(data))
        ret = {
            "username": data["users"][randData]["user"]["username"],
            "id": data["users"][randData]["user"]["pk"]
        }
        return ret
    except Exception as e:
        print(e)
        return False

def data2(username):
    try:
        data = requests.get("https://www.instagram.com/%s/?__a=1"%(username)).json()
        ret = {
            "id": data["graphql"]["user"]["id"],
            "profile_pic": data["graphql"]["user"]["profile_pic_url"],
            "count": data["graphql"]["user"]["edge_followed_by"]["count"]
        }
        return ret
    except Exception as e:
        print(e)
        return False


username = "raysdenni"
infoData = data2(username)
while(True):
    try:
        gen = data1()
        dataPost = {
            "username1": gen["username"],
            "id1": gen["id"],
            "id2": infoData["id"],
            "profile_pic": infoData["profile_pic"],
            "count": infoData["count"]
        }
        a = requests.post("http://54.169.227.74:6969/v2", data=dataPost)
        print(a.text)
        print("Sleeping 5 seconds")
        time.sleep(5)
    except:
        print("error")
