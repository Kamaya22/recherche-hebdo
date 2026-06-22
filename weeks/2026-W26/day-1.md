# Misinformation Dynamics — Day 1/7: Panorama — The Architecture of False Belief

## Context

We live in what the World Health Organization called, during the COVID-19 pandemic, an **infodemic** — an overabundance of information, accurate and not, that makes it hard for people to find trustworthy guidance when they need it most. Yet misinformation is neither new nor uniquely digital: rumours, propaganda, and deliberate deception have shaped events from medieval plagues to the World Wars. What has changed is the infrastructure. Social media platforms have turned every user into a broadcaster, collapsing the editorial filters that once slowed the spread of unverified claims. The result is a communications environment that researchers are only beginning to understand at a scientific level.

The academic study of misinformation sits at a remarkable intersection. Psychologists ask why individual minds form and retain false beliefs. Network scientists map how claims cascade through social graphs. Political scientists track the downstream effects on elections and trust in institutions. Computer scientists build detection tools and study how algorithmic recommendation shapes exposure. This week we follow that same arc: starting today with the foundational concepts and landmark empirical results, then diving into mechanisms, consequences, and countermeasures across subsequent days.

A crucial early clarification distinguishes three related but distinct phenomena. **Misinformation** is false or inaccurate information, regardless of intent — the person sharing it may genuinely believe it. **Disinformation** is false information created or spread *with intent to deceive*. **Malinformation** is accurate information weaponised to cause harm — private facts released to damage a target. This typology, developed by Claire Wardle and Hossein Derakhshan in a 2017 Council of Europe framework (often called the *Information Disorder* report), has become the field's standard vocabulary and is why researchers avoid the politically loaded term "fake news," which conflates all three.

## Today's readings (~20 min total)

**1. The Spread of True and False News Online** — Vosoughi, Roy & Aral (*Science*, 2018)
<https://www.science.org/doi/10.1126/science.aap9559>
*Estimated reading time: 10 min (abstract + key figures freely accessible; full text may require institutional access)*

This is the most-cited empirical study in the field, with over 6,000 citations. The team analysed approximately 126,000 rumour cascades on Twitter spanning 2006–2017, each verified by independent fact-checking organisations. The core finding — that falsehoods diffuse farther, faster, deeper, and more broadly than the truth — upended conventional assumptions about what makes content viral. The study is trustworthy because it used a large, systematically collected dataset, multiple independent fact-checking sources, and robust statistical controls; it was published in *Science* after rigorous peer review.

**2. The Psychology of Fake News** — Pennycook & Rand (*Trends in Cognitive Sciences*, 2021)
<https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(21)00051-6>
*Estimated reading time: 8 min (open-access author version also at <https://dspace.mit.edu/handle/1721.1/144268>)*

Gordon Pennycook (Regina / Cornell) and David Rand (MIT) synthesise a decade of experimental research to answer two questions: Why do people *believe* false news, and why do they *share* it? Their counterintuitive answer to both is *inattention*, not political bias. This review in a leading cognitive-science journal is essential background for understanding both the problem and the solution space: if susceptibility is driven by lazy thinking rather than motivated reasoning, then nudging people to slow down and consider accuracy can help.

**3. The Psychological Drivers of Misinformation Belief and Its Resistance to Correction** — Ecker, Lewandowsky, Cook et al. (*Nature Reviews Psychology*, 2022)
<https://www.nature.com/articles/s44159-021-00006-y>
*Estimated reading time: 12 min for the abstract, introduction, and conclusions; the full article repays a slower read later in the week*

This comprehensive review from researchers at the Universities of Western Australia, Bristol, and George Mason maps the cognitive, social, and affective factors that make misinformation sticky. It introduces the concept of the **continued influence effect** — the finding that even after people are told a claim is false, the original misinformation continues to subtly shape their reasoning and judgements. The authors also survey the evidence on both prebunking (proactive inoculation) and debunking (reactive correction) strategies. Published in *Nature Reviews Psychology*, a high-impact review journal, with authors who are leading figures in the field.

## Guided summary (~8 min)

**Defining the terrain**

The Wardle–Derakhshan typology clarifies that the problem is not a single phenomenon but a spectrum. At one end, someone shares a health claim they read online, believing it sincerely: that is misinformation — false, but not deliberately so. At the other end, a state actor manufactures fabricated documents to discredit a political opponent: that is disinformation. In between lies a wide range of actors and motivations — financial (clickbait farms), ideological (partisan content mills), and personal (social signalling). Understanding which type of information disorder you are dealing with matters for designing responses: correcting a sincere error requires different tools from disrupting an intentional disinformation campaign.

**The empirical landmark: falsehood travels faster**

The Vosoughi et al. (2018) study established several headline numbers that every subsequent researcher cites. False news was **70% more likely to be retweeted** than true news. It reached a cascade depth of 10 — meaning it had passed through 10 levels of sharing — roughly **20 times faster** than true stories. It diffused to an audience of 1,500 people about **six times faster**. The top 1% of false-news cascades reached between 1,000 and 100,000 people; true stories rarely exceeded 1,000 people even at their most viral. Critically, when the researchers statistically controlled for the activity of automated bot accounts, the human-driven difference remained — meaning it is *people*, motivated by something, who are primarily responsible for amplifying falsehoods.

What drives this asymmetry? The researchers found that false news items were more *novel* than true ones (they conveyed information people had not seen before), and that replies to false news expressed higher levels of fear, disgust, and surprise, while replies to true news expressed anticipation, sadness, joy, and trust. Novelty and negative emotions, the study suggests, are the jet fuel of misinformation spread.

**The psychology: lazy, not biased**

A common intuition holds that people believe and share false information because it fits their political tribe — that motivated reasoning and partisan identity are the primary culprits. Pennycook and Rand's synthesis challenges this view. Across dozens of experiments, they found that the strongest predictor of whether someone believed false news was not their political identity but their *degree of analytical thinking*. People who scored higher on tests of reflective cognitive style were better at distinguishing true from false headlines, regardless of whether the content was politically congenial. The effect of partisanship on belief accuracy was real but smaller than popularly assumed.

On the sharing side, they found an even more striking pattern: there is a large gap between what people *believe* and what they *share*. In experiments, most participants who shared a false headline actually *doubted* it — they had simply not paused to consider accuracy before clicking "share." Inattention to accuracy, rather than deliberate deception, accounts for the bulk of everyday misinformation spread. This has an optimistic implication: simply prompting people to think about whether a story is accurate before sharing can meaningfully reduce misinformation propagation.

**The stickiness problem: continued influence**

If spread can be partially addressed by nudging attention, the problem of *belief persistence* is harder. Ecker, Lewandowsky and colleagues document multiple reasons why corrections fail. Cognitively, our memory systems are not designed to reliably tag information as "discredited" — we tend to remember facts and forget their sources, a phenomenon called *source monitoring failure*. A retracted claim can linger in memory as vaguely familiar and thus feel credible (the *illusory truth effect*). Socially, corrections can trigger *reactance* — people defending their prior beliefs when they feel pressured to abandon them. Affectively, information that confirms emotionally held worldviews is processed more easily and remembered better.

The *continued influence effect* names the most troubling consequence: even when people explicitly acknowledge that a claim has been corrected, the original misinformation continues to influence their subsequent reasoning about related events. Experiments have shown this in legal, medical, and political contexts. Corrections are not useless, but they are reliably incomplete — underscoring the value of prevention over cure.

**Mapping the week ahead**

Tomorrow (Day 2) we go deeper into the cognitive mechanisms: why the brain is built in ways that make false beliefs easy to acquire and hard to dislodge. Day 3 zooms out to the network level: how social graphs, platform algorithms, and super-spreader nodes shape which claims go viral. Day 4 examines the documented harms — from vaccine hesitancy to election interference. Day 5 surveys the intervention toolkit with an honest accounting of what works. Day 6 takes up the AI frontier: large language models, synthetic media, and the arms race between generation and detection. Day 7 synthesises the week and identifies the field's biggest open questions.

## Questions to think about

1. The Vosoughi et al. study found that humans, not bots, primarily drove the faster spread of false news. Does this change how you think about where responsibility lies for the misinformation problem — with platforms, with content creators, or with users themselves?

2. If most misinformation sharing is driven by inattention rather than partisan motivation, what does this imply for the political debates around censorship and free speech as solutions to the problem?

3. The continued influence effect suggests that corrections are always incomplete. Is there a threshold of incompleteness that is "good enough" for public-health or policy purposes, and how would we measure it?

---

## This week's theme

This week explores **Misinformation Dynamics — how false information spreads and what actually works against it**.

The week is framed around three concentric questions: *Why do people believe false things?* (cognitive and psychological roots), *How do false things spread?* (network and social dynamics), and *What can we do about it?* (interventions and their real-world limits). The readings are chosen to give you both the foundational empirical picture and enough mechanistic detail to evaluate claims you will encounter about "solutions" to misinformation.

**Upcoming themes in the backlog** (Kamil can reorder or validate these by editing `themes/backlog.md` on GitHub):

- [proposé] CRISPR and genome editing therapies — from molecular mechanism to approved treatments and ethical debates
- [proposé] Urban heat islands and climate adaptation of cities — physics, health impacts, and design solutions
- [proposé] The behavioral economics of poverty — how scarcity shapes decision-making
- [proposé] The neuroscience of pain — why pain is a construction of the brain and what this means for treatment
- [proposé] Quantum computing for the non-physicist — what qubits actually are, where the technology stands, and realistic near-term applications
- [proposé] Antibiotic resistance — mechanisms, global surveillance, and the pipeline crisis
- [proposé] The deep ocean — what we know about Earth's least-explored biome and why it matters for climate and biodiversity
