# Introduction
BrunnerCTF is the first CTF me and my friend, "portablefan", have ever participated in. We are studying Data Science and Computer Science, respectively. With scarce cybersecurity knowledge, we decided to dive head first anyway. Let's see how we did!


<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/27b6b818-c633-4992-8bd1-d6faf3be0730" />

Hooray! Out of all the teams that captured at least one flag, we ranked 396 out of 1196, or roughly the 33rd percentile!
---
### In this writeup, I will go over all of the flags we captured (in order from mainly easiest to hardest), as well as our thoughts and the methods we conducted in order to capture each flag. 

<sub>The first two flags were verification, so I won't go over them, but for transparency, they were as follows: 

<sub> Sanity Check (10): Enter the flag given: brunner{n0w-y0u-kn0w-y0ur-C-T-F} 

<sub>Join the Discord (20): Read the discord's rules and check the announcement where there is a hidden comment: brunner{1t5_4_P13C3_0f_c4K3_T0_B4k3_4_pr3TTy_C4k3!}.</sub>

# DoughBot

```
Difficulty: Beginner
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

# Where Robots Cannot Search

```
Difficulty: Beginner
Author: The Mikkel

Ahh, the Brunnerne company.
But they have a secret, hidden away from robot search.
```

In this challenge, we are greeted with a website this time.

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/bd2be517-ad8b-4f75-b85f-4f2bba7c4d38" />

The trick to this one is to read the title of the challenge: _Where Robots Cannot Search..._

One Google search later:

<img width="300" height="100" alt="image" src="https://github.com/user-attachments/assets/9b69979d-8f7b-45bf-95f7-120a17f8c4cb" />



<img width="500" height="180" alt="image" src="https://github.com/user-attachments/assets/07c3c62e-b78d-438b-9eec-2aa8906e593a" /> <img width="500" height="180" alt="image" src="https://github.com/user-attachments/assets/ecc4d434-998d-4096-982c-0e755a54bcb8" />

Our flag: brunner{r0bot5_sh0u1d_nOt_637_h3re_b0t_You_g07_h3re}





