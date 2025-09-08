
import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

base_path = os.path.dirname(__file__)
eugene_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(eugene_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(data_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    rows = list(file_data)

missing = []
select_query = """
SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
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
WHERE s.name = %s AND s.second_name = %s AND g.title = %s
AND b.title = %s AND sub.title = %s AND l.title = %s AND m.value = %s
LIMIT 1
"""

with db.cursor() as cursor:
    for row in rows:
        params = [
            row.get('name'),
            row.get('second_name'),
            row.get('group_title'),
            row.get('book_title'),
            row.get('subject_title'),
            row.get('lesson_title'),
            row.get('mark_value')
        ]
        cursor.execute(select_query, params)
        if cursor.fetchone() is None:
            missing.append({
                'name': row.get('name'),
                'second_name': row.get('second_name'),
                'group_title': row.get('group_title'),
                'book_title': row.get('book_title'),
                'subject_title': row.get('subject_title'),
                'lesson_title': row.get('lesson_title'),
                'mark_value': row.get('mark_value')
            })

if missing:
    print('Отсутствуют в БД следующие записи:')
    for item in missing:
        print(item)
else:
    print('Все строки из CSV присутствуют в БД.')

db.close()
