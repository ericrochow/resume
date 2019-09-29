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

CAREER_SUMMARY = ""

SKILLS = [
    {"title": "OSPF", "level": "90"},
    {"title": "BGP", "level": "80"},
    {"title": "STP :(", "level": "90"},
    {"title": "Python", "level": "60"},
    {"title": "Linux", "level": 80},
    {"title": "Ansible", "level": "60"},
    {"title": "BASH", "level": "40"},
    {"title": "Docker", "level": "40"},
    {"title": "LXD", "level": "55"},
]

PROJECT_INTRO = ""

SIDE_PROJECTS = [
    {
        "title": "ScrAPI",
        "tagline": "A personal tool to collect data about myself from various"
        " APIs and store them centrally to graph trends over time.",
    },
    {"title": "Archibald", "tagline": "My personal Slack butler."},
    {
        "title": "sdnify",
        "tagline": "Tool to query various network operating systems and return"
        " the results in a consistent model. More for my own personal fun than"
        " being anything useful due to more mature (better) projects such as"
        " nornir or NAPALM.",
    },
]

INTERESTS = [
    "Health and Wellness" "Home Automation",
    "Lawncare",
    "Liverpool FC",
    "Running",
    "Science Fiction Novels",
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
        "Company": "Liquid Web, Lansing, MI",
        "details": "",
        "highlights": [
            "Did the thing",
            "Crushed it",
            "Knocked it out of the park",
        ],
    },
    {
        "job_title": "Network Engineer",
        "time": "October 2011 - July 2015",
        "company": "Spartan-Net, East Lansing, MI",
        "details": "description goes here",
        "highlights": [],
    },
    {
        "job_title": "IT Contractor",
        "time": "2009 - 2011",
        "company": "TEK Systems, West Michigan",
        "details": "",
    },
]

EDUCATION_HISTORY = [
    {
        "degree": "B.S. in Computer Networking",
        "meta": "Davenport University",
        "time": "2011",
    },
    {"degree": "High School", "meta": "Lansing Christian", "time": "2006"},
]

CERTIFICATIONS = [
    {
        "cert": "CCNP",
        "meta": "Cisco Certified Network Professional",
        "date": "2017 - Present",
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
