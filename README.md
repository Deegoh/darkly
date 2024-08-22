# Darkly
Introductory project to computer security in the specific field of the web, this project will have you dissect a vulnerable website. In doing so, you will develop your own approach to thinking about security in a web application and become aware of issues related to simple development errors, both from a programming and a design perspective.

## Installation
For this project, you have to install a VM with the ISO file Darkly.iso
In my case, I used Qemu:

- Install brew if isn't already done
- brew install qemu

Now, we create a dedicated space for the VM:
- qemu-img create -f qcow2 darkly.qcow2 20G

After, the creation of the space, we will launch the VM with Qemu:
- sudo qemu-system-x86_64 -hda darkly.qcow2 -cdrom Darkly_i386.iso -m 2G -nic vmnet-bridged,ifname=en0
Caution: 
	On my laptop, Network do not have privilage to be created, it is why we used sudo mode.

