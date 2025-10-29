#  AI in Software Engineering – Week 4 Assignment  
**Theme:** Building Intelligent Software Solutions  

This project demonstrates how Artificial Intelligence (AI) can automate, enhance, and optimize different aspects of software engineering.  
It includes both theoretical analysis and hands-on implementation using Python, Scikit-learn, Selenium, and GitHub Copilot.



## Project Structure

ai-week-four/
│
├── docs/
│ ├── theoretical_analysis.md # Answers to theoretical questions
│ ├── task1_notes.md # AI-Powered Code Completion summary
│ ├── task2_notes.md # AI-Driven Automated Testing summary
│ ├── ethical_reflection.md # Discussion on bias and fairness
│ └── ai_report.pdf # Final exported report
│
├── src/
│ ├── task1_code_completion.py # Python code for AI-assisted sorting
│ ├── task2_automated_testing.py # Selenium login test script
│ └── task3_predictive_model.ipynb # Predictive analytics notebook
│
├── venv/ # Virtual environment (not uploaded)
└── README.md # Project overview (this file)

markdown
Copy code



##  Assignment Overview

### **Part 1 – Theoretical Analysis**
- Explained how **AI-driven code generation** (e.g., Copilot) improves productivity.
- Compared **supervised vs unsupervised learning** for bug detection.
- Discussed **bias mitigation** in AI-driven personalization.
- Analyzed **AIOps** and its role in automating software deployment.

### **Part 2 – Practical Implementation**
1. **AI-Powered Code Completion**  
   - Tool: GitHub Copilot  
   - Task: Python function to sort dictionaries.  
   - Comparison between AI-suggested and manual implementations.

2. **AI-Driven Automated Testing**  
   - Tool: Selenium IDE / Testim.io  
   - Task: Automated login test (valid/invalid credentials).  
   - Compared manual vs AI-enhanced testing.

3. **Predictive Analytics for Resource Allocation**  
   - Tool: Scikit-learn (Random Forest)  
   - Dataset: Kaggle Breast Cancer Dataset  
   - Goal: Predict issue priority (High, Medium, Low).  
   - Evaluation: Accuracy & F1-score.

### **Part 3 – Ethical Reflection**
- Discussed dataset bias and fairness.
- Proposed use of **IBM AI Fairness 360** for model audit and bias correction.



## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/ai-week-four.git
cd ai-week-four
2. Create and Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
3. Install Required Libraries
bash
Copy code
pip install -r requirements.txt
(Create a requirements.txt file with the following:)

Copy code
scikit-learn
pandas
numpy
selenium
matplotlib
4. Run Each Task
bash
Copy code
# Code completion example
python src/task1_code_completion.py

# Automated testing example
python src/task2_automated_testing.py
 Tools and Resources
AI Tools: GitHub Copilot, Testim.io

Libraries: Scikit-learn, Pandas, Selenium

Dataset: Kaggle Breast Cancer Dataset

IDE: Visual Studio Code

Environment: Python 3.11

 Learning Outcomes
Applied AI tools to real-world software engineering workflows.

Implemented automated code generation and testing.

Understood ethical AI development and fairness evaluation.

Produced a report and demo presentation as part of assessment.

 Author
Name: Lynn Bitok
Course: Software Engineering
Institution: University of Eastern Africa, Baraton
Year: 3

How to View the Report
To read the final report locally:

Open docs/ai_report.pdf

Or view Markdown files in the docs/ folder using VS Code’s Markdown preview (Ctrl+Shift+V).

 Demo Video
 A short 3-minute demo video will be shared separately for peer review.

yaml
Copy code
