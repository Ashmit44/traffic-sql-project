import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='system',
        database='violations_db'
    )
    print("✅ Connected to MySQL successfully!")
    connection.close()
except Exception as e:
    print(f"❌ Error: {e}")