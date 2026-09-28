CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    user_type TEXT
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    teacher_id INTEGER REFERENCES users
);

CREATE TABLE courseParticipants (
    course_id INTEGER REFERENCES courses,
    student_id INTEGER REFERENCES users
);

CREATE TABLE tests (
    id INTEGER PRIMARY KEY,
    course_id INTEGER REFERENCES courses,
    name TEXT
);

CREATE TABLE lessons (
    id INTEGER PRIMARY KEY,
    course_id INTEGER REFERENCES courses,
    name TEXT, 
    material TEXT
);

CREATE TABLE exercises (
    id INTEGER PRIMARY KEY,
    test_id INTEGER REFERENCES tests,
    question TEXT,
    max_points INTEGER,
    correct_answer TEXT
);

CREATE TABLE answers (
    id INTEGER PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises,
    answer TEXT,
    is_correct BOOLEAN
);

CREATE TABLE results (
    student_id INTEGER REFERENCES users,
    test_id INTEGER REFERENCES tests,
    score INTEGER
);