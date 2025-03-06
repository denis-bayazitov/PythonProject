
from database import get_db_connection, log_search
from user_input import get_valid_category


def handle_empty_result(results, search_type, search_query):
    if not results:
        print(f"\nNo results found for {search_type}: {search_query}")
        print("****************************")
        return True
    return False


def search_by_category():
    conn, cursor = get_db_connection() # Распаковка кортежа (conn, cursor)
    cursor.execute("SELECT category_id, name FROM category")
    categories = cursor.fetchall()

    category_id, category_name = get_valid_category(categories) # Распаковка кортежа
    if not category_id:
        return # Прерываем выполнение функции, если категория не найдена и возвращаемся в main

    query = """
        SELECT f.title FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        WHERE fc.category_id = %s LIMIT 5;
    """
    cursor.execute(query, (category_id,))
    films = cursor.fetchall()

    if handle_empty_result(films, "Category", category_name):
        return

    print(f"\nSearch results for Category {category_name}:")
    for film in films:
        print(film[0])

    print("****************************")

    log_search("By Category", category_name)


def search_by_actor():
    conn, cursor = get_db_connection()
    actor_name = input("Enter Actor's first name: ")

    query = """
        SELECT f.title FROM film f
        JOIN film_actor fa ON f.film_id = fa.film_id
        JOIN actor a ON fa.actor_id = a.actor_id
        WHERE a.first_name = %s LIMIT 5;
    """
    cursor.execute(query, (actor_name,))
    films = cursor.fetchall()

    if handle_empty_result(films, "Actor", actor_name):
        return

    print(f"\nSearch results for Actor {actor_name}:")
    for film in films:
        print(film[0])

    print("****************************")

    log_search("By Actor", actor_name)


import datetime


def search_by_genre_and_year():
    conn, cursor = get_db_connection()
    cursor.execute("SELECT category_id, name FROM category")
    categories = cursor.fetchall()

    category_id, category_name = get_valid_category(categories)
    if not category_id:
        return

    year = input("Enter release Year: ")

    # Проверка, что год введен корректно
    if not year.isdigit():
        print("\nInvalid Year format. Please enter a numeric Year.")
        print("****************************")
        return

    # Преобразуем год в целое число
    year = int(year)

    # Получаем текущий год
    current_year = datetime.datetime.now().year

    # Проверяем, что год в пределах допустимого диапазона
    if year < 1800 or year > current_year:
        print(f"\nInvalid Year. Please enter a year between 1895 and {current_year}.")
        print("****************************")
        return

    query = """
        SELECT f.title FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        WHERE fc.category_id = %s AND f.release_year = %s LIMIT 5;
    """
    cursor.execute(query, (category_id, year))
    films = cursor.fetchall()

    if handle_empty_result(films, "Genre and Year", f"{category_name}, {year}"):
        return

    print(f"\nSearch results for Genre {category_name} and Year {year}:")
    for film in films:
        print(film[0])

    print("****************************")

    log_search("By Genre and Year", f"{category_name}, {year}")


# def search_by_genre_and_year():
#     conn, cursor = get_db_connection()
#     cursor.execute("SELECT category_id, name FROM category")
#     categories = cursor.fetchall()
#
#     category_id, category_name = get_valid_category(categories)
#     if not category_id:
#         return
#
#     year = input("Enter release Year: ")
#     if not year.isdigit():
#         print("\nInvalid Year format. Please enter a numeric Year.")
#         print("****************************")
#         return
#
#
#     query = """
#         SELECT f.title FROM film f
#         JOIN film_category fc ON f.film_id = fc.film_id
#         WHERE fc.category_id = %s AND f.release_year = %s LIMIT 5;
#     """
#     cursor.execute(query, (category_id, year))
#     films = cursor.fetchall()
#
#     if handle_empty_result(films, "Genre and Year", f"{category_name}, {year}"):
#         return
#
#     print(f"\nSearch results for Genre {category_name} and Year {year}:")
#     for film in films:
#         print(film[0])
#
#     print("****************************")
#
#     log_search("By Genre and Year", f"{category_name}, {year}")


def search_by_keyword():
    conn, cursor = get_db_connection()
    keyword = input("Enter keyword for movie title: ")

    query = """
        SELECT f.title FROM film f
        WHERE f.title LIKE %s LIMIT 5;
    """
    cursor.execute(query, ('%' + keyword + '%',))
    films = cursor.fetchall()

    if handle_empty_result(films, "Keyword", keyword):
        return

    print(f"\nSearch results for Keyword '{keyword}':")
    for film in films:
        print(film[0])

    print("****************************")  # Добавляем разделитель

    log_search("By Keyword", keyword)
