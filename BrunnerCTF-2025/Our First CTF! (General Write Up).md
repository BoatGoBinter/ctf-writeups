# Introduction
BrunnerCTF was the first CTF my friend, "portablefan," and I had ever participated in. We are studying Computer Science and Data Science, respectively. With scarce cybersecurity knowledge, we decided to dive head first anyway. Let's see how we did!


<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/27b6b818-c633-4992-8bd1-d6faf3be0730" />

Hooray! Out of all the teams that captured at least one flag, we ranked 396 out of 1196, or roughly the top 33rd percentile!
---
In this writeup, I will go over all of the flags we captured (from least to most points, so easiest at start), as well as our thoughts and the methods we conducted in order to capture each flag.<br>
<sub><sub>The first two flags were verification, so I won't go over them, but for transparency, they were as follows:<br> 
<sub><sub>Sanity Check (10): Enter the flag given: brunner{n0w-y0u-kn0w-y0ur-C-T-F} <br>
<sub><sub>Join the Discord (20): Read the discord's rules and check the announcement where there is a hidden comment: brunner{1t5_4_P13C3_0f_c4K3_T0_B4k3_4_pr3TTy_C4k3!}.</sub>

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

# Where Robots Cannot Search (30)

```
Author: The Mikkel

Ahh, the Brunnerne company.
But they have a secret, hidden away from robot search.
```

In this challenge, we are greeted with a website this time.

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/bd2be517-ad8b-4f75-b85f-4f2bba7c4d38" />

The trick to this one is to read the title of the challenge: _Where Robots Cannot Search..._

One Google search later:

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/9b69979d-8f7b-45bf-95f7-120a17f8c4cb" />

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/07c3c62e-b78d-438b-9eec-2aa8906e593a" /><img width="500" height="180" alt="image" src="https://github.com/user-attachments/assets/ecc4d434-998d-4096-982c-0e755a54bcb8" />

Our flag: brunner{r0bot5_sh0u1d_nOt_637_h3re_b0t_You_g07_h3re}

# The Great Mainframe Bake-off (30)

```
Author: H4N5

It's 1974. Deep inside the crusty vaults of CrumbTrust Bank, a covert team of COBOL developers and pastry chefs created a
failsafe for their most prized possession: The Marzipan Reverse Recipe.

This sacred document was too valuable to be stored on paper.
So, they did the unthinkable - they encoded it and buried it in the production mainframe under a fake batch job titled IEBCAKED.
Only those with knowledge of both banking ops and baking science could ever retrieve it.

Years later, the IEBCAKED job has mysteriously reappeared in the job output spool of an IBM z/OS LPAR.
But what's left is a string of mysterious byte codes.
It's clearly not hex, not ASCII... maybe something older... something only the graybeards of computing would recognize.

Can you decipher the original recipe and unlock the secret to the perfect butterbyte tart?

d0-85-97-89-83-85-d9-6d-85-a2-99-85-a5-85-d9-6d-95-81-97-89-a9-99-81-d4-6d-85-88-e3-6d-a2-c9-6d-a2-89-88-e3-6d-84-95-c1-6d-a2-85-94-81-99-c6-95-89-
81-d4-6d-95-d6-6d-f0-f7-f9-f1-6d-85-88-e3-6d-95-c9-6d-84-85-a2-e4-6d-a2-81-e6-6d-c3-c9-c4-c3-c2-c5-c0-99-85-95-95-a4-99-82
```

We know its a ciphered text. And we are given the year 1974. So, let's think about what byte codes were used in 1974 and prior? ASCII? They said no? Hmmm. Let's google.

<img width="600" height="150" alt="image" src="https://github.com/user-attachments/assets/22bb46a2-5167-4a18-b089-70e435e592ce" />

EBCDIC it is. Let's decode it. 

<img width="1634" height="419" alt="image" src="https://github.com/user-attachments/assets/9b4fce40-93e1-497f-ac4c-b8cdc6fc27da" />

When we decode we got a string thats reversed. When we reverse we get the flag: brunner{EBCDIC_Was_Used_In_The_1970_On_MainFrames_And_This_Is_The_Marzipan_Reverse_Recipe}

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

Flag: brunner{b4k3r_br14n_w1ll_b3_r1ch!}  (Tip: Don't try to install ncat on University Wifi!)

# Insanity Check (30)

```
Author: OddNorseman

Our CTF page is pretty cool, right? Nom nom nom
```

Go to https://ctf.brunnerne.dk/. 

we can go into the JavaScript code on the website. 

```
  let g = [
    84, 68,  67, 88, 88,  83, 68, 77,  79,  6,  67, 105, 82, 7,
    82, 105, 7,  66, 23,  23, 23, 105, 88,  6,  65, 105, 66, 68,
    79, 105, 66, 6,  105, 2,  85, 66,  67,  2,  90, 90,  79, 105,
    70, 90,  2,  79, 105, 66, 94, 5,   105, 85, 66, 80,  75
  ];
```

Each of these numbers is XOR-encoded using the number 54.
Decode Here:

```
g = g.map(j => j ^ 54); 

let decoded = g.map(L => String.fromCharCode(L)).join("");

console.log(decoded);
```
Output: brunner{y0u_d1d_1t!!!_n0w_try_t0_4ctu4lly_pl4y_th3_ctf}

Alternatively,  Eat the brunners!!! 1337 of them and feel your sanity drop!!!!!!

# Cookie Jar (40)

```
Author: Quack

We just got our hands on grandma's legendary cookie jar! What delicious treats could she be hiding here?
```
We are given a webpage. 

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/3d48a34d-7b11-49bd-a9eb-bc944cc48b43" />

Initially we were stumped. There's nothing to do... However, portablefan caught on to the name of the challenge. _**Cookie**_ Jar. Cookies!

<img width="2466" height="246" alt="image" src="https://github.com/user-attachments/assets/cf2f81a9-c291-47d2-ba78-5710df1b5e4b" />

Change the false to true and we get: 

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/636fc96b-011b-4349-880e-7d7f7ed8a45f" />

flag: brunner{C00k135_4R3_p0W3rFu1_4nD_D3l1c10u5!}

# The Baking Case (40)

```
Author: H4N5

I hid a message for you here, see if you can find it! Take it slow, little by little, bit by bit.

i UseD to coDE liKe A sLEEp-dEprIVed SqUirRel smasHInG keYs HOPinG BugS would dISApPear THrOugh fEAr
tHeN i sPilled cOFfeE On mY LaPTop sCReameD
iNTerNALly And bakeD BanaNa bREAd oUt oF PAnIc TuRNs OUT doUGh IS EasIEr tO dEbUG ThaN jaVASCrIPt
Now I whIsPeR SWEEt NOtHIngs TO sOurDoUGh StARtERs aNd ThReATEN CrOissaNts IF they DoN'T rIsE My OVeN haS fEWeR
CRasHEs tHAN mY oLD DEV sErvER aNd WHeN THInGS BurN i jUSt cAlL iT cARAMElIzEd FeatUReS no moRE meetInGS ThAt coUlD HAVE
bEeN emailS JUst MufFInS THAt COulD HAvE BEen CupCAkes i OnCE tRIeD tO GiT PuSh MY cInnAmON rOLLs aND paNICkED WHEn
I coUldn't reVErt ThEm NOw i liVe IN PeaCE uNLESs tHe yEast getS IDeas abOVe iTs StATion oR a COOkiE TrIES To
sEgfAult my toOTH FILlings

```

So, this one took a while. The first thing we thought was reading the description. "Little by little" caught my eye. Neither of us are steganography experts so I googled "little by little steganography" and ended up with a result about "Least Significant Bit (LSB)". This brought us down a rabbithole that didn't give any help. 

Our next approach was to take the uppercase and lowercase and change them into zeros and ones. 

Here is the code I wrote.
```
a = "i UseD to coDE liKe A sLEEp-dEprIVed SqUirRel smasHInG keYs HOPinG BugS would dISApPear THrOugh fEAr tHeN i sPilled cOFfeE On mY LaPTop sCReameD iNTerNALly And bakeD BanaNa bREAd oUt oF PAnIc TuRNs OUT doUGh IS EasIEr tO dEbUG ThaN jaVASCrIPt Now I whIsPeR SWEEt NOtHIngs TO sOurDoUGh StARtERs aNd ThReATEN CrOissaNts IF they DoN'T rIsE My OVeN haS fEWeR CRasHEs tHAN mY oLD DEV sErvER aNd WHeN THInGS BurN i jUSt cAlL iT cARAMElIzEd FeatUReS no moRE meetInGS ThAt coUlD HAVE bEeN emailS JUst MufFInS THAt COulD HAvE BEen CupCAkes i OnCE tRIeD tO GiT PuSh MY cInnAmON rOLLs aND paNICkED WHEn I coUldn't reVErt ThEm NOw i liVe IN PeaCE uNLESs tHe yEast getS IDeas abOVe iTs StATion oR a COOkiE TrIES To sEgfAult my toOTH FILlings"
binary_str = ""

for i in a:
   if i.isupper():
     binary_str += "1"
   elif i.islower()
      binary_str += "0"

print(binary_str)
```
output & conversion:

<img width="1792" height="342" alt="image" src="https://github.com/user-attachments/assets/580e7b71-0c06-40bf-8107-57488835c2a4" />

flag: brunner{I_like_Baking_More_That_Programming}

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

# Whisk (40)

```
Author: rvsms

Someone tried sabotaging our operation by "whisking” away the secret ingredient for the perfect brunsviger.
All that's left on the workbench is this sticky note full of pastry-themed symbols and random letters.

Can you help us recover the secret ingredient?
```

Here is the text we are given. 

```
DR🥐 C🥐TZ🥐D 🧁SXZ🥐A🧁🥐SD 🧁C 🍰KE🍰FC K🍩M🥐. D🍩 O🍰Q🥐 🍰 Y🥐ZP🥐TD
OZ🥖SCM🧁X🥐Z, H🥐KD O🥖DD🥐Z E🧁DR OZ🍩ES C🥖X🍰Z, Y🍩🥖Z 🧁D 🍩M🥐Z DR🥐 E🍰ZH
A🍩🥖XR, 🍰SA K🥐D DR🥐 CFZ🥖Y C🥐🥐Y 🧁SD🍩 🥐M🥐ZF T🍩ZS🥐Z. D🍰CD🥐, CH🧁K🥐,
🍰SA Z🥐H🥐HO🥐Z: CR🍰Z🧁SX Y🍰CDZF N🍩F 🧁C H🍰SA🍰D🍩ZF.
OZ🥖SS🥐Z{S0_H0Z3_K🥖HYF_T1YR3Z}
```

A substitution cipher. We know that "OZ🥖SS🥐Z" in the last line is brunner. So replace O with b, Z with r, and so on. Until the entire ingrediant is decrypted. 

<img width="600" height="175" alt="image" src="https://github.com/user-attachments/assets/0c0c16f3-a70b-4beb-94a5-6e5304baf9ea" />
flag: brunner{n0_m0r3_lumpy_c1h3r}


# Based Brunner (40)

```
Author: Nissen

Brunsviger is just so based, I think I could eat it in any form - from binary to decimal!

Tip: This might require a bit of programming, I would recommend looking into the int() function in Python.
```
In this challenge we are given an encoded text file and the way it was encoded via a python file.

encode.py:
```
def encode_char(ch: str, base: int) -> str:
    """
    Encode a single character into a string of digits in the given base
    """
    value = ord(ch)
    digits = []
    while value > 0:
        digits.append(str(value % base))
        value //= base

    return "".join(reversed(digits))


with open("flag.txt") as f:
    text = f.read().strip()

# Encode the text with all bases from decimal to binary
for base in range(10, 1, -1):
    text = " ".join(encode_char(ch, base) for ch in text)

with open("based.txt", "w") as f:
    f.write(text)

```

As said in the tip, it requires so programming. I think we should let the CS student do this explaining. PLEASE CHECK HIS GITHUB OUT!!!: 
https://github.com/billpark1234/ctf-writeup/blob/main/20250824-BrunnerCTF/based-brunner.md

Code:
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/ccd51bde-a848-43b0-ab31-27e76ad84092" />

flag: brunner{1s_b4s3d}

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

# The Secret Brunsviger (50)

```
Author: Ha1fdan

I have intercepted encrypted HTTPS traffic from the secret brunsviger baking forum, but I need help decrypting it.
```

In this challenge, we are given 2 files, a packet capture and the SSL/TLS secrets log file, generated by NSS.

In order to get the flag, we use WireShark and open the TLS protocol on the packet capture and use the logs file as the Master-secret log filename.

<img width="1024" height="620" alt="image" src="https://github.com/user-attachments/assets/d6070a01-ed1a-4ba5-ba22-c2f417eca8e8" />


The secret is encoded in base64. So we just decode it:

```
└─$ echo "YnJ1bm5lcntTM2NyM3RfQnJ1bnp2MWczcl9SM2MxcDNfRnIwbV9HcjRuZG00c19DMDBrYjAwa30=" | base64 -d
brunner{S3cr3t_Brunzv1g3r_R3c1p3_Fr0m_Gr4ndm4s_C00kb00k}          
```
Flag: brunner{S3cr3t_Brunzv1g3r_R3c1p3_Fr0m_Gr4ndm4s_C00kb00k}

# Caffeine (Root) (50)

Here is the second part of the website. Portablefan figured this one out and here is his brief explanation.

1. type sudo -l to find all sudo commands I can run.
2. there is only one command I can run. Run that
3. it says that brew [file] command reads a file
4. sudo brew ../../../root/root.txt
(sidenote: you can execute multiple shell commands by separating each command with semicolon)


<img width="556" height="793" alt="image" src="https://github.com/user-attachments/assets/b66737af-0320-44f8-acf6-8059d76d25f3" />

flag: brunner{5uD0_pR1V1L3g35_T00_h0t_F0r_J4v4_J4CK!}


# There Is a Lovely Land (100)

```
The Danish national anthem is called "Der er et yndigt land" ("There Is a Lovely Land"), and I fully agree.

A friend of mine took this picture, but I don't know the name of the bridge! Please help me find it so I can go see it!

Flag format: brunner{<bridge name in Danish in lowercase>}
```
Here is the bridge:
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/9c19d8f4-47bd-44c7-917a-731a47a2ae67" />


The strategy was simple. Go through Denmark's waterways and find bridges. What I didn't expect was to find it in the first try. 

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/89be6c1d-1054-4aec-b860-20902b35019a" />

The reasoning behind choosing this location is likely based off a few things, but I'd likely attribute it to Geoguessing on Geoguessr.
My initial thought was that it can't be a river but rather a much larger body of water. The bridge has to be straight unlike the one south of it. And it should be in a more rural but still inner Denmark with land on both sides. That's how I landed on this bridge first try.

Flag: brunner{sallingsundbroen}

# Train Mania

```
Author: Quack

I recently stumpled upon this cool train! But I'd like to know a bit more about it...
Can you please tell me the operating company, model number and its maximum service speed (km/h in regular traffic)?

The flag format is brunner{OPERATOR-MODELNUMBER-SERVICESPEED}.
So if the operator you have found is DSB, the model number RB1, and the maximum service speed is 173 km/h, the flag would be brunner{DSB-RB1-173}.
```

We are given an mp4 of a train moving. One frame in the video was enough to give away very important details.

<img width="500" height="450" alt="image" src="https://github.com/user-attachments/assets/dda47475-5940-46ab-af5b-7a5f0790db9c" />

On the train it says "SJ", A Swedish train company. And on wikipedia we can find the train, the X2000.

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/7baf7b59-7748-4947-8afa-048c7fef6151" />

Another search shows 200km/hr. 

So for our final flag: brunner{SJ-X2-200}

# Conclusion

There are a few other flags we captured, which I will add later when I get the time.

In total we spent about 6-7 hours (6,7 lol) on the CTF with some breaks. It was great fun and I can't wait to go into the next one after I do a lot more studying. Thanks for the fun and cheers.

Please check out the creators of the CTF BrunnerNE: https://dk.linkedin.com/company/brunnerne.
