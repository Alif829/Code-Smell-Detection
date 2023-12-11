def process_data(data, threshold):
    filtered_data = filter(lambda x: x["value"] > threshold and (x["name"] == "foo" or x["priority"] > 10), data)
    funcs = [lambda x: x + i for i in range(3)]
    sorted_data = sorted(filtered_data, key=lambda x: ((x["value"] * 2) + (x["priority"] / 3)) * (1 if x["active"] else -1))
    return sorted_data

result = process_data(data, 10)