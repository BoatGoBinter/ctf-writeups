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
