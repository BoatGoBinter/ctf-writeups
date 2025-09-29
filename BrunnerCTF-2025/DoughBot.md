# DoughBot (20 points)

```
Author: rvsmvs

Our state-of-the-art smart mixer, DoughBot, crashed during a routine kneading cycle.
Luckily, a technician was monitoring the device over UART and captured the memory output just before the reboot.

Analyze the captured dump and see what the DoughBot was trying to say before it rebooted.
```
In this challenge, we are given a bin file with a log dump:

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/465911da-c4be-4cb0-9f8f-2e86a063bfa5" />

Right before it is rebooted, we see a dev note with a bootleg flag: "YnJ1bm5lcnttMXgzZF9zMWduYWxzXzRfc3VyZX0=". 
We immediately recognized this as base64 and converted it:

<img width="500" height="90" alt="image" src="https://github.com/user-attachments/assets/090dae67-faa0-41ba-a0bc-39e3b73bf4ed" />

Our flag: brunner{m1x3d_s1gnals_4_sure}
