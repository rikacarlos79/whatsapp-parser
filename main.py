import re

def line_cleaner(line):
    line = line.strip()
    # Remove timestamp format: D/MM/YYYY or DD/MM/YYYY, H:MM pm -
    # The ' ' is a narrow no-break space (U+202F) often found in these exports
    line = re.sub(r'^\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2} [ap]m - ', '', line)
    return line

# Regex pattern to match: Rika: Hey <hosts>! (or Hey <hosts>,) <someone> and I are here... or Rika: Hey <hosts>! I'm here...
# Allows for emojis before "Hey" (e.g. Rika: 🤗Hey) and works regardless of the specific event/party ending sentence.
start_pattern = re.compile(
    r'^Rika: .*?Hey .+[!,] (?:.+ and I are|I\'m) here for any major issues\.'
)

content = ""
started = False

with open('content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        
        cleaned = line_cleaner(line)
        if not started:
            if start_pattern.match(cleaned):
                started = True
            else:
                continue
        
        # Using strip() to remove the trailing newline character
        content += cleaned + " | "
        print(content, cleaned)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(content)