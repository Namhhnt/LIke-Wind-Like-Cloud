init -5 python:

    PHONE_MAILS = {
        "company_interview_invitation": {
            "id": "company_interview_invitation",
            "from": "HR Department",
            "subject": "Interview Invitation \u2014 October 12th (Friday)",
            "preview": "You are invited to an interview on Friday, October 12th.",
            "body": "Dear Candidate,\n\nWe are pleased to invite you to an interview for the Junior Staff position at our company.\n\nDate: Friday, October 12th\nTime: 9:00 AM\nLocation: Company Headquarters, 3rd Floor \u2014 Waiting Area\n\nPlease bring your portfolio, CV, and any relevant certificates. The interview will include a short skill assessment and a discussion about your experience.\n\nWe look forward to meeting you.\n\nBest regards,\nHR Department",
            "unlock_conditions": ["flag:tam_interview_invitation_received"],
            "sort_order": 110,
            "effects_on_read": {
                "flags": ["read_interview_invitation"],
            },
        },
        "company_onboarding_process": {
            "id": "company_onboarding_process",
            "from": "HR Department",
            "subject": "Onboarding Plan & Next Steps",
            "preview": "Welcome aboard! Your onboarding plan is ready.",
            "body": "Dear Tam,\n\nCongratulations on passing the interview! We are excited to welcome you to the team.\n\nYour onboarding plan includes:\n- 2-week training and process familiarisation\n- Company policy orientation\n- Team introductions\n- Setup of work tools and accounts\n\nPlease report to the HR office on Monday at 8:30 AM to begin your first day.\n\nWe will also send you a separate invitation for the upcoming company gathering.\n\nBest regards,\nHR Department",
            "unlock_conditions": ["flag:tam_c01_onboarding_mail_sent"],
            "sort_order": 95,
            "effects_on_read": {
                "flags": ["read_onboarding_email"],
                "chapter_unlocks": ["tam_c02_company_party"],
            },
        },
        "company_salary_first_month": {
            "id": "company_salary_first_month",
            "from": "HR Department",
            "subject": "Salary Notification \u2014 First Payment",
            "preview": "Your first salary payment has been processed.",
            "body": "Dear Tam,\n\nYour first salary payment has been processed. As this is a partial month (starting mid-October), the amount reflects the days worked in the current period.\n\nPlease check your bank account for the deposit and contact HR if you have any questions.\n\nBest regards,\nHR Department",
            "unlock_conditions": ["flag:tam_c02_salary_mail_sent"],
            "sort_order": 100,
            "effects_on_read": {
                "inventory_add": {
                    "tam": ["tam_first_salary_envelope"],
                },
                "known_info_add": {
                    "tam": ["First salary has arrived."],
                    "huyen": ["Started work at the same time as Tam."],
                },
                "flags": ["read_first_salary_mail"],
            },
        },
        "company_party_invitation": {
            "id": "company_party_invitation",
            "from": "Company Affairs",
            "subject": "Company Gathering Invitation",
            "preview": "You are invited to the upcoming company gathering.",
            "body": "You are invited to the upcoming company gathering. Dress code: semi-formal. Please arrive ten minutes early for seating.",
            "unlock_conditions": ["flag:tam_c02_party_invitation_sent"],
            "sort_order": 90,
            "effects_on_read": {},
        },
        "project_brief_followup": {
            "id": "project_brief_followup",
            "from": "Minh",
            "subject": "Tomorrow's Brief",
            "preview": "A short note before the meeting.",
            "body": "Read the brief once for details and once for pressure points. People usually miss one of those two.",
            "unlock_conditions": ["completed:tam_c06_minh_returns"],
            "sort_order": 80,
            "effects_on_read": {
                "known_info_add": {
                    "minh": ["Gives advice in a way that sounds practical first and personal second."],
                },
            },
        },
    }
