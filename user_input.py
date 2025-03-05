
def get_valid_category(categories):
    category_dict = {str(category[0]): category[1] for category in categories}
    print("\nMovie Categories:")
    for category_id, category_name in category_dict.items():
        print(f"{category_id}. {category_name}")

    category_id = input("\nEnter Category number: ")
    if category_id not in category_dict:
        print("\nInvalid Category number. Please try again.")
        return None, None
    return category_id, category_dict[category_id]


def get_valid_year():
    year = input("\nEnter release Year: ")
    if not year.isdigit():
        print("\nInvalid Year format. Please enter a numeric Year.")
        return None
    return year
