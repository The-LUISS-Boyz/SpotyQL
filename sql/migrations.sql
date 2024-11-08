CREATE TABLE IF NOT EXISTS Track (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    streams INT,
    release_date DATE,
    cover_url VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Vendor (
    name VARCHAR(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS MusicalStats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bpm INT,
    "key" VARCHAR(100),
    "mode" VARCHAR(100),
    valence INT,
    danceability INT,
    energy INT,
    acousticness INT,
    instrumentalness INT,
    liveness INT,
    speechiness INT,
    track_id INT,
    FOREIGN KEY (track_id) REFERENCES Track(id)
);

CREATE TABLE IF NOT EXISTS Track_Artist (
    artist_id INT,
    track_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(id),
    FOREIGN KEY (track_id) REFERENCES Track(id)
);

CREATE TABLE IF NOT EXISTS Track_Playlist (
    count INT,
    track_id INT,
    vendor_name VARCHAR(100),
    FOREIGN KEY (track_id) REFERENCES Track(id),
    FOREIGN KEY (vendor_name) REFERENCES Vendor(name)
);

CREATE TABLE IF NOT EXISTS Track_Chart (
    count INT,
    track_id INT,
    vendor_name VARCHAR(100),
    FOREIGN KEY (track_id) REFERENCES Track(id),
    FOREIGN KEY (vendor_name) REFERENCES Vendor(name)
);