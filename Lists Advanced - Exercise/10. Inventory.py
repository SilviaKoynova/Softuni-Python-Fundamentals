items = input().split(', ')
data = input()


def is_item_in_list(item_list, i):
    if i in item_list:
        return True
    return False


def collect_item(item_list, i):
    if not is_item_in_list(item_list, i):
        item_list.append(i)
    return item_list


def drop_item(item_list, i):
    if is_item_in_list(item_list, i):
        item_list.remove(i)
    return item_list


def combine_items(item_list, i):
    old_item = i.split(':')[0]
    new_item = i.split(':')[1]
    if is_item_in_list(item_list, old_item):
        index_old_item = item_list.index(old_item)
        index_new_item = index_old_item + 1
        item_list.insert(index_new_item, new_item)
    return item_list


def renew_item(item_list, i):
    if is_item_in_list(item_list, i):
        item_list.remove(i)
        item_list.append(i)
    return item_list


while not data == 'Craft!':
    command, item = data.split(' - ')
    if command == 'Collect':
        items = collect_item(items, item)
    elif command == 'Drop':
        items = drop_item(items, item)
    elif command == 'Combine Items':
        items = combine_items(items, item)
    elif command == 'Renew':
        items = renew_item(items, item)

    data = input()
print(', '.join(items))
