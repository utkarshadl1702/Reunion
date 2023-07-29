-- Create a SQLite database
CREATE DATABASE orchestra_data;

-- Create the Orchestras table
CREATE TABLE Orchestras (
    orchestra_id INTEGER PRIMARY KEY,
    orchestra_name TEXT NOT NULL,
    country TEXT NOT NULL
);

-- Create the Concerts table
CREATE TABLE Concerts (
    concert_id INTEGER PRIMARY KEY,
    orchestra_id INTEGER NOT NULL,
    location TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (orchestra_id) REFERENCES Orchestras(orchestra_id)
);

-- Create the Works table
CREATE TABLE Works (
    concert_id INTEGER NOT NULL,
    work_id INTEGER NOT NULL,
    work_name TEXT NOT NULL,
    PRIMARY KEY (concert_id, work_id),
    FOREIGN KEY (concert_id) REFERENCES Concerts(concert_id)
);

-- Create the Artists table
CREATE TABLE Artists (
    concert_id INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    artist_name TEXT NOT NULL,
    instrument TEXT NOT NULL,
    PRIMARY KEY (concert_id, artist_id),
    FOREIGN KEY (concert_id) REFERENCES Concerts(concert_id)
);
