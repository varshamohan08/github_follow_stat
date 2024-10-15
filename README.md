##### github_follow_stat
## GitHub Follow Stats
This project provides a Python script to fetch and analyze the follow statistics of a specified GitHub user. Using the GitHub API, the script identifies the accounts a user follows, their followers, and any users who are not following back. It also displays the total followers and following counts.

#### Features
- Retrieve Followers & Following: Uses the GitHub API to fetch followers and the users followed by the specified account.
- Pagination Handling: Automatically handles paginated API responses.
- Reciprocal Follow Check: Identifies accounts that you follow but do not follow you back.
- Summary Output: Displays useful follow statistics in a clear format.
#### Prerequisites
- Python 3.x
- requests library
  Install it using:
  ```
  pip install requests
  ```
#### Usage
- Clone the repository:
  ```
  git clone https://github.com/varshamohan08/github_follow_stat.git
  cd github_follow_stat
  ```
- Update the username:
  Replace the following line in the script with the desired GitHub username:
  ```
  get_github_follow_stats('username')
  ```
- Run the script:
  ```
  python follow_stats.py
  ```
- Example Output
  ```markdown
  Follow stats
  ------------
  Accounts not following back: user1, user2, user3
  Followers: 15
  Following: 20
  ```
#### Notes
Be mindful of GitHub’s API rate limits.
If you run into rate limits, you can use a personal access token (PAT) for higher request limits by passing it to the headers in the request.
#### License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/varshamohan08/github_follow_stat/blob/main/LICENSE) file for more details.

#### Contributing
Contributions are welcome! If you would like to make any changes, please open an issue or create a pull request.

#### Author
Developed by [varshamohan08](https://github.com/varshamohan08). Feel free to reach out with questions or suggestions.

### ***Disclaimer***
***This project was created for fun and as a way to explore the GitHub API. If you encounter any issues or have concerns, please feel free to reach out. I’ll be happy to address them or take down the project if needed.***
