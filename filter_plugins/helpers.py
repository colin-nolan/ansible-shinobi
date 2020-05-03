#!/usr/bin/python


class FilterModule(object):
    def filters(self):
        return {
            "addUserDetailsToMonitor": self.monitor_user_match,
        }

    def monitor_user_match(self, monitors, users):
        user_password_map = {user["email"]: user["password"] for user in users}
        processed = []
        for monitor in monitors:
            for user_email in monitor["users"]:
                entry = dict(email=user_email, password=user_password_map[user_email],
                             configuration=monitor["configuration"], id=monitor["id"])
                processed.append(entry)
        return processed