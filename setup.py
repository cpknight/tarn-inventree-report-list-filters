from setuptools import setup, find_packages

setup(
    name="tarn-inventree-report-list-filters",
    version="1.3.1",
    description="Adds tarn_split and tarn_replace template tags to InvenTree reports and labels",
    url="https://github.com/cpknight/tarn-inventree-report-list-filters",
    author="Project Tarn contributors",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "inventree_plugins": [
            "tarn_report_list_filters = tarn_inventree_report_list_filters:TarnReportListFiltersPlugin",
        ],
    },
)
