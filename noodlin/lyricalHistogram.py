lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"

# print(lyrics)  #set up to check output

#separte string into a list of individual words
list_of_lyrics = lyrics.split(' ')

# print(list_of_lyrics) #to check differences in two print outs

#get length of list
print(len(list_of_lyrics))

#make a list of unique words
unique_words = set(list_of_lyrics)

#allocate space for each unique word
unique_words = set(list_of_lyrics)

print(len(unique_words))

#create a dictionary
word_counts = {'Ann': 2, 'Barbara': 3, 'Ba': 8}

#accessing a value associated with a key

print(word_counts['Ann'])


#create a dictionary with each key as a separate word and set its value to 0
word_histogram = dict.fromkeys(unique_words,0)

print(word_histogram)


#create a for-loop

for number in [1,2,3,4]:
    print(number + 10)

