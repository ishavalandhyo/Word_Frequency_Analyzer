# Function that takes the path to a  text file as input and read the text file.
def read(filepath):
    with open(filepath) as f:
        # read the content of the text file and change upper case letter into lower case
        string = f.read().lower()
        return string
              

# Function that analyzes the frequency of each word in the text.
def frequency(words):

    ''' create empty dictionary and store the frequency of each word in key value pair
    where key is the word in the text and value is the frequency of that word'''

    word_counts = {}

    # split text into words.
    words_text = words.split()

    for word in words_text:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


# function that sort the frequency of words in descending order
def sort_des(word_counts):
     sorted_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    #Give a value from 0 to 9 index from the above sorted_list.
     Top_10 = sorted_list[:10]
     return Top_10


def main():
    print("Word Frequency Analyzer")
    print("<------------------------------------------------------------------------------------------------------------------->")
    # Text file is pass to the function and returned string is stored in text variable
    text = read('cleaned_sample.txt')
    word_counts = frequency(text)
    result = sort_des(word_counts)
    print("Top 10 words with highest frequency")
    print(result)


if __name__=="__main__":
    main()
