input_file = "transcript.txt"
output_file = "output.txt"

# Reading the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Combining lines based on speaker
combined_lines = []
current_speaker = ""
current_text = ""

for line in lines:
    if line.startswith("[Speaker"):
        speaker = line[:12]
        text = line[12:].strip()
        if speaker == current_speaker:
            current_text += " " + text
        else:
            if current_speaker:
                combined_lines.append(f"{current_speaker} {current_text.strip()}\n")
            current_speaker = speaker
            current_text = text
    else:
        current_text += " " + line.strip()

# Adding the last speaker's text
if current_speaker:
    combined_lines.append(f"{current_speaker} {current_text.strip()}\n")

# Writing the output file
with open(output_file, "w") as file:
    file.writelines(combined_lines)

print("Processing complete. Check output.txt for the result.")
