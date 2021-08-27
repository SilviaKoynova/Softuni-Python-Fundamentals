# version = input().split(".")
# integer_version = int(''.join(version))
# new_version = int(integer_version + 1)
# print('.'.join(str(new_version)))
version = input().split(".")
integer_version = int(''.join(version)) + 1
print('.'.join(str(integer_version)))
