### tools contain three scripts.

#### 1) gen_cluster.py\
   * generates a cluster with a separate number of cores, whose parameter values can be given through input.\
   * parameter values can directly be provided into the script as input.\
   * gives us a heterogeneous architecture in the generic .cfg format, which can be run directly on the sniper simulator.\
   * run through terminal with command: \
   
      ```
      $ python gen_cluster.py cluster_with_2_cores  //passing a new cluster through argument      
      ```
      
      
#### 2) make_config.py\
   * generates different config files with its own parameter values provided through input.\
   * parameter values for each config files can be directly provided into the script as input.\
   * gives us different architectures in the generic .cfg format, which can be directly run on sniper simulator.\   
   * run through the terminal with the command:\
      ```
      $ python make_config.py
      ```
   
   
#### 3) evaluate_sniper.py\
   * run the sniper simulator under the Deffe framework.\
   * parameter values are provided through the JSON Configuration, which formulates different architectural configurations.\
   * generates each of the simulation results based on those architectural configurations.
