
from search import search_by_category, search_by_actor, search_by_genre_and_year, search_by_keyword
from display import display_popular_searches

def main():
    while True:
        print("\nChoose a movie search method:")
        print("1 - Search by Category")
        print("2 - Search by Actor's Name")
        print("3 - Search by Genre and Year")
        print("4 - Search by Keyword in Movie Title")
        print("5 - View popular user searches")
        print("0 - Exit")
        choice = input("Enter number: ")

        if choice == "1":
            search_by_category()
        elif choice == "2":
            search_by_actor()
        elif choice == "3":
            search_by_genre_and_year()
        elif choice == "4":
            search_by_keyword()
        elif choice == "5":
            display_popular_searches()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
