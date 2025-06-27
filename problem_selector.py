import requests
import random

def get_problem_for_rating(user_rating):
    url = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url).json()
    if response['status'] != 'OK':
        return None

    problems = response['result']['problems']
    problems = [p for p in problems if 'rating' in p and abs(p['rating'] - user_rating) <= 100]

    if not problems:
        return None

    chosen = random.choice(problems)
    return {
        "name": f"{chosen['contestId']}{chosen.get('index')}: {chosen['name']}",
        "url": f"https://codeforces.com/problemset/problem/{chosen['contestId']}/{chosen['index']}"
    }
