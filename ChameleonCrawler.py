import re

def find_keywords_and_link_to_username(posts, keywords):
    """
    Finds specified keywords in social media posts and links them to usernames.

    Args:
        posts: A list of dictionaries, where each dictionary represents a post 
               and contains 'text' (post content) and 'username' keys.
        keywords: A list of keywords to search for.

    Returns:
        A dictionary where keys are keywords and values are lists of usernames 
        whose posts contain that keyword. Returns an empty dictionary if no 
        matches are found. Handles case-insensitive keyword matching.
    """

    keyword_username_map = {}
    for keyword in keywords:
        keyword_username_map[keyword] = []

    for post in posts:
        text = post.get('text', '').lower()
        username = post.get('username', 'unknown')
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', text):
                keyword_username_map[keyword].append(username)

    return keyword_username_map


# Example usage:
posts_data = [
    {'text': 'This is a test post about Python. #python #programming', 'username': 'user1'},
    {'text': 'Another post mentioning JavaScript. #javascript', 'username': 'user2'},
    {'text': 'Python is awesome! #python', 'username': 'user3'},
    {'text': 'I love programming in Java. #java', 'username': 'user4'}
]

keywords_to_search = ['python', 'javascript', 'java']

results = find_keywords_and_link_to_username(posts_data, keywords_to_search)
print(results)
