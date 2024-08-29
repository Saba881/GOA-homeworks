def manual_count(input_string, count_char):
    count = 0
    for char in input_string:
        if char == count_char:
            count += 1
    return count

result = manual_count("hello world", "o")
print(result)
