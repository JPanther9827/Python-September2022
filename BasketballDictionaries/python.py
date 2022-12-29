players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_jason = Player("Jason Tatum", "small forward", "Boston Celtics", 24)
player_Kyrie = Player("Kyrie Irving", "Point Guard", "Brooklyn Nets", 32)
player_Kevin = Player("Kevin Durant", "small forward", "Brooklyn Nets", 34)
# (=================================================================================================================)

# ... (class definition and large list of players here)
# new_team = []
# # ... (class definition and large list of players here)
class New_team:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

Kobe = {
    	"name": "Kobe Bryant", 
    	"age":41, 
    	"position": "Shooting-Guard", 
    	"team": "Lakers"
}
Stephen = {
    	"name": "Stephen Curry", 
    	"age":34, 
    	"position": "Point Guard", 
    	"team": "Golden State Warriors"
}
Lebron = {
    	"name": "Lebron James", 
    	"age":37,
        "position": "small forward", 
    	"team": "Lakers"
}

# Write your for loop here to populate the new_team variable with Player objects.
for i in range(New_team):
	print(New_team)

# Write your for loop here to populate the new_team variable with Player objects.
    # Finally, given the example list of players at the top of this module (the one with many players) 
    # write a for loop that will populate an empty list with Player objects from the original list of dictionaries.