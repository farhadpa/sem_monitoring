test_data = [
    {
        "payload" : {
            "action": "maxmin_attendance",
            "data": {
                "item_1": "lecture_attendance",
                "attendance_1": 20,
                "item_2": "lab_sessions",
                "attendance_2": 15,
                "item_3": "support-sessions",
                "attendance_3": 22,
                "item_4": "canvas_activity",
                "attendance_4": 40
            }
        }, 
        "result":{
            "error": False,
            "items": [
                "lecture_attendance",
                "lab_sessions",
                "support-sessions",
                "canvas_activity"
            ],
            "attendance": [
                "20",
                "15",
                "22",
                "40"
            ],
            "max_item": "canvas_activity - 40",
            "min_item": "lab_sessions - 15"
        }
    },
    {
        "payload" : {
            "action": "maxmin_attendance",
            "data": {
                "item_1": "lecture_attendance",
                "attendance_1": 30,
                "item_2": "lab_sessions",
                "attendance_2": 10,
                "item_3": "support-sessions",
                "attendance_3": 38,
                "item_4": "canvas_activity",
                "attendance_4": 35
            }
        }, 
        "result": {
            "error": False,
            "items": [
                "lecture_attendance",
                "lab_sessions",
                "support-sessions",
                "canvas_activity"
            ],
            "attendance": [
                "30",
                "10",
                "38",
                "35"
            ],
            "max_item": "support-sessions - 38",
            "min_item": "lab_sessions - 10"
        }
    },
    {
        "payload" : {
            "action": "sort_attendance",
            "data": {
                "item_1": "lecture_attendance",
                "attendance_1": 20,
                "item_2": "lab_sessions",
                "attendance_2": 15,
                "item_3": "support-sessions",
                "attendance_3": 22,
                "item_4": "canvas_activity",
                "attendance_4": 40
                }
        }, 
        "result": {
            "error": False,
            "items": [
                "lecture_attendance",
                "lab_sessions",
                "support-sessions",
                "canvas_activity"
            ],
            "attendance": [
                "20",
                "15",
                "22",
                "40"
            ],
            "sorted_attendance": [
                {
                    "item": "canvas_activity",
                    "attendance": "40"
                },
                {
                    "item": "support-sessions",
                    "attendance": "22"
                },
                {
                    "item": "lecture_attendance",
                    "attendance": "20"
                },
                {
                    "item": "lab_sessions",
                    "attendance": "15"
                }
            ]
        }
    },
    {
        "payload" : {
            "action": "sort_attendance",
            "data": {
                "item_1": "lecture_attendance",
                "attendance_1": 30,
                "item_2": "lab_sessions",
                "attendance_2": 10,
                "item_3": "support-sessions",
                "attendance_3": 38,
                "item_4": "canvas_activity",
                "attendance_4": 35
                }
        }, 
        "result": {
            "error": False,
            "items": [
                "lecture_attendance",
                "lab_sessions",
                "support-sessions",
                "canvas_activity"
            ],
            "attendance": [
                "30",
                "10",
                "38",
                "35"
            ],
            "sorted_attendance": [
                {
                    "item": "support-sessions",
                    "attendance": "38"
                },
                {
                    "item": "canvas_activity",
                    "attendance": "35"
                },
                {
                    "item": "lecture_attendance",
                    "attendance": "30"
                },
                {
                    "item": "lab_sessions",
                    "attendance": "10"
                }
            ]
        }
    },
    {
        "payload": {
            "action": "total_attendance",
            "data": {
                "lecture_attendance": 20,
                "lab_attendance": 15,
                "support_attendance": 22,
                "canvas_activity": 40
            }
        },
        "result": {
            "result": "97.0",
            "status": "200"  
        }
    }, 
    {
        "payload": {
            "action": "total_attendance",
            "data": {
                "lecture_attendance": 30,
                "lab_attendance": 10,
                "support_attendance": 38,
                "canvas_activity": 35
            }
        },
        "result": {
            "result": "113.0",
            "status": "200"
        }
    }, 
    {
        "payload": {
            "action": "engagement_score",
            "data": {
                "lecture_attendance": 20,
                "lab_attendance": 15,
                "support_attendance": 22,
                "canvas_activity": 40
            }
        },
        "result": {
            "result": "63.86",
            "status": 200
        }
    }, 
    {
        "payload": {
            "action": "engagement_score",
            "data": {
                "lecture_attendance": 30,
                "lab_attendance": 10,
                "support_attendance": 38,
                "canvas_activity": 35
            }
        },
        "result": {
            "result": "67.95",
            "status": 200
        }
    },
    {
        "payload": {
            "action": "risk_assessment",
            "data": {
                "engagement_score": 80,
                "cutOff_score": 50
            }
        },
        "result": {
            "result": "Not Risky"
        }
    },
    {
        "payload": {
            "action": "risk_assessment",
            "data": {
                "engagement_score": 40,
                "cutOff_score": 50
            }
        },
        "result": {
            "result": "Risky"
        }
    }
]