PRAGMA foreign_keys = ON;

CREATE TABLE house (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    address     TEXT,
    landlord_id INTEGER REFERENCES "user"(id)
);

CREATE TABLE room (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    house_id INTEGER NOT NULL REFERENCES house(id),
    name     TEXT NOT NULL
);

CREATE TABLE shared_space (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    house_id INTEGER NOT NULL REFERENCES house(id),
    name     TEXT NOT NULL
);

CREATE TABLE "user" (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id  INTEGER REFERENCES room(id),
    username TEXT NOT NULL UNIQUE,
    email    TEXT NOT NULL UNIQUE,
    password TEXT,
    role     TEXT NOT NULL DEFAULT 'tenant'
             CHECK (role IN ('tenant', 'landlord'))
);

CREATE TABLE maintenance_request (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL REFERENCES "user"(id),
    title       TEXT NOT NULL,
    description TEXT,
    category    TEXT,
    status      TEXT NOT NULL DEFAULT 'new'
                CHECK (status IN ('new', 'in_progress', 'done')),
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    resolved_at DATETIME
);

CREATE TABLE complaint (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    reporter_id   INTEGER NOT NULL REFERENCES "user"(id),
    about_user_id INTEGER NOT NULL REFERENCES "user"(id),
    description   TEXT,
    landlord_note TEXT,
    status        TEXT NOT NULL DEFAULT 'new'
                  CHECK (status IN ('new', 'in_progress', 'done')),
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reservation (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL REFERENCES "user"(id),
    space_id   INTEGER NOT NULL REFERENCES shared_space(id),
    start_time DATETIME NOT NULL,
    end_time   DATETIME NOT NULL,
    CHECK (end_time > start_time)
);

CREATE TABLE absence (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL REFERENCES "user"(id),
    start_date DATE NOT NULL,
    end_date   DATE NOT NULL,
    note       TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date >= start_date)
);