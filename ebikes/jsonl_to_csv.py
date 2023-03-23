import csv
import json
import sys
sys.path.append('/Users/lansang/Desktop/validities-main/src')
import sentencizer

#Call the Sentencizer class from the sentencizer.py file in src folder
sn = sentencizer.Sentencizer()

#Function to extract links, texts, break the texts and write them into a csv file named text_break_output.csv
def jsonl_to_csv(input, output):
    with open(input, 'r') as input_file, open(output, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['url', 'sentence'])
        
        for line in input_file:
            
            data = json.loads(line)
            # Extract the "body" and "permalink" fields
            body = data['body']
            url = data['permalink']
            # Split the body text into sentences
            sentences = sn.sentencize(body)
            
            # Write each sentence and permalink to the CSV file
            for sentence in sentences:
                writer.writerow([url, sentence])
    return output_file

#Call this jsonl_to_csv function to generate a csv file of broken sentences and links.
jsonl_to_csv('/Users/lansang/Desktop/validities-main/ebikes/to_lan.jsonl', '/Users/lansang/Desktop/validities-main/ebikes/text_break_output.csv') 
