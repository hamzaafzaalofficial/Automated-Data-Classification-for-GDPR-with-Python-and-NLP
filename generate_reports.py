import pandas as pd

def generate_summary_report(data):
    # Count the occurrence of each category
    category_counts = data['categories'].explode().value_counts()

    # Generate a summary report
    summary_report = {
        'Total Records': len(data),
        'Records with Personal Data': len(data[data['categories'].map(len) > 0]),
        'Category Breakdown': category_counts.to_dict()  # Fixed key name
    }
    print("\nSummary Report:")
    print("---------------")
    print(f"Total Records: {summary_report['Total Records']}")
    print(f"Records with Personal Data: {summary_report['Records with Personal Data']}")
    print("\nCategory Breakdown:")
    for category, count in summary_report['Category Breakdown'].items():  # Fixed key name
        print(f"{category}: {count}")

    return summary_report

def generate_detailed_report(data):
    # Detailed compliance report
    detailed_report = data[data['categories'].map(len) > 0][['name', 'personal_data', 'categories']]

    # Export the report to a CSV file
    detailed_report.to_csv('compliance_report.csv', index=False)
    print("\nDetailed compliance report generated and saved as 'compliance_report.csv'")

    return detailed_report

def main():
    try:
        # Load your analyzed data
        data = pd.read_csv('gdpr_analysis_results.csv')

        # Convert string representations back to lists/dicts
        data['personal_data'] = data['personal_data'].apply(eval)
        data['categories'] = data['categories'].apply(eval)

        # Generate summary report
        summary_report = generate_summary_report(data)

        # Generate detailed report
        detailed_report = generate_detailed_report(data)

        print("\nReport generation complete!")

    except Exception as e:
        print(f"Error during report generation: {str(e)}")

if __name__ == "__main__":
    main()
