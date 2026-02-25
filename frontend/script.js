
const API_URL = 'http://localhost:8000/playlist';
let playlist = [];

async function fetchPlaylist() {
    const res = await fetch(API_URL);
    playlist = await res.json();
    renderPlaylist();
}

async function addSong() {
    const title = document.getElementById('song-title').value;
    const artist = document.getElementById('song-artist').value;
    const duration = document.getElementById('song-duration').value;
    if (title && artist && duration) {
        await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, artist, duration })
        });
        document.getElementById('song-title').value = '';
        document.getElementById('song-artist').value = '';
        document.getElementById('song-duration').value = '';
        fetchPlaylist();
    }
}

function renderPlaylist() {
    const ul = document.getElementById('playlist');
    ul.innerHTML = '';
    playlist.forEach((song, idx) => {
        ul.innerHTML += `<li>${song.title} - ${song.artist} (${song.duration}) <button onclick="removeSong(${idx})">Remove</button></li>`;
    });
}

async function removeSong(index) {
    await fetch(`${API_URL}/${index}`, { method: 'DELETE' });
    fetchPlaylist();
}

// Spotify API search (client-side demo)
async function searchSpotify() {
    const query = document.getElementById('spotify-search').value;
    if (!query) return;
    // You need to provide your own Spotify API token here
    const token = 'YOUR_SPOTIFY_API_TOKEN';
    const url = `https://api.spotify.com/v1/search?q=${encodeURIComponent(query)}&type=track&limit=5`;
    const res = await fetch(url, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    const data = await res.json();
    const resultsDiv = document.getElementById('spotify-results');
    resultsDiv.innerHTML = '';
    if (data.tracks && data.tracks.items.length > 0) {
        data.tracks.items.forEach(track => {
            resultsDiv.innerHTML += `<div><strong>${track.name}</strong> by ${track.artists.map(a => a.name).join(', ')} <button onclick="addSpotifySong('${track.name}', '${track.artists[0].name}', '${Math.floor(track.duration_ms/60000)}:${Math.floor((track.duration_ms%60000)/1000).toString().padStart(2,'0')}')">Add</button></div>`;
        });
    } else {
        resultsDiv.innerHTML = 'No results found.';
    }
}

async function addSpotifySong(title, artist, duration) {
    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, artist, duration })
    });
    fetchPlaylist();
}

// Initial load
window.onload = fetchPlaylist;
