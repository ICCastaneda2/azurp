"""
Targil1 Flask server, support access from multiple IPS concurently
"""

import time
from datetime import datetime
import math
from flask import Flask, request, Response
from flask import jsonify, send_file
import GVARS

app = Flask(__name__, static_folder='www', template_folder='www')

#flag_process = True
#flag_active = True

# API, will be documented when system is more stable

@app.route('/')
def main_index_html():
    """
    On start of the web page send the index.html page
    which will later will be manipulate by the client side
    """
    # req = request     # debug only
    return send_file("www/templates/index.html")


@app.route('/get_primes', methods=["GET"])
def get_primes():
    """
    Get primes numbers
    """
    req = request
    print request.remote_addr
    curr_dict, curr_dict2 = get_curr_dict(request)

    def read_prime():
        glb_num = 3
        prime_sent = 0
        for prime1 in get_primes(glb_num, curr_dict):
            glb_num = prime1 + 1
            ps = str(prime1)
            prime_sent += 1
            curr_dict["last_prime"] = ps
            curr_dict["count_sent"] = str(prime_sent)

            now1x = curr_dict2["time_start"]
            now1 = time.mktime(now1x.timetuple())
            now2 = time.mktime(datetime.now().timetuple())
            try: 
                tp = prime_sent / ((now2 - now1) / 60)
            except Exception as e:
                tp = "N/A"
            curr_dict["throughput"] = str(tp)

            GVARS.dictips[curr_dict["ip"]][0] = curr_dict
            print "curr_dict, curr_dict2 = ", curr_dict, '*', curr_dict2
            yield ps

    return Response(read_prime(), mimetype= 'text/plain' )


def get_curr_dict(req):
    curr_ip = str(req.remote_addr)
    if curr_ip in GVARS.dictips:
        curr_dict = GVARS.dictips[curr_ip][0]   # first elment in the list
        curr_dict2 = GVARS.dictips[curr_ip][1]   # first elment in the list
    else:
        GVARS.dictips[curr_ip] = [GVARS.new_ip_dict, {}]
        curr_dict = GVARS.dictips[curr_ip][0]
        curr_dict2 = GVARS.dictips[curr_ip][1]
        curr_dict["ip"] = curr_ip
        curr_dict["time_start"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        curr_dict2["time_start"] = datetime.now()
   
    return curr_dict, curr_dict2


@app.route('/finish_primes', methods=["GET"])
def finish_primes():
    """
    signal to finish the primes numbers
    """
    req = request
    curr_dict, curr_dict2 = get_curr_dict(request)
    curr_dict["flag_process"] = False
    sj = jsonify({"result": "process of upstream primes stped succesfully"})
    return sj


@app.route('/dashboard', methods=["GET"])
def dashboard():
    """
    Continuously send the active downloads data
    """
    req = request
    args = request.args

    list_dictips_keys = GVARS.dictips.keys()
    len_active_list = len(list_dictips_keys)
    if len_active_list:
        GVARS.curr_active_list += 1
        if GVARS.curr_active_list >= len_active_list:
            GVARS.curr_active_list = 0

        active_x = GVARS.dictips[list_dictips_keys[GVARS.curr_active_list]][0]
    else:
        GVARS.curr_active_list = -1  # no active ip
        active_x = {"ip":"no_activities"}

    ret_val = {"curr_active": active_x}
    print "ret_val = ", ret_val
    sj = jsonify(ret_val)
    return sj


def get_primes(number, curr_dict):
    while curr_dict["flag_process"]:      # number < 5:
        if is_prime(number):
            yield number
        number += 1


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    """
    primes number, flask server, main
    """
    ms1 = "port number is {}".format(GVARS.tf_port)
    print ms1    # will be converter to use python logging

    app.run(host="0.0.0.0",
            threaded=True,
            debug=True,
            use_reloader=False,
            use_debugger=False,
            port=GVARS.tf_port)


"""
@app.route('/large.csv')
def generate_large_csv():
    def generate():
        for row in iter_all_rows():
            yield ','.join(row) + '\n'
    return Response(generate(), mimetype='text/csv')
            return flask.Response(str1, mimetype= 'text/plain' )
    print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    # return flask.Response(read_prime(), mimetype= 'text/plain' )
    # return render_template('data.json'), 201, {'Content-Type': 'application/json'}


    # -------
    resp = Response(response=dict1,
                    status=200,
                    mimetype="application/json")
    return resp
    # -------
"""

"""
import time
import datetime
date1 = datetime.datetime(2012, 10, 10, 10, 15, 44)
date2 = datetime.datetime(2012, 10, 17, 8, 45, 38)
var1 = time.mktime(date1.timetuple())
var2 = time.mktime(date2.timetuple())
result_in_seconds = var2 - var1

>>> var2 - var1
599394.0
d1 = {"ip":"127.0.0.1", "time_start":"10:30:10", "count_sent":"1001", "last_prime":"11001", "throughput":"100"}
d2 = {"ip":"127.0.0.2", "start_time":"20:30:20", "count_sent":"2002", "last_prime":"22001", "throughput":"200"}
active_list = [d1,d2]
"""
