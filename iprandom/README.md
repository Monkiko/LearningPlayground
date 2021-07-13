# IPRandom
Generate random CIDR IP Address (useful for practicing subnetting)

###Usage
#####- Run script to generate  a random CIDR ip address
#####- Check answer using the following site: http://www.ipaddressguide.com/cidr


###Requirements

#####- Requires Python (Tested using Python 2.7.x)
#####- Can be installed on the cbast or local machine if Python is installed


###Installation

Check your PATH variable:

	echo $PATH
	
Example output:

	/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/usefulscripts/ht/bin:/home/ian8775/.local/bin:/home/ian8775/bin
	
I recommend appending :$HOME/bin to your path as follows:

	nano .bash_profile
	
	# .bash_profile
	
	# Get the aliases and functions
	
	if [ -f ~/.bashrc ]; then
	. ~/.bashrc
	fi
	
	#User specific environment and startup programs
	
	PATH=$PATH:$HOME/.local/bin:$HOME/bin
	
	export PATH

Setup the file:

	mkdir bin
	cd bin
	touch iprandom; chmod +x iprandom; nano iprandom
	
Copy the raw code from [here](https://raw.github.rackspace.com/ian8775/iprandom/master/iprandom?token=AAAV2Tbpbicb-JaWrRSqTJrOnJXa06Ufks5YLe4UwA%3D%3D) and then paste it in the editor.

Now you can run the program:

	iprandom
	212.244.136.25/26
	
Enjoy!
