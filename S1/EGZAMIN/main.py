from Homework import Homework
from exam import Exam
from grade import ExamD


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

print("__________GRADE___________")

st3_first = ExamD()
st3_first.math_grade = 78
st3_first.wraiting_grade = 89

print(f'ocena math: {st3_first.wraiting_grade}')
print(f'ocena math: {st3_first.math_grade}')

st3_sec = ExamD()
st3_sec.math_grade = 90
st3_sec.wraiting_grade = 98

print(f'ocena math: {st3_sec.wraiting_grade}')
print(f'ocena math: {st3_sec.math_grade}')
print("jeszcze raz pierwszy")
print(f'ocena math: {st3_first.wraiting_grade}')
print(f'ocena math: {st3_first.math_grade}')


