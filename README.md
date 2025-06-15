# 🧠 AI Resume Matcher

An intelligent resume matching application that uses Natural Language Processing (NLP) to calculate the similarity between resumes and job descriptions. Built with Streamlit for an intuitive web interface.

## 🚀 Features

- **Multi-format Support**: Upload resumes in PDF or DOCX format
- **AI-Powered Matching**: Uses TF-IDF vectorization and cosine similarity for accurate matching
- **Real-time Analysis**: Instant similarity score calculation
- **User-Friendly Interface**: Clean and intuitive Streamlit web app
- **Safe File Handling**: Automatic cleanup of temporary files

## 🛠️ Technologies Used

### Core Libraries
- **Streamlit**: Web application framework for creating interactive data apps
- **scikit-learn**: Machine learning library for TF-IDF vectorization and similarity calculations
- **pdfplumber**: PDF text extraction with high accuracy
- **python-docx**: Microsoft Word document processing

### NLP Approach
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Converts text into numerical vectors
- **Cosine Similarity**: Measures the similarity between resume and job description vectors
- **Stop Words Filtering**: Removes common English words for better matching accuracy

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd AI-Resume-Matcher
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   Open your web browser and navigate to `http://localhost:8501`

3. **Use the application**
   - Upload a resume file (PDF or DOCX format)
   - Paste the job description in the text area
   - View the calculated similarity score percentage

## 📁 Project Structure

```
AI Resume Matcher/
│
├── app.py                 # Main Streamlit application
├── resume_matcher.py      # Core matching logic
├── utils.py              # Text extraction utilities
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
│
├── __pycache__/         # Python cache files
├── job_descriptions/    # Sample job descriptions (optional)
├── sample_resumes/      # Sample resumes for testing (optional)
└── temp_resume          # Temporary file (auto-generated)
```

## 🧮 How It Works

1. **File Upload**: Users upload resume files through the Streamlit interface
2. **Text Extraction**: 
   - PDF files: Processed using `pdfplumber` for accurate text extraction
   - DOCX files: Processed using `python-docx` library
3. **Text Preprocessing**: 
   - Convert text to TF-IDF vectors
   - Remove English stop words
4. **Similarity Calculation**: 
   - Use cosine similarity to compare resume and job description vectors
   - Return percentage match score

## 🔍 Code Explanation

### Main Components

- **`app.py`**: Streamlit web interface handling file uploads and displaying results
- **`resume_matcher.py`**: Contains core functions:
  - `load_resume()`: Determines file type and extracts text
  - `calculate_similarity()`: Computes similarity using TF-IDF and cosine similarity
- **`utils.py`**: Utility functions for text extraction from different file formats

### Key Functions

```python
# Text extraction
extract_text_from_pdf(file_path)    # Extract text from PDF files
extract_text_from_docx(file_path)   # Extract text from DOCX files

# Matching logic
load_resume(file_path)              # Load and extract text from resume
calculate_similarity(resume_text, jd_text)  # Calculate similarity percentage
```

## 📊 Example Output

```
Resume Match Score: 87.5%
```

The score represents the percentage similarity between the uploaded resume and the provided job description.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues

1. **File Upload Error**: Ensure the uploaded file is in PDF or DOCX format
2. **Empty Text Extraction**: Some PDF files may have text as images - consider using OCR for such files
3. **Low Similarity Scores**: Try using more specific keywords in the job description

### Dependencies Issues

If you encounter installation issues:

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 🔮 Future Enhancements

- [ ] Add support for multiple file formats (TXT, RTF)
- [ ] Implement OCR for image-based PDFs
- [ ] Add keyword highlighting and analysis
- [ ] Include detailed breakdown of matching sections
- [ ] Add resume suggestions for improvement
- [ ] Implement batch processing for multiple resumes

## 📞 Support

For support, please open an issue on the GitHub repository or contact the development team.

---

**Built with ❤️ using Python and Streamlit**
