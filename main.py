from pathlib import Path
def sort_on(dict):
    return dict["num"]
def main():
    path = Path(__file__).parent.absolute()
    with open(f"{path}/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        char_map = {}
        for char in "".join(words).lower():
            if not char.isalpha():
                continue
            if not char in char_map:
               char_map[char] = 1
               continue
            char_map[char] += 1
        char_map_list = []
        for key in char_map:
            char_map_list.append({
                "name" : key,
                "num" : char_map[key]
            })
        char_map_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        print(" ")
        for chars_map in char_map_list:
            print(f"The '{chars_map["name"]}' character was found {chars_map["num"]} times")
        print("--- End report ---")

main()
