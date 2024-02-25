class User:
    def __init__(self, user_id, user_name):
    # Initialize the user object
        self.userid = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Steve")
user_2 = User("002", "Rac")

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)