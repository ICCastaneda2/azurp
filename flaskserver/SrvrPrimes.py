"""
Targil1 Flask server, support various options
to access the targil1 database
"""

#import flask
import math
from flask import Flask, request, Response
from flask import jsonify, send_file

d1 = {"ip":"127.0.0.1", "time_start":"10:30:10", "count_sent":"1001", "last_prime":"11001", "throughput":"100"}
d2 = {"ip":"127.0.0.2", "start_time":"20:30:20", "count_sent":"2002", "last_prime":"22001", "throughput":"200"}
active_list = [d1,d2]

tf_port = int("7777")
app = Flask(__name__, static_folder='www', template_folder='www')

curr_active_list = -1
flag_process = True
flag_active = True

# API

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
    global flag_process
    flag_process = True

    def read_prime():
        glb_num = 3
        prime_sent = 0
        # while flag_process:     # True:
        for prime1 in get_primes(glb_num):
            glb_num = prime1 + 1;
            ps = str(prime1)
            prime_sent += 1
            print "glb_num, prime, sent = ", glb_num, ' ', ps, ' ', prime_sent
            yield ps

    return Response(read_prime(), mimetype= 'text/plain' )


@app.route('/finish_primes', methods=["GET"])
def finish_primes():
    """
    signal to finish the primes numbers
    """
    global flag_process
    req = request
    flag_process = False
    # print "in finish_primes, flag_process == false"
    sj = jsonify({"result": "stop primes upstream, succeeded"})
    return sj


@app.route('/dashboard', methods=["GET"])
def dashboard():
    """
    Continuously send the active downloads data
    """
    global curr_active_list
    req = request
    args = request.args

    len_active_list = len(active_list)
    if len_active_list:
       curr_active_list += 1
       if curr_active_list >= len_active_list: 
           curr_active_list = 0

       active_x = active_list[curr_active_list]
    else:
        active_x = {"ip":"no_activities"}

    ret_val = {"curr_active": active_x}
    # print "ret_val = ", ret_val
    sj = jsonify(ret_val)
    return sj


def get_primes(number):
    while flag_process:      # number < 5:
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
    ms1 = "port number is {}".format(tf_port)
    print ms1    # will be converter to use python logging

    app.run(host="0.0.0.0",
            threaded=True,
            debug=True,
            use_reloader=False,
            use_debugger=False,
            port=tf_port)


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

