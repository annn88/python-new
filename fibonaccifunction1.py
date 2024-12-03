'''
name:ann mariya biju
date: 03/12/2024
python program to create fibonacci series
'''
def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
