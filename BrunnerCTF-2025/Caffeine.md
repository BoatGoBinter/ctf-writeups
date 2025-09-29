# Caffeine (50)

```
Author: Quack
This new coffee shop recently opened and you've been waiting too long for your daily caffeine injection!
Can you find a way to see a little more than just your order status?
```

Here is the website we are given.

<img width="400" height="250" alt="image" src="https://github.com/user-attachments/assets/e35b0a53-1720-413b-a0d6-0e7dcc14c11a" />

We can add orders and also search for orders through order ID. The vulnerability in the website is through the order ID we can execute code. In order to get the flag we need to get a reverse shell or some other remote code execution (RCE) on the server. 

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/34dacbd5-482b-4f32-a3e4-cc6996f80213" /> <br>

<img width="620" height="200" alt="image" src="https://github.com/user-attachments/assets/53868499-892e-40c6-8e8c-4aa6c25230f4" />

#### There a second part of this CTF which involves getting root access later.

# Caffeine (Root) (50)

Here is the second part of the website. Portablefan figured this one out and here is his brief explanation.

1. type sudo -l to find all sudo commands I can run.
2. there is only one command I can run. Run that
3. it says that brew [file] command reads a file
4. sudo brew ../../../root/root.txt
(sidenote: you can execute multiple shell commands by separating each command with semicolon)


<img width="556" height="793" alt="image" src="https://github.com/user-attachments/assets/b66737af-0320-44f8-acf6-8059d76d25f3" />

flag: brunner{5uD0_pR1V1L3g35_T00_h0t_F0r_J4v4_J4CK!}
