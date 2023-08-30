from flask import Blueprint, render_template, request
from .benchmarking import (
    get_all_workload,
    get_workload_data,
    get_testcase_data,
    get_cloud_data,
    get_machine_type_data,
)

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
    workloads = get_workload_data()
    workload_ip = request.args.get("workload")
    testcase_ip = request.args.get("testcase")
    cloud_ip = request.args.get("cloud")
    testcases = []
    clouds = []
    microarchitectures = []
    if workloads:
        testcases = get_testcase_data(workload_ip)
        if testcases:
            clouds = get_cloud_data(workload_ip, testcase_ip)
            if clouds:
                microarchitectures = get_machine_type_data(
                    workload_ip, testcase_ip, cloud_ip
                )
    return render_template(
        "benchmarking.html",
        workloads=workloads,
        workload_ip=workload_ip,
        testcases=testcases,
        testcase_ip=testcase_ip,
        clouds=clouds,
        cloud_ip=cloud_ip,
        microarchitectures=microarchitectures,
    )


@views.route("/workloads")
def workload():
    return render_template("workload.html")
