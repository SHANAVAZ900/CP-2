# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):

    repeat = s1.count(s2)
    if repeat == 0:
        return s1

    position = [i for i in range(len(s1) - len(s2)+1) if s1.startswith(s2, i)]
    j = position[0]

    for i in range(len(position)):
        s1 = s1[:j]+s3+s1[j+len(s2):]
        if i == len(position)-1:
            break
        j = position[i+1]+len(s3)-len(s2)
    return s1
