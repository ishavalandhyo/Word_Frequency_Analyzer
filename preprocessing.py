import string

# read the text file
with open('sample.txt') as f:
    data = f.read()


printable = set(string.printable)

# removes the special character
def remove_spec_chars(in_str):
    return ''.join([c for c in in_str if c in printable])


output_data=remove_spec_chars(data)

# create new txt file
output_files='cleaned_sample.txt'

# write the preprocess text files to new text file
with open(output_files, 'w') as f:
    f.write(output_data)

print(output_files)


