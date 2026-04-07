from django.shortcuts import render

def index(request):
    context = {
        'name': 'Annapoorneshwari K G',
        'title': 'Business System Analyst',
        'email': 'anukanaka1312@gmail.com',
        'phone': '+91 6366058861',
        'location': 'Bengaluru, India',
        'linkedin': 'https://www.linkedin.com/in/annapoorneshwari-k-g',
        'languages': ['English', 'Kannada', 'Hindi'],
        'hobbies': ['Reading', 'Travelling', 'Cooking', 'Music'],
        'summary': 'Data and Business Analytics professional with experience in SQL, Oracle, Databricks, Python, reporting, and data-driven problem-solving. Skilled in analyzing large datasets, writing complex queries, validating data, and delivering actionable insights to support business decisions. Experienced in business analysis, process improvement, requirement gathering, campaign execution, and cross-functional collaboration to streamline operations.',
        'skills': {
            'Data & Querying': ['SQL (Oracle, MySQL)', 'PySpark', 'Databricks', 'Python (Pandas, NumPy)'],
            'Analytics': ['Exploratory Data Analysis (EDA)', 'Statistical Hypothesis Testing', 'A/B Test Validation', 'Data Modeling'],
            'Visualization & Reporting': ['Tableau', 'Matplotlib', 'Seaborn', 'Cognos Reporting'],
            'Martech': ['Adobe Campaign Classic', 'Salesforce Marketing Cloud', 'Email Marketing Automation', 'Audience Segmentation', 'Campaign QA'],
            'Web & Development': ['Django', 'HTML', 'CSS'],
            'Cloud': ['AWS'],
            'Tools & Processes': ['Data Validation (QA/QC)', 'ETL', 'Git', 'GitHub', 'Advanced MS Excel'],
        },
        'experience': [
            {
                'company': 'Epsilon, Bengaluru',
                'period': 'Aug 2023 - Present',
                'roles': [
                    {
                        'title': 'Business System Analyst',
                        'points': [
                            'Gathered and analyzed business requirements, reporting needs, data workflows, and process dependencies to support process improvements.',
                            'Executed end-to-end email and direct mail channel campaigns for sales and aftersales programs.',
                            'Developed and supported welcome campaigns by translating business requirements into campaign workflows.',
                            'Performed data validation, reporting analysis, visualization, and campaign performance checks.',
                            'Developed an internal web-based validation tool using Python, Django, HTML, CSS, and Amazon Q Developer.',
                            'Supported UAT, system testing, implementation validation, and requirement verification.',
                        ]
                    },
                    {
                        'title': 'Associate Business System Analyst',
                        'points': [
                            'Analyzed, validated, and interpreted large volumes of business data using SQL, Oracle, and Python.',
                            'Executed end-to-end email and direct mail campaigns for sales and aftersales programs.',
                            'Automated manual intervention and repetitive tasks through Python-based automation.',
                            'Conducted comprehensive data validation, quality checks, and test-run analysis.',
                            'Prepared and supported reports, summaries, dashboards, and ad hoc analyses.',
                        ]
                    },
                ]
            }
        ],
        'projects': [
            'Advanced Data Analytics Capstone',
            'Predictive Customer Analytics Engine',
            'Automation of repetitive tasks using Python',
            'Built a file validation web application using Python, Django, HTML, and CSS with Amazon Q Developer support',
        ],
        'education': {
            'degree': 'Bachelor of Engineering (BE)',
            'institute': 'Nitte Meenakshi Institute of Technology, Bengaluru',
            'field': 'Electronics and Communication Engineering',
            'period': 'Aug 2019 - Jun 2023',
            'cgpa': '8.23',
        },
        'certifications': [
            'Advanced Google Data Analytics',
            'Salesforce Marketing Cloud',
            'PowerBI',
            'Python',
        ],
    }
    return render(request, 'bio/index.html', context)
