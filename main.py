def main():
    search_query = input("What do you want to search for? ")
    print("Choose detail level:")
    detail_levels = ['short', 'medium', 'large', 'enormous']
    for i, level in enumerate(detail_levels, 1):
        print(f"{i}. {level}")
    choice = int(input("Enter the number of your choice: ")) - 1

    if choice < 0 or choice >= len(detail_levels):
        print("Invalid choice!")
        return

    detail_level = detail_levels[choice]
    print(f"Searching for '{search_query}' with detail level '{detail_level}'...")
    # Actual search logic would go here

if __name__ == '__main__':
    main()