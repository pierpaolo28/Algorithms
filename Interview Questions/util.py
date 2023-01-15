df_to_list = """    0   25     yes    yes
    1   32      no     no
    2   10     yes     no
    3   40     yes     no
    4   75      no     no
    5   80     yes     no
    6   60     yes     no
    7   60      no    yes
    8   40     yes    yes
    9   80     yes     no"""

print(df_to_list.split()[3::4])
print(list(map(int, df_to_list.split()[1::4])))