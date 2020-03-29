# WaveOracle: Surf Predictor Microservice

![couldnt_load_header][header-img]

---

TODO(jp): Descriptuon

## Setup, running & debugging

Note: `$ [commands here]` means use the terminal to insert those commands, you do not need to input the $ sign.

  1. Ensure python 3.7 is installed:  
    1.1 `$ sudo apt-get install python3`  
    1.2 `$ sudo apt-get install python3-pip`   
  2. Install the AWS CLI with homebrew: (if you don't have homebrew, see [here](https://docs.brew.sh/Installation))  
    2.1 `$ brew tap aws/tap`  
    2.2 `$ brew install aws-sam-cli`  
    2.3 `$ sam --version` --> should give you version info now (eg: `$ SAM CLI, version 0.46.2`)
  3. Building code:  
    3.1 run `$ sam build` and the code should build to .aws-sam/*  
    3.2 Building for debug / release coming **    
  4. Running code:  
    4.1 Run: `$ sam local invoke "SurfPredictor" -e events/__event-name__.json` - replace *event_name* with the event you want to trigger the function with.  
    4.2 Debug (VSCode): `$ sam local invoke "SurfPredictor" -e events/__event-name__.json -d 5890` - Note: Firstly you'll need the VSCode launch file (*.vscode/launch.json*), secondly the port numbers must match. 

## Architecture

![architecture-failed to-load][sys-architecture][]

## Data fetch
### Wind

**Source:** [Windguru][]

Wind data fetching will be performed by 2 components: 
  
  1. A webscraper: Encapsulates the html structure of the source
  2. A wind interface: Modifies data to the schema required by the system (will use the wind model)


### Swell

[header-img]: ./supporting-files/jbay_sunrise.png
[Windguru]: https://www.windguru.cz/68531
[sys-architecture]: ./supporting-files/Surf-Predictor-Architecture.png
