
import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('M', 'Kostina3')")
student_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group for mkostina3', 'aug 2025', 'sep 2025')")
group_id = cursor.lastrowid

cursor.execute("UPDATE students SET group_id = %s where id = %s", (group_id, student_id))

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('PFirstM3', student_id),
        ('PSecondM3', student_id)
    ]
)

subject_ids = []
subjects = ['PFirstS3', 'PSecondS3']
for subj in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subj,))
    subject_ids.append(cursor.lastrowid)

lesson_ids = []
lessons = [
    ('PFirstL3', subject_ids[0]),
    ('PSecondL3', subject_ids[0]),
    ('PFirstLL3', subject_ids[1]),
    ('PSecondLL3', subject_ids[1])
]
for title, subj_id in lessons:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (title, subj_id))
    lesson_ids.append(cursor.lastrowid)

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (12, lesson_ids[0], student_id),
        (10, lesson_ids[1], student_id),
        (12, lesson_ids[2], student_id),
        (10, lesson_ids[3], student_id)
    ]
)

cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
print(marks)

cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
print(books)

select_query = """
SELECT
    s.id,
    s.name,
    s.second_name,
    g.title AS group_title,
    g.start_date,
    g.end_date,
    b.title AS book_title,
    m.value AS mark_value,
    l.title AS lesson_title,
    sub.title AS subject_title
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
"""
cursor.execute(select_query, (student_id,))
student_info = cursor.fetchall()
print(student_info)

db.commit()
db.close()
