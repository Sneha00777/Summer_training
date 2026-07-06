world_cup = {
    "2023": {
        "teams": ["India", "England", "Bangladesh", "Pakistan"],
        "captains": ["Virat", "Aaron Finch", "Eoin Morgan"],
        "winner": "India"
    },
    "2024": {
        "teams": ["India", "England", "Bangladesh", "Pakistan"],
        "captains": ["Virat", "Aaron Finch", "Eoin Morgan"],
        "winner": "India"
    }
}


year = input("Enter a year: ")

if year in world_cup:
    print("Teams:", world_cup[year]["teams"])
    print("Captains:", world_cup[year]["captains"])
    print("Winner:", world_cup[ year]["winner"])
else:
    print("Sorry, data for that year does not exist!")
for year in world_cup:
    print("Teams:", world_cup[year]["teams"])
    print("Captains:", world_cup[year]["captains"])
    print("Winner:", world_cup[year]["winner"])
    print()  