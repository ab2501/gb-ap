import yaml

data = {
    "list": ["item1", "item2", "item3"],
    "number": 245,
    "dictionary": {
        "EUR": 0x20AC,
        "USA": 0x0024,
        "RUB": 0x20BD
    }
}

file_name = 'file.yaml'

with open(file_name, 'w') as f_n:
    yaml.dump(data, f_n)

with open(file_name) as f_n:
    print(f_n.read())
