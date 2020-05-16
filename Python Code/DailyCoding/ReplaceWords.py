def replace(dict, st):
    st = st.split()
    for i in range(len(dict)):
        for j in range(len(st)):
            if st[j].startswith(dict[i]):
                st[j] = dict[i]
    return " ".join(st)

dict = ["cat", "bat", "rat"]
st = "the cattle was rattled by the battery"
print(replace(dict, st))
