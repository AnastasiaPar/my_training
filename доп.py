import statistics
grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
b=[[statistics.mean(grades[0])],[statistics.mean(grades[1])],[statistics.mean(grades[2])],[statistics.mean(grades[3])],[statistics.mean(grades[4])]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=sorted(students)
dictionary = dict(zip(a,b))
print(dictionary)
