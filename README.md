# mr-provisioner-role
Ansible role for installing/upgrading a Mr. Provisioner system.

# Overview

This role allows you to install Mr Provisioner from a release or build it from source.

# Variables

```yaml
    - mr_provisioner_path: "/opt/mr-provisioner"
    - mr_provisioner_build_path: "{{mr_provisioner_path}}/build"
    - mr_provisioner_version: "0.3.0"
    - mr_provisioner_source: "https://github.com/mr-provisioner/mr-provisioner/releases/download/v{{mr_provisioner_version}}/mr-provisioner-{{mr_provisioner_version}}.tar.gz"
    - mr_provisioner_ws_subprocess_version: "0.1"
    - mr_provisioner_ws_subprocess_source: "https://github.com/bwalex/ws-subprocess/releases/download/v{{mr_provisioner_ws_subprocess_version}}/ws-subprocess"
    - mr_provisioner_tftp_http_proxy_version: "0.4"
    - mr_provisioner_tftp_http_proxy_source: "https://github.com/bwalex/tftp-http-proxy/releases/download/v{{mr_provisioner_tftp_http_proxy_version}}/tftp-http-proxy"
    - mr_provisioner_kea_plugin_version: "0.1"
    - mr_provisioner_venv_path: "{{mr_provisioner_path}}/venv"
    - mr_provisioner_config: "/etc/mr-provisioner.ini"
    - mr_provisioner_banner: "My First Provisioner"
    - mr_provisioner_default_bootfile: "mlab-grubaa64.efi"
    - mr_provisioner_tftp_root: "/var/lib/mr-provisioner/tftp"
    - mr_provisioner_log_level: "DEBUG"
    - mr_provisioner_db_name: "provisioner"
    - mr_provisioner_db_user: "provisioner"
    - mr_provisioner_db_pass: "your password"
    - mr_provisioner_public_iface: "eth0" #access url
    - mr_provisioner_bmc_iface: "eth1" #used for tftp proxy
    - mr_provisioner_public_port: "5000"
    - mr_provisioner_services:
        - mr-provisioner
        - mr-provisioner-ws
        - mr-provisioner-tftp

    - mr_provisioner_app_secret: "{{ lookup('password', '/dev/null length=15 chars=ascii_letters') }}"

    - mr_provisioner_networks:
        - name: "bmc_network"
          subnet: "192.71.0.0/16"
          static_net: "192.71.0.0/16"
          reserved_net: ""
        - name: "machine_network"
          subnet: "192.70.16.0/20"
          static_net: "192.70.20.0/22"
          reserved_net: "192.70.24.0/22"
```

### For additional variables, please refer to defaults/main.yml and the kea.conf.j2 template.

# Usage:
```yaml

  pre_tasks:
    - apt:
        update_cache: yes
    - file:
        path: "{{item}}"
        state: directory
      with_items:
        - "{{mr_provisioner_build_path}}"
        - "{{mr_provisioner_path}}/bin"
        - "{{mr_provisioner_tftp_root}}"
        - "{{mr_provisioner_path}}/logs"
  roles:
    - mr-provisioner
```

### For Kea DHCP support please refer to this role :
https://github.com/Linaro/mr-provisioner-kea-dhcp4-role
