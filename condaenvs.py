## Make sure that you run the command prompt and powershell prompt as Administrator if not done so already

PS C:\WINDOWS\system32> conda install -c conda-forge conda                                   		 ## We are first going to test out package installation
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\ProgramData\Anaconda3

  added / updated specs:
    - conda


The following packages will be UPDATED:

  conda                       pkgs/main::conda-4.8.5-py38_0 --> conda-forge::conda-4.8.5-py38h32f6830_1


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done





## https://towardsdatascience.com/13-conda-commands-for-data-scientists-e443d275eb89
## Next, we want to test out environments in the powershell.
## We will use the <conda create -n firstenv> function


(base) PS C:\Users\andem> conda create -n firstenv
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.8.3
  latest version: 4.8.5

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\andem\.conda\envs\firstenv



Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate firstenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) PS C:\Users\andem> conda activate firstenv
(firstenv) PS C:\Users\andem>                                                					  ## Notice that the command line now begins with (firstenv) instead of (base)





## Next, lets deactivate the environment so we can update our outdated version of python.
(firstenv) PS C:\Users\andem> conda deactivate
(base) PS C:\Users\andem>                                                               ## We are back in the base environment.

(base) PS C:\Users\andem> conda update -n base -c defaults conda                        ## Update the conda package
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\ProgramData\Anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.8.5                |           py38_0         2.9 MB
    ------------------------------------------------------------
                                           Total:         2.9 MB

The following packages will be UPDATED:

  conda                                        4.8.3-py38_0 --> 4.8.5-py38_0


Proceed ([y]/n)? y



##This is the step that I am stuck at. Error message:
EnvironmentNotWritableError: The current user does not have write permissions to the target environment.
  environment location: C:\ProgramData\Anaconda3
## Got past this by running PowerShell Prompt as Administrator which I had forgotten to do lol##



(firstenv) PS C:\WINDOWS\system32> conda --version
conda 4.8.3
(firstenv) PS C:\WINDOWS\system32> conda update -n base -c defaults conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\ProgramData\Anaconda3

  added / updated specs:
    - conda


The following packages will be UPDATED:

  conda                                        4.8.3-py38_0 --> 4.8.5-py38_0


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(firstenv) PS C:\WINDOWS\system32> conda --version
conda 4.8.5                                                                                 ## This is the version we wanted!


## Next, we want to install some popular packages for data science using this format.
(firstenv) PS C:\WINDOWS\system32> conda install conda-forge pandas


