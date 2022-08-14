# A2C model
A2C er en asynkron deterministisk variant af A3C ([Asynchronous Advantage Actor Critic](https://arxiv.org/abs/1602.01783)), som igen er en variant af Actor-Critic, med et fokus på parallel træning https://lilianweng.github.io/posts/2018-04-08-policy-gradient/. Derfor bliver Actor-critic algoritmen beskrevet her. 
A2C modellen er valgt fordi den både fungere med diskrete og deterministiske miljøre https://stable-baselines3.readthedocs.io/en/master/guide/algos.html, og det er en af de fundementale agenter. 

Agenten ser en state, og skal tage en action ud fra dette. Dette gøres på baggrund af agentens 'policy'. Hele RL problemet er altså at finde den 'policy' der maksimere agentens belønning over tid.  

Agenten ved ikke hvordan dens actions påvirker miljøet. Derfor bliver dynamikken (miljøets dynamik) beskrevet med en sansynligheds fordeling.

$$P(s', r| s,a) $$
Sandsynligheden for at få statens s' og belønningen r, når man er i staten s, og vælger aktion a.
Værdierne kendes ikke, før vi begynder at ineragere med miljøet.

Da vi har med sansynligheder at gøre, skal vi tænke i forhold til forventede værdier. 
Expectation values er at tage alle muliige udfald ganget med sansynligheden med udfaldet, ganget med belønnignen for udfaldet. 
![[Pasted image 20220426093214.png]]

 En episode er når miljøet er kørt fra start til slut. 

En vigtigt ting er  value function:
Den afhænger af agentens policy og den nuværende state af miljøet, og giver os den forventede værdi af agentes belønning fra tiden t og staten s, antaget at vi følger policien. PI

Der er også  en lignende funktion, for værdien af staten og action paret, som fortæller og værdien for at tage action a og state s, og derefter følge policien. Det hedder action Value function Q

I virkeligheden løser vi ikke de ligninger, men vi approksimere dem vha. neurale netværk.
Vi tager nogle sampels af belønninger for miljøet, og bruger dem til at opdatere vægtene i netværkert. 

Estimatiting value state er vigtigt da den fortæller os værdien af den nuværende state, og værdierne af alle de fremtidige states, som agenten kan komme ud for.

Actor-critic metoden bruger 2 'deep neural networks'
Den ene approksimere agentens policy, hvilket kan gøres da det bare er en matematisk funcktion.

Det andet netværk kaldet kritik netværket. Det bruget til at approksimere value funktionen. Kritikkeren fortæller aktøren hvor god hver aktion er, baseret på om den resulterende state er værdifuld.

De to netværk arbejder sammen for at opdage hvordan agenten skal agere i miljøet. Aktøren vælger actions som kritkeren evaluere statesene,  og resultatet sammenlignes med belønningen fra miljøet
Med tiden vil kritikeren blive mere akkurat til at vurdere værdierne til statesne, hvilket gør at aktøren kan vælge de aktions som føre til de states.

Hvert netværk får en kost funcktion, som gør at vi kan opdatere deres vægte. 
Kost funktionen er delta, som er: ![[Pasted image 20220426103217.png]]
Det er summen af den nuværende belønning, samt den diskountede værdi for den nye state minus værdien for den nuværende state.

For kritikkeren er kosten delta^2.
Kosten for aktøren er:![[Pasted image 20220426103511.png]]
Og det skal vi bare acceptere, da det er lidt komplekst.
