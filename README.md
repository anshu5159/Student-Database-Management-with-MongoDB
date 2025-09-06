# 📚 Student Database Management using MongoDB
This project demonstrates how to design and manage a student database using **MongoDB**. The goal is to simulate a real-world academic scenario where student data is stored, updated, and analyzed using CRUD operations and aggregation queries. The project covers database setup, insertion of records, querying, updating, deleting, aggregating, and exporting data in JSON format.

---

## 🗂 Dataset Design

The dataset includes **15 student records**, each having the following fields:

- **Roll**: Unique identifier for each student.
- **Name**: Student’s name.
- **Course**: Academic program (e.g., Data Science, Computer Science).
- **Marks**: Numeric value representing the student’s score.
- **City**: Location where the student resides.
- **EmailID**: Contact email of the student.

The dataset was created to cover multiple courses and cities, with diverse academic performances to allow meaningful filtering and aggregation.

---

## 🔍 Queries Executed

1. Display all student records.
2. Retrieve students enrolled in a specific course.
3. Find students with marks greater than 75.
4. Retrieve students from a specific city.
5. Update the email address of a student.
6. Add 10 marks to all students in the “Mechanical” course.
7. Delete students with marks less than 40.
8. Count the number of students in each course.
9. Calculate average marks per course.
10. Find the top 3 students by marks.
11. Sort all students by marks in descending order.
12. Export the dataset into a `students.json` file.

---

## 📊 Insights Discovered

- The **Data Science** course had the highest-performing students.
- The **top 3 students** by marks were:
  - Sara (95 marks)
  - Ananya (92 marks)
  - Vikram (91 marks)
- Students in the **Mechanical** course improved after receiving bonus marks.
- Students with marks below 40 were removed to ensure dataset integrity.

---

## 📂 Files

- `studentDB.py`: Python script containing all database operations using PyMongo.
- `students.json`: Exported JSON file containing all student records.
- `Student Database Management Report`: Explanation document.
