CREATE TABLE IF NOT EXISTS track (
    name VARCHAR(100) PRIMARY KEY,
    streams INT,
    release_date DATE,
    vendor_name VARCHAR(100),
    FOREIGN KEY (vendor_name) REFERENCES Vendor(name)
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
    track_name VARCHAR(100),
    FOREIGN KEY (track_name) REFERENCES track(name)
);

CREATE TABLE IF NOT EXISTS Track_Artist (
    artist_id INT,
    track_id VARCHAR(100),
    FOREIGN KEY (artist_id) REFERENCES Artist(id),
    FOREIGN KEY (track_id) REFERENCES track(name),
    PRIMARY KEY (artist_id, track_id)
);
