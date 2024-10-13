def find_completions(search_data, partial_query):
       results = []
    for entry in search_data:
        if entry.startswith(partial_query):
            results.append(entry)
    return results

search_data = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]


user_query = input("Enter the start of your search query: ")


matched_results = find_completions(search_data, user_query)

if matched_results:
    print("Possible completions:")
    for item in matched_results:
        print(item)
else:
    print("No matches for your query.")
