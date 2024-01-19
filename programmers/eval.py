# python의 eval
"""
eval 은 string 형태로 된 문자열을 수식화 해 준다
"""
string_command = "2*3"
eval_command = eval(string_command)
print(string_command)  # '2*3
print(eval_command)  # 6