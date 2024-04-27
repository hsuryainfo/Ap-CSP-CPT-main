def music_picker(genre, mood, tempo):

    genres = ["rock", "pop", "hip-hop"]
    moods = ["happy", "sad"]
    tempos = ["fast", "medium", "slow"]

    rock_songs = [
        [
            "rock song 1",
            "Livin' On A Prayer by Bon Jovi",
            "Sweet Child O' Mine by Guns N' Roses",
        ],
        [
            "November Rain by Guns N' Roses",
            "Everybody Hurts by R.E.M.",
            "Hurt by Johnny Cash",
        ],
    ]
    pop_songs = [
        [
            "Uptown Funk by Mark Ronson ft. Bruno Mars",
            "Happy by Pharrell Williams",
            "Someone Like You by Adele",
        ],
        [
            "Someone You Loved by Lewis Capaldi",
            "Shallow by Lady Gaga and Bradley Cooper",
            "All of Me by John Legend",
        ],
    ]
    hip_hop_songs = [
        [
            "Can't Stop the Feeling! by Justin Timberlake",
            "Old Town Road by Lil Nas X ft. Billy Ray Cyrus",
            "Let her Go by Passenger",
        ],
        [
            "See You Again by Wiz Khalifa ft. Charlie Puth",
            "Stan by Eminem ft. Dido",
            "Changes by Tupac",
        ],
    ]

    if genre in genres and mood in moods and tempo in tempos:
        if genre == "rock":
            songs = rock_songs
        elif genre == "pop":
            songs = pop_songs
        elif genre == "hip-hop":
            songs = hip_hop_songs

        if mood == "happy":
            mood_index = 0
        else:
            mood_index = 1

        if tempo == "fast":
            tempo_index = 0
        elif tempo == "medium":
            tempo_index = 1
        else:
            tempo_index = 2

        return songs[mood_index][tempo_index]
    else:
        return (
            "Sorry, we couldn't find a song recommendation matching your preferences."
        )


genres = ["rock", "pop", "hip-hop"]
moods = ["happy", "sad"]
tempos = ["fast", "medium", "slow"]


input1 = input("Choose a genre: rock, hiphop, pop ")

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

while input2 not in moods:
    print("This is not an option. Please try again. ")
    input2 = input("Choose a mood: happy or sad ")

if input2.lower() == "happy":
    mood = "happy"
if input2.lower() == "sad":
    mood = "sad"

input3 = input("Choose a tempo: fast, medium, or slow ")

while input3 not in tempos:
    print("This is not an option. Please try again")
    input3 = input("Choose a tempo: fast, medium, or slow ")

if input3.lower() == "fast":
    tempo = "fast"
if input3.lower() == "medium":
    tempo = "medium"
if input3.lower() == "slow":
    tempo = "slow"


recommended_song = music_picker(genre, mood, tempo)
print("Recommended song:", recommended_song)
