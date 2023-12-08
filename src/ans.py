""" 
Practice Question 3: Check Username Availability

Task:

Write a function is_username_available that takes two lists: current_users and new_users. The function should return a list of booleans indicating if each new user's username is available (not in current_users). The comparison should be case insensitive.
"""

def is_username_available(current_users, new_users):
    ans = []
    for i in range(len(current_users)):
        current_users[i] = current_users[i].lower()
    
    for user in new_users:
        ans.append(user.lower() not in current_users)

    return ans