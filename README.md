# Word Frequency Analyzer

The word frequency analyzer determines how often each word appears in the text file.

# Process
0. I have taken sample.txt from the "Fundamentals of Data Science" book. And clean the text by removing special characters from the text.
1. Develop a word Frequency Analyzer that counts the frequency of the top 10 words with the highest frequency from cleaned_sample.txt file.

# To run the program 
Run " python preprocessing.py" to clean the text file. 

Run "python main.py" to execute the main python script.
 
# Working of Word Frequency Analyzer
1. Read the sample.txt file and store the text file in a string variable
2. Each words of it  are change into lowercase using the lower() function 
3. Text is split into words.
4. Then, using a dictionary called word_counts, it iterates through each word and keeps track of how often it appears.
5. The key-value pairs are kept in the Python Dictionary, where the key is a word and the value is the frequency with which that word appears in the text.
6. A word's count is increased by 1 if it is already included in the word_counts dictionary. If not, a fresh entry is created with a count of 1. 
7. The word_counts dictionary, which contains the word counts for each distinct word, is what the function finally returns.
8. The word_counts dictionary is sorted using the sorted() method based on the values (word frequencies). Key=lambda x: x[1] is required to indicate that the sorting should be based on the second element.
9. The reverse=True parameter is used to sort the items in descending order.
   
