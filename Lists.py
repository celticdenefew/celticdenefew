## Playing with lists on Code Academy
## Starting with a list of votes, I feel like manipulating them

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

## Adding and printing out the number of times each candidate was voted for
votes_for_Jake = votes.count("Jake")
votes_for_Laurie = votes.count("Laurie")
votes_for_Cassie = votes.count("Cassie")

print("Jake has", votes_for_Jake, "votes")
print("Laurie has", votes_for_Laurie, "votes")
print("Cassie has", votes_for_Cassie, "votes")
print()

## Finding out who won with if statements
if votes_for_Jake > votes_for_Laurie and votes_for_Jake > votes_for_Cassie:
    print("Jake won with", votes_for_Jake, "votes!")
if votes_for_Laurie > votes_for_Cassie and votes_for_Jake < votes_for_Laurie:
    print("Laurie won with", votes_for_Laurie, "votes!")
if votes_for_Cassie > votes_for_Laurie and votes_for_Jake < votes_for_Cassie:
    print("Cassie won with", votes_for_Cassie, "votes!")

