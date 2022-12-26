# Secret Santa Drawing Tool

This is a digital drawing tool for the German game "Wichteln" to draw names to determine whom each participant will be giving a small gift to.  
**Important:** As the giver's identity is usually kept a secret until the gift is exchanged the user of this tool does not need to see the results of this tool.

## How to use

> 1. Start the script with a list of participants:
> ```shell
> python3 main.py Tick Trick Track
> ```
> 2. See the results in the `results/` folder. 
> This script creates a text file for each participant that contains to whom he should give a gift.

## Features
> - Ignores if the same name is given multiple times
> - Ensures that nobody gives himself a gift
> - In case of an incorrect result a validity check is made before writing the results to the output folder