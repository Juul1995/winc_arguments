# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# In de opdracht werd getipt dat libraries moest kunnen indexen - Creating and indexing dictionaries; Writing functions and function arguments; Using various operators?

# Part 1, string method ; replace


def greet(name, greet_template="Hello, <name>!"):
    return greet_template.replace("<name>", name)


#print(greet('Bob', "What's up, <name>!"))

# Part 2, force = mass × gravity, start met een library met alle gravities
# dict body, gravity afgerond tot 1 decimaal, per planeet. Dat zijn dus floats, planeet is in kleine letters.

planet = {"sun": 247.0, "jupiter": 24.92, "neptune": 11.15, "saturn": 10.44, "earth": 9.798,
          "uranus": 8.87, "venus": 8.87, "mars": 3.71, "mercury": 3.7, "moon": 1.62, "pluto": 0.58}


def force(mass, body="earth"):
    h = round(planet[body.lower()], 1)
    return mass * h


print(force(39, "sun"))
print(force(79, "Jupiter"))
print(force(5))

# Part 3, function "Pull" 3'arguments, pull = G × ((m1 × m2)/d2)


def pull(m1, m2, d):
    return (6.674*10**-11)*((m1*m2)/(d**2))


print(pull(38, 85, 3))
