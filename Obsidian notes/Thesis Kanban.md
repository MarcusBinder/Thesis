---

kanban-plugin: basic

---

## Someday

- [ ] Look into dynamic floris https://github.com/MarcusBecker-GitHub/FLORIDyn_Matlab<br>#Someday
- [ ] UC berkley kursus om RL<br>http://rail.eecs.berkeley.edu/deeprlcourse/
- [ ] Maybe read this blog post <br>https://lilianweng.github.io/posts/2018-04-08-policy-gradient/


## To do, low priority

- [ ] Make a short picture detailing what turbine is what in the "simulation"
- [ ] Afsnit hvor du træner agenten på en nedskaleret setup, også tester på virkelige vindfarme
- [ ] Lav et NN, som giver power output af farmen.
- [ ] Papers som forklare GCH:<br>Control-oriented model for secondary effects of wake steering <br><br>Sensitivity and uncertainty of the FLORIS model applied on the lillgrund wind farm
- [ ] Add back in the scaling factor to Floris<br>#Brainless
- [ ] Add to intro that layout optimization is a thing
- [ ] man kunne lave power og thrust coefficienter som en funktion. Evt se paper: Integrated wind farm layout and control optimization. figur 1


## To do, high pririty

- [ ] Lav tabel om beregningstid af GCH og curl model for 1-30 møller
- [ ] Deep Reinforcement Learning for Automatic Generation Control of Wind Farms<br>tjek det paper.<br>Det har intro som minder om mit RL intro


## Waiting

- [ ] 


## Doing

- [ ] Undersøg damage i floris


## Done

- [ ] Spinning up code algorithms<br>#thinking
- [ ] "code algorithm"<br>#thinking
- [ ] Lav en liste over hvilke parametre der kan tunes, i forhold til optuna TD3<br>https://stable-baselines3.readthedocs.io/en/master/modules/td3.html
- [ ] Read about and choose algorithm<br>#thinking
- [ ] Se og kod det her: https://www.youtube.com/watch?v=ZhFO8EWADmY
- [ ] Sæt discount factor til 0 og se hvad det gør af forskel!
- [ ] Look into transfer learning<br>[[Transfer learning]]
- [ ] Add a twist for the introduction so that it covers some of the problems with wind power.
- [ ] Power point for meetingg
- [ ] Make colors for plots the same<br>So wind_color is all the same and so on...
- [ ] Change environment so that the upper and lower limits are hardcoded, on the observations, but the limits still sample.
- [ ] Lav et nyt environment så den sampler hele tiden en ny state.
- [ ] Create different environments and an overview of them
- [ ] Find limits for yaw angels Floris<br>#thinking<br>Wainting on guthub reply
- [ ] Make overview and train some agents
- [ ] Change reward to be percentage increase and test it a bit
- [ ] Make code that can compare the trained agents
- [ ] Make code so that trained agent can be loaded on windows.<br>https://github.com/hill-a/stable-baselines/issues/1024
- [ ] Make docs for overview of trained agents
- [ ] Create plots like YT video for introduction about future power<br>2050 projections<br>#Brainless
- [ ] Do the overleaf layout
- [ ] Get tensorboard to work
- [ ] Update Floris
- [ ] Create + refine environment for RL
- [ ] Reinforcement learning tutorial https://www.youtube.com/watch?v=XbWhJdQgi7E
- [ ] Create overleaf document<br>#admin
- [ ] Do this course https://www.youtube.com/watch?v=Mut_u40Sqz4&t=1011s<br>#maybe
- [ ] Read/watch Multi-agent Reinforcement learning 10 min
- [ ] Do petting zoo tutorial https://towardsdatascience.com/multi-agent-deep-reinforcement-learning-in-15-lines-of-code-using-pettingzoo-e0b963c0820b
- [ ] Create new timers <br>#admin
- [ ] Do RLVS 2021 course<br>Videos done 4/24 <br>https://www.youtube.com/playlist?list=PLJct-r1rjHKmqdcLMXHsX8Hp-cvUWMild
- [ ] SB3 tutorial https://github.com/araffin/rl-tutorial-jnrr19/tree/sb3
- [ ] Make a gif of the horns rev power plots https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
- [ ] Find out why the yaw optimization isnt symmetric... I think it is from the secondary effects
- [ ] Project contract<br>Din specialekontrakt skal afleveres senest den 14. juni 2022. Du skal påbegynde dit speciale senest den 29. august 2022.
- [ ] Check more of floris. Why does gauss give so much more power then jensen..<br><br>Higher a gives bigger wake??
- [ ] https://careers.vestas.com/search/?q=loads%20and%20control&q2=&alertId=&locationsearch=&title=&location=aarhus%20N&department=&shifttype=&date=&fbclid=IwAR3hDZbUFlOVbjYTBB-Yf9kZ2jc31RDX-iWFWpHbdCjQRoNIzwDEFy2CuOI
- [ ] Add timeplan for project in overleaf
- [ ] Look at ulriks final problem statement, and brainstom my own
- [ ] Write the stuff for HornsRev in overleaf
- [ ] Find out what that new model in 3.0 was, and how to use it.<br>Do this by writing on hithub
- [ ] Read: analytical-solution-for-the-cumulative-wake-of-wind-turbines-in-wind-farms, this "a new cumulative model for wake superposistion"
- [ ] Translate the dynamic floris to python.. <br>Maybe use this? <br>https://github.com/ebranlard/matlab2python
- [ ] Read:  Addressing deep array effects and impacts to wake steering with the cumulative-curl wake model, this is "The new cumulative curl model"
- [ ] Try and get this paper https://www.osti.gov/pages/biblio/1781613<br>This content will become publicly available on April 20, 2022
- [ ] Check the axial induction optimzation and try out different solvers to see if they give different results
- [ ] Look into what the full_flow_sequential_solver does!<br>I think it is used for plotting!
- [ ] Ask Dario wtf is going on here, and how to do the example?<br>https://github.com/NREL/floris/pull/322
- [ ] Python OOP course. Video 17-25<br>https://www.youtube.com/watch?v=GZeGkjE38bI&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_&index=17<br>Est: 2 hours
- [ ] No axial induction control?<br>https://github.com/NREL/floris/issues/314
- [ ] Support for multiple turbine types, maybe look into it: <br>https://github.com/NREL/floris/pull/325
- [ ] Power_scaler is weird, when saving to yaml...<br><br>This idea is scrapped
- [ ] Spend 4 hours doing overleaf
- [ ] Implement axial Induction in Floris https://github.com/search?p=2&q=axial+induction+floris&type=Code <br>Est 2 Days<br>This is probably a work in progress, but atm it's done.<br>Look at [[Adding axial induction to floris]]
- [ ] Look into the new super posisiton model for Floris <br>Est 1 hr<br>Im pretty sure that it is only avaliable in the cc model


## Scrapped

- [ ] Reward functions:<br><br>1) Percentage increase<br>2) Mere power end sidst, indenfor et interval
- [ ] konkretiser evaluering af agent performance efter træning
- [ ] Hvis intet virker, så undersøg imitation learning
- [ ] Undersøg parameter noise<br>https://openai.com/blog/better-exploration-with-parameter-noise<br>https://github.com/openai/baselines/tree/master/baselines/ddpg<br>https://github.com/openai/baselines/blob/master/baselines/ddpg/ddpg.py<br>https://github.com/openai/baselines/blob/master/baselines/ddpg/ddpg_learner.py<br>https://github.com/openai/baselines/blob/master/baselines/ddpg/noise.py
- [ ] Number of cluster cores - Waiting on christoffer
- [ ] Read about how to make stable baselines only save best agents
- [ ] Save and load model parameters<br>https://stable-baselines3.readthedocs.io/en/master/guide/examples.html#id3
- [ ] Create multi environment.<br>Look into already made environments for help<br>#maybe




%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%