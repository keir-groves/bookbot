def get_num_words(str):
    return len(str.split())

# Returns a dictionary of each unique character
# in a string and the number of appearances
def get_char_counts(str):
    char_counts = {}
    for char in str:
        lowered = char.lower()
        if lowered in char_counts:
            char_counts[lowered] += 1
        else:
            char_counts[lowered] = 1
    return char_counts

# Accepts a dictionary of character counts
# Returns a list of dictionaries sorted via character count
def sort_char_counts(char_counts_dict):
    # create list of character count dicts
    char_counts_list = []
    for char in char_counts_dict:
        count = char_counts_dict[char]
        dict = {
            "char": char,
            "count": count
        }
        char_counts_list.append(dict)

    # sort created list
    def sort_on(dict):
        return dict["count"]
    
    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list
