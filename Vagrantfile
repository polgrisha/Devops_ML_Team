Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.box_url = "Vagrantfile"

    config.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--memory", 1024]
        v.customize ["modifyvm", :id, "--cpus", 1]
    end
    
    config.ssh.forward_agent = true

    config.vm.synced_folder "vm", "/srv/"

    # config.vm.network :forwarded_port, guest: 8888, host: 18888, host_ip: "127.0.0.1"
    config.vm.network :forwarded_port, guest: 8889, host: 18889, host_ip: "127.0.0.1"
    # config.vm.network :forwarded_port, guest: 8890, host: 18890, host_ip: "127.0.0.1"

    # config.vm.provision "shell", inline: <<-SHELL
    #     sudo apt-get update
    #     sudo apt-get install software-properties-common
    #     sudo add-apt-repository ppa:deadsnakes/ppa 
    #     sudo apt-get -y install python3.6
    # SHELL

    ## Set your salt configs here
    config.vm.provision :salt do |salt|

        ## Minion config is set to ``file_client: local`` for masterless
        salt.minion_config = "vm/minion"

        ## Installs our example formula in "salt/roots/salt"
        salt.run_highstate = true

        ## Display salt highstate output
        salt.verbose = true

    end
end