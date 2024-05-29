from flask import Flask, request, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import datetime

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
def log_ip():
    # Get the visitor's IP address
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)

    # Open or create the log file
    with open("ip_log.txt", "a") as log_file:
        # Write the IP address and the current timestamp to the log file
        log_file.write(f"{datetime.datetime.now()} - {ip_address}\n")

    return render_template("index.html", ip_address=ip_address)


if __name__ == "__main__":
    app.run(debug=True)
