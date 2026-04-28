"""
Test fixtures for Karma API responses
"""

# Sample Karma API response structure
SAMPLE_KARMA_RESPONSE = {
    "status": "success",
    "timestamp": "2025-09-04T10:00:00Z",
    "version": "v0.120",
    "upstreams": {
        "counters": {"healthy": 1, "failed": 0},
        "instances": [
            {
                "name": "alertmanager",
                "cluster": "teddy-prod",
                "publicURI": "http://alertmanager.monitoring.svc.cluster.local",
                "version": "0.25.0",
                "error": "",
            }
        ],
    },
    "grids": [
        {
            "labelName": "",
            "labelValue": "",
            "alertGroups": [
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "KubePodCrashLooping"},
                        {"name": "severity", "value": "critical"},
                    ],
                    "alerts": [
                        {
                            "annotations": [
                                {
                                    "name": "description",
                                    "value": "Pod is crash looping",
                                },
                                {"name": "summary", "value": "Pod crash loop detected"},
                            ],
                            "labels": [
                                {"name": "instance", "value": "10.1.1.1:8080"},
                                {"name": "namespace", "value": "production"},
                                {"name": "pod", "value": "app-pod-123"},
                            ],
                            "startsAt": "2025-09-04T09:30:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-1",
                        },
                        {
                            "annotations": [
                                {
                                    "name": "description",
                                    "value": "Another pod crash looping",
                                },
                                {"name": "summary", "value": "Second pod crash loop"},
                            ],
                            "labels": [
                                {"name": "instance", "value": "10.1.1.2:8080"},
                                {"name": "namespace", "value": "staging"},
                                {"name": "pod", "value": "app-pod-456"},
                            ],
                            "startsAt": "2025-09-04T09:45:00Z",
                            "state": "suppressed",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "suppressed",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-2",
                        },
                    ],
                    "id": "group-1",
                    "alertmanagerCount": {"active": 1, "suppressed": 1},
                    "stateCount": {"active": 1, "suppressed": 1},
                    "totalAlerts": 2,
                },
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "HighMemoryUsage"},
                        {"name": "severity", "value": "warning"},
                    ],
                    "alerts": [
                        {
                            "annotations": [
                                {
                                    "name": "description",
                                    "value": "Memory usage is high",
                                },
                                {"name": "summary", "value": "High memory detected"},
                            ],
                            "labels": [
                                {"name": "instance", "value": "10.1.1.3:9100"},
                                {"name": "namespace", "value": "monitoring"},
                                {"name": "job", "value": "node-exporter"},
                            ],
                            "startsAt": "2025-09-04T09:15:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-3",
                        }
                    ],
                    "id": "group-2",
                    "alertmanagerCount": {"active": 1},
                    "stateCount": {"active": 1},
                    "totalAlerts": 1,
                },
            ],
            "totalGroups": 2,
            "stateCount": {"active": 2, "suppressed": 1},
        }
    ],
    "totalAlerts": 3,
    "labelNames": ["alertname", "severity", "instance", "namespace"],
    "colors": {},
    "filters": [],
    "silences": [],
    "settings": {},
    "authentication": {},
    "receivers": ["web.hook"],
}

# Sample response where severity is in shared labels (deduplicated by Karma).
# This is the most common real-world scenario: Karma groups by alertname,
# and since severity is the same across all alerts in the group, Karma
# deduplicates it into group.shared.labels.
SAMPLE_KARMA_RESPONSE_SEVERITY_ON_ALERT = {
    "status": "success",
    "timestamp": "2025-09-04T10:00:00Z",
    "version": "v0.120",
    "upstreams": {
        "counters": {"healthy": 1, "failed": 0},
        "instances": [
            {
                "name": "alertmanager",
                "cluster": "infratest-dev",
                "publicURI": "http://alertmanager.monitoring.svc.cluster.local",
                "version": "0.25.0",
                "error": "",
            }
        ],
    },
    "grids": [
        {
            "labelName": "",
            "labelValue": "",
            "alertGroups": [
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "KubePodCrashLooping"},
                    ],
                    "shared": {
                        "labels": [
                            {"name": "severity", "value": "critical"},
                        ],
                        "annotations": [],
                        "silences": {},
                        "sources": [],
                        "clusters": ["infratest-dev"],
                    },
                    "alerts": [
                        {
                            "annotations": [
                                {
                                    "name": "description",
                                    "value": "Pod is crash looping",
                                },
                            ],
                            "labels": [
                                {"name": "instance", "value": "10.55.158.226:8080"},
                                {"name": "namespace", "value": "argocd-edge"},
                                {"name": "pod", "value": "app-pod-789"},
                            ],
                            "startsAt": "2025-09-04T09:30:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "infratest-dev",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-4",
                        },
                    ],
                    "id": "group-3",
                    "alertmanagerCount": {"active": 1},
                    "stateCount": {"active": 1},
                    "totalAlerts": 1,
                },
            ],
            "totalGroups": 1,
            "stateCount": {"active": 1},
        }
    ],
    "totalAlerts": 1,
    "labelNames": ["alertname", "severity", "instance", "namespace"],
    "colors": {},
    "filters": [],
    "silences": [],
    "settings": {},
    "authentication": {},
    "receivers": ["web.hook"],
}

# Sample response with `team` ownership labels.
# Used to exercise team-based filtering. Mixes group-level and alert-level
# team labels and includes one alert without any team label.
SAMPLE_KARMA_RESPONSE_WITH_TEAMS = {
    "status": "success",
    "timestamp": "2025-09-04T10:00:00Z",
    "version": "v0.120",
    "upstreams": {
        "counters": {"healthy": 1, "failed": 0},
        "instances": [
            {
                "name": "alertmanager",
                "cluster": "teddy-prod",
                "publicURI": "http://alertmanager.monitoring.svc.cluster.local",
                "version": "0.25.0",
                "error": "",
            }
        ],
    },
    "grids": [
        {
            "labelName": "",
            "labelValue": "",
            "alertGroups": [
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "SherlocksHighLatency"},
                        {"name": "severity", "value": "critical"},
                        {"name": "team", "value": "sherlocks"},
                    ],
                    "alerts": [
                        {
                            "annotations": [
                                {"name": "summary", "value": "Latency too high"}
                            ],
                            "labels": [
                                {"name": "instance", "value": "10.1.1.1:8080"},
                                {"name": "namespace", "value": "production"},
                            ],
                            "startsAt": "2025-09-04T09:30:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-team-1",
                        }
                    ],
                    "id": "group-team-1",
                    "alertmanagerCount": {"active": 1},
                    "stateCount": {"active": 1},
                    "totalAlerts": 1,
                },
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "PerAlertTeamLabel"},
                    ],
                    "alerts": [
                        {
                            "annotations": [],
                            "labels": [
                                {"name": "severity", "value": "warning"},
                                {"name": "team", "value": "Sherlocks"},
                                {"name": "namespace", "value": "production"},
                                {"name": "instance", "value": "10.1.1.2:8080"},
                            ],
                            "startsAt": "2025-09-04T09:31:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-team-2",
                        },
                        {
                            "annotations": [],
                            "labels": [
                                {"name": "severity", "value": "warning"},
                                {"name": "team", "value": "watson"},
                                {"name": "namespace", "value": "production"},
                                {"name": "instance", "value": "10.1.1.3:8080"},
                            ],
                            "startsAt": "2025-09-04T09:32:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-team-3",
                        },
                    ],
                    "id": "group-team-2",
                    "alertmanagerCount": {"active": 2},
                    "stateCount": {"active": 2},
                    "totalAlerts": 2,
                },
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "NoTeamAlert"},
                        {"name": "severity", "value": "warning"},
                    ],
                    "alerts": [
                        {
                            "annotations": [],
                            "labels": [
                                {"name": "namespace", "value": "production"},
                                {"name": "instance", "value": "10.1.1.4:8080"},
                            ],
                            "startsAt": "2025-09-04T09:33:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-team-4",
                        }
                    ],
                    "id": "group-team-3",
                    "alertmanagerCount": {"active": 1},
                    "stateCount": {"active": 1},
                    "totalAlerts": 1,
                },
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "PlatformOnEdge"},
                        {"name": "severity", "value": "warning"},
                        {"name": "team", "value": "platform"},
                    ],
                    "alerts": [
                        {
                            "annotations": [],
                            "labels": [
                                {"name": "namespace", "value": "edge"},
                                {"name": "instance", "value": "10.2.2.1:8080"},
                            ],
                            "startsAt": "2025-09-04T09:34:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "edge-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-team-5",
                        }
                    ],
                    "id": "group-team-4",
                    "alertmanagerCount": {"active": 1},
                    "stateCount": {"active": 1},
                    "totalAlerts": 1,
                },
                {
                    "receiver": "web.hook",
                    "labels": [
                        {"name": "alertname", "value": "PlatformOnTeddy"},
                        {"name": "severity", "value": "warning"},
                        {"name": "team", "value": "platform"},
                    ],
                    "alerts": [
                        {
                            "annotations": [],
                            "labels": [
                                {"name": "namespace", "value": "production"},
                                {"name": "instance", "value": "10.1.1.5:8080"},
                            ],
                            "startsAt": "2025-09-04T09:35:00Z",
                            "state": "active",
                            "alertmanager": [
                                {
                                    "cluster": "teddy-prod",
                                    "name": "alertmanager",
                                    "state": "active",
                                }
                            ],
                            "receiver": "web.hook",
                            "id": "alert-team-6",
                        }
                    ],
                    "id": "group-team-5",
                    "alertmanagerCount": {"active": 1},
                    "stateCount": {"active": 1},
                    "totalAlerts": 1,
                },
            ],
            "totalGroups": 5,
            "stateCount": {"active": 6},
        }
    ],
    "totalAlerts": 6,
    "labelNames": ["alertname", "severity", "team", "instance", "namespace"],
    "colors": {},
    "filters": [],
    "silences": [],
    "settings": {},
    "authentication": {},
    "receivers": ["web.hook"],
}


# Sample empty response
EMPTY_KARMA_RESPONSE = {
    "status": "success",
    "timestamp": "2025-09-04T10:00:00Z",
    "version": "v0.120",
    "upstreams": {"counters": {"healthy": 1, "failed": 0}, "instances": []},
    "grids": [],
    "totalAlerts": 0,
    "labelNames": [],
    "colors": {},
    "filters": [],
    "silences": [],
    "settings": {},
    "authentication": {},
    "receivers": [],
}

# Sample health response
HEALTH_RESPONSE = {"status": "ok", "version": "v0.120"}

# Sample error responses
ERROR_RESPONSES = {
    "connection_error": Exception("Connection refused"),
    "timeout_error": Exception("Request timeout"),
    "500_error": {"status": "error", "message": "Internal server error"},
    "404_error": {"status": "error", "message": "Not found"},
}
