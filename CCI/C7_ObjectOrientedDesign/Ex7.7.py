class User():
    id = 0
    def __init__(self, user_name):
        User.id += 1
        self.id = type(self).id
        self.name = user_name
        self.books = []
        self.last_read = None
        self.profile = None
        self.friends = set()
        self.conv = {}
        self.unread = []

    def change_name(self):
        pass

    def change_profile(self):
        pass

    def add_friend(self, user):
        self.friends.add(user)

    def send_msg(self, friend, msg):
        if (user.id, friend.id) not in self.conv:
            self.conv = Conversation(user.id, friend.id)
        conv = self.conv[(user.id, friend.id)]
        conv.send(msg)

    def read_msg(self):
        for conv in self.unread:
            print(conv.log)

class Conversation():
    id = 0
    def __init__(self, user1, user2):
        type(self).id += 1
        self.id = type(self).id
        self.user1 = user1
        self.user2 = user2
        self.log = []

    def send(self, user2):
        user2.unread += [self]
