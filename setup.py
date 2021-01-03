from pathlib import Path
from setuptools import setup

base_dir = Path(__file__).resolve().parent

with open(base_dir / "README.md") as fp:
    README = fp.read()

with open(base_dir / "requirements.txt") as fp:
    requirements = fp.read().strip().split("\n")


setup(
    name="usb-creator",
    version="0.3.3",
    description="startup disk creator",
    packages=[
        "usbcreator",
        "usbcreator.frontends",
        "usbcreator.frontends.gtk",
        "usbcreator.frontends.base",
        "usbcreator.backends",
        "usbcreator.backends.base",
        "usbcreator.backends.udisks",
    ],
    data_files=[("", ["usbcreator/gui/usbcreator-gtk.ui"])],
    include_package_data=True,
    scripts=["bin/usb-creator-gtk"],
    install_requires=requirements,
)
