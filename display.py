
def display_results(films, search_type, search_query):
    print(f"\nSearch results for {search_type} - {search_query}:")
    for film in films:
        print(film[0])

def display_popular_searches():
    from database import get_log_connection
    conn_logs, cursor_logs = get_log_connection()

    query = """
        SELECT keyword, COUNT(*) as count FROM Denis_logs
        GROUP BY keyword ORDER BY count DESC LIMIT 5;
    """
    cursor_logs.execute(query)
    searches = cursor_logs.fetchall()

    print("\nMost popular searches:\n-----------------------------|")
    for search in searches:
        print(f"{search[0]} - {search[1]} times\n-----------------------------|")


    cursor_logs.close()
    conn_logs.close()
