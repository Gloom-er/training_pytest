def read_from_file(filepath):
    with open(filepath, "r") as f_o:
        return f_o.readlines()
