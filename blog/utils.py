import re


def slugify(string): # Change string into slug
    string = string.lower().strip()
    string = re.sub(r"[^\w\s-]", "", string)
    string = re.sub(r"[\s_-]+", "-", string)
    string = re.sub(r"^-+|-+$", "", string)
    return string
