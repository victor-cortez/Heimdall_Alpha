# Heimdall_Alpha
A basic prototype of a project about internet-based cluster computing using the Ploxys as the task.



#How to use it:


#The master
  
  
  The master is the computer that will not perform the heavy computing, but distribute the tasks, the data, grab the results and etc.
  
  
  1- Execute the python script (make sure you have full access to your network and system)
  
  
  2- Type the number of rounds you want.
  
  
  3- Check the prints throughout the entire execution or simply check the data.txt file at the end of the execution.
  
#The slave
  
  
  The slave is the computer or core that will actually execute the heavy computing, it can exist inside the master machine (using another core or process for example) or in a different one. It can work through the internet, even from another continent. As it is a alpha stage, there is no safe way to take out the computer from the cluster without desynchronizing or interrupting the entire cluster, but you can add as much new slaves as you want in the cluster, at anytime you want, without worry.
  
  
  1- Execute the python script (make sure you have full access to your network and system)
  
  
  2- Type the IP address of your master
  
  
  3- Enjoy the prints, now you have a slave computing for you.
  
  
#The project
This system is the first implementation of an upcoming project about clustering and distributed computing to be used on any platform and to be accessible for every user. It has been developed focusing the reuse of old computers called UCA (which lack of hardware performance and bad OS made the project a failure in modern days, leading to abandonment and oblivion) and inspired by the Folding project by the Stanford University


About the UCA's (English) : https://www.youtube.com/watch?v=ovG_k2b3AXU (the UCA in this video is a little bit different from the used ones in this project)


More about the UCA's (Portuguese) : http://www.cceinfo.com.br/uca/ (Hardware information)| https://blog.ufba.br/ucabahia/nosso-blog/


Also check the ploxys directory for more information about the base-task of this implementation.


https://github.com/victor-cortez/ploxys

