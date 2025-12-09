def wordcount(file):
    words = file.split()
    return len(words)

def count_chars(text):
    lower_text = text.lower()
    counter = {}
    for f in lower_text:
        if f in counter:
            counter[f] += 1
        else:
            counter[f] = 1
    return counter

def sort_on(items):
    return items["num"]

def sorted_dict(d):
    sorted = []
    for ch, count in d.items():
            sorted.append({"char": ch,"num": count})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
    

    
