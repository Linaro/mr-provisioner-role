#!/usr/bin/env python3

from run_provisioner import app
from mr_provisioner import db
from mr_provisioner.models import User, Network, BMC


def main():

    with app.app_context():
        {% for network in mr_provisioner_networks %}
        network = Network(**network)
        db.session.add(network)
        db.session.commit()
        {% endfor %}

        {% for bmc in mr_provisioner_bmcs %}
        bmc = BMC(**bmc)
        db.session.add(bmc)
        db.session.commit()
        {% endfor %}


if __name__ == "__main__":
    main()
