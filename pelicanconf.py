#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Eric Rochow"
SITENAME = "Eric Rochow Resume"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Detroit"

DEFAULT_LANG = "en"

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
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Profile information
NAME = AUTHOR
TAGLINE = ""
PIC = ""

# Sidebar links
EMAIL = "ericrochow@gmail.com"
PHONE = ""
WEBSITE = "ericroc.how"
LINKEDIN = "erochow"
GITHUB = "ericrochow"
TWITTER = "@eric_rochow"

CAREER_SUMMARY = ""

SKILLS = [{"title": "", "level": "90"}]

PROJECT_INTRO = ""

SIDE_PROJECTS = [{"title": "", "tagline": ""}]

INTERESTS = [
    "Home Automation",
    "Lawncare",
    "Liverpool FC",
    "Science Fiction Novels",
]

EXPERIENCES = [
    {
        "job_title": "Network Engineer",
        "time": "July 2015 - Present",
        "Company": "Liquid Web",
        "details": "",
    },
    {
        "job_title": "Network Engineer",
        "time": "October 2011 - July 2015",
        "company": "Spartan-Net, East Lansing, MI",
        "details": "description goes here",
    },
]

EDUCATIONS = [
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
    },
    {
        "cert": "CCNA",
        "meta": "Cisco Certified Network Associate",
        "time": "2011 - Present",
    },
    {
        "cert": "CCDA",
        "meta": "Cisco Certified Network Associate",
        "time": "2019 - Present",
    },
]
