from setuptools import setup, find_packages

setup(
    name="tarn-inventree-report-list-filters",
    version="1.3.0",
    description="Adds |tarn_split and |tarn_replace template filters to InvenTree reports and labels",
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
