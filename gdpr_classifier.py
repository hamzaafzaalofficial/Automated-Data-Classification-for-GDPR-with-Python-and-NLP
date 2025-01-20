import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Load the dataset
data = pd.read_csv('sample_customer_data.csv')

def scan_for_personal_data(text):
    """Scan text for personal data using spaCy's NER"""
    doc = nlp(str(text))
    return [(ent.text, ent.label_) for ent in doc.ents]

def process_row(row):
    """Process each row of the dataset"""
    # Combine relevant fields into text
    text_to_scan = f"{row['name']} {row['email']} {row['address']} {row['phone']} {row['organization']} {row['notes']}"

    # Scan for personal data
    return scan_for_personal_data(text_to_scan)

def tag_personal_data(personal_data):
    """Extract tags from personal data"""
    return [item[1] for item in personal_data]

def categorize_personal_data(tags):
    """Convert tags to human-readable categories"""
    category_mapping = {
        'PERSON': 'Name',
        'ORG': 'Organization',
        'GPE': 'Geopolitical Entity',
        'LOC': 'Location',
        'DATE': 'Date',
        'TIME': 'Time',
        'MONEY': 'Financial Information',
        'EMAIL': 'Email',
        'PHONE': 'Phone Number'
    }
    return list(set(category_mapping.get(tag, 'Other') for tag in tags))

def main():
    # Step 1: Find personal data
    print("Step 1: Scanning for personal data...")
    data['personal_data'] = data.apply(process_row, axis=1)

    # Step 2: Extract tags
    print("Step 2: Extracting tags...")
    data['tags'] = data['personal_data'].apply(tag_personal_data)

    # Step 3: Categorize
    print("Step 3: Categorizing data...")
    data['categories'] = data['tags'].apply(categorize_personal_data)

    # Display results
    print("\nResults for first 5 records:")
    print("-" * 50)
    for idx, row in data.head().iterrows():
        print(f"\nRecord {idx + 1}:")
        print(f"Name: {row['name']}")
        print("Personal Data Found:")
        for item in row['personal_data']:
            print(f"   • {item[0]} -> {item[1]}")
        print("Categories:", row['categories'])
        print("-" * 50)

    # Save results to new CSV
    output_file = 'gdpr_analysis_results.csv'
    data.to_csv(output_file, index=False)
    print(f"\nComplete results saved to {output_file}")

if __name__ == "__main__":
    main()
