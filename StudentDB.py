#   ASSIGNMENT  -|
#   -------------|
#   Student Database Management with MongoDB  -|
#   -------------------------------------------|


#   Introduction  -|
#   ---------------|
#   This assignment on Student Database Management using MongoDB focuses on applying database design principles
#   and query operations to manage student information efficiently.
#   The project workflow includes:
#    - Database Setup: Creating a MongoDB database named StudentDB and a collection called students.
#    - Data Insertion: Populating the collection with at least 15 diverse student records, including fields such as Roll, 
#                      Name, Course, Marks, City, and EmailID.
#    - Query Operations: Retrieving student data using basic queries, such as finding students by course, marks threshold, 
#                        or city.
#    - Update and Delete: Modifying specific student records by updating email and marks, and removing records with low marks.
#    - Aggregation and Reporting: Generating statistics such as count and average marks per course, identifying top performers, 
#                                and sorting records for better insights.
#    - Data Export: Saving the student dataset in JSON format for external use.
#   The goal is to demonstrate how MongoDB can be effectively used for CRUD operations and data analysis in managing student
#   information within an academic setting.




from pymongo import MongoClient
            # MongoDB client library
import json
            # JSON library for exporting data


#   Task 1  -|
#   ---------|
client = MongoClient()
            # Create a MongoDB client
db = client["StudentDB"]
            # Creating the StudentDB database
students = db["students"]
            # Creating the students collection

students.delete_many({})
            # clear existing records if any

students_data = [
    {"Roll": 1001, "Name": "Aarav", "Course": "Data Science", "Marks": 88, "City": "Delhi", "EmailID": "sharmaarav@gmail.com"},
    {"Roll": 1002, "Name": "Ananya", "Course": "Computer Science", "Marks": 92, "City": "Mumbai", "EmailID": "ananya102@gmail.com"},
    {"Roll": 1003, "Name": "Rohan", "Course": "Data Science", "Marks": 76, "City": "Pune", "EmailID": "gupta06rohan@gmail.com"},
    {"Roll": 1004, "Name": "Isha", "Course": "Information Technology", "Marks": 67, "City": "Delhi", "EmailID": "i9sha@gmail.com"},
    {"Roll": 1005, "Name": "Kabir", "Course": "Electronics", "Marks": 45, "City": "Jaipur", "EmailID": "kabir78mehta@gmail.com"},
    {"Roll": 1006, "Name": "Priya", "Course": "Computer Science", "Marks": 39, "City": "Kochi", "EmailID": "priyanr@gmail.com"},
    {"Roll": 1007, "Name": "Vikram", "Course": "Mechanical", "Marks": 81, "City": "Pune", "EmailID": "joshi136@gmail.com"},
    {"Roll": 1008, "Name": "Sara", "Course": "Data Science", "Marks": 95, "City": "Mumbai", "EmailID": "sara54kh@gmail.com"},
    {"Roll": 1009, "Name": "Neha", "Course": "Information Technology", "Marks": 72, "City": "Ahmedabad", "EmailID": "neha@gmail.com"},
    {"Roll": 1010, "Name": "Arjun", "Course": "Electronics", "Marks": 64, "City": "Hyderabad", "EmailID": "arjun@gmail.com"},
    {"Roll": 1011, "Name": "Divya", "Course": "Computer Science", "Marks": 78, "City": "Delhi", "EmailID": "divya4moon@gmail.com"},
    {"Roll": 1012, "Name": "Kunal", "Course": "Mechanical", "Marks": 53, "City": "Surat", "EmailID": "kunal@gmail.com"},
    {"Roll": 1013, "Name": "Meera", "Course": "Data Science", "Marks": 84, "City": "Chennai", "EmailID": "meera111@gmail.com"},
    {"Roll": 1014, "Name": "Aditya", "Course": "Information Technology", "Marks": 59, "City": "Bengaluru", "EmailID": "adi7tya1kp@gmail.com"},
    {"Roll": 1015, "Name": "Riya", "Course": "Computer Science", "Marks": 47, "City": "Kolkata", "EmailID": "riya96@gmail.com"}
]

students.insert_many(students_data)
print("Inserted", len(students_data), "student records.")
            # inserting multiple records


#   Task 2  -|
#   ---------|
for s in students.find({}):
    print(f"\nStudent details for roll number {s['Roll']}:")
    print(s)
            # to display all records of students

course = "Data Science"
print(f"\nStudents enrolled in {course}:")
for s in students.find({"Course": course}):
    print(s["Roll"],s["Name"],s["Course"])
            # query to fetch all students enrolled in specific course

print("\nStudents with marks > 75:")
for s in students.find({"Marks": {"$gt": 75}}):
    print(s["Roll"],s["Name"],s["Course"],s["Marks"])
            # query to find and fetch students with marks greater than 75

city = "Pune"
print(f"\nStudents from city = {city}:")
for s in students.find({"City": city}):
    print(s["Roll"],s["Name"],s["City"])
            # query to retrieve students from a specific city


#   Task 3  -|
#   ---------|
students.update_one({"Roll": 1011}, {"$set": {"EmailID": "divya.kapoor@gmail.com"}})
print("\nUpdated email for roll number 1011.")
            # updating email of a student with a specific roll number

for s in students.find({"Roll": 1011}):
    print(f"\nStudent details for roll number {s['Roll']}:")
    print(s)
            # displaying updated record of the student

course = "Mechanical"
print("\nStudents marks:")
for s in students.find({"Course": course}):
    print(s["Roll"],s["Name"],s["Course"],s["Marks"])
            # displaying marks of students enrolled in a specific course

students.update_many({"Course": course}, {"$inc": {"Marks": 10}})
print(f"Added +10 marks to students in {course}.")
            # increasing marks of all students in that specific course by 10

print(f"\nUpdated student details in {course}:")
for s in students.find({"Course": course}):
    print(s["Roll"],s["Name"],s["Course"],s["Marks"])
            # displaying updated records of students in that course

for s in students.find({"Marks": {"$lt": 40}}):
    print(s["Roll"],s["Name"],s["Course"],s["Marks"])
            # displaying students with marks less than 40

students.delete_many({"Marks": {"$lt": 40}})
print(f"Deleted students with marks < 40.")
            # deleting students record with marks less than 40

for s in students.find({"Marks": {"$lt": 40}}):
    print(s["Roll"],s["Name"],s["Course"],s["Marks"])
            # verifying deletion of records


#   Task 4  -|
#   ---------|
print("\nNumber of students per course:")
count = [{"$group": {"_id": "$Course", "count": {"$sum": 1}}}, {"$sort": {"count": 1}}]
for r in students.aggregate(count):
    print(r)
            # aggregate to count the number of students per course while sorting in ascending order

print("\nStudents average marks per course:")
avg = [{"$group": {"_id": "$Course", "avg_marks": {"$avg": "$Marks"}}},{"$sort": {"avg_marks": 1}}]
for s in students.aggregate(avg):
    print(s)
            # aggregate to calculate average marks per course while sorting in ascending order

print("\nTop 3 students by marks:")
for s in students.find({}).sort("Marks", -1).limit(3):
    print(s["Roll"],s["Name"],s["Course"],s["Marks"])
            # query to find and display top 3 students with highest marks

print("\nAll students sorted by marks in descending order:")
for s in students.find({}).sort("Marks", -1):
    print(f"\nStudent details for roll number {s['Roll']}:")
    print(s)
            # query to display all students sorted by marks in descending order


#   Task 5  -|
#   ---------|
docs = list(students.find({}, {"_id": 0}))
            # fetching all records excluding the MongoDB generated _id field
            # converting to a list of dictionaries
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(docs, f, ensure_ascii=False, indent=2)
            # exporting the list of dictionaries to a JSON file
            # ensure_ascii=False to handle any special characters
print("Exported to students.json")




#   Conclusion  -|
#   -------------|
#   The assignment successfully implemented a complete database management pipeline using MongoDB for student data,
#   covering data insertion, querying, updating, deletion, aggregation, and export functionalities.
#   Key Findings:
#    - The database handled diverse student records, supporting efficient storage and retrieval through flexible queries.
#    - Aggregation pipelines provided valuable insights, such as counting students per course and calculating average marks.
#    - Updates and deletions ensured data integrity by reflecting changes like email correction and removing underperforming
#      students.
#    - Sorting and top-performer queries helped highlight high-achieving students across various courses.
#    - Exporting data into JSON format allowed seamless sharing and integration with other systems.
#   Overall, the project demonstrated how MongoDB’s document-oriented structure and aggregation framework can be leveraged
#   to manage, analyze, and report on structured datasets effectively, making it a powerful tool for academic and real-world
#   applications.