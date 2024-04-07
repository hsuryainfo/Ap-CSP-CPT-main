def music_picker(genre, mood, tempo):

    genres = ["rock", "pop", "hip-hop"]
    moods = ["happy", "sad"]
    tempos = ["fast", "medium", "slow"]

    rock_songs = [
        [
            "Don't Stop Believin' by Journey",
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
            "Good as Hell by Lizzo",
            "Old Town Road by Lil Nas X ft. Billy Ray Cyrus",
        ],
        [
            "See You Again by Wiz Khalifa ft. Charlie Puth",
            "Stan by Eminem ft. Dido",
            "Changes by Tupac",
        ],
    ]

    # Retrieve song recommendation based on user preferences
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


# Example usage:
recommended_song = music_picker("rock", "happy", "fast")
print("Recommended song:", recommended_song)
