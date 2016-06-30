"""
General variables and contstants
"""

curr_active_list = -1 # gneral working variables
dictips = {}   # active IPs, struct is: {"ip-address": [{new_ip_dict}, {start_time_in date time format: datetime}]}
new_ip_dict = {"ip": "x.x.x.x", "flag_process": "True", "time_start": "-1", "count_sent": "-1", 
                "last_prime": "-1", "throughput": "-1"}

tf_port = int("7777") # server port number
