dqnc
==============================

DQN-based cooling & heating system 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


# Project introduction. 
This project aims to bring a new optimized cooling and heating system which will has the ability to reduce energy costs due to heating and cooling by up to 40%. 
The solution created in this project is based on deep Q-Learning network technique which is a subfield of the deep learning and much developed subfield of the reinforecement learning. 

# Parameters. 

- atmospheric_temperature: The monthly average atmospheric temperature.
- optimal_temperature: The optimal temperature range of the server, which we'll set as.
- min_temperature: The minimum temperature, below which the server fails to operate.
- max_temperature: The maximum temperature, above which the server fails to operate.
- min_number_users: The minimum number of users in the server.
- max_number_users: The maximum number of users in the server.
- max_update_users: The maximum change of users in the server per minute.
- min_rate_data: The minimum rate of data transmission in the server.
- max_rate_data: The maximum rate of data transmission in the server.
- max_update_data: The maximum change of the rate of data transmission per minute.
- out_range: The current temperature is within the range or not

# Variables.

- The temperature of the server at a given minute.
- current_number_users: The number of users connected to the server at a given minute.
- current_rate_data: The rate of data transmission at a given minute.
- total_energy_ai: The energy spent by the AI onto the server (to cool it down or heat it up) at a giving minute.
- total_energy_noai: The energy that would be spent by the classic server's cooling system.



# Asumptions. 

## First asumption: 
<br> 

The server temperature is apporximated since I don't have hestorical data of the server temperature. I apporximate the temperature through the multiple linear regression equation:

<em>Server temperature</em> =  <em>$ b_{\mathrm{0}\;}$ +  $ b_{\mathrm{1}\;}$ x Atmospheric temperature +  $ b_{\mathrm{2}\;}$ x number of users +  $ b_{\mathrm{3}\;}$ x Rate of data transmission.</em>


 <em>Where:</em> $ b_{\mathrm{0}\;}$ ${\in}$  ${\rm I\!R}$, $ b_{\mathrm{1}\;} > 0,\hspace{.1cm}  b_{\mathrm{2}\;} > 0,\hspace{.1cm}  b_{\mathrm{3}\;} > 0$. 


Assuming we performe the multiple linear regression and I get the values : 

$$
b_{\mathrm{0}\;} = 0,\hspace{.2cm}
b_{\mathrm{1}\;} = 1, \hspace{.2cm}
b_{\mathrm{2}\;} = 1.25\hspace{.2cm}
b_{\mathrm{3}\;} = 1.25
$$

then the equation becomes: 

<em>Server temperature</em> =  <em> Atmospheric temperature +  $ 1.25$ x number of users +  $ 1.25$ x Rate of data transmission.</em>

<br>
<br>
<br>

## Second assumption: 
<br>

The cost of energy needed to bring back the server into the optimal temperature are approximated also with a linear regression. 

$$
e_{\mathrm{hv}\;} = \alpha \vert T_{\mathrm{t+1}\;}-T_{\mathrm{t}\;}  \vert + \beta
$$

$\newline$ 

<em> where: 



$e_{\mathrm{hv}\;}$ : is the energy spent either for heating or ventilation to bring back the server to optimal range of temperature. 

$\vert T_{\mathrm{t+1}\;}-T_{\mathrm{t}\;}  \vert$ : is the temperature change in the server between t and t+1.

$\newline$ 

$\alpha > 0, \hspace{.2cm} \beta \in {\rm I\!R}$

and indeed we dont't have reel temperature data so I assume that the value after performing the linear regression :

$\alpha = 1 \hspace{.2cm}and\hspace{.2cm}  \beta = 0$.

therefore the assumption becomes : $e_{\mathrm{hv}\;} = \alpha \vert T_{\mathrm{t+1}\;}-T_{\mathrm{t}\;}  \vert$.

</em>

# Study case. 

We are dealing with a particular server located inside a data center that is governed by the preceeding list of parameters and variables. The number of users actively using the service is updated every minute as some new users sign up and some existing users log off.
Also, each minute some existing data is communicated outside the server and some new data is transmitted within, changing the server's internal data transmission rate. 

So, based on Assumption 1 from before, the server's temperature is updated once every minute. 
The AI or the classic cooling system are two potential solutions that can control the server's temperature. the classic cooling system mechanism automatically returns the server's temperature to within its ideal temperature range. 
The temperature of the server is updated every minute. If the server is using its classic cooling system, it keeps track on changes and updates the system if necessary so that the temperature stays within the range of ideal temperatures [18 degC, 24 degC] or move it past this boundary. The classic cooling system mechanism automatically lowers the temperature to the nearest bound of the optimal range, in this case 24C, if it exceeds the optimal range, for example to 30C. For the purposes of our simulation, we're assuming also that the classic cooling system can return the temperature to the ideal range in less than a minute, regardless of how large the difference in temperature is.

Instead, if the server is employing AI, its the classic cooling system is turned off, and the AI is responsible for updating the server's temperature in order to control it optimally. As opposed to the classic cooling system, the AI solution modifies the temperature after making certain forecasts in the past. The AI anticipates whether it should cool down the server, do nothing, or heat it up, and then takes action before there is a change in the number of users and the rate of data transmission, which would cause a change in the server's temperature. The temperature changes after that, and the AI repeats the process. 

Given that these two systems are different from one another, we can assess each one independently to compare how well it performs. For example, we could train or run the AI on a server while monitoring how much energy the classic cooling system would have consumed under the same conditions. The AI's main objective is to reduce the server's energy consumption, as a result, our AI must attempt to consume less energy than the server's non-intelligent cooling system would. Given that Assumption 2 stated above states that the energy used by every system on the server is proportional to the change in temperature within one unit of time:
$E_{\mathrm{t+1}\;} = \vert \Delta T_{\mathrm{t}\;}  \vert = \vert T_{\mathrm{t+1}\;}-T_{\mathrm{t}\;}  \vert$ 

therfore : 

$E_{\mathrm{t}\;} = E_{\mathrm{t+1}\;} - E_{\mathrm{t}\;} $  if $E_{\mathrm{t+1}\;} > E_{\mathrm{t}\;}$ (if the server is heated up)

$E_{\mathrm{t}\;} = E_{\mathrm{t}\;} - E_{\mathrm{t+1}\;} $  if $E_{\mathrm{t}\;} > E_{\mathrm{t+1}\;}$ (if the server is cooled down)


Thus, the difference in absolute temperature changes induced in the server between the AI and the unintelligent server's integrated cooling system between iteration t and iteration t+1 is equal to the energy saved by the AI at each iteration t (per minute): 

Energy saved by the AI between $t$ and $t +1$

$\vert \Delta T_{\mathrm{t}\;}^{noAI} \vert - \vert \Delta T_{\mathrm{t}\;}^{AI} \vert$ 


where: 

$\Delta T_{\mathrm{t}\;}^{noAI}$ : is is the change of temperature that the classic cooling
system would cause in the server during the iteration t, that is, from $t$ to $t +1$ minute. 

$\Delta T_{\mathrm{t}\;}^{AI}$ : is the change of temperature that the AI would cause in the server
during the iteration t, that is, from $t$  to $t +1$ minute.


