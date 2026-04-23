def search_documents(query):
    """Return document matches for a simple in-memory search index."""
    documents = [
        {
            'title': 'Python basics',
            'tags': ['python', 'programming', 'beginners'],
            'summary': 'Introduction to Python syntax, variables and control flow.',
            'details': 'Python is a popular high-level language used for web development, scripting, and automation. It supports dynamic typing, easy-to-read syntax, and many libraries.'
        },
        {
            'title': 'Tkinter GUI',
            'tags': ['python', 'gui', 'tkinter'],
            'summary': 'Build desktop applications with Tkinter.',
            'details': 'Tkinter is included with Python and lets you create windows, buttons, labels, text fields, and handle user events. It is good for simple GUI tools.'
        },
        {
            'title': 'Digital clock app',
            'tags': ['clock', 'time', 'tkinter', 'python'],
            'summary': 'Display multiple time zones in a desktop window.',
            'details': 'A digital clock app shows the current time for several timezones and updates every second. You can use pytz or zoneinfo for timezone support.'
        }
    ]

    query_lower = query.lower().strip()
    results = []

    for doc in documents:
        if query_lower in doc['title'].lower() or any(query_lower in tag for tag in doc['tags']):
            results.append(doc)

    return results


def format_result(doc, detail_level):
    """Format the result text depending on the requested detail level."""
    if detail_level == 'short':
        return f"- {doc['title']}"
    if detail_level == 'medium':
        return f"- {doc['title']}: {doc['summary']}"
    if detail_level == 'large':
        return f"- {doc['title']}:\n  {doc['summary']}\n  {doc['details']}"
    if detail_level == 'enormous':
        return f"- {doc['title']}:\n  Tags: {', '.join(doc['tags'])}\n  Summary: {doc['summary']}\n  Details: {doc['details']}"
    return f"- {doc['title']}"


def choose_detail_level():
    detail_levels = ['short', 'medium', 'large', 'enormous']
    print('Choose detail level:')
    for i, level in enumerate(detail_levels, 1):
        print(f"{i}. {level}")

    while True:
        choice = input('Enter the number of your choice: ').strip()
        if not choice.isdigit():
            print('Please enter a number.')
            continue

        index = int(choice) - 1
        if 0 <= index < len(detail_levels):
            return detail_levels[index]

        print('Invalid choice, try again.')


def main():
    search_query = input('What do you want to search for? ').strip()
    if not search_query:
        print('You must enter a search query.')
        return

    detail_level = choose_detail_level()
    print(f"\nSearching for '{search_query}' with detail level '{detail_level}'...\n")

    results = search_documents(search_query)
    if not results:
        print('No results found. Try a different query.')
        return

    for doc in results:
        print(format_result(doc, detail_level))


if __name__ == '__main__':
    main()
