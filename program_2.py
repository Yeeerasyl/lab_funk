comments = {}
index = 1

while True:
    comment = input().strip()
    if not comment:
        break
    if comment not in comments.values():
        comments[index] = comment
        index += 1

unique_comments = len(comments)
print(unique_comments)

