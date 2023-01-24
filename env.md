Programming Environment
-----------------------

Laptops are required for all CPSC courses and should be available in the classroom each day.

Unless otherwise specified, programming assignments for this course have been tested to work in an environment similar to the following:

- Linux kernel version: 5.10
- Architecture: [x64](https://en.wikipedia.org/wiki/X86-64)
- `python` version: 3.9
- `gcc` version: 10.2
- `make` version: 4.3

While assignments are generally designed to work in a wide variety of environments, it is strongly recommended to have an environment as close to the one described above as possible. If you do not run x64 Linux natively on your machine, a virtualized environment can used via tools such as [QEMU](https://www.qemu.org/), [virt-manager](https://virt-manager.org/), or [VirtualBox](https://www.virtualbox.org/).

It is recommended to install a Debian-based distribution such as Debian itself, Ubuntu, or Kali. You can either download the install media and run through the installation process yourself or you can download a pre-installed image from a provider such as [Linux VM Images](https://www.linuxvmimages.com/)  or [OSBoxes](https://www.osboxes.org/).

The following are explicitly unsupported:

- Python versions prior to 3.7, as these are [no longer officially supported](https://devguide.python.org/versions/).
- Any compiled programs for architectures other than x64. If you are using a machine with a different architecture, you will need a virtualized x64 environment.

M1/M2 Mac Setup
---------------

M1 and M2 Macs may be especially challenging to get working VMs due to not all software being ported to the architecture yet. The following should work to get x64 VMs working using QEMU.

1. Install xcode by running the following in your terminal:

```sh
xcode-select --install
```

Follow on-screen prompts and approve the agreement.

2. Install Homebrew (`brew`) which will allow us to install other packages by running the following command:

```
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh | sh
```

Alternative Environments
------------------------

- Google Cloud Platform (Free e2-micro instance)
- Amazon Web Services (Free credits for first year)