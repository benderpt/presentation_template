import streamlit as st
import json

def page1():
    return {"link": "frontend/app/pages/home.py", "title": "Home", "short_title": "Home", "icon": ":material/home:"}

def page2():
    return {"link": "frontend/app/pages/media.py", "title": "Media", "short_title": "Media", "icon": ":material/newspaper:"}

def page3():
    return {"link": "frontend/app/pages/website.py", "title": "Website", "short_title": "Website", "icon": ":material/web_asset:"}

def page4():
    return {"link": "frontend/app/pages/linkedin.py", "title": "Linkedin", "short_title": "Linkedin", "icon": ":material/magnification_small:"}

def page5():
    return {"link": "frontend/app/pages/projects_dash.py", "title": "Projetos", "short_title": "Projetos", "icon": ":material/rocket_launch:"}

def page6():
    return {"link": "frontend/app/pages/events.py", "title": "Eventos", "short_title": "Eventos", "icon": ":material/local_activity:"} 

def page7():
    return {"link": "frontend/app/pages/projects_admin.py", "title": "Projetos ADMIN", "short_title": "Projetos ADMIN", "icon": ":material/bookmark_manager:"} 

def create_navigation():
    pages = [page1(), page2(), page3(), page4(), page5(), page6(), page7()]
    return st.navigation([st.Page(page["link"], title=page["title"], icon=page["icon"]) for page in pages])