import os
import re

lectures = [f for f in os.listdir('lectures') if re.match("^\d\d.*html$", f)]
lectures.sort()

with open("lectures/index.md", "w") as out:
    out.write("# Lectures\n\n")

    for lecture in lectures:
        day = re.search("\d\d", lecture).group(0)
        slides = lecture
        markdown = lecture.replace(".html", ".md")
    
        out.write(f"- Lecture {int(day)}: [Slides]({lecture}) [Markdown]({markdown})\n")

    out.write("\n[Combined Slides](all-slides.html)")
