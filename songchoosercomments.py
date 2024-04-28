# here we define our main function - the music picker function
def music_picker(genre, mood, tempo):

    # these are the genres, moods, and tempos that are being used in a list
    genres = ["rock", "pop", "hip-hop"]
    moods = ["happy", "sad"]
    tempos = ["fast", "medium", "slow"]

    # we organize our lists in a way that will incorporate calling indexes for returning our final song
    # i have put "rock song 1", "pop song 2" and so forth, but it can all be replaced with real songs
    rock_songs = [
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

    # here we make sure that the inputted genre, mood, and tempo, is in the correct lists
    while genre in genres and mood in moods and tempo in tempos:
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

# the purpose of this while loop is to make sure the user's inputs fall in the right lists
# it will prompt you infinitely until a correct input is provided
while input1 not in genres:
    print("This is not an option. Please try again. ")
    input1 = input("Choose a genre: rock, hiphop, pop ")

if input1.lower() == "rock":
    genre = "rock"
if input1.lower() == "hiphop":
    genre = "hip-hop"
if input1.lower() == "pop":
    genre = "pop"

input2 = input("Choose a mood: happy, sad, ")

# while loop for moods
while input2 not in moods:
    print("This is not an option. Please try again. ")
    input2 = input("Choose a mood: happy or sad ")

if input2.lower() == "happy":
    mood = "happy"
if input2.lower() == "sad":
    mood = "sad"

input3 = input("Choose a tempo: fast, medium, or slow ")

# while loops for tempos
while input3 not in tempos:
    print("This is not an option. Please try again")
    input3 = input("Choose a tempo: fast, medium, or slow ")

if input3.lower() == "fast":
    tempo = "fast"
if input3.lower() == "medium":
    tempo = "medium"
if input3.lower() == "slow":
    tempo = "slow"

# Conclusively, we use our main function, to give out a recommended song.
recommended_song = music_picker(genre, mood, tempo)
print("Recommended song:", recommended_song)
