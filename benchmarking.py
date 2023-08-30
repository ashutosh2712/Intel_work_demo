from .models import Workload
from . import db


def get_all_workload():
    all_workload = Workload.query.all()
    all_data = []
    for data in all_workload:
        all_data.append(
            {
                "Workload": data.workload,
                "Testcase": data.testcase,
                "Run-uri": data.run_uri,
                "Date": data.date,
                "Cloud": data.cloud,
                "Microarchitecture": data.microarchitecture,
                "Value": data.value,
                "Unit": data.unit,
            }
        )

    return all_data


def get_workload_data():
    workloads = Workload.query.with_entities(Workload.workload).all()

    final_workload = [workload for (workload,) in workloads]
    return final_workload


def get_testcase_data(workload_ip):
    testcases = (
        Workload.query.with_entities(Workload.testcase)
        .filter_by(workload=workload_ip)
        .all()
    )

    final_testcase = [testcase for (testcase,) in testcases]
    return final_testcase


def get_cloud_data(workload_ip, testcase_ip):
    clouds = (
        Workload.query.with_entities(Workload.cloud)
        .filter_by(workload=workload_ip, testcase=testcase_ip)
        .all()
    )

    final_cloud = [cloud for (cloud,) in clouds]
    return final_cloud


def get_machine_type_data(workload_ip, testcase_ip, cloud_ip):
    microarchitectures = (
        Workload.query.with_entities(Workload.microarchitecture)
        .filter_by(workload=workload_ip, testcase=testcase_ip, cloud=cloud_ip)
        .all()
    )

    final_microarchitecture = [
        microarchitecture for (microarchitecture,) in microarchitectures
    ]
    return final_microarchitecture
