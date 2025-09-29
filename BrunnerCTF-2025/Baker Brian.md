# Baker Brian (30)
```
Author: Nissen

Baker Brian says he has a plan to make him super rich, but he refuses to share any details 😠
Can you access his Cake Vault where he keeps all his business secrets?

Info: The challenge has both a file download and a server to connect to. Please click "Start Challenge"
below and wait a minute for your team's challenge instance to start, then connect to the server from a terminal with the command that appears.

```

We are given a python file to read through to analyze Brian's security system. It has a username and a password that is created with if statements. Here is the solution. You can read the if statements and match them up with the password.

```
if username != "Br14n_th3_b3st_c4k3_b4k3r":
    print("❌ Go away, only Baker Brian has access!")
    exit()
```
This is before the password, meaning that the username is Br14n_th3_b3st_c4k3_b4k3r.

<img width="3059" height="1863" alt="image" src="https://github.com/user-attachments/assets/33ed435c-cc76-44d1-89ee-2319f19a6b9f" />

Flag: brunner{b4k3r_br14n_w1ll_b3_r1ch!} 
