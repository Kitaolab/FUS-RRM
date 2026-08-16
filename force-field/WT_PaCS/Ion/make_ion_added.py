lines = [
    "[ moleculetype ]",
    "Ion          3",
    "[ atoms ]"
]

for i in range(201):
    lines.append(f"{i+1} IK {128+i} K+ K+ {i+1} 0.9 39.1")

for i in range(178):
    lines.append(f"{i+202} IIM {128+202+i} Cl- Cl- {i+202} -0.9 35.45")

lines.extend([
    "[ exclusions ]",
    "[ system ]",
    "title",
    "",
])

open("gleap_converted.top", "w").write("\n".join(lines))
