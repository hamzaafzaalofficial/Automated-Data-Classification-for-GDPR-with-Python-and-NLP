import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_dataset(num_records=100):
    # Sample data generators
    names = ['Ali Ahmed', 'Sara Khan', 'Mohammad Qasim', 'Fatima Zahra', 'Hassan Ali',
            'Ayesha Malik', 'Zainab Hussain', 'Omar Farooq', 'Maryam Nawaz', 'Bilal Khan']

    emails = ['ali@example.com', 'sara@company.pk', 'mqasim@email.com', 'fatima@org.com',
             'hassan@mail.pk', 'amalik@work.com', 'zh@email.pk', 'omar@company.com',
             'maryam@org.pk', 'bkhan@mail.com']

    addresses = ['123 Main St, Karachi', '456 Park Road, Lahore', '789 Avenue, Islamabad',
                '321 Plaza, Rawalpindi', '654 Market, Faisalabad']

    phone_numbers = ['+92300-1234567', '+92333-7654321', '+92321-9876543',
                    '+92345-1234567', '+92312-7654321']

    # Added just organizations list
    organizations = ['Tech Solutions Ltd', 'Global Systems Inc', 'Data Corp Pakistan',
                    'Innovation Hub', 'Digital Services', 'Pakistan Software House',
                    'AI Solutions Pakistan', 'Cloud Tech Services', 'Data Analytics PK',
                    'Cyber Security Solutions']

    # Generate records
    records = []
    for _ in range(num_records):
        record = {
            'name': random.choice(names),
            'email': random.choice(emails),
            'address': random.choice(addresses),
            'phone': random.choice(phone_numbers),
            'date_of_birth': (datetime.now() - timedelta(days=random.randint(7300, 25000))).strftime('%Y-%m-%d'),
            'account_balance': random.randint(1000, 100000),
            'last_transaction': random.randint(100, 5000),
            'organization': random.choice(organizations),  # Added organization field
            'notes': f"Customer contacted on {(datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')} regarding account services."
        }
        records.append(record)

    # Create DataFrame
    df = pd.DataFrame(records)

    # Save to CSV
    df.to_csv('sample_customer_data.csv', index=False)
    print("Dataset generated and saved as 'sample_customer_data.csv'")
    return df

if __name__ == "__main__":
    # Generate sample dataset
    df = generate_sample_dataset()
    print("\nSample of generated data:")
    print(df.head())
    print("\nDataset Information:")
    print(df.info())
