"""
Targil1 Flask server, support various options
to access the targil1 database
"""

import math
import flask
from flask import Flask, request, Response
from flask import jsonify, send_file

tf_port = int("7777")
app = Flask(__name__, static_folder='www', template_folder='www')

flag_process = True

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

    print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    return Response(read_prime(), mimetype= 'text/plain' )


@app.route('/finish_primes', methods=["GET"])
def finish_primes():
    """
    signal to finish the primes numbers
    """
    global flag_process
    req = request
    flag_process = False
    print "in finish_primes, flag_process == false"
    sj = jsonify({"result": "stop primes upstream, succeeded"})
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
"""

