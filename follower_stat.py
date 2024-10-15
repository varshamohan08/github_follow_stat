import requests

def fetch_paginated_data(url):
    """Helper function to handle pagination and collect all data."""
    results = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            results.extend(response.json())
            # Check if there's another page
            url = response.links.get('next', {}).get('url')
        elif response.status_code == 404:
            raise ValueError(f"Invalid username or resource not found. Status code: {response.status_code}")
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}.")
            return []
    return results

def get_github_follow_stats(username):
    try:
        base_url = f"https://api.github.com/users/{username}"

        # Fetch all following users
        following_url = f"{base_url}/following"
        following_data = fetch_paginated_data(following_url)
        following = {user['login'] for user in following_data}

        # Fetch all followers
        followers_url = f"{base_url}/followers"
        followers_data = fetch_paginated_data(followers_url)
        followers = {user['login'] for user in followers_data}

        # Check who isn't following back
        not_following_back = following - followers

        print("Follow stats")
        print("------------")
        print(f"Followers: {len(followers)}")
        print(f"Following: {len(following)}")
        if not following:
            print("You are not following anyone!")
        elif not not_following_back:
            print("Everyone you follow follows you back!")
        else:
            print("Accounts not following back:", ', '.join(not_following_back))
    except ValueError as e:
        print(e)


# Replace 'username' with your GitHub username
get_github_follow_stats('username')
