def solution(my_string, overwrite_string, s):
    var = len(overwrite_string)
    new_str = my_string[:s]+overwrite_string+my_string[s+var:]
    return new_str