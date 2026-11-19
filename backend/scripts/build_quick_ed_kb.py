"""Regenerate the Quick Ed Solutions knowledge base from the public website content.

Source of truth: C:\\Users\\akash\\OneDrive\\Desktop\\quick-ed-demo\\src\\components
Only facts visible on the website are written here. Fees, batch dates, class
timings, refund terms and placement statistics are explicitly marked as not
published instead of being invented.
"""
from pathlib import Path

from openpyxl import Workbook

OUT = Path(__file__).resolve().parent.parent / "QuickEd_Knowledge_Base"

CONTACT = "admissions@quickedsolutions.com or +91 83748 52001"


def write(name, sheet, headers, rows, widths=None):
    wb = Workbook()
    ws = wb.active
    ws.title = sheet
    ws.append(headers)
    for r in rows:
        ws.append(r)
    if widths:
        for col, w in zip("ABCDEFGHIJ", widths):
            ws.column_dimensions[col].width = w
    wb.save(OUT / name)


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    write(
        "01_Company_Profile.xlsx",
        "Company",
        ["Field", "Value"],
        [
            ["Company Name", "Quick Ed Solutions"],
            ["Type", "Corporate tech training and placement agency"],
            ["Motto", "Learn. Build. Succeed."],
            ["Headline", "Engineering Elite Careers With Quick-Ed Solutions"],
            ["Mission", "Get industry-relevant skills, hands-on projects and expert guidance to help learners grow in their career and achieve their goals."],
            ["Training Areas", "Full Stack Python, Full Stack Java, Cybersecurity, AI & GenAI, Software Testing"],
            ["Founder", "Suhas Nagulapalli"],
            ["Founder Role", "Founder & Chief Mentor (HR, Marketing, Entrepreneur)"],
            ["Founder Message", "Stop consuming tutorials. Start engineering real systems. The industry pays for the systems you can build, the bugs you can solve under pressure and the ownership you bring to the team."],
            ["Admissions Email", "admissions@quickedsolutions.com"],
            ["Admissions Phone", "+91 83748 52001"],
            ["WhatsApp", "+91 83748 52001"],
            ["Address", "No street address is published on the website. Contact admissions for the current location."],
            ["Support", "Admissions and academic counseling team. Email support states a reply within 15 minutes."],
        ],
        [22, 110],
    )

    write(
        "02_Course_Catalogue.xlsx",
        "Courses",
        ["Course Name", "Category", "Badge", "Duration", "Level", "Projects", "Tagline", "Core Skills", "Key Highlights", "Fees"],
        [
            [
                "Java Full Stack Development",
                "Full Stack",
                "Bestseller",
                "16 Weeks",
                "Beginner to Advanced",
                "8 Enterprise Projects",
                "Enterprise-grade Java backend paired with high-performance React frontend.",
                "Core Java, Spring Boot, Microservices, React.js, Hibernate, RESTful APIs, MySQL, Docker, AWS",
                "End-to-end enterprise microservices architecture; Spring Security with JWT & OAuth2; frontend state management with Redux Toolkit; CI/CD deployment pipelines on AWS Cloud",
                "On request - contact admissions",
            ],
            [
                "Python Full Stack Development",
                "Full Stack",
                "High Demand",
                "14 Weeks",
                "All Levels",
                "6+ Production Apps",
                "Build ultra-fast modern web applications and scalable data backends.",
                "Python 3, Django, FastAPI, Next.js, PostgreSQL, Redis, Tailwind CSS, Docker",
                "Async microservices using FastAPI & Pydantic; modern SSR web apps with Next.js & React; database optimization with PostgreSQL & Redis caching; automated testing with PyTest & GitHub Actions",
                "On request - contact admissions",
            ],
            [
                "GenAI & Large Language Models",
                "AI",
                "Trending #1",
                "10 Weeks",
                "Intermediate",
                "5 Production AI Deployments",
                "Master Generative AI, Retrieval Augmented Generation (RAG) and Autonomous Agents.",
                "LLMs, Prompt Engineering, LangChain, LlamaIndex, RAG Pipelines, Vector DBs (Pinecone), OpenAI APIs, Fine-Tuning",
                "Building enterprise context-aware RAG systems; multi-agent collaboration with LangGraph & CrewAI; vector embeddings & semantic search optimization; custom fine-tuning of open-source models (Llama 3)",
                "On request - contact admissions",
            ],
            [
                "Cybersecurity & Ethical Hacking",
                "Cybersecurity",
                "Career Accelerator",
                "12 Weeks",
                "Beginner to Advanced",
                "12 Hands-on Virtual Labs",
                "Protect digital assets, analyze live threats and master offensive security techniques.",
                "Kali Linux, Network Defense, Penetration Testing, Wireshark, Metasploit, OWASP Top 10, SOC Analysis, SIEM",
                "Real-world offensive penetration testing in isolated cyber ranges; vulnerability assessment & exploit development basics; web application security auditing (OWASP standards); incident response, log forensics & SIEM setup",
                "On request - contact admissions",
            ],
            [
                "Software Testing & QA Automation",
                "Testing",
                "Job Ready",
                "10 Weeks",
                "Beginner Friendly",
                "4 Real Automation Suites",
                "Master automation frameworks with Playwright, Selenium and CI/CD test pipelines.",
                "Manual Testing, Selenium WebDriver, Playwright, Postman API Testing, RestAssured, JUnit/TestNG, JIRA, Jenkins",
                "Modern web automation with Playwright & TypeScript/Java; comprehensive REST API testing & automation with Postman; test design patterns such as Page Object Model (POM); continuous testing integration inside Jenkins CI/CD pipelines",
                "On request - contact admissions",
            ],
        ],
        [34, 14, 18, 12, 20, 26, 60, 60, 80, 30],
    )

    write(
        "03_Trainer_Details.xlsx",
        "Trainers",
        ["Trainer Name", "Role", "Specialty", "Mentored", "Bio"],
        [
            [
                "Sri Hari Chilumuri",
                "Java Developer | Frontend & Backend Development",
                "Java, HTML5, CSS3, JavaScript, React.js & SQL",
                "430+ Engineers",
                "Computer Science graduate with a strong foundation in Java programming, frontend development and database management. Focused on building responsive web applications, developing practical software solutions and continuously strengthening technical skills.",
            ],
            [
                "Akash Katam",
                "GenAI & Python Full-Stack Developer",
                "Generative AI, LLMs, Prompt Engineering, Python, Django, FastAPI, REST APIs & Full-Stack Development",
                "380+ Engineers",
                "Specializes in Generative AI concepts and Python-based application development, with a focus on building intelligent applications, developing backend services and integrating AI capabilities into modern full-stack solutions.",
            ],
            [
                "Karthik Neelagiri",
                "Cybersecurity & Network Security Specialist",
                "Ethical Hacking, Network Security, TCP/IP, Routing & Switching, Linux, SOC Operations & SIEM Tools",
                "310+ Engineers",
                "Focuses on cybersecurity fundamentals and network infrastructure, covering ethical hacking, network defense, Linux security and security monitoring. Emphasizes hands-on lab exercises, practical troubleshooting and real-world security concepts.",
            ],
            [
                "Ameesha Gade",
                "Software Testing & QA Trainer",
                "Manual Testing, Automation Testing, Selenium, Playwright, API Testing, SQL & Test Case Design",
                "390+ Engineers",
                "Focuses on software testing fundamentals and quality assurance practices, covering manual and automation testing, test case design, API validation and defect tracking. Emphasizes practical exercises and hands-on projects to help learners develop industry-relevant testing skills.",
            ],
        ],
        [26, 46, 70, 16, 110],
    )

    write(
        "04_Batch_Schedules.xlsx",
        "Batch Info",
        ["Batch Type", "Status", "Details"],
        [
            ["Upcoming batch dates", "Not published", f"Batch start dates are not published on the website. Contact {CONTACT} to confirm the next batch."],
            ["Class timings", "Not published", f"Daily class timings are not published on the website. Contact {CONTACT} for current timings."],
            ["Weekend batches", "Not published", f"The website does not publish a separate weekend batch schedule. Contact {CONTACT} to check availability."],
            ["Mode of training", "Not published", f"The website does not state whether classes are online or offline. Contact {CONTACT} to confirm."],
        ],
        [26, 16, 100],
    )

    write(
        "05_Fee_Structure.xlsx",
        "Course Fees",
        ["Course", "Fees", "Notes"],
        [
            [course, "On request - contact admissions", f"The website does not publish fees. Contact {CONTACT} for the current fee and payment options."]
            for course in [
                "Java Full Stack Development",
                "Python Full Stack Development",
                "GenAI & Large Language Models",
                "Cybersecurity & Ethical Hacking",
                "Software Testing & QA Automation",
            ]
        ],
        [34, 32, 100],
    )

    write(
        "06_Placement_Support.xlsx",
        "Placement",
        ["Area", "Details"],
        [
            ["Placement support", "Quick Ed Solutions is a corporate tech training and placement agency."],
            ["Mentorship", "1-on-1 senior architect mentorship with weekly code reviews and live debugging sessions."],
            ["Projects", "Learners architect, containerize and deploy production-grade systems and real automation frameworks instead of toy projects."],
            ["Career support", "Industry project guidance, career and interview mentorship, and 1-on-1 code reviews."],
            ["Placement details", f"The course brochure references placement details. Current placement terms and outcomes are shared by admissions at {CONTACT}."],
            ["Placement statistics", "No placement statistics, salary figures or job guarantee are published on the website."],
        ],
        [26, 120],
    )

    write(
        "07_Student_FAQs.xlsx",
        "FAQs",
        ["Question", "Answer"],
        [
            ["What courses does Quick Ed Solutions offer?", "Five flagship programs: Java Full Stack Development (16 weeks), Python Full Stack Development (14 weeks), GenAI & Large Language Models (10 weeks), Cybersecurity & Ethical Hacking (12 weeks) and Software Testing & QA Automation (10 weeks)."],
            ["How do I enroll in a course?", f"Click Enroll Now or Syllabus & Enroll on the course card, or contact admissions at {CONTACT}."],
            ["Can I download a course brochure?", "Yes. Use View Brochure on any course card or View All Brochures in the courses section."],
            ["Who will teach me?", "Programs are taught by Sri Hari Chilumuri (Java and frontend/backend), Akash Katam (GenAI and Python full stack), Karthik Neelagiri (cybersecurity) and Ameesha Gade (software testing and QA automation)."],
            ["Do you provide placement support?", f"Quick Ed Solutions provides placement support and career mentorship, including 1-on-1 code reviews, industry project guidance and interview mentorship. The website does not publish placement statistics or promise a job. Confirm current placement terms with admissions at {CONTACT}."],
            ["What are the course fees?", f"Fees are not published on the website. Contact admissions at {CONTACT} for the current fee and payment options."],
            ["When is the next batch?", f"Batch start dates are not published on the website. Contact admissions at {CONTACT} to confirm the next batch."],
            ["Are classes online or offline?", f"The website does not specify online or offline mode. Contact admissions at {CONTACT} to confirm."],
            ["Do you have weekend batches?", f"The website does not publish a weekend batch schedule. Contact admissions at {CONTACT} to check availability."],
            ["What is the refund policy?", f"No refund or cancellation policy is published on the website. Contact admissions at {CONTACT}."],
            ["Where are you located?", f"No street address is published on the website. Contact admissions at {CONTACT} for the current location."],
            ["Who founded Quick Ed Solutions?", "Suhas Nagulapalli is the Founder & Chief Mentor of Quick Ed Solutions."],
            ["What is Quick Ed Solutions?", "A corporate tech training and placement agency focused on Full Stack Python and Java, Cybersecurity, AI and GenAI, and Software Testing. Its motto is Learn. Build. Succeed."],
            ["What is the motto of Quick Ed Solutions?", "Learn. Build. Succeed."],
            ["What tools and frameworks will I learn?", "Java 21, Python, React.js, OpenAI & LLMs, LangChain, Kali Linux, Wireshark, Playwright, Selenium, and MySQL/Oracle. Each tool maps to a program such as Java Full Stack, Python Full Stack, GenAI, Cybersecurity or Software Testing."],
            ["What does the Quick Ed Solutions website include?", "A home hero, an industry tools showcase, five flagship courses, corporate trainers, a why-choose-us section with the founder's message, a contact strip with call/email/social options, a footer with quick links, brochure downloads and the AI assistant."],
            ["How do I apply for the next batch?", f"Open a course card and choose Syllabus & Enroll or Apply for Next Batch, or contact admissions at {CONTACT}. The site confirms the application and says an advisor will reach out."],
            ["Can I contact you on WhatsApp?", f"Yes. The help panel links to WhatsApp at +91 83748 52001 for instant syllabus and brochure help."],
            ["Do you have social media?", "The website links to LinkedIn, YouTube, Instagram, GitHub and X/Twitter through icons in the contact strip and footer."],
            ["Are there filters on the courses page?", "Yes. Courses can be filtered by All Courses, Full Stack, GenAI, Cybersecurity and Software Testing."],
        ],
        [40, 130],
    )

    write(
        "08_Company_Policies.xlsx",
        "Policies",
        ["Policy", "Details"],
        [
            ["Refund policy", f"Not published on the website. Contact admissions at {CONTACT}."],
            ["Cancellation and rescheduling", f"Not published on the website. Contact admissions at {CONTACT}."],
            ["Attendance policy", f"Not published on the website. Contact admissions at {CONTACT}."],
            ["Certification", f"The website does not publish certificate details. Contact admissions at {CONTACT}."],
            ["Discounts and offers", f"No discounts or offers are published on the website. Contact admissions at {CONTACT} for any current offer."],
            ["Privacy and terms", "The website footer links to Privacy Policy and Terms of Service."],
        ],
        [30, 120],
    )

    write(
        "09_Projects_Details.xlsx",
        "Projects",
        ["Course", "Projects", "Project Highlights"],
        [
            [
                "Java Full Stack Development",
                "8 Enterprise Projects",
                "End-to-end enterprise microservices architecture; Spring Security with JWT & OAuth2; frontend state management with Redux Toolkit; CI/CD deployment pipelines on AWS Cloud",
            ],
            [
                "Python Full Stack Development",
                "6+ Production Apps",
                "Async microservices using FastAPI & Pydantic; modern SSR web apps with Next.js & React; database optimization with PostgreSQL & Redis caching; automated testing with PyTest & GitHub Actions",
            ],
            [
                "GenAI & Large Language Models",
                "5 Production AI Deployments",
                "Enterprise context-aware RAG systems; multi-agent collaboration with LangGraph & CrewAI; vector embeddings & semantic search optimization; custom fine-tuning of open-source models (Llama 3)",
            ],
            [
                "Cybersecurity & Ethical Hacking",
                "12 Hands-on Virtual Labs",
                "Offensive penetration testing in isolated cyber ranges; vulnerability assessment & exploit development basics; web application security auditing (OWASP standards); incident response, log forensics & SIEM setup",
            ],
            [
                "Software Testing & QA Automation",
                "4 Real Automation Suites",
                "Web automation with Playwright & TypeScript/Java; REST API testing & automation with Postman; Page Object Model test design; continuous testing inside Jenkins CI/CD pipelines",
            ],
        ],
        [34, 28, 120],
    )

    write(
        "10_Website_Sections.xlsx",
        "Sections",
        ["Section", "Location", "Contents"],
        [
            ["Home / Hero", "Top of the page", "Headline 'Engineering Elite Careers With Quick-Ed Solutions', mission lead paragraph, motto badge and an Explore Courses button, plus highlight cards for Industry-Focused Curriculum, Hands-On Projects, Expert Mentors and Career Support."],
            ["Navigation", "Top navbar", "Home, Courses (dropdown listing the five programs), Help, About Agency, Trainers and Contact, plus a mobile menu."],
            ["Tools & Frameworks", "Below the navbar", "Scrolling showcase titled 'Industry Tools & Frameworks You Will Command' featuring Java 21, Python, React.js, OpenAI & LLMs, LangChain, Kali Linux, Wireshark, Playwright, Selenium and MySQL/Oracle."],
            ["Courses", "Courses section", "Five flagship programs with filters for All Courses, Full Stack, GenAI, Cybersecurity and Software Testing. Each card shows duration, level, project count, key skills, a View Brochure button and a Syllabus & Enroll button."],
            ["Trainers", "Trainers section", "Corporate faculty carousel with four mentors: Sri Hari Chilumuri, Akash Katam, Karthik Neelagiri and Ameesha Gade."],
            ["Why Quick Ed Solutions", "Why-us section", "Two pillars (production-grade GitHub repositories and 1-on-1 senior architect mentorship) plus the founder's motivational speech by Suhas Nagulapalli."],
            ["Contact", "Contact strip", "Make a Call, Send an Email and Connect on Social cards with the admissions hotline, academic desk email and social icons."],
            ["Footer", "Bottom of the page", "Company mission, quick links (Home, About Agency, Flagship Courses, Corporate Faculty, Why Choose Us), contact details, social icons and Privacy Policy / Terms of Service links."],
            ["Brochure", "Courses section and course cards", "Download Course Brochure modal for the 2026 curriculum with syllabus, project blueprints and hiring company list."],
            ["AI Assistant", "Floating button at bottom right", "A 'Need help? Let's chat' assistant that answers questions about Quick Ed Solutions using the website knowledge base."],
        ],
        [26, 28, 120],
    )

    write(
        "11_Tools_And_Frameworks.xlsx",
        "Tools",
        ["Tool", "Category", "Used In"],
        [
            ["Java 21", "Backend", "Java Full Stack Development"],
            ["Python", "AI & Backend", "Python Full Stack Development, GenAI & LLMs"],
            ["React.js", "Frontend", "Java Full Stack Development, Python Full Stack Development"],
            ["OpenAI & LLMs", "GenAI", "GenAI & Large Language Models"],
            ["LangChain", "AI Agents", "GenAI & Large Language Models"],
            ["Kali Linux", "Security", "Cybersecurity & Ethical Hacking"],
            ["Wireshark", "Cyber", "Cybersecurity & Ethical Hacking"],
            ["Playwright", "Testing", "Software Testing & QA Automation"],
            ["Selenium", "Automation", "Software Testing & QA Automation"],
            ["MySQL, Oracle", "Database", "Java Full Stack Development"],
        ],
        [24, 20, 60],
    )

    write(
        "12_Why_Quick_Ed.xlsx",
        "Why Quick Ed",
        ["Pillar", "Details"],
        [
            ["Production-grade GitHub repositories", "No toy projects: learners architect, containerize and deploy distributed microservices, LLM pipelines and automated test frameworks."],
            ["1-on-1 senior architect mentorship", "Weekly code reviews and live debugging sessions with corporate leads who review pull requests like top engineering teams."],
            ["Industry-focused curriculum", "Programs are engineered for corporate standards and current production engineering skills."],
            ["Hands-on projects", "8 enterprise Java projects, 6+ Python production apps, 5 GenAI deployments, 12 cybersecurity labs and 4 automation suites."],
            ["Expert mentors", "Every mentor is described as a verified senior engineer or architect with industry experience."],
            ["Career support", "Industry project guidance, career and interview mentorship, and 1-on-1 code reviews."],
            ["Positioning", "Traditional colleges teach yesterday's theory; Quick Ed Solutions focuses on today's production engineering skills."],
            ["Founder", "Suhas Nagulapalli, Founder & Chief Mentor (HR, Marketing, Entrepreneur)."],
            ["Founder message", "Stop consuming tutorials. Start engineering real systems. The industry pays for the systems you can build, the bugs you can solve under pressure and the ownership you bring to the team."],
            ["Motto", "Learn. Build. Succeed."],
        ],
        [34, 120],
    )

    write(
        "13_Contact_And_Social.xlsx",
        "Contact",
        ["Channel", "Details"],
        [
            ["Admissions phone", "+91 83748 52001. The site labels it the direct admissions hotline and education helpline."],
            ["Admissions email", "admissions@quickedsolutions.com, labelled the academic desk and admissions email support."],
            ["WhatsApp", "+91 83748 52001. The help panel opens a WhatsApp chat for syllabus and brochure help."],
            ["Call card", "Make a Call - Direct Admissions Hotline, available for inquiries."],
            ["Email card", "Send an Email - Academic Desk. The site advertises an instant response in under 15 minutes."],
            ["Help panel", "Instant Student Support with three channels: contact number, email and WhatsApp."],
            ["Social media", "LinkedIn, YouTube, Instagram, GitHub and X/Twitter icons appear in the contact strip and footer."],
            ["Address", "No street address is published on the website. Contact admissions for the current location."],
        ],
        [24, 120],
    )

    write(
        "14_Brochure_And_Enrollment.xlsx",
        "Enrollment",
        ["Topic", "Details"],
        [
            ["Brochure title", "Download Course Brochure - Official 2026 Curriculum."],
            ["Brochure contents", "Complete day-by-day syllabus, hands-on lab plans, architectural diagrams, capstone project blueprints and a hiring company list."],
            ["Hiring partners", "The brochure advertises a 500+ hiring partners list of MNCs, unicorns and product firms."],
            ["Brochure delivery", "Enter a student email for instant PDF delivery. The site confirms the brochure was downloaded and dispatched."],
            ["Where to find it", "Each course card has a View Brochure button; the courses section also has a View All Brochures action."],
            ["Enrollment", "Click Enroll Now or Syllabus & Enroll on a course card. The site shows that the application is initialized and an advisor will reach out."],
            ["Next batch action", "The syllabus modal has an Apply for Next Batch action."],
            ["Syllabus modal", "Shows the curriculum overview, key architectural highlights and technologies mastered for the selected course."],
        ],
        [26, 120],
    )

    print(f"Wrote {len(list(OUT.glob('*.xlsx')))} knowledge base files to {OUT}")


if __name__ == "__main__":
    main()
