''''   
Accept the average score of the student and print the result as follow:
0 to 59: "Fail"
 60 to 84: "second class"
 85 to 95: "first class"
 96 to 100: "Excellent"  
'''

average_score = float(input("Enter the average score of the student: "))
if 0 <= average_score >= 100:
    print("invalid score")
elif 60 <= average_score < 85:
    print("second class")
elif 85<=average_score<95:
    print("first class")
elif 0 <= average_score < 59:
    print("fail")
else:
    print("result is excellent")