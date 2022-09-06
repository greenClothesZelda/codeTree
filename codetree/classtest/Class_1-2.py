class User:
    def __init__(self, id = "codetree", level = 10):
        self.id = id
        self.level = level

arr = input().split()

user2 = User(arr[0], arr[1])
user1 = User()

print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")