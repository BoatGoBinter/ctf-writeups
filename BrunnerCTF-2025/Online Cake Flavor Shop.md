# Online Cake Flavour Shop (40)

```
Author: olexmeister

Brunnerne made an online flavour shop! Your wildest dreams can be fulfilled, it's actually hard to WRAP your head AROUND how amazing this software is!
nc cake-flavour-shop.challs.brunnerne.xyz 33000

```

In this challenge, we open a TCP connection to the flavor shop server. We can only sample a few cake flavors. But the flavor we want is $100 and we can't afford it!

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/6f121548-1a61-456d-b8a2-62eeabde9708" />

Luckily in the the provided Python code we can see a very simple vulnerability. Overflow. It can only process an integer number. So let's input a number bigger than an integr for the amount of bruner flavors I want to test.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/02956d39-85e1-4c9c-a11c-33ac4f180603" />

flag: brunner{wh0_kn3w_int3g3rs_c0uld_m4k3_y0u_rich}
