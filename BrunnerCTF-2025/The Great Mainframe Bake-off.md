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
