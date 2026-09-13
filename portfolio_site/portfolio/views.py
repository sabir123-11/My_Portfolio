import os

from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect

# ---------------------------------------------------------------------------
# All portfolio content lives in this one place. Sabir, if your details ever
# change (new project, new certificate, updated CGPA...) this is the only
# file you need to edit -- the template just loops over these lists.
# ---------------------------------------------------------------------------

PROFILE = {
    "name": "Sk Sabir Raja",
    "role": "Backend-focused Full-Stack Developer",
    "tagline": "I build Django-powered web apps, from the database schema to the last pixel of CSS.",
    "location": "Jajpur, Odisha, India",
    "email": "razasksabir@gmail.com",
    "phone": "+91 73270 59507",
    "linkedin": "https://www.linkedin.com/in/shaikh-sabir-raja",
    "linkedin_label": "shaikh-sabir-raja",
    "github": "https://github.com/sabir-raja",
    "github_label": "sabir-raja",
    "about": (
        "I'm a computer science engineering student at DRIEMS University, Tangi, "
        "currently interning as a Fullstack Developer. I like turning a blank "
        "models.py into a working product: appointment systems, real-time "
        "meeting apps, task managers, REST APIs -- if it needs a backend and a "
        "clean UI in front of it, I want to build it. Off the field, I've been "
        "part of the Smart India Hackathon as a backend developer, and I keep a "
        "running list of AI tools I use daily to ship faster."
    ),
}

EDUCATION = [
    {
        "school": "DRIEMS University, Tangi",
        "degree": "B.Tech, Computer Science Engineering",
        "meta": "CGPA 8.35",
        "period": "Aug 2023 -- July 2027",
        "location": "Odisha, India",
    },
    {
        "school": "Gurukul Kalinga Residential College",
        "degree": "Intermediate (10+2)",
        "meta": "62%",
        "period": "Sep 2020 -- July 2022",
        "location": "Odisha, India",
    },
]

COURSEWORK = [
    "Data Structures & Algorithms",
    "Operating Systems",
    "Database Management Systems (DBMS)",
    "Object-Oriented Programming",
]

SKILLS = {
    "Languages": ["Python", "Java", "JavaScript", "SQL", "HTML", "CSS",],
    "Frameworks & Tools": [
        "Django", "Django REST Framework", "React", "Node.js", "Express.js",
        "Bootstrap", "NumPy", "Pandas", "Matplotlib",
    ],
    "Developer Tools": ["VS Code", "Android Studio", "Git", "MySQL", "SQLite"],
    "AI Tools": ["ChatGPT", "Claude", "Grok", "Agentic AI", "OpenAI"],
}

EXPERIENCE = [

    {
        "role": "Fullstack Developer Intern",
        "org": "CodeDais Software Pvt. Ltd.",
        "location": "Bhubaneswar, India",
        "period": "Jun 2026 -- Jul 2026",
        "points": [
            "Built and maintained web applications end-to-end using Django and Python.",
            "Collaborated with the development team on responsive websites and backend functionality.",
            "Integrated databases, fixed application bugs, and tested features before release.",
            "Picked up real-world habits: version control, debugging, and shipping production code.",
        ],
    },
]

PROJECTS = [
    {
        "slug": "meeting-app",
        "name": "Meeting Website -- Video Conferencing App",
        "tag": "Real-time",
        "period": "Jan 2026",
        "stack": ["React", "HTML", "CSS", "JavaScript", "WebRTC", "Socket.io"],
        "description": (
            "A Zoom-style video conferencing app built with React. People can create "
            "or join a meeting room and talk over live video and audio, with "
            "mic/camera controls handled through reusable React components."
        ),
        "highlights": [
            "Peer-to-peer video and audio using WebRTC, signalled over Socket.io",
            "Create-or-join meeting room flow with a clean, focused interface",
            "Mic and camera toggle controls built as reusable components",
            "Responsive layout that holds up across devices",
        ],
        "accent": "violet",
        # Drop a screenshot at portfolio/static/portfolio/img/projects/meeting-app.jpg
        # and it will replace the placeholder tile automatically.
        "screenshot": "",
        "github": "",   # e.g. "https://github.com/sabir-raja/meeting-app"
        "live": "",     # e.g. "https://your-live-demo-link.com"
    },
    {
        "slug": "hospital-management",
        "name": "Hospital Management System",
        "tag": "Full-stack",
        "period": "Jul 2026",
        "stack": ["Django", "Python", "HTML", "CSS", "JavaScript", "Bootstrap", "MySQL"],
        "description": (
            "A full hospital operations platform: patients can book appointments, "
            "browse services and doctors, message the hospital, and get instant "
            "answers from an AI chatbot -- all backed by a proper Django data model."
        ),
        "highlights": [
            "Appointment booking with department, date, time and status tracking",
            "Patient profiles built on Django's auth system",
            "Contact-message and career-application inboxes for staff",
            "An AI chatbot with its own conversation log for instant support",
        ],
        "accent": "teal",
        "screenshot": "",
        "github": "",
        "live": "",
    },
    {
        "slug": "cricket-academy",
        "name": "Cricket Academy Website",
        "tag": "Django",
        "period": "2026",
        "stack": ["Django", "Python", "HTML", "CSS", "Bootstrap"],
        "description": (
            "A multi-page marketing site for a cricket coaching academy -- home, "
            "about, facilities, gallery, events and contact -- built as a clean "
            "Django app with named URL routes for every page."
        ),
        "highlights": [
            "Home, About, Facilities, Gallery, Events and Contact pages",
            "Django views mapped to clearly named URL patterns",
            "Structured as a reusable template app for similar academy/club sites",
        ],
        "accent": "amber",
        "screenshot": "",
        "github": "",
        "live": "",
    },
    {
        "slug": "task-management",
        "name": "Task Management App",
        "tag": "CRUD",
        "period": "2026",
        "stack": ["Django", "Python", "SQLite", "HTML", "CSS"],
        "description": (
            "A to-do list app that goes beyond add/delete: tasks can be marked "
            "done, undone, edited in place, or bulk-cleared, with live counts of "
            "completed vs. pending work."
        ),
        "highlights": [
            "Full CRUD -- create, edit, complete, undo, delete, per task",
            "Bulk actions: clear completed, delete pending, remove all",
            "Live dashboard counts of total, completed and pending tasks",
        ],
        "accent": "rose",
        "screenshot": "",
        "github": "",
        "live": "",
    },
    {
        "slug": "student-api",
        "name": "Student REST API",
        "tag": "API",
        "period": "2026",
        "stack": ["Django", "Django REST Framework", "SQLite"],
        "description": (
            "A clean Django REST Framework API for managing student records -- "
            "built to practice serializers, viewsets and the full range of HTTP "
            "verbs a real front end would need."
        ),
        "highlights": [
            "GET / POST /api/students/ and GET / PUT / PATCH / DELETE /api/students/<id>/",
            "ModelSerializer-based validation with clear error responses",
            "Documented endpoints so any frontend (or Postman) can plug straight in",
        ],
        "accent": "blue",
        "screenshot": "",
        "github": "",
        "live": "",
    },
]

CERTIFICATIONS = [
    {
        "title": "Full Stack Python Development -- Summer Internship",
        "issuer": "CodeDais Software and Research Pvt. Ltd.",
        "meta": "1 Jun 2026 -- 30 Jul 2026 · Certificate No. CDSR/INT/SI/0056",
        "image": "portfolio/img/certificates/codedais-internship.jpg",
    },
    {
        "title": "Web Development Certification",
        "issuer": "Apna College",
        "meta": "",
        "image": "portfolio/img/certificates/webdevelopment.jpg",
    },
    {
        "title": "Python -- Industrial Training",
        "issuer": "Central Tool Room & Training Centre, Bhubaneswar (Govt. of India, Ministry of MSME)",
        "meta": "16 Jun 2025 -- 15 Jul 2025 · Roll No. BBST202506001553",
        "image": "portfolio/img/certificates/cttc-python.jpg",
    },
]

ACHIEVEMENTS = [
    {
        "title": "DRIEMS Internal Hackathon -- Smart India Hackathon 2025",
        "role": "Participant, Software Category",
        "period": "13 Sep 2025",
        "location": "DRIEMS University, Tangi",
        "description": (
            "Participated in the DRIEMS Internal Hackathon under Smart India Hackathon "
            "2025, organised by the Institution's Innovation Council, collaborating "
            "with a team to build an impactful software solution. Received a "
            "Certificate of Participation."
        ),
        "image": "portfolio/img/certificates/sih-hackathon.jpg",
    },
]

NAV_SECTIONS = [
    ("home", "Home"),
    ("about", "About"),
    ("education", "Education"),
    ("skills", "Skills"),
    ("projects", "Projects"),
    ("experience", "Experience"),
    ("certifications", "Certifications"),
    ("achievements", "Achievements"),
    ("resume", "Resume"),
    ("contact", "Contact"),
]


def home(request):
    context = {
        "profile": PROFILE,
        "education": EDUCATION,
        "coursework": COURSEWORK,
        "skills": SKILLS,
        "experience": EXPERIENCE,
        "projects": PROJECTS,
        "certifications": CERTIFICATIONS,
        "achievements": ACHIEVEMENTS,
        "nav_sections": NAV_SECTIONS,
    }
    return render(request, "portfolio/index.html", context)


def contact_submit(request):
    """Handle the contact form. No email server configured yet, so the
    message is simply logged to the console via Django's messages framework
    and the console email backend -- swap EMAIL_BACKEND in settings.py once
    you have real SMTP credentials to actually receive these by email."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message_text = request.POST.get("message", "").strip()

        if name and email and message_text:
            print(f"[Portfolio contact form] {name} <{email}>: {message_text}")
            messages.success(
                request,
                "Thanks! Your message has been received -- I'll get back to you soon.",
            )
        else:
            messages.error(request, "Please fill in every field before sending.")

    return redirect("/#contact")


def download_resume(request):
    resume_path = os.path.join(
        settings.BASE_DIR, "portfolio", "static", "portfolio", "resume", "Sk_Sabir_Raja_Resume.pdf"
    )
    if not os.path.exists(resume_path):
        raise Http404("Resume file not found.")
    return FileResponse(
        open(resume_path, "rb"),
        content_type="application/pdf",
        as_attachment=False,
        filename="Sk_Sabir_Raja_Resume.pdf",
    )
