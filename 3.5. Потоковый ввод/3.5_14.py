import json
a = {}
output_filename = ""
for i in range(2):
    filename = input()
    if i == 0:
        output_filename = filename
    with open(filename, "r", encoding="UTF-8") as file:
        input_data = json.load(file)
        for user_dict in input_data:
            username = user_dict["name"]
            user_dict = dict(sorted(user_dict.items()))
            if username not in a.keys():
                a[username] = {}
                for key, value in user_dict.items():
                    if key != "name":
                        a[username].update({key: value})
            else:
                for key, value in user_dict.items():
                    if key != "name" and key not in a[username].keys():
                        a[username].update({key: value})
                    elif key != "name" and a[username][key] < value:
                        a[username].update({key: value})

with open(output_filename, "w", encoding="UTF-8") as file:
    json.dump(a, file, ensure_ascii=False, indent=4)
