def delete(list_, index=-1):
    lenght = len(list_)
    if index < 0:
        index = lenght + index
    return list_[:index] + list_[index + 1:]

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
