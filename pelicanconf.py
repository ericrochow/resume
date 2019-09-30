#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = "Eric Rochow"
SITENAME = "Eric Rochow Resume"
SITEURL = "http://127.0.0.1:8000"
# SITEURL = "https://resume.ericroc.how"
UPDATED_DATE = datetime.now().strftime("%B %d, %Y")

PATH = "content"

TIMEZONE = "America/Detroit"

DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# THEME = "resume"
THEME = "themes/resume"

# Blogroll
LINKS = (("Website", "https://ericroc.how"),)

# Social widget
# SOCIAL = (
# ("You can add links in your config file", "#"),
# ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Profile information
NAME = AUTHOR
TAGLINE = "Network Reliability Engineer"
PIC = "images/face.png"

STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Sidebar links
EMAIL = "ericrochow@gmail.com"
PHONE = ""
WEBSITE = "ericroc.how"
LINKEDIN = "erochow"
GITHUB = "ericrochow"
TWITTER = "@eric_rochow"

CAREER_SUMMARY = (
    "I like networks. I like Linux. I like building and integrating tools to"
    " augement the operations of both. I hate buzzwords like SDN and Intent-based."
    " I like it when things work. I don't like it when things don't work. I"
    " <i>really</i> don't like when things work and noone knows why they work. I"
    " like learning what makes things tick, and I like working with people"
    " that do too."
)

SKILLS = sorted(
    [
        {"title": "OSPF", "level": "90"},
        {"title": "BGP", "level": "80"},
        {"title": "STP :(", "level": "90"},
        {"title": "Python", "level": "60"},
        {"title": "Linux", "level": 80},
        {"title": "Ansible", "level": "60"},
        {"title": "BASH", "level": "40"},
        {"title": "Docker", "level": "40"},
        {"title": "LXD", "level": "55"},
        {"title": "git", "level": "70"},
        {"title": "IOS-XR", "level": "65"},
        {"title": "NX-OS", "level": "80"},
        {"title": "JunOS", "level": "55"},
        {"title": "FortiOS", "level": "30"},
        {"title": "PANOS", "level": "40"},
    ],
    key=lambda skill: int(skill["level"]),
    reverse=True,
)
PROJECT_INTRO = ""

SIDE_PROJECTS = [
    {
        "title": "ScrAPI",
        "tagline": "A personal tool to collect data about myself from various"
        " APIs and store them centrally to graph trends over time.",
    },
    {"title": "Archibald", "tagline": "My personal Slack butler."},
    {"title": "ssslack", "tagline": "An API wrapper around Slack's WebAPI."},
    {
        "title": "sdnify",
        "tagline": "Tool to query various network operating systems and return"
        " the results in a consistent model. More for my own personal fun than"
        " being anything useful due to more mature (read: better) projects"
        " such as nornir or NAPALM.",
    },
]

PERSONAL_INTERESTS = [
    "Health and Wellness",
    "Home Automation",
    "Lawncare",
    "Liverpool FC",
    "Running",
    "Science Fiction Novels",
]

TECHNICAL_INTERESTS = [
    "Containerization",
    "Routing",
    "Slack Integration/ChatOps",
]

PREFERENCES = {
    "OS": "Ubuntu 18.04",
    "EDITOR": "vim",
    "TERMINAL": "Tilix",
    "COLOR_THEME": "Solarized",
    "CODE_COMPLETION": "kite",
    "CODE_STYLE": "black",
    "LANGUAGE": "Python 3",
    "TEST_SUITES": ["pytest", "flake8", "Bandit"],
    "PRONOUNS": "he/him",
}

EXPERIENCES = [
    {
        "job_title": "Network Engineer",
        "time": "July 2015 - Present",
        "company": "Liquid Web, Lansing, MI",
        "company_summary": "Provider of dedicated, VPS, and  managed"
        " application hosting solutions.",
        "job_summary": "Report to the Director of Network and Security Operations;"
        " serve as a key member on a team of 10 IT and networking"
        " professionals. Manage three ASNs (AS32244, AS53824, AS201682) for"
        " accessibility internally and for ~40K global customers. Direct"
        "projects of variable size and complexity, either as a sole "
        "contributor or team leader.",
        "details": [
            "<b>Configured, optimized, and maintained</b> network devices including"
            " Cisco routers (IOS-XR), Cisco Nexus switches (NX-OS), and "
            " legacy Cisco switching platforms (IOS), along with Cisco and"
            " Palo Alto firewalls.",
            "<b>Developed Python code</b> with flake8 linting; performed testing in"
            " pytest and Bandit. Maintained version control through Git."
            " Implementations varied between vanilla virtualenv installs to"
            " containerized deployments.",
            "<b>Proactively researched emerging trends</b> in networking, to develop"
            " an in-depth understanding of the interactions among different"
            " network applications and designed risk mitigation strategies for"
            " averting conflicts and potential downtime.",
            "<b>Automated notifications and workflow processes</b> with"
            " ChatOps Slack bot tied in to various internal and external APIs."
            "Delivered results that reduced individual task times as much as"
            " 80±% and empowered fellow employees to focus on what's"
            " important.",
            "<b>Achieved double-digit labor reduction percentages</b> in management"
            " of network team server environments, with Ansible implementations.",
            "<b>Managed data center end of life (EOL) refreshes.</b> Evaluated"
            " hardware platform capabilities, HVAC and power requirements,"
            " vendors, and pricing. Drafted budgets and detailed execution plans.",
            "<b>Leveraged communications skills</b> in developing and facilitating"
            " ongoing classroom training on networking topics such as"
            " troubleshooting on Linux, DDoS mitigation tools, strategies, and others.",
        ],
        "highlights": [
            "<b>Successfully completed assigned tasks</b>, meeting a time-critical"
            " requirement in a $500K forklift overhaul of core infrastructure,"
            " for the company’s largest region, with zero customer downtime.",
            "Crafted a flawless migration to a spine-and-leaf FabricPath"
            " architecture that provided a significant reduction in developer"
            " cycles, while allowing customers to upgrade, downgrade, or"
            " otherwise migrate their VPS, without their IP address changing.",
            "<b>Overhauled DDoS mitigation abilities</b> with implementation of"
            " Layer 3 inter-VRF routing, a software upgrade, addition of a"
            " redundant in-line software vendor, and a cloud mitigation"
            " scrubbing center, able to withstand over 100Gs of attack bandwidth.",
            "<b>Slashed expenditures</b> - went from 67.5% to 80% discounts off"
            " list for hardware with other concessions that included training"
            " credits and better RMA options. Obtained unlimited use of"
            " cloud-based DDoS scrubbing for less than the original 12-use/yr. proposal.",
        ],
    },
    {
        "job_title": "Network Engineer",
        "time": "October 2011 - July 2015",
        "company": "Spartan-Net, East Lansing, MI",
        "company_summary": "Privately-owned Internet and managed services provider.",
        "job_summary": "Managed an explosive growth within tenure with a 50%"
        " expansion of residential customers and facilitated the growth of the"
        " new Enterprise Services portfolio. Developed improved business"
        " processes and deployed new networking platforms/devices"
        " that ensured network reliability, scalability, performance, and"
        " sustainability for both wired and wireless networks.",
        "details": [
            "Drove all aspects of support for Cisco, Juniper, and"
            " Alcatel Lucent switched Ethernet networks, along with"
            " GPON networks using the Alcatel Lucent ISAM platform."
            " Maintained Ubuntu Linux DNS, DHCP, Apache, MySQL,"
            " and monitoring servers.",
            "Developed configuration-generating scripts using Python with"
            " Jinja2 for templates for IOS and Junos platforms,"
            " speeding up deployment, while reducing initial errors.",
            "Negotiated an additional 15&#37; in pricing discounts for Juniper"
            " products, going from 45&#37; from 60%.",
        ],
        # "highlights": [],
    },
    {
        "job_title": "IT Contractor",
        "time": "2009 - 2011",
        "company": "TEKSystems, West Michigan",
        "company_summary": "Talent-management firm specializing in technology"
        " solutions.",
        "job_summary": "Contract jobs during college ranging from one-day jobs"
        " installing point-of-sale (POS) systems to multi-month engagements"
        " offering helpdesk support.",
        # "details": [],
        # "highlights": [],
    },
]

EDUCATION_HISTORY = [
    {
        "degree": "B.S. in Computer Networking",
        "meta": "Davenport University",
        "time": "2011",
    },
    {
        "degree": "High School",
        "meta": "Lansing Christian School",
        "time": "2006",
    },
]

CERTIFICATIONS = [
    {
        "cert": "CCNP",
        "meta": "Cisco Certified Network Professional",
        "time": "2017 - Present",
        "progress": "100",
        "valid": True,
    },
    {
        "cert": "CCNA",
        "meta": "Cisco Certified Network Associate",
        "time": "2011 - Present",
        "progress": "100",
        "valid": True,
    },
    {
        "cert": "CCDA",
        "meta": "Cisco Certified Network Associate",
        "time": "2019 - Present",
        "progress": "100",
        "valid": True,
    },
    {
        "cert": "IPv6 Sage",
        "meta": "Hurricane Electric IPv6 Certification",
        "time": "2015 - Present",
        "progress": "100",
        "valid": True,
    },
    {
        "cert": "CCDP",
        "meta": "Cisco Certified Design Professional",
        "time": "In Progress",
        "progress": "75",
        "valid": False,
    },
    {
        "cert": "CCIE",
        "meta": "Cisco Certified Internetwork Expert",
        "time": "In Progress",
        "progress": "10",
        "valid": False,
    },
    {
        "cert": "RHCSA",
        "meta": "Red Hat Certified System Administrator",
        "time": "2015 - 2018",
        "progress": "100",
        "valid": False,
    },
    {
        "cert": "Network+",
        "meta": "CompTIA Network+",
        "time": "2011 - 2014",
        "progress": "100",
        "valid": False,
    },
]

COMPITENCIES = [
    "Rapid Issue Resolution",
    "Automation",
    "Integration",
    "Project Management",
    "Vendor Management",
    "Training",
]
