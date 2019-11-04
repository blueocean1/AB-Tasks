def reverse(st):
    words = st.split()
    lis_t = []
    for i in range(1, len(words) + 1):
        lis_t.append(words[-i])
    st_r = ' '.join(lis_t)
    return st_r
