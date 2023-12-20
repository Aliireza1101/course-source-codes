import re


def slugify(string):
    string = string.lower().strip()
    string = re.sub(r"[^\w\s-]", "", string)
    string = re.sub(r"[\s_-]+", "-", string)
    string = re.sub(r"^-+|-+$", "", string)
    return string
