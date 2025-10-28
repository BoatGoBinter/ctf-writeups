# Intergalactic Copyright Infringement
```
NASA received a notification from their ISP that it appeared that some copyrighted files were transferred to and from the ISS (Guess astronauts need movies too). We weren't able to recover the all of the files, but we were able to capture some traffic from the final download before the user signed off. If you can help recover the file that was downloaded perhaps you can shed some light on what they were doing?
```

We are given a pcapng file with traffic from and to BitTorrent. What we need to do is to recover the file that was downloaded. To do that let's go through the dumps.

In evidence.pcapng, lets find a packet from the BitTorrent protocol that has a high length.
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/23b7d88d-9c9b-4898-9b26-21669169fb65" />

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/66fa76b1-8279-4539-bee7-78b0d429e206" />

Now we have the stream. Let's run a script to extract the contents.

I made the script here: 
https://github.com/BoteGoesBinted/ctf-writeups/blob/main/SunshineCTF-2025/Intergalactic-Copyright-Infringement/reconstruct.py

From there we get the PDF file, and also the flag!

<img width="1549" height="1105" alt="image" src="https://github.com/user-attachments/assets/ff61f0da-fe0f-4b05-83b0-cdbe23d0fb45" />

flag: sun{4rggg_sp4c3_p1r4cy} 

I'll write a more detailed explanation of the code at a later point. But right now I'm working on GIS stuff.
