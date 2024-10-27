#Grocery-shopping-list
# Grocery Shopping List
shopping_list = []

# Add item to the list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

# Remove item from the list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

# Display the current shopping list
def display_list():
    if shopping_list:
        print("Current shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

add_item("Milk")
add_item("Bread")
remove_item("Milk")
display_list()

#SENARIO 2 : Student-Grade:
# Student Grades
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Eve": 88
}

# Calculate average grade
def calculate_average(grades):
    total = sum(grades.values())
    average = total / len(grades)
    return average

# Display average grade
average_grade = calculate_average(grades)
print(f"Average grade: {average_grade:.2f}")

#SENARIO 3: _Word frequency counter
# Word Frequency Counter
word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

# Count word frequency
def count_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Display word frequencies
word_frequencies = count_frequency(word_list)
for word, count in word_frequencies.items():
    print(f"{word}: {count}")

#SENARIO_4 : Voting system
# List of candidates
candidates = ["Candidate A", "Candidate B", "Candidate C"]

# Dictionary to store votes for each candidate
votes = {candidate: 0 for candidate in candidates}

# Function to display candidates and take votes
def voting_process(num_voters):
    print("Candidates:")
    for idx, candidate in enumerate(candidates, start=1):
        print(f"{idx}. {candidate}")
    
    # Record votes
    for voter in range(1, num_voters + 1):
        while True:
            try:
                vote = int(input(f"\nVoter {voter}, please enter the number of your preferred candidate (1-{len(candidates)}): "))
                if 1 <= vote <= len(candidates):
                    selected_candidate = candidates[vote - 1]
                    votes[selected_candidate] += 1
                    print(f"Vote recorded for {selected_candidate}.")
                    break
                else:
                    print(f"Invalid input. Please enter a number between 1 and {len(candidates)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Function to display the voting results
def display_results():
    print("\nVoting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    
    # Determine the winner
    max_votes = max(votes.values())
    winners = [candidate for candidate, count in votes.items() if count == max_votes]

    # Display the winner(s)
    if len(winners) > 1:
        print("\nIt's a tie between: " + ", ".join(winners))
    else:
        print(f"\nThe winner is: {winners[0]}")

# Main logic
def main():
    try:
        num_voters = int(input("Enter the number of voters: "))
        if num_voters <= 0:
            print("The number of voters must be greater than zero.")
            return
        
        voting_process(num_voters)
        display_results()

    except ValueError:
        print("Invalid input. Please enter a valid number of voters.")

# Run the program
if __name__ == "__main__":
    main()
