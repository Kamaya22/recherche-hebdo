# The science of sleep — Day 2/7: The sleeping brain — circuits, oscillations, and the machinery of NREM and REM

## Context

On Day 1 we surveyed the landscape: the architecture of a typical night (NREM stages N1–N3 cycling with REM roughly every 90 minutes), the two-process model that times sleep (homeostatic adenosine pressure interacting with the circadian clock), and the main theories of what sleep actually accomplishes — restoration, synaptic homeostasis, memory consolidation, and the now-contested glymphatic hypothesis. We ended with the observation that sleep is almost certainly polyfunctional: no single theory captures everything.

Today we go inside the machinery. Rather than asking *why* the brain sleeps, we ask *how*: which neurons and circuits produce the characteristic electrical signatures of sleep — slow waves, sleep spindles, and hippocampal sharp-wave ripples — and how do they cooperate? What circuit in the brainstem orchestrates the transitions into and out of REM sleep? And why does REM produce a brain that looks electrically almost indistinguishable from wakefulness while the body lies paralysed?

Understanding the circuit architecture of sleep is not a detour into dry wiring diagrams. It is the foundation for understanding why different sleep stages serve different functions, why some sleep disorders are circuit-level failures, and why targeting specific oscillations during sleep is becoming a serious therapeutic avenue.

## Today's readings (~20 min total)

**1. Oscillating circuitries in the sleeping brain**
Adamantidis, A.R., Gutierrez Herrera, C. & Gent, T.C. — *Nature Reviews Neuroscience*, 20(12), 746–762 (2019) — [https://doi.org/10.1038/s41583-019-0223-4](https://doi.org/10.1038/s41583-019-0223-4) — estimated reading time: ~12 min (abstract, the main circuit diagrams, and the NREM/REM sections)

The authoritative circuit-level review of the sleeping brain by Adamantidis and colleagues at the University of Bern. It maps the thalamocortical loops that generate slow oscillations and spindles, the hippocampal circuitry underlying sharp-wave ripples, and the brainstem–hypothalamic networks that gate transitions between NREM and REM. The central argument is that understanding the *relationships* between oscillations and the sleep-promoting networks that house them — not just cataloguing the oscillations themselves — is the key unsolved problem. *Nature Reviews Neuroscience* publishes peer-reviewed review articles only and is one of the highest-impact journals in the field.

**2. How coupled slow oscillations, spindles and ripples coordinate neuronal processing and communication during human sleep**
Staresina, B.P., Niediek, J., Borger, V., Surges, R. & Mormann, F. — *Nature Neuroscience*, 26(8), 1429–1437 (2023) — [https://doi.org/10.1038/s41593-023-01381-w](https://doi.org/10.1038/s41593-023-01381-w) — free full text via PubMed Central: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400429/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400429/) — estimated reading time: ~5 min (abstract, key results, and the main schematic figure)

The state-of-the-art human study of the slow oscillation → spindle → ripple cascade. Staresina and colleagues at the University of Oxford and University of Bonn Medical Center used intracranial EEG with simultaneous multi-unit activity recordings from the human hippocampus and surrounding medial temporal lobe — only possible in epilepsy patients with surgically implanted depth electrodes. They showed that slow oscillation up-states gate spindle occurrence, spindles set a precise time window for hippocampal ripples, and this sequential coupling produces stepwise increases in neuronal firing rates and cross-regional coordination, theorised to be the cellular mechanism of sleep-dependent memory consolidation. *Nature Neuroscience* is among the highest-ranked peer-reviewed journals in neuroscience; this paper is available free of charge via PMC.

**3. Cracking the complexity of REM sleep**
Dong, Y. & Liu, D. — *Trends in Neurosciences*, 48(12), 977–993 (2025) — [https://www.cell.com/trends/neurosciences/abstract/S0166-2236(25)00221-8](https://www.cell.com/trends/neurosciences/abstract/S0166-2236(25)00221-8) — estimated reading time: ~5 min (abstract and the brainstem/hypothalamic circuit sections)

A recent synthetic review from the Institute of Neuroscience, Chinese Academy of Sciences, covering the hierarchical circuit architecture that generates REM sleep — from brainstem executive centres (sublaterodorsal nucleus, periaqueductal gray) through hypothalamic modulatory inputs (orexin, MCH) to limbic and cortical influences. The review also synthesises what is known about the functions of REM sleep in memory, emotion, and higher-order cognition. *Trends in Neurosciences* is a Cell Press journal dedicated exclusively to high-quality reviews.

---

## Guided summary (~8 min)

### Slow oscillations: the cortex talking to itself

The most visible hallmark of deep NREM (stage N3) sleep is the **cortical slow oscillation** — a large-amplitude, sub-1 Hz rhythm that generates the "slow waves" in the EEG. At the level of single neurons, each cycle reflects a bistable alternation of membrane potential. During the **UP state** (depolarised, typically 0.5–1 s), cortical networks fire vigorously, almost as during wakefulness. During the **DOWN state** (hyperpolarised, ~0.2–0.5 s), outward potassium currents hold the membrane silent and no action potentials are generated.

Decades of work by Mircea Steriade and Igor Timofeev established that slow oscillations arise primarily within the neocortex: they persist in isolated cortical slabs disconnected from the thalamus, and their fundamental mechanism lies in the balance between intracortical excitatory and inhibitory currents. However, the thalamus is far from passive — it receives the UP state signals from the cortex and amplifies and synchronises them across large cortical territories, ensuring that the slow waves seen on scalp EEG represent coordinated activity across millions of neurons rather than local patches. Recent work with multi-electrode arrays confirms that slow oscillations propagate across the cortex in travelling waves, often initiating frontally and sweeping posteriorly, and that the thalamus plays a critical role in this propagation.

### Sleep spindles: the thalamocortical oscillator

**Sleep spindles** — the waxing-and-waning 12–16 Hz bursts that mark N2 sleep and continue into N3 — are generated by a dedicated circuit in the thalamus involving two interacting populations:

- **Thalamocortical (TC) relay neurons** in the dorsal thalamic nuclei: glutamatergic, projecting to the cortex. During NREM, they shift from tonic spiking (waking mode) into a rhythmic burst-pause firing mode.
- **Thalamic reticular nucleus (TRN) neurons**: a thin shell of GABAergic (inhibitory) neurons wrapping the lateral thalamus. The TRN receives collateral excitatory input from both cortex and relay neurons, and projects *back only* to relay neurons.

The spindle circuit oscillates as follows: a cortical UP state depolarises TRN neurons, which inhibit relay neurons via GABA-B receptors, producing a long-duration hyperpolarisation. This hyperpolarisation de-inactivates T-type calcium channels in relay neurons, which then burst (the "rebound burst"), simultaneously exciting the cortex — producing the positive peak of the spindle wave — and re-exciting TRN neurons. TRN neurons in turn rebound and inhibit relay neurons again. The loop oscillates at 12–16 Hz for roughly 0.5–2 seconds until the hyperpolarisation accumulates enough to shut it down. Because the UP state of the slow oscillation is what triggers each spindle sequence, spindles are predictably nested within the rising phase of slow oscillations — a hierarchical coupling with important functional consequences.

Two subtypes have been identified: **slow spindles** (~11–12 Hz, frontally dominant) arising from frontal thalamocortical loops, and **fast spindles** (~14–16 Hz, centro-parietally dominant) from parietal loops. Fast spindles are more strongly associated with memory consolidation; slow spindles may primarily serve to suppress sensory arousal during sleep.

### Hippocampal sharp-wave ripples: the replay machine

While slow oscillations and spindles unfold in the thalamocortical system, a parallel and complementary drama occurs in the hippocampus. During NREM sleep — especially in the brief DOWN states between slow oscillation cycles, and in the transition toward UP states — the hippocampus generates **sharp-wave ripples (SWRs)**.

A sharp wave is a large excitatory deflection driven by the massive recurrent collateral network of **CA3** pyramidal cells discharging synchronously onto **CA1** pyramidal cells. Riding on top of each sharp wave is a **ripple**: a brief (50–150 ms) oscillation at 80–120 Hz in humans (higher in rodents), generated by the interplay of CA1 pyramidal cell firing and fast-spiking parvalbumin-positive basket cell interneurons. The result is a burst of highly synchronised activity in the hippocampus, visible as a compound event in local field potential recordings.

The critical functional property of SWRs is that the neurons firing within each ripple are not selected randomly: they replay, in compressed time, the sequences of hippocampal neurons that were active during a prior waking experience. Place cells that encoded a maze route fire in the same temporal order during SWRs — sometimes forward, sometimes in reverse — at timescales 10–20 times faster than during waking exploration. This compressed hippocampal replay is thought to broadcast memory content to the neocortex for consolidation. (We will examine the evidence for this mechanism in detail on Day 3.)

### The SO–spindle–ripple cascade: a symphony in three nested movements

The landmark contribution of Staresina et al. (2023) was to demonstrate, using direct recordings from awake human neurons during sleep, that these three oscillatory events are **hierarchically coupled in a fixed sequential order**:

1. A cortical **slow oscillation UP state** activates thalamocortical circuits.
2. This UP state triggers a burst of **sleep spindles** in the thalamic reticular-relay loop.
3. The spindles, at a precise phase of their waxing, open a brief time window in which hippocampal **ripples** preferentially occur.

The coupling is not merely correlational. In the human hippocampus, each successive level of the hierarchy produced a **stepwise increase** in multi-unit neuronal firing rates, in short-latency correlations among local neuronal assemblies, and in cross-regional coordination between hippocampal subfields and the surrounding medial temporal lobe. The authors interpret this as the cellular mechanism by which the sleeping brain organises conditions for **spike-timing-dependent plasticity**: when pre- and post-synaptic neurons fire within milliseconds of each other (as they do when spindle-nested ripples drive synchronised bursts), Hebbian synaptic strengthening is maximally efficient.

Disruption of this cascade has clinical significance. Patients in the early stages of Alzheimer's disease show impaired temporal coupling between sleep spindles and slow oscillations, years before overt cognitive decline — suggesting that the SO–spindle–ripple machinery may be an early and sensitive biomarker of the neural changes that eventually manifest as dementia.

### The brainstem REM flip-flop: governing the switch between sleep states

If slow oscillations, spindles, and ripples define NREM, what switches the brain into REM — and keeps it there? The answer lies in a circuit in the brainstem that functions as a **bistable flip-flop switch**, first articulated in anatomical and functional terms by Saper and colleagues (Lu et al., *Nature*, 2006).

The switch has two mutually inhibitory sides:

- **REM-ON** neurons, concentrated in the **sublaterodorsal nucleus (SLD)** of the dorsolateral pons (homologous to what was called peri-locus coeruleus-α in the cat literature). These neurons — both glutamatergic and GABAergic — are active during REM sleep and send inhibitory projections onto the REM-OFF side.
- **REM-OFF** neurons, concentrated in the **ventrolateral periaqueductal gray (vlPAG)** and **lateral pontine tegmentum (LPT)**. These GABAergic neurons fire during NREM and waking and inhibit the SLD.

Because each side suppresses the other, the system has two stable attractors: either vlPAG/LPT dominates (non-REM/wake state) or SLD dominates (REM state). Small perturbations from modulatory inputs — cumulative REM pressure from the homeostatic system, timed signals from the circadian clock — can tip the balance, triggering rapid transitions into or out of REM.

When the SLD fires (REM state), its glutamatergic projections branch along two critical pathways:

1. **To the basal forebrain**: driving cortical **EEG desynchronisation** and generating the hippocampal **theta rhythm** (4–8 Hz) that characterises REM. This theta oscillation — generated by cholinergic and GABAergic septal projections to the hippocampus — reflects a fundamentally different mode of hippocampal operation than the ripple-based replay of NREM.
2. **To the medulla and spinal cord**: activating glycinergic and GABAergic interneurons that hyperpolarise spinal motor neurons, producing **REM atonia** — the active muscle paralysis that prevents us from physically enacting dream content. Failure of this pathway leads to REM sleep behaviour disorder (RBD), in which people physically act out their dreams; crucially, RBD is now known to be a prodromal marker of alpha-synuclein pathology (Parkinson's disease, Lewy body dementia) in the vast majority of cases.

### Hypothalamic tuning: orexin, MCH, and the stability of sleep states

The brainstem flip-flop is itself modulated from above. Two hypothalamic neuropeptide systems play antagonistic roles:

**Orexin/hypocretin neurons** (in the lateral hypothalamus) fire during waking, project to the vlPAG and LPT (stabilising the REM-OFF side), and also excite multiple wake-promoting monoaminergic populations (locus coeruleus norepinephrine, raphe serotonin, tuberomammillary histamine). In narcolepsy — caused by selective destruction of orexin neurons — the REM flip-flop loses its stabilising bias, and the system flickers inappropriately between states: patients experience sudden muscle atonia while awake (cataplexy), hypnagogic hallucinations, and sleep paralysis — all fragments of REM intrusion into wakefulness.

**MCH (melanin-concentrating hormone) neurons** (also lateral hypothalamus, interleaved with orexin neurons) have the opposite profile: they are maximally active during REM, project to and support the SLD, and facilitate both REM entry and REM maintenance. Optogenetic activation of MCH neurons during sleep increases REM duration; silencing them reduces it.

At the transition into each REM episode, monoaminergic REM-OFF neurons (noradrenergic locus coeruleus, serotonergic raphe) go nearly silent — their activity during waking had been tonically suppressing SLD neurons; their silence now releases the REM-ON circuit. This architecture explains one of the oldest puzzles in sleep pharmacology: antidepressant drugs that block monoamine reuptake (SSRIs, SNRIs, TCAs) all potently suppress REM sleep, because they maintain monoaminergic tone that keeps the REM flip-flop in the off position.

### REM as active processing: theta, PGO waves, and the dreaming cortex

REM sleep may look like waking on the scalp EEG, but the internal organisation is distinct. The dominant hippocampal rhythm is **theta** (4–8 Hz), which reflects continuous, rapid network cycling through place cell sequences — a different mode from the episodic, compressed replay of NREM ripples. Theta-phase-coupled gamma oscillations structure the timing of spike sequences, potentially enabling the integration of recently encoded episodes with long-term semantic knowledge networks.

The **rapid eye movements** themselves — the defining feature of the state — are driven by bursts of excitation called **PGO waves** (ponto-geniculo-occipital waves) originating in the brainstem, propagating through the lateral geniculate nucleus of the thalamus to the primary visual cortex. PGO waves activate the visual cortex in the absence of any external visual input, producing the vivid, quasi-perceptual imagery of dreams. The motor commands that would accompany this visual activation in waking are blocked by the atonia circuit — meaning that the dreaming brain is simultaneously generating a rich simulation of experience and suppressing all output to the motor system.

Together, these circuit observations suggest that NREM and REM are not simply "lighter" and "deeper" variants of the same state but represent **qualitatively different operational modes** of the brain — each with its own oscillatory signature, circuit logic, and likely functional specialisation. What those specialisations are, in terms of memory, emotion, and cognition, is the question we turn to on Day 3.

---

## Questions to think about

1. Sleep spindles are generated by the thalamo-reticular circuit, but their functional relevance — memory consolidation — is expressed in hippocampal ripples hundreds of milliseconds later. What does this imply about how the thalamus can "know" when to generate a spindle in coordination with hippocampal ripples? And what could go wrong in the signalling chain between them?

2. REM atonia is actively generated by inhibition of motor neurons — it is not simply an absence of motor commands but a positive, circuit-driven suppression. What does the existence of REM sleep behaviour disorder (where this suppression fails) tell us about the independence of the components of REM? Could there be a state that has cortical REM oscillations without atonia, or atonia without REM EEG activity?

3. Narcolepsy is caused by loss of orexin neurons — a surprisingly specific cellular loss — producing intrusions of REM components into wakefulness. What does this suggest about the nature of states like wakefulness and sleep: are they truly discrete states, or are they always in competition, held apart by specific neuromodulatory signals? What would it mean if moments of "micro-sleep" in normal people are actually brief releases of the same inhibitory balance?
