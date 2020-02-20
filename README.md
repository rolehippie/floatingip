# floatingip

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/floatingip/status.svg)](https://cloud.drone.io/rolehippie/floatingip)

Ansible role to configure floatingip

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

None.

## License

Apache-2.0

## Author

Thomas Boerger
