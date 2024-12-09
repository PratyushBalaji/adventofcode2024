with open(r'adventofcode2024\Day 9\input.txt', 'r') as file:
    data = file.readlines()[0]
# print(data)

# call with a string disk
def checksum(num):
    total = 0
    count = -1
    for i in num:
        count+=1
        if i == '.':
            continue
        total+=int(i)*count
    return total

# call with str(diskmap)
# def makeDisk(diskmap):
#     isFree = False
#     id = 0
#     ret = ''
#     for i in diskmap:
#         if isFree:
#             ret+= int(i)*'.'
#         else:
#             ret+= int(i)*str(id)
#             id += 1
#         isFree = not isFree
#     return ret
def makeDisk(diskmap):
    isFree = False
    id = 0
    ret = []
    for i in diskmap:
        if isFree:
            ret+= int(i)*['.']
        else:
            ret+= int(i)*[str(id)]
            id += 1
        isFree = not isFree
    return ret

# print(checksum(list('0099811188827773336446555566')))

def frag(disk):
    x = len(disk)
    y = x - disk.count('.')
    curr = 0
    unorgDisk = disk
    while x != y:
        if unorgDisk[-1] == '.':
            unorgDisk = unorgDisk[:-1]
        else:
            while unorgDisk[curr] != '.':
                curr += 1
            unorgDisk[curr] = unorgDisk[-1]
            unorgDisk = unorgDisk[:-1]
        x-=1
    return unorgDisk

def partOne():
    return checksum(frag(makeDisk(data)))

def makeDisk2(diskmap):
    isFree = False
    id = 0
    ret = []
    for i in diskmap:
        if isFree:
            ret+= [int(i)*['.']]
        else:
            ret+= [int(i)*[str(id)]]
            id += 1
        isFree = not isFree
    return ret

def fileFrag(disk):
    # Flatten the disk for easier traversal
    flat_disk = [block for group in disk for block in group]

    # Get list of files and their lengths
    files = [(int(group[0]), len(group)) for group in disk if group and group[0] != '.']
    files.sort(reverse=True)  # Process files by decreasing file ID

    for file_id, file_length in files:
        # Find the first span of free space large enough to fit the file
        free_start = -1
        free_length = 0
        for i, block in enumerate(flat_disk):
            if block == '.':
                if free_start == -1:
                    free_start = i  # Mark start of free space
                free_length += 1
                if free_length == file_length:
                    # Found a valid span, move the file here
                    for j in range(free_start, free_start + file_length):
                        flat_disk[j] = str(file_id)
                    # Remove the file from its original position
                    for _ in range(file_length):
                        flat_disk.remove(str(file_id))
                    break
            else:
                # Reset free space tracking
                free_start = -1
                free_length = 0

    # Regroup the fragmented disk
    regrouped_disk = []
    current_group = []
    for block in flat_disk:
        if current_group and block != current_group[-1]:
            regrouped_disk.append(current_group)
            current_group = []
        current_group.append(block)
    if current_group:
        regrouped_disk.append(current_group)

    return regrouped_disk

def partTwo():
    # Create grouped disk layout
    grouped_disk = makeDisk2(data)

    # Perform file-level fragmentation
    fragmented_disk = fileFrag(grouped_disk)

    # Flatten disk for checksum calculation
    flat_disk = [block for group in fragmented_disk for block in group]

    # Calculate checksum
    return checksum(flat_disk)

# print(makeDisk2('2333133121414131402'))

# print(partOne())
# print(checksum(list('00992111777.44.333....5555.6666.....8888..')))
# print(makeDisk(data))

print(partTwo())