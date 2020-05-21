Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.box_url = "Vagrantfile"

    # virtualbox system configs
    config.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--memory", 1024]
        v.customize ["modifyvm", :id, "--cpus", 1]
    end
    
    config.ssh.forward_agent = true
    config.vm.synced_folder "vm", "/srv/"

    # Forwarded ports
    # config.vm.network :forwarded_port, guest: 8888, host: 18888, host_ip: "127.0.0.1"
    config.vm.network :forwarded_port, guest: 8889, host: 18889, host_ip: "127.0.0.1"
    # config.vm.network :forwarded_port, guest: 8890, host: 18890, host_ip: "127.0.0.1"


    # Salt configs
    config.vm.provision :salt do |salt|
        salt.minion_config = "vm/minion"
        salt.run_highstate = true
        salt.verbose = true

    end
end