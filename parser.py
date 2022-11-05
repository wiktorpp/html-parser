from snippets import snippets
html = open("html.txt", "r").read()

output = ""
for group in html.split(snippets[0])[1:]:
    group_name = group.split(">")[1].split("<")[0]
    group_name = group_name.replace("&amp;", "&")
    group_name = " ".join(group_name.split())
    output += f"\n\n=={group_name}==\n"
    for item in group.split(snippets[1])[1:]:
        name = item.split("</div>")[0]
        name = " ".join(name.split())
        output += f"{name}\n"
        description = item.split(snippets[2])[1].split("</div>")[0]
        description = " ".join(description.split())
        output += f"     {description}\n"

print(output)
