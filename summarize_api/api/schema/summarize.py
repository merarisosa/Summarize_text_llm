from pydantic import BaseModel
from enum import Enum
from templates.meetings.user import template_user_meeting_summary
from templates.meetings.system import template_system_meeting_summary
from templates.papers.user import template_user_papers_summary
from templates.papers.system import template_system_papers_summary
from templates.general.user import template_user_general_summary
from templates.general.system import template_system_general_summary
from templates.emails.user import template_user_emails
from templates.emails.system import template_system_emails

# Enum para los tipos de templates de resumir
class TemplateType(Enum):
    REUNIONES = "Reuniones"
    EMAILS = "Correos"
    PAPERS = "Papers"
    GENERAL = "General"
    
# Modelo para plain text
class TextSummary(BaseModel):
    text: str
    type_template: TemplateType 

# Diccionario para mapear los templates de users a sus funciones
TEMPLATE_USER_FUNCTIONS = {
    TemplateType.REUNIONES: template_user_meeting_summary,
    TemplateType.PAPERS: template_user_papers_summary,
    TemplateType.GENERAL: template_user_general_summary,
    TemplateType.EMAILS: template_user_emails,
}

# Diccionario para mapear los templates de system a sus funciones
TEMPLATE_SYSTEM_FUNCTIONS = {
    TemplateType.REUNIONES: template_system_meeting_summary,
    TemplateType.PAPERS: template_system_papers_summary,
    TemplateType.GENERAL: template_system_general_summary,
    TemplateType.EMAILS: template_system_emails,
}


