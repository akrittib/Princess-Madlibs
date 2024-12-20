import random
name = input("Name: ")
adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
place = input("Place: ")
adj3 = input("Adjective: ")
friend = input('Name: ')
occupation = input('Job: ')
ing = input("Verb ending in ing: ")
noun1 = input("Noun: ")
age = input('Number: ')
noun2 = input("Noun: ")
bp = input("Body Part: ")
number = input("Number: ")



madlib1 = f"Once upon a time there lived a princess named {name}. {name} was known for being the most {adj1} and {adj2} girl in the kingdom of \
{place}. But little did eveyone else know, {name} had a sercet. One {adj3} morning, {name} snuck out of the palace to meet her friend {friend}. \
{friend} was the town {occupation}, who was known for his trouble making ways. {friend} convinced {name} to start {ing} {noun1} and has been \
addicted ever since. This addiction lead to her untimely death at age {age}"

madlib2 = f"Long ago there lived a {adj1} princess named {name}. When {name} was {age} years old, she was kidnapped from her home, the {adj2} \
palace of {place} by an evil witch. {friend}, the witch, desguised herself as a {adj3} {occupation} by day, but her real passion lied somewhere \
else. {friend} was intent on turning {noun1} into {noun2}, a task that could only be completed using the princesses {bp}. Each night the witch \
would come visit the princess in her cell and steal some of her {bp} to mix into her potion. However, before {friend} could complete her evil \
spell, {name} managed to escape and the witch was thrown in jail, sentenced to {number} years in prison."

madlib3 = f"In a {adj1} kingdom called {place}, Princess {name} dreamed of becoming a {adj2} {occupation}. But in the royal life, there was no \
place for {ing} {noun1}. One day, while exploring the palace gardens, {name} discovered a magical {noun2}. It foretold that only the {adj3} of \
heart can save the kingdom, from impending doom. With the help of {friend}, {name} embarked on a quest to save the kingdom, proving that princesses \
can be anything they dream of being."


madlibs = [madlib1, madlib2, madlib3]

chosen_madlib = random.choice(madlibs)

print(chosen_madlib)


