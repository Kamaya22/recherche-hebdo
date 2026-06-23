# Misinformation Dynamics — Day 2/7: The Cognitive Machinery of Belief

## Context

Yesterday's panorama established the landscape: false news travels farther and faster than true news, and the culprit is primarily human psychology, not automated bots. We met three foundational concepts — the **continued influence effect**, the **illusory truth effect**, and the **inattention hypothesis** — and saw how Pennycook and Rand's synthesis challenged the intuition that partisan bias is the root cause of misinformation susceptibility.

Today we descend a level, into the actual cognitive mechanisms. Why does the brain, built by evolution to be a remarkably efficient learning machine, turn out to be systematically exploitable by false information? The answer lies in how the mind uses shortcuts — *heuristics* — to evaluate truth. Processing fluency, repetition-based familiarity, and attentional lapses are not bugs in human cognition; they are features that work well in most environments but become liabilities in a media ecosystem engineered to maximize engagement. We also correct one of the most widely cited *misconceptions about misinformation research*: the claim that corrections backfire and make false beliefs stronger. The evidence has moved sharply, and what we now know is more nuanced — and more hopeful.

A word on how today connects to the week's arc: if Day 1 was the aerial view (how bad is the problem, how big are the numbers), Day 2 is the mechanistic view (why does the brain let this happen at all?). Understanding the mechanisms is essential before we can evaluate interventions — a question we will take up in detail on Day 5.

## Today's readings (~20 min total)

**1. The illusory truth effect: A review of how repetition increases belief in misinformation** — Udry & Barber (*Current Opinion in Psychology*, 2024)
<https://www.sciencedirect.com/science/article/abs/pii/S2352250X23001811>
*Estimated reading time: 7 min (abstract, introduction, and "Mechanisms" section; the full article can be read at leisure)*

This concise review in a high-impact psychology journal (Elsevier's *Current Opinion* series publishes invited reviews by active researchers in the field) summarises more than four decades of experiments on the illusory truth effect. The core finding is deceptively simple: **repeated exposure to a claim increases the probability that people judge it to be true**, even when the claim is implausible or contradicts prior knowledge. The authors synthesise the two main proposed mechanisms — cognitive **fluency** (repeated information is processed more easily, and ease of processing is unconsciously interpreted as a signal of truth) and **familiarity** (repeated information feels more familiar, and familiarity is confused with truth). The review also surveys boundary conditions and promising intervention points.

**2. Shifting attention to accuracy can reduce misinformation online** — Pennycook, Epstein, Mosleh et al. (*Nature*, 2021)
<https://www.nature.com/articles/s41586-021-03344-2>
*Estimated reading time: 9 min (abstract + "Results" section; MIT Media Lab has an author copy at <https://www.media.mit.edu/publications/shifting-attention-to-accuracy-can-reduce-misinformation-online/>)*

This is the definitive experimental test of the **inattention hypothesis** introduced in Day 1. The authors combine survey experiments with a real-world field experiment on Twitter to show that simply asking users to rate the accuracy of a single (unrelated) headline — a one-time prompt that takes seconds — measurably improves the quality of news they subsequently share, shifting them away from false content and toward true content. Crucially, this "accuracy nudge" worked across partisan lines. Published in *Nature*, with authors from MIT and the University of Regina, it is the paper most cited in platform policy discussions about low-cost, privacy-preserving interventions.

**3. The elusive backfire effect: Mass attitudes' steadfast factual adherence** — Wood & Porter (*Political Behavior*, 2019)
<https://link.springer.com/article/10.1007/s11109-018-9443-y>
*Estimated reading time: 6 min (abstract + "Discussion" section; a preprint version is available at <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2819073>)*

This paper delivered one of the most important corrections in the misinformation literature. The original "backfire effect" — the idea that correcting a false political belief causes people to *believe it more strongly* — was introduced by Nyhan and Reifler (2010) and became one of the most widely cited results in political psychology. Wood and Porter ran five large-scale experiments (over 10,100 participants, 52 different political issues) and found **no evidence of backfire whatsoever**. Corrections consistently moved beliefs in the direction of the facts, regardless of political identity. The paper is important both for what it says about corrections and for what it illustrates about the sociology of science: a dramatic, counterintuitive finding can take hold in public discourse long before the replication literature catches up.

## Guided summary (~8 min)

**The fluency shortcut and the illusory truth effect**

Human memory is associative and reconstructive rather than photographic. When we encounter a claim, we rarely have the time or knowledge to verify it from first principles. Instead, the brain uses a battery of quick cues to assess plausibility. One of the most powerful is *processing fluency*: the subjective sense of how easily information is understood. Fluent information — information that feels smooth and effortless to process — is experienced as more familiar, more credible, and more true. This is not irrational in the statistical sense: in a world where accurate information generally circulates more widely than false information, fluency is a reasonable proxy for truth. The problem is that fluency can be manufactured.

The illusory truth effect, first documented by Hasher, Goldstein, and Toppino in 1977 and extended by decades of subsequent research, shows that **the mere repetition of a statement increases its perceived truth**, independently of its actual accuracy. When a claim is encountered a second or third time, it is processed more quickly (fluency increases), and the brain unconsciously interprets this ease as evidence that the claim is familiar and therefore credible. Udry and Barber's review confirms that this effect is robust across domains — trivia, fake news headlines, conspiracy claims — and that it persists even when participants are explicitly warned that repeated statements may be false. The effect is somewhat attenuated when participants are instructed to focus on accuracy, but it is never fully eliminated. In a social media environment where false claims can be encountered dozens of times across feeds, retweets, and reposts, the cumulative impact on perceived credibility is substantial.

**Familiarity, source monitoring, and the confusion of knowing with truth**

The illusory truth effect is closely related to a memory phenomenon called *source monitoring failure*. When we retrieve information from memory, we do not always retrieve the *source* along with the content. We remember the claim, but we forget where we heard it — from a trusted expert, from a partisan website, or from a friend who was speculating. Because the claim feels familiar (we have encountered it before), the brain may experience it as something "known," which is then confused with something that has been verified. This is why repeated exposure to a rumour can eventually convert a vague suspicion into a firm belief: the rumour accumulates the subjective texture of established knowledge simply by being recalled repeatedly.

Cognitive load matters here too. When people are distracted, time-pressed, or cognitively depleted — all common states while scrolling — they rely more heavily on fluency and familiarity as truth cues, and less on deliberate evaluation. This creates a vulnerability that is especially acute for social media, where content is designed to be consumed quickly.

**Inattention, not bias: the experimental evidence**

Day 1's theoretical synthesis by Pennycook and Rand established the inattention hypothesis: most people share false news not because they want to spread it but because they are not thinking about accuracy at the moment of sharing. The 2021 *Nature* paper tests this directly. In one survey experiment, participants were shown a mix of true and false news headlines and asked about their sharing intentions. The result replicated a well-known asymmetry: the accuracy of a headline had almost no effect on sharing intentions, even though the same participants — when explicitly asked — were perfectly capable of distinguishing true from false headlines. Sharing is decoupled from accuracy judgement because accuracy is simply not salient at the moment of clicking.

The intervention exploited this gap. Before completing the sharing task, a random subset of participants was shown an unrelated article and asked: "Is this headline accurate?" This single prompt — taking about 15 seconds — made the concept of accuracy temporarily salient. Participants in the nudge condition subsequently shared significantly more true content and significantly less false content. The field experiment, using actual Twitter users, confirmed the result in a real-world environment. The nudge did not suppress sharing overall; it selectively improved its *quality*. The effect held across Republicans and Democrats.

What makes this finding so important for the cognitive story is what it implies about the underlying mechanism. If misinformation spread were primarily about motivated reasoning — people actively seeking out and sharing content that confirms their identity — then a generic accuracy prompt would have no effect (or would even backfire for partisan content). The fact that it works symmetrically across political identities supports the inattention account: the dominant failure mode is cognitive, not motivational.

**The backfire correction: a myth bites the dust**

For much of the 2010s, the "backfire effect" was treated as settled science in popular accounts of misinformation. The idea was both intuitive and alarming: trying to correct someone's false political belief could make them hold it *more* tightly, as the correction was perceived as an attack on their identity and triggered defensive entrenchment. Nyhan and Reifler's 2010 experiments, while relatively small, were widely cited in journalism, political campaigns, and policy circles.

Wood and Porter's large-scale replication found the opposite. Across 52 different political topics — immigration, gun control, tax policy, climate, vaccines — and across participants spanning the full ideological spectrum, **corrections reliably moved beliefs toward the facts**. The magnitude of the correction effect varied by topic and by how strongly the belief was identity-laden, but in no experiment did correction increase false belief. The backfire effect, it turned out, was a fragile laboratory artefact that did not survive methodological scrutiny.

This is not to say that corrections are fully effective. The *continued influence effect* (Day 1) remains robust: even when people update their explicit beliefs, the original misinformation continues to subtly shape their reasoning about related events. The question for Day 5 will be: given that corrections are real but partial, how should we design correction strategies, and what combinations of prebunking and debunking maximise the reduction of misinformation's downstream effects?

**A note on individual differences**

The picture emerging from cognitive research is not that everyone is equally susceptible all the time. Analytical thinking style, numeracy, cognitive flexibility, and prior domain knowledge all moderate susceptibility to the illusory truth effect and the inattention gap. People with higher scores on the Cognitive Reflection Test — a measure of the tendency to override fast, intuitive answers with careful deliberation — are better calibrated even under high repetition. This matters for intervention design: some people need prompting to deploy analytical thinking they already possess, while others would benefit from training in analytical habits. The cognitive framework points toward scalable, structural nudges (like accuracy prompts) for the former group, and longer-term education for the latter.

## Questions to think about

1. The illusory truth effect shows that familiarity is confused with truth. Does this suggest that *repetition of corrections* — repeating the true version of a false claim — might itself have an illusory-truth-like effect that boosts the correction's persuasiveness over time? What would you need to test that hypothesis?

2. The accuracy nudge works by making the concept of accuracy salient before a sharing decision. What are the limits of this approach at scale? Could platforms design entire interfaces around this principle, and would users adapt and habituate to it?

3. Wood and Porter found no backfire effect across 52 political issues, yet many people in public life behave as though corrections are futile or counterproductive. Why might the "backfire effect" narrative have been so sticky — and what does its persistence tell us about the sociology of scientific ideas?
