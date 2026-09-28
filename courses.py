import db

def add_course(name, teacher_id):
    sql = "INSERT INTO courses (name, teacher_id) VALUES (?, ?)"
    db.execute(sql, [name, teacher_id])
    course_id = db.last_insert_id()
    return course_id

def add_participant(course_id, student_id):
    sql = "INSERT INTO courseParticipants (course_id, student_id) VALUES (?, ?)"
    db.execute(sql, [course_id, student_id])

def add_lesson(course_id, name, material, file):
    sql = "INSERT INTO courses (course_id, name, material, file) VALUES (?, ?, ?, ?)"
    db.execute(sql, [course_id, name, material, file])
    lesson_id = db.last_insert_id()
    return lesson_id

def add_test(course_id, name):
    sql = "INSERT INTO courses (course_id, name) VALUES (?, ?)"
    db.execute(sql, [course_id, name])
    test_id = db.last_insert_id()
    return test_id

def add_exercise(test_id, question, type, correct_answer):
    sql = "INSERT INTO courses (test_id, question, type, correct_answer) VALUES (?, ?, ?, ?)"
    db.execute(sql, [test_id, question, type, correct_answer])
    exercise_id = db.last_insert_id()
    return exercise_id

def add_answer(exercise_id, answer, is_correct):
    sql = "INSERT INTO answers (exercise_id, answer, is_correct) VALUES (?, ?, ?)"
    db.execute(sql, [exercise_id, answer, is_correct])
    answer_id = db.last_insert_id()
    return answer_id

def add_result(student_id, test_id, score):
    sql = "INSERT INTO answers (student_id, test_id, score) VALUES (?, ?, ?)"
    db.execute(sql, [student_id, test_id, score])

def get_courses():
    sql = "SELECT id, name FROM courses ORDER BY name"
    courses = db.query(sql)
    return courses

def get_teacher_courses(teacher_id):
    sql = "SELECT id, name  FROM courses WHERE teacher_id = ? ORDER BY name"
    courses = db.query(sql, [teacher_id])
    return courses

def get_student_courses(student_id):
    sql = """SELECT p.course_id, c.name
            FROM courses c, courseParticipants p
            WHERE p.student_id = ? AND c.id = p.course_id
            ORDER BY c.name"""
    courses = db.query(sql, [student_id])
    return courses