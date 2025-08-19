INSERT INTO students (name, second_name) VALUES ('M', 'Kostsina')

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group for mkostsina', 'aug 2025', 'sep 2025')

INSERT INTO books (title, taken_by_student_id) VALUES ('FirstM', 21017)

INSERT INTO books (title, taken_by_student_id) VALUES ('SecondM', 21017)

UPDATE students SET group_id = 5556 where id = 21017

INSERT INTO subjects (title) VALUES ('FirstS')

INSERT INTO subjects (title) VALUES ('SecondS')

INSERT INTO lessons (title, subject_id) VALUES ('FirstL', 11716)

INSERT INTO lessons (title, subject_id) VALUES ('SecondL', 11716)

INSERT INTO lessons (title, subject_id) VALUES ('FirstLL', 11717)

INSERT INTO lessons (title, subject_id) VALUES ('SecondLL', 11717)

INSERT INTO marks (value, lesson_id, student_id) VALUES (12, 11812, 21017)

INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 11813, 21017)

INSERT INTO marks (value, lesson_id, student_id) VALUES (12, 11814, 21017)

INSERT INTO marks (value, lesson_id, student_id) VALUES (10, 11815, 21017)

SELECT value FROM marks where student_id = 21017

SELECT title FROM books where taken_by_student_id = 21017

SELECT 
    s.id,
    s.name,
    s.second_name,
    g.title,
    g.start_date,
    g.end_date,
    b.title,
    m.value,
    l.title,
    sub.title
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 21017