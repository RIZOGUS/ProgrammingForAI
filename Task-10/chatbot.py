import re
from datetime import datetime

class AdmissionChatbot:
    def __init__(self):
        # Knowledge base
        self.programs = {
            "computer science": {
                "requirements": "High school diploma with Mathematics and Physics. Minimum GPA: 3.0",
                "deadline": "Fall: June 30, Spring: December 15",
                "duration": "4 years (Bachelor's)",
                "tuition": "$12,000 per year"
            },
            "business administration": {
                "requirements": "High school diploma with Mathematics. Minimum GPA: 2.8",
                "deadline": "Fall: July 15, Spring: January 10",
                "duration": "4 years (Bachelor's)",
                "tuition": "$10,000 per year"
            },
            "engineering": {
                "requirements": "High school diploma with Mathematics, Physics, and Chemistry. Minimum GPA: 3.2",
                "deadline": "Fall: June 15, Spring: December 1",
                "duration": "4 years (Bachelor's)",
                "tuition": "$15,000 per year"
            },
            "medicine": {
                "requirements": "High school diploma with Biology, Chemistry, and Physics. Minimum GPA: 3.5",
                "deadline": "Fall: May 31 (limited seats)",
                "duration": "5 years (MBBS)",
                "tuition": "$20,000 per year"
            },
            "law": {
                "requirements": "High school diploma. Minimum GPA: 3.0",
                "deadline": "Fall: July 1, Spring: December 20",
                "duration": "4 years (LLB)",
                "tuition": "$11,000 per year"
            }
        }
        
        # Patterns for intent recognition
        self.patterns = {
            "greeting": [r"\bhello\b", r"\bhi\b", r"\bhey\b", r"\bgreetings\b"],
            "programs": [r"\bprograms?\b", r"\bcourses?\b", r"\bmajors?\b", r"\bdegrees?\b", r"\bwhat.*offer\b"],
            "requirements": [r"\brequirements?\b", r"\beligibility\b", r"\bqualifications?\b", r"\bneed\b"],
            "deadline": [r"\bdeadline\b", r"\bdue date\b", r"\bwhen.*apply\b", r"\blast date\b"],
            "tuition": [r"\btuition\b", r"\bfees?\b", r"\bcost\b", r"\bprice\b", r"\bhow much\b"],
            "duration": [r"\bduration\b", r"\bhow long\b", r"\byears?\b", r"\blength\b"],
            "help": [r"\bhelp\b", r"\bassist\b", r"\bguide\b"]
        }
    
    def detect_intent(self, message):
        """Detect user intent from message."""
        message_lower = message.lower()
        
        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, message_lower):
                    return intent
        return "unknown"
    
    def detect_program(self, message):
        """Detect which program the user is asking about."""
        message_lower = message.lower()
        
        for program in self.programs.keys():
            if program in message_lower or program.replace(" ", "") in message_lower:
                return program
        return None
    
    def get_response(self, message):
        """Generate response based on user message."""
        intent = self.detect_intent(message)
        program = self.detect_program(message)
        
        # Greeting
        if intent == "greeting":
            return "Hello! Welcome to the University Admission Chatbot. 👋\n\nI can help you with:\n• Available programs\n• Admission requirements\n• Application deadlines\n• Tuition fees\n\nHow can I assist you today?"
        
        # List all programs
        if intent == "programs" and not program:
            programs_list = "\n".join([f"• {p.title()}" for p in self.programs.keys()])
            return f"We offer the following programs:\n\n{programs_list}\n\nWhich program would you like to know more about?"
        
        # Specific program query
        if program:
            program_info = self.programs[program]
            
            if intent == "requirements":
                return f"**{program.title()} - Requirements:**\n{program_info['requirements']}"
            
            elif intent == "deadline":
                return f"**{program.title()} - Deadlines:**\n{program_info['deadline']}"
            
            elif intent == "tuition":
                return f"**{program.title()} - Tuition:**\n{program_info['tuition']}"
            
            elif intent == "duration":
                return f"**{program.title()} - Duration:**\n{program_info['duration']}"
            
            else:
                # General program info
                return f"**{program.title()} Program:**\n\n" \
                       f"📋 Requirements: {program_info['requirements']}\n\n" \
                       f"📅 Deadlines: {program_info['deadline']}\n\n" \
                       f"⏱️ Duration: {program_info['duration']}\n\n" \
                       f"💰 Tuition: {program_info['tuition']}"
        
        # Help
        if intent == "help":
            return "I can help you with:\n\n" \
                   "• **Programs**: Ask 'What programs do you offer?'\n" \
                   "• **Requirements**: Ask 'What are the requirements for Computer Science?'\n" \
                   "• **Deadlines**: Ask 'When is the deadline for Engineering?'\n" \
                   "• **Tuition**: Ask 'How much is tuition for Medicine?'\n\n" \
                   "Try asking about any program!"
        
        # Default fallback
        return "I'm not sure I understood that. You can ask me about:\n" \
               "• Available programs\n" \
               "• Admission requirements\n" \
               "• Application deadlines\n" \
               "• Tuition fees\n\n" \
               "Try asking 'What programs do you offer?' or type 'help' for more options."
