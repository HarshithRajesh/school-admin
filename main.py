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

    sql = '''INSERT INTO student_details
            (student_name,father_name,mother_name,address,phone1,phone2)
            VALUES (%s,%s,%s,%s,%s,%s);'''
    cur.execute(sql,(student_name,father_name,mother_name,address,phone1,phone2))
    conn.commit()
    cur.close()
    conn.close()


student_details()
