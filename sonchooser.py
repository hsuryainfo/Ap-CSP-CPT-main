def music_picker(genre, mood, tempo):

    # these are the genres, moods, and tempos that are being used in a list
    genres = ["rock", "pop", "hip-hop"]
    moods = ["happy", "sad"]
    tempos = ["fast", "medium", "slow"]

    # we organize our lists in a way that will incorporate using indexes for returning our final song
    # i have put "rock song 1", "pop song 2" and so forth, but it can all be replaced with real songs
    rock_songs = [  # specifically, we have two main sections, inside which 3 songs are placed, corresponding to 2 moods and 3 tempos
        [
            "rock song 1",
            "rock song 2",
            "rock song 3",
        ],
        [
            "rock song 4",
            "rock song 5",
            "rock song 6",
        ],
    ]
    pop_songs = [
        [
            "pop song 1",
            "pop song 2",
            "pop song 3",
        ],
        [
            "pop song 4",
            "pop song 5",
            "pop song 6",
        ],
    ]
    hip_hop_songs = [
        [
            "hiphop song 1",
            "hiphop song 2",
            "hiphop song 3",
        ],
        [
            "hiphop song 4",
            "hiphop song 5",
            "hiphop song 6",
        ],
    ]

    # Now I have a while loop, which is for validation of user inputs
    while True:
        if genre not in genres:
            print("Invalid genre. Please choose from: rock, hiphop, or pop")
            genre = input("Choose a genre: ")
        elif mood not in moods:
            print("Invalid mood. Please choose from: happy or sad")
            mood = input("Choose a mood: ")
        elif tempo not in tempos:
            print("Invalid tempo. Please choose from: fast, medium, slow")
            tempo = input("Choose a tempo: ")
        else:
            break  # breaks the loop when all inputs are valid

    # here we make sure, if for some reason the while loop doesn't function correctly, that the inputted genre, mood, and tempo, is in the correct lists
    if genre in genres and mood in moods and tempo in tempos:

        if genre == "rock":
            final_song = rock_songs
        elif genre == "pop":
            final_song = pop_songs
        elif genre == "hip-hop":
            final_song = hip_hop_songs

        # here we assign indexed to inputted values for tempos and moods
        if tempo == "fast":
            tempo_ind = 0
        elif tempo == "medium":
            tempo_ind = 1
        else:
            tempo_ind = 2

        if mood == "happy":
            mood_ind = 0
        else:
            mood_ind = 1

        # finally, we are returning a song, based on the indexes
        return final_song[mood_ind][tempo_ind]


# defined lists again
genres = ["rock", "pop", "hip-hop"]
moods = ["happy", "sad"]
tempos = ["fast", "medium", "slow"]

input1 = input("Choose a genre: rock, hiphop, pop ")
genre = ""  # we set this to empty string as the default choice if the user didn't input anything

# Assign input variables
if input1.lower() == "rock":
    genre = "rock"
elif input1.lower() == "hiphop":
    genre = "hip-hop"
elif input1.lower() == "pop":
    genre = "pop"

input2 = input("Choose a mood: happy, sad, ")
mood = ""  # we set this to empty string as the default choice if the user didn't input anything

# Assign input variables
if input2.lower() == "happy":
    mood = "happy"
elif input2.lower() == "sad":
    mood = "sad"

input3 = input("Choose a tempo: fast, medium, or slow ")
tempo = ""  # we set this to empty string as the default choice if the user didn't input anything

# Assign input variables
if input3.lower() == "fast":
    tempo = "fast"
elif input3.lower() == "medium":
    tempo = "medium"
elif input3.lower() == "slow":
    tempo = "slow"

# Conclusively, we use our main function, to give out a recommended song.

if __name__ == "__main__":
    recommended_song = music_picker(genre, mood, tempo)  # we call our function here
    print("Recommended song:", recommended_song)  # finally, print the recommended song
