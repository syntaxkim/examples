# Systemd
2019-01-12

[Tutorial](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)

## Introduction
Systemd init system operates on and manage system resources such as services, network, devices, etc.
These resources are defined using configuration files called unit files.
Therefore, units are the objects that systemd knows how to manage.
Unlike many other init systems, systemd provides simple declarative syntax.

## Location
- System's unit files location: /lib/systemd/system (You should not edit files in this directory)
- In-between priority location: /run/systemd/system (Only used by systemd process itself)
- Override files location:      /etc/systemd/system (This will supersede the files in general location)

### How to override only specific directives.
Create a subdirectory named after the unit file .d appened on the end.
Within this directory a file ending .conf can be used to override or extend the system's unit file.
For example,
```
$cat /lib/systemd/system/apache2.service
[Service]
Type=forking
PrivateTmp=true
Restart=on-abort

$cat /lib/systemd/system/apache2.service.d/apache2-systemd.conf
[Service]
Type=forking
RemainAfterExit=no
```

## Types of Units
Each unit file has its suffix that describes the type of it. For example,
* .service: Management of a service or application
* .socket: A network or IPC socket, or a FIFO buffer
* .target: Synchronization points for other units
* .timer: Similar to a `cron` job for delayed or scheduled activation.
* .device, .mount, .automount, .swap, .path, .snapshot, .slice, .scope

## Anatomy of a Unit File (.service)
```
[Section1]
Directive1=value
Directive2=value
```
* Section names are well defined and case-sensitive.
* If you need to add non-standard sections, add a X- prefix to the section name.
* The default value can be eliminated in an override file by an empty string.
```
Directive1=
```
* Accpeted boolean expressions: 1, yes, on, true / 0, no off, false

### [Unit] Section Directives
This section comes in first in most unit files.
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
```
* Description=:the name and basic functionality
* Requires=:a list of any units upon which this unit essentially depends
* Wants=:Less strict than Requires= (Recommended way for most dependency relationships)
* After=:Start the current unit after the units listed in this directive
* Before=:The opposite to After=
* Documentation=, BindsTo=, Conficts=, etc.

### [Install] Section Directives (optional)
This section often comes as the last section.
```
[Install]
WantedBy=multi-user.target
```
* WantedBy=:The most common way to specify how a unit should be enabled.
* RequiredBy=, Alias=, Also=, DefaultInstance=

### Unit-Specific Section Directives (In between [Unit] and [Install] sections)
#### [Service] Section Directives (.service)
* Type=:`simple` is the default value if it's not set.
* PIDFile=
* ExecStart=
* ExecReload=
* ExecStop=
* Restart=

#### [Socket] Section Directives (.socket)
Socket units are commonly used to provide better parallelization and flexibility.
* ListenStream=:An address for a stream socket for TCP services.
* ListenDatagram=:An address for a datagram socket for UDP services.

#### [Timer] Section Directives (.timer)
Timer units are used to schedule tasks to operate at a specific time or after a certain delay.
This unit type replaces or supplements some of the functionality of the cron and at daemons.