from setuptools import setup, find_packages

setup(
    name="tarn-inventree-report-list-filters",
    version="1.0.1",
    description="Adds |split and |replace template filters to InvenTree reports and labels",
    author="CP Knight",
    author_email="chris@tarn.parts",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "inventree_plugins": [
            "tarn_report_list_filters = tarn_inventree_report_list_filters:ListFiltersPlugin",
        ],
    },
)
