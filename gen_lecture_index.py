import os
import re

lectures = [f for f in os.listdir('lectures') if re.match("^\d\d.*html$", f)]
lectures.sort()

with open("lectures/index.md", "w") as out:
    out.write("# Lectures\n\n")

    out.write("Day|Description|Slides\n")
    out.write(":--|:----------|:-----\n")

    for lecture in lectures:
        day = re.search("\d\d", lecture).group(0)
        description = lecture[2:-5]
        description = description.replace('-',' ')
        description = description.title().strip()
        print(lecture, description)
        slides = lecture
        markdown = lecture.replace(".html", ".md")
    
        out.write(f"{int(day)}|{description}|[Slides]({lecture})\n")

    out.write("\n[Combined Slides](all-slides.html)")
