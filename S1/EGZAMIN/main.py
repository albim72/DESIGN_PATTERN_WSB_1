from Homework import Homework
from exam import Exam


print("__________HOMEWORK___________")
st = Homework()
st.grade = 86
assert st.grade == 86
print(st.grade)

print("__________EXAM___________")

st2 = Exam()
st2.writing_grade = 78
st2.math_grade = 67

assert st2.writing_grade == 78
assert st2.math_grade == 67

print(st2.writing_grade)
print(st2.math_grade)
