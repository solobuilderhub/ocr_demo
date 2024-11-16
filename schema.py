{
    "page_1": {
        "company_name": "string",
        "alternate_trade_name": "string",
        "mailing_address": "string",
        "city": "string",
        "state": "string",
        "zip_code": "string",
        "physical_address": "string",
        "company_phone": "string",
        "company_email": "string",
        "company_website": "string",
        "company_contact_person": {
            "name": "string",
            "title": "string",
            "phone": "string",
            "email": "string"
        },
    },
    
    "page_4": {
        "physical_location_equipment": [
            {
                "address": "string",
                "description": "string",
                "property_owner": "string",
            }
        ],
        "brokers_details": [
            {
                "name": "string",
                "phone": "string",
            }
        ],
    },

    "page_5": {
            "equipment_driver_details": {
            "single_units": int,
            "cabs": int,
            "trailers": int,
            "containers": int,
            "drivers": int,
        },
    },
    
    "page_7": {
        "equity_holder_details": {
            "individuals": [
                {
                    "name": "string",
                    "ss_number": "string",
                    "percentage": "string",
                }
            ],
            "officers": [
                {
                    "name": "string",
                    "ss_number": "string",
                    "percentage": "string",
                }
            ],
            "directors": [
                {
                    "name": "string",
                    "ss_number": "string",
                    "percentage": "string",
                }
            ],
            "llc_members": [
                {
                    "name": "string",
                    "ss_number": "string",
                    "percentage": "string",
                }
            ],
            "family_members": [
                {
                    "name": "string",
                    "ss_number": "string",
                    "percentage": "string",
                }
            ],
        },
    },
    
    "page_12":{
        "judgement_details": {
            "has_judgements": bool,
            "has_litiations": bool,
            "has_bankruptcy": bool,
        }
    }
}