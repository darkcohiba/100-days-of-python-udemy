class User:
    def __init__(self, username, age, id):
        self.id = id
        self.username = username
        self.age = 0

    def print_username(self):
        return f"My username is {self.username}"

    def print_age(self):
        return f"{self.username}'s age is {self.age} years old."

    def got_older(self, years):
        return f'{self.username} played video games and before you knew it {years} years went by!'
        self.age += years


sam = User("darkness", 15, 10)

print(sam.id)
print(sam.print_username())
print(sam.print_age())
print(sam.got_older(18))
print(sam.print_age())


