from setuptools import setup, find_packages

setup(
    name="arqmathcode",
    version="0.0.1",
    description="Packaged version of ARQMath/ARQMathCode",
    author="Vít Novotný",
    author_email="witiko@mail.muni.cz",
    url="https://github.com/MIR-MU/ARQMathCode",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["xmlr~=0.3.1"],
    package_data={
        "arqmathcode": [
            "Clef_Class Diagram.jpg",
            "Visualization/arqmath.png",
            "Visualization/mse.svg",
        ]
    },
)
