def filter_words(st):
    lis_t = st.lower().split()
    st_r = ' '.join(lis_t)
    return st_r[0].upper() + st_r[1:]


print(filter_words("Hello WORLD!"))
