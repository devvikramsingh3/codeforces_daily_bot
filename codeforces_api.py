# import requests

# def get_user_rating(handle):
#     url = f"https://codeforces.com/api/user.info?handles={handle}"
#     response = requests.get(url).json()

#     if response['status'] != 'OK':
#         return None
    
#     return response['result'][0].get('rating', 0)  # 0 if unrated
import requests

def get_user_rating(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()  # raises HTTPError for bad status codes

        data = res.json()
        if data['status'] != 'OK':
            return None
        return data['result'][0].get('rating', 0)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network issue: {e}")
        return None
    except ValueError as e:
        print(f"[ERROR] JSON decode failed: {e}")
        print("Response content was:", res.text)
        return None
