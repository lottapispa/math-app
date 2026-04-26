# Plan for the database and website

### Goal features of the app
- The user can log in and out and register as a user. 
- The student can see a list of courses and can join courses. 
- The student can read the text material of the course and solve the course exercises. 
- The student can see the statistics of which course assignments they have solved. 
- The teacher can create a new course, edit existing courses, and delete a course. 
- The teacher can add text material and exercises to the course. The task can be multiple choice or a text field where you have to write the correct answer. 
- The teacher can see the statistics of their course, which students are in the course and which course exercises each has solved. 
- The website looks nice visually. 

### Features divided into smaller tasks (and prioritized)
- [x] The user can register as a user. 
- [x] The user can log in and out. 
- [ ] Edit the database to make the next changes possible. 
- [ ] The teacher can create a new course. 
- [ ] The teacher can add multiple-choice exercises to the course. 
- [ ] The teacher can add exercises with a text field to the course.
- [ ] The teacher can add text material to the course. 
- [ ] The teacher can delete a course. 
- [ ] The teacher can edit a course.

### Thoughts
- Change database: where to add unique or not null, text vs varchar (max length). Can a course not include text material and only have tests or vice versa; which elements are mandatory? 
- Automate answer checking, or does the teacher do it? 
- Option to add a deadline for tests? 
- Is a student joining a course different from just starting it? Do you need to join to do the exercises? 
- Add the option to need a key to join a course? 

### Plan for the database

Table Users

| id | username | password | role |
| --- | --- | --- | --- |
|   |   |   |   |

Table Courses

| id  | name | teacher |
| --- | --- | --- |
|   |   |   |

Table CourseParticipants

| course_id  | student_id |
| --- | --- |
|   |   |

Table Lessons/Teaching material

| id  | course_id | name | material |
| --- | --- | --- | --- |
|   |   |   |   |

Table Tests

| id  | course_id | name |
| --- | --- | --- |
|   |   |   |

Table Exercises

| id  | test_id | question | correct_answer | max_points |
| --- | --- | --- | --- | --- |
|   |   |   |   |   |

Table Answer

| id  | exercise_id | answer (input) | is_correct |
| --- | --- | --- | --- |
|   |   |   |   |

Table TestResults
| student_id  | test_id | score |
| --- | --- | --- |
|   |   |   |
