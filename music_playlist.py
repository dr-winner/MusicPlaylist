class MusicPlaylist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title, artist, duration):
        """Add a song to the playlist"""
        song = {
            "title": title,
            "artist": artist,
            "duration": duration
        }
        self.songs.append(song)
        print(f"Added: {title} by {artist}")

    def remove_song(self, index):
        """Remove a song by index"""
        if 0 <= index < len(self.songs):
            removed = self.songs.pop(index)
            print(f"Removed: {removed['title']}")

    def display_playlist(self):
        """Display all songs in the playlist"""
        print(f"\n=== {self.name} ===")
        for i, song in enumerate(self.songs):
            print(
                f"{i+1}. {song['title']} - {song['artist']} ({song['duration']})")

    def total_duration(self):
        """Calculate total playlist duration"""
        total = sum(int(song['duration'].split(':')[0]) * 60 +
                    int(song['duration'].split(':')[1])
                    for song in self.songs)
        return total

    def edit_song(self, index, title=None, artist=None, duration=None):
        """Edit song details by index. Only provided fields are updated."""
        if 0 <= index < len(self.songs):
            song = self.songs[index]
            if title:
                song['title'] = title
            if artist:
                song['artist'] = artist
            if duration:
                song['duration'] = duration
            print(f"Song at position {index+1} updated.")
        else:
            print("Invalid song index.")


# Create a playlist
playlist = MusicPlaylist("My Favorites")
playlist.add_song("Blinding Lights", "The Weeknd", "3:20")
playlist.add_song("Shape of You", "Ed Sheeran", "3:53")
playlist.add_song("Levitating", "Dua Lipa", "3:23")

playlist.display_playlist()

playlist.edit_song(1, title="Shape of You (Remix)",
                   artist="Ed Sheeran (Remixed)", duration="4:05")
