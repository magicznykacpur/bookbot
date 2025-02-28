def count_words(text):
    return len(text.split())

def count_characters(text):
    chars = {}

    for character in text:
        character_lower = character.lower()
        if character_lower in chars:
            chars[character_lower] = chars[character_lower] + 1
        else:
            chars[character_lower] = 1
    
    return chars

def sort_on(dict):
    return dict['count']

def sort_stats(char_count):
    sorted = []

    for key in char_count:
        sorted.append({'character': key, 'count': char_count[key]})

    sorted.sort(reverse=True, key=sort_on)

    return sorted