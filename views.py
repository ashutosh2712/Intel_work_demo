from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home_page.html")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/admin")
def admin():
    return render_template("admin.html")


@views.route("/benchmarking")
def benchmarking():
    return render_template("benchmarking.html")


@views.route("/workloads")
def workload():
    return render_template("workload.html")
