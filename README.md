# Automated-Data-Classification-for-GDPR-with-Python-and-NLP

---

## Automated GDPR Data Classification System

### Overview
An automated system for scanning and classifying personal data in datasets using Natural Language Processing (NLP) techniques, designed to assist organizations in maintaining GDPR compliance.

### Key Features
- **Automated Data Scanning**: Uses advanced NLP to identify personal information in datasets.
- **Smart Classification**: Automatically categorizes different types of personal data (names, addresses, etc.).
- **Compliance Reporting**: Generates both summary and detailed reports for compliance tracking.
- **Flexible Processing**: Handles various data formats and text fields.

---

### Technical Stack
- **Python 3.x**
- **spaCy** for NLP processing
- **Pandas** for data handling

---

### How It Works
1. **Data Ingestion**: System reads datasets from various sources.
2. **NLP Processing**: Uses spaCy to analyze text and identify entities.
3. **Classification**: Categorizes identified entities into GDPR-relevant categories.
4. **Report Generation**: Creates detailed compliance reports and summaries.
5. **Cron Scheduling**: If we are getting continously new data, adding a cron scheduler to automate the report generation is crucial.

---

### Output Examples
The system generates:
- Category breakdown of personal data
- Detailed record-level analysis
- Compliance status reports

---

### Benefits
- Reduces manual effort in GDPR compliance
- Increases accuracy in personal data identification
- Provides consistent classification across datasets
- Enables regular compliance monitoring
