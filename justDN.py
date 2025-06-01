
def filter_dialogue_and_narration(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        lines = infile.readlines()
    
    filtered_lines = [line for line in lines if line.startswith('D:') or line.startswith('N:')]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(filtered_lines)

input_file = r'C:\Users\zaimi\Desktop\MOVIES\scripts\parsed\tagged\ZOOTOPIA_parsed.txt' 
output_file = r'C:\Users\zaimi\Desktop\MOVIES\scripts\parsed\tagged\ZOOTOPIA_filtered.txt' 

filter_dialogue_and_narration(input_file, output_file)

print("Filtering completed! The filtered content has been saved.")
