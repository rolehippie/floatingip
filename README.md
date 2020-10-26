# floatingip

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/floatingip) [![Build Status](https://img.shields.io/drone/build/rolehippie/floatingip/master?logo=drone)](https://cloud.drone.io/rolehippie/floatingip) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/floatingip)](https://github.com/rolehippie/floatingip/blob/master/LICENSE) 

Ansible role to configure additional IPs for ifup. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [floatingip_devices](#floatingip_devices)
  * [floatingip_path](#floatingip_path)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### floatingip_devices

Definition of floating ip devices

#### Default value

```YAML
floatingip_devices: []
```

#### Example usage

```YAML
floatingip_devices:
  - config: 90-myinterface.cfg
    device: '{{ ansible_default_ipv4.interface }}:1'
    address: 1.2.3.4
    netmask: 255.255.255.255
```

### floatingip_path

Path to interface device definitions

#### Default value

```YAML
floatingip_path: /etc/network/interfaces.d
```

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
