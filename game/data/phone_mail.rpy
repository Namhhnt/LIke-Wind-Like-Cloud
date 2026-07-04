init -5 python:

    PHONE_MAILS = {
        "company_salary_first_month": {
            "id": "company_salary_first_month",
            "from": "HR Department",
            "subject": "Salary Notification",
            "preview": "Your first monthly salary has been processed.",
            "body": "Your first monthly salary has been processed. Please check the attached payroll notice for details.",
            "unlock_conditions": ["flag:tam_huyen_first_job_offer"],
            "sort_order": 100,
            "effects_on_read": {
                "character_status": {
                    "tam": {
                        "job_title": "Junior Staff",
                        "job_level": 1,
                        "income_monthly": 1200,
                    },
                    "huyen": {
                        "job_title": "Junior Staff",
                        "job_level": 1,
                        "income_monthly": 1200,
                    },
                },
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
            "unlock_conditions": ["completed:tam_c01_interview_day"],
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
