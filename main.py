def count_words(story):
    words = story.split();
    count = 0;
    for i in words:
        count += 1;
    return count;

def count_alphabets(story):
    letter_count = {}
    for i in story:
       if i.isalpha():
            letter = i.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count;

def return_sort(letter_count):
    result = []
    for letter, count in letter_count.items():
        result.append({"letter": letter, "count": count})
    return sorted(result, key=sort_on, reverse=True)

def sort_on(d):
    return d["count"]

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read();
        print(f"Total number of words in the is {count_words(file_contents)}");
        letter_dict = count_alphabets(file_contents);
        sort_list = return_sort(letter_dict)
        for i in sort_list:
            print(f"The {i['letter']} character was found {i['count']} times")

main()