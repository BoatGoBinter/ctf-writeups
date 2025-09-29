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
