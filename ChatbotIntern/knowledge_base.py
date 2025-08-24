class InternshipKnowledgeBase:
    def __init__(self):
        self.faq_data = {
            'application_process': {
                'questions': [
                    'How do I apply for internships?',
                    'What is the application process?',
                    'Where can I submit my application?'
                ],
                'answers': [
                    'Most internship applications require submitting a resume, cover letter, and sometimes a portfolio or transcripts. Start by researching companies, checking their career pages, and following their specific application instructions.',
                    'Common steps include: 1) Research opportunities, 2) Prepare application materials, 3) Submit applications online, 4) Complete any required assessments, 5) Participate in interviews if selected.',
                    'Applications are typically submitted through company career portals, job boards like LinkedIn or Indeed, or university career centers. Some companies also attend career fairs for recruitment.'
                ]
            },
            'requirements': {
                'questions': [
                    'What are the requirements for internships?',
                    'Do I need specific qualifications?',
                    'What skills do I need?'
                ],
                'answers': [
                    'Requirements vary by field, but generally include being enrolled in a relevant degree program, having a good GPA (usually 3.0+), and demonstrating relevant skills through coursework or projects.',
                    'Technical internships often require programming skills, familiarity with specific tools, and problem-solving abilities. Soft skills like communication, teamwork, and adaptability are valued across all fields.',
                    'Most internships are open to students in their sophomore, junior, or senior years. Some programs accept graduate students or recent graduates. Check specific eligibility criteria for each opportunity.'
                ]
            },
            'timeline': {
                'questions': [
                    'When should I apply for internships?',
                    'What are the application deadlines?',
                    'How long do internships last?'
                ],
                'answers': [
                    'Summer internship applications typically open in early fall and close between January-March. Apply early as many programs have rolling admissions and positions fill quickly.',
                    'Internships usually last 10-12 weeks for summer programs, though some can be 6-16 weeks. Academic year internships may be part-time for a full semester or longer.',
                    'Start preparing 6-12 months in advance. Update your resume, build a portfolio, and begin networking. The earlier you start, the more opportunities you\'ll have.'
                ]
            },
            'compensation': {
                'questions': [
                    'Are internships paid?',
                    'How much do interns earn?',
                    'What benefits do interns receive?'
                ],
                'answers': [
                    'Many internships are paid, especially in tech, finance, and engineering. Rates vary widely from $15-50+ per hour depending on the industry, company size, and location.',
                    'Some internships offer additional benefits like housing stipends, transportation allowances, meal vouchers, or professional development opportunities.',
                    'Unpaid internships are less common but still exist, particularly in non-profits, government, and some creative fields. Ensure unpaid internships meet legal requirements and provide valuable learning experiences.'
                ]
            },
            'location': {
                'questions': [
                    'Where are internships located?',
                    'Can I work remotely?',
                    'Do I need to relocate?'
                ],
                'answers': [
                    'Internships are available in major cities, smaller towns, and increasingly as remote opportunities. Tech companies often offer remote internships, while others may require on-site presence.',
                    'Many companies provide relocation assistance or housing for interns who need to move. Some offer housing stipends or connect interns with temporary housing options.',
                    'Remote internships have become more common post-2020. These can be great options for gaining experience without geographical constraints, though networking opportunities may be different.'
                ]
            },
            'selection_process': {
                'questions': [
                    'What is the interview process like?',
                    'How are interns selected?',
                    'What should I expect in interviews?'
                ],
                'answers': [
                    'The selection process typically includes resume screening, phone/video interviews, and sometimes technical assessments or case studies. Larger companies may have multiple interview rounds.',
                    'Interviews often focus on technical skills, problem-solving abilities, cultural fit, and motivation. Prepare for behavioral questions using the STAR method (Situation, Task, Action, Result).',
                    'Technical interviews may include coding challenges, system design questions, or field-specific problems. Practice common interview questions and research the company thoroughly.'
                ]
            },
            'program_details': {
                'questions': [
                    'What will I do as an intern?',
                    'What kind of projects do interns work on?',
                    'Will I have a mentor?'
                ],
                'answers': [
                    'Interns typically work on real projects that contribute to the company\'s goals. This might include software development, research, marketing campaigns, data analysis, or supporting ongoing initiatives.',
                    'Most structured internship programs provide mentorship, either through a dedicated mentor or supervisor. Mentors help with professional development, project guidance, and career advice.',
                    'Good internship programs include orientation, training sessions, networking events, and opportunities to present your work. Some also offer rotations through different departments.'
                ]
            },
            'company_culture': {
                'questions': [
                    'What is the work environment like?',
                    'What should I wear?',
                    'How do I fit into company culture?'
                ],
                'answers': [
                    'Work environments vary greatly. Tech companies often have casual cultures with flexible hours, while finance or law firms may be more formal. Research the company culture beforehand.',
                    'Dress codes range from casual to business formal. When in doubt, err on the side of being slightly overdressed, especially for your first day. Ask your recruiter or manager for guidance.',
                    'Be observant, ask questions, participate in team activities, and be open to learning. Show enthusiasm, take initiative, and build relationships with colleagues and other interns.'
                ]
            },
            'preparation': {
                'questions': [
                    'How should I prepare for an internship?',
                    'What skills should I develop?',
                    'How can I make a good impression?'
                ],
                'answers': [
                    'Before starting, research the company, industry, and your role. Review relevant technical skills, prepare questions, and set learning goals for your internship experience.',
                    'Focus on both technical and soft skills. Practice communication, time management, and collaboration. For technical roles, brush up on relevant programming languages, tools, or methodologies.',
                    'Show up with a positive attitude, be proactive, ask thoughtful questions, and seek feedback regularly. Take notes, meet deadlines, and look for ways to add value beyond your assigned tasks.'
                ]
            },
            'general_info': {
                'questions': [
                    'What are the benefits of doing an internship?',
                    'How do internships help my career?',
                    'Should I do multiple internships?'
                ],
                'answers': [
                    'Internships provide real-world experience, help you explore career paths, build professional networks, and often lead to full-time job offers. They bridge the gap between academic learning and professional work.',
                    'Multiple internships can be valuable, especially if they\'re in different areas or companies. This helps you compare industries, build diverse skills, and expand your professional network.',
                    'Internships also help you develop professional skills, understand workplace dynamics, and make informed career decisions. Many employers prefer candidates with internship experience.'
                ]
            },
            'greeting': {
                'questions': ['Hello', 'Hi', 'Hey'],
                'answers': [
                    'Hello! I\'m here to help you with internship-related questions. Feel free to ask about application processes, requirements, timelines, or any other internship topics!',
                    'Hi there! I\'m your internship advisor chatbot. I can help you with questions about finding, applying for, and succeeding in internships. What would you like to know?'
                ]
            },
            'goodbye': {
                'questions': ['Bye', 'Goodbye', 'Thanks'],
                'answers': [
                    'Goodbye! Best of luck with your internship search. Feel free to come back anytime you have more questions!',
                    'Thank you for chatting! I hope I was helpful. Good luck with your internship applications and career journey!'
                ]
            }
        }
    
    def get_faq_by_intent(self, intent):
        """
        Get relevant FAQ information for a given intent
        """
        if intent in self.faq_data:
            faq = self.faq_data[intent]
            return f"Common questions: {', '.join(faq['questions'][:2])}\n\nKey information: {faq['answers'][0]}"
        else:
            return "I can help with questions about internship applications, requirements, timelines, compensation, and more!"
    
    def search_faqs(self, query):
        """
        Search for relevant FAQs based on query
        """
        query_lower = query.lower()
        relevant_faqs = []
        
        for intent, data in self.faq_data.items():
            for question in data['questions']:
                if any(word in question.lower() for word in query_lower.split()):
                    relevant_faqs.append({
                        'intent': intent,
                        'question': question,
                        'answer': data['answers'][0]
                    })
        
        return relevant_faqs[:3]  # Return top 3 matches
