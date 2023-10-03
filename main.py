import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database="Spectrum",
    user="postgres",
    password="babe123"
)
print("Connected to PostgreSQL!")

def student_details():
    student_name = "Harshith"
    father_name = "Rajesh"
    mother_name = "Usha"
    address  = 'XYZ'
    phone1 = '3545'
    phone2 = '53153'
    cur = conn.cursor()
    student_id = cur.execute("SELECT student_id FROM student_details ORDER BY student_id DESC LIMIT 1")
    if student_id == None:
        print(student_id)
    else:
        print('0')

    # sql = '''INSERT INTO student_details
    #         (student_id,student_name,father_name,mother_name,address,phone1,phone2)
    #         VALUES (%s,%s,%s,%s,%s,%s,%s)'''
    # cur.execute(sql,(student_id+1,student_name,father_name,mother_name,address,phone1,phone2))
    cur.close()

student_details()
