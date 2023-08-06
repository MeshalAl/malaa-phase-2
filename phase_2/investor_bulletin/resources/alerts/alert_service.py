""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_dal import create_alert, get_alerts

def create_new_alert_service( alert: AlertCreate, session ):
    return create_alert( alert=alert, session=session)

def get_alerts_service(session):
    return get_alerts(session)
