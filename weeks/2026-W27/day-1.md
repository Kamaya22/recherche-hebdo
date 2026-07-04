# CRISPR and genome editing therapies — Day 1/7: From bacterial immunity to programmable scalpel

## Context

Every technology that transforms medicine arrives with a backstory rooted in basic science far removed from any clinic. The double helix was solved by crystallographers and biochemists who had no particular interest in therapeutics. Recombinant insulin emerged from research on restriction enzymes discovered in bacteria. CRISPR-Cas9 is the latest and perhaps most dramatic instance of this pattern: a system that bacteria evolved over hundreds of millions of years to defend against viral attack has been repurposed, in less than fifteen years, into a programmable molecular scalpel capable of cutting — and now precisely rewriting — DNA at any chosen address in the human genome.

This week follows that story from its bacterial origins to its clinical reality. Today we begin with the panorama: what CRISPR-Cas9 is, how it was discovered step by step, and why it represents a categorical improvement over the gene-editing tools that preceded it — zinc finger nucleases (ZFNs) and transcription activator-like effector nucleases (TALENs). Understanding the "why it won" question matters for appreciating both the power and the remaining limitations of the technology. Subsequent days will drill into the molecular mechanism (Day 2), the clinical landscape of approved therapies (Day 3), next-generation precision tools (Day 4), off-target safety (Day 5), governance and ethics (Day 6), and synthesis (Day 7).

## Today's readings (~22 min total)

**1. CRISPR Provides Acquired Resistance Against Viruses in Prokaryotes** — Barrangou, Fremaux, Deveau et al. (*Science*, 2007)
<https://www.science.org/doi/10.1126/science.1138140>
*Estimated reading time: 8 min — abstract, introduction, and discussion*

Published in *Science* on 23 March 2007, this paper settled a question that had puzzled microbiologists since the 1980s: what are those strange, regularly-spaced repeat sequences in bacterial genomes for? The answer Barrangou, Fremaux, Deveau, and colleagues provided — experimentally, in *Streptococcus thermophilus* — was that CRISPR (Clustered Regularly Interspaced Short Palindromic Repeats) together with associated *cas* genes forms an adaptive immune system. When bacteria survive a phage infection, they can snip out a fragment of the phage's DNA and insert it into the CRISPR array as a "spacer," creating a molecular memory. If that same phage attacks again, the spacer sequences guide the Cas machinery to recognise and destroy the invading DNA. This paper is the critical experimental proof that CRISPR is, in its native biological context, an immune mechanism — not a mere genomic curiosity. Without it, the conceptual leap to repurposing the system as a gene-editing tool would have lacked its scientific foundation. *Science* is one of the two most cited multidisciplinary journals in the world; the paper has been cited over 7,000 times.

**2. A Programmable Dual-RNA-Guided DNA Endonuclease in Adaptive Bacterial Immunity** — Jinek, Chylinski, Fonfara, Hauer, Doudna, and Charpentier (*Science*, 2012)
<https://www.science.org/doi/10.1126/science.1225829>
*Estimated reading time: 10 min — abstract, introductory paragraphs, and the "Single Guide RNA" and "Discussion" sections*

This is the paper. Published in *Science* on 17 August 2012 (epub 28 June), it is the direct ancestor of every CRISPR therapy now in clinical use. Jennifer Doudna (UC Berkeley) and Emmanuelle Charpentier (Umeå University) and their co-authors demonstrated three things in rapid succession: first, that Cas9 is a double-stranded DNA endonuclease guided to its target by a two-component RNA system (crRNA + tracrRNA); second, that this two-piece RNA can be fused into a single chimeric "guide RNA" (sgRNA) without loss of function; and third — the pivotal insight — that the sgRNA can be freely re-engineered to direct Cas9 to cut any DNA sequence of your choosing, provided it is adjacent to a short sequence motif called the PAM. The implication was immediate: instead of designing an entirely new protein for every new target (as ZFNs and TALENs required), CRISPR-Cas9 reduced the programming of a genome editor to designing a ~20-nucleotide RNA sequence. The pair were awarded the 2020 Nobel Prize in Chemistry for this work. For a reader engaging with this paper for the first time, focus on how the authors move from describing the natural system to demonstrating programmable cleavage — that conceptual movement is the scientific core of the CRISPR revolution.

**3. The Nobel Prize in Chemistry 2020 — Popular Information** — Nobel Committee for Chemistry, Royal Swedish Academy of Sciences (2020)
<https://www.nobelprize.org/prizes/chemistry/2020/popular-information/>
*Estimated reading time: 8–10 min*

The Royal Swedish Academy of Sciences publishes popular-science descriptions of each Nobel Prize that are edited for a scientifically literate but non-specialist audience. The 2020 Chemistry prize description covers the path from CRISPR's discovery as a bacterial immune element through Doudna and Charpentier's reconstitution of its programmable editing function in a test tube, and ends with its early clinical applications and the ethical questions it raises. It is particularly useful for placing the 2012 Science paper in a broader historical context: Mojica's identification of repeat sequences in archaea in the 1990s, Pourcel and Bolotin's analysis of CRISPR spacers in 2005, Barrangou's 2007 immune function experiment, and the race to show editing in human cells in 2013. It also provides a clear, accessible account of why CRISPR eclipsed ZFNs and TALENs — not because those tools didn't work, but because CRISPR was faster, cheaper, and far easier to multiplex. The Nobel Committee's popular information documents are reviewed by the prize committee and are among the most reliable science communications available.

## Guided summary (~8 min)

**CRISPR in nature: a molecular scrapbook of past enemies**

All organisms face pathogens, and bacteria face them relentlessly. Bacteriophages (viruses that infect bacteria) may be the most abundant biological entities on Earth, and they can devastate bacterial populations. Bacteria have evolved multiple defensive strategies, but CRISPR-Cas represents something unusual: an *adaptive* system. When a bacterium survives a phage infection, a dedicated complex of proteins snips a fragment of the phage's DNA — a "protospacer" — and inserts it into the CRISPR array between the genomic repeats. That spacer acts as a molecular mugshot. The next time that phage appears, the bacterium transcribes the CRISPR array, generating a pre-crRNA that is processed into short crRNA fragments each carrying one spacer sequence. These crRNAs bind to Cas proteins and guide them to matching sequences in any invading DNA, which is then cut and destroyed. Barrangou et al.'s 2007 experiment demonstrated this mechanism directly by challenging *S. thermophilus* with known phages and showing that surviving bacteria had acquired spacers matching the attacking phage's genome — and that those spacers conferred specific resistance to subsequent attack by the same phage.

**The Cas9 protein and the two-RNA system**

Among the ~40 or more families of CRISPR-associated proteins identified, Cas9 is the workhorse of most therapeutic applications because it couples target recognition and DNA cleavage in a single polypeptide. Cas9 is guided by two RNA molecules: the CRISPR RNA (crRNA), which encodes the ~20-nucleotide sequence complementary to the target DNA, and the trans-activating CRISPR RNA (tracrRNA), which folds into a secondary structure that the Cas9 protein recognises and binds. Charpentier's lab had independently identified the tracrRNA as an essential component of the natural system. The 2012 Jinek et al. paper showed that these two RNAs could be fused end-to-end into a single-guide RNA (sgRNA) that retains full functionality — a simplification that transformed the system from a biological curiosity into an accessible tool. Cas9 in complex with an sgRNA will then scan DNA until it finds a "protospacer adjacent motif" (PAM) — for the most widely used SpCas9 from *S. pyogenes*, this is the simple three-nucleotide sequence NGG — and if the adjacent 20 bases match the guide sequence, Cas9 will unwind the double helix, form an R-loop between the guide RNA and the target strand, and cut both DNA strands through its two catalytic domains (HNH and RuvC). The cut leaves a blunt-ended double-strand break (DSB) that the cell's own repair machinery must mend — the nature of that repair determines the editing outcome.

**Why CRISPR won: the comparison with ZFNs and TALENs**

Genome editing is not new to 2012. Zinc finger nucleases were developed in the 1990s and demonstrated efficient, targeted cutting in human cells by 2005. TALENs, developed around 2010, improved on ZFNs in several respects and reached clinical trials. Both systems work by the same principle: fuse a programmable DNA-recognition domain to a non-specific nuclease (the FokI domain) that cuts DNA when two copies dimerize at the target site. The recognition domain is what distinguishes the tools and determines their practical limitations. In ZFNs, each "zinc finger" protein domain recognises a three-base sequence; to target a 18-base site you need six domains, and their design requires significant protein engineering expertise. In TALENs, each TALE repeat recognises a single base pair, offering simpler engineering — but TALEN pairs must be custom-designed and synthesised for every new target, a process taking weeks and requiring specialist molecular biology skills.

CRISPR-Cas9 changed this arithmetic dramatically. Programming a new target requires designing a 20-nucleotide RNA sequence — a task that takes hours, not weeks, can be done computationally, and costs a few hundred dollars rather than thousands. Multiple targets can be edited simultaneously by introducing multiple sgRNAs. The efficiency of editing in human cells proved equal to or better than ZFNs or TALENs in head-to-head comparisons. The simplicity of the system democratised genome editing: within two years of the 2012 paper, the technique had spread to thousands of laboratories worldwide that had previously lacked the protein engineering expertise to use ZFNs or TALENs.

CRISPR-Cas9 does retain two important limitations relative to ZFNs and TALENs. First, the NGG PAM requirement restricts which sequences can be targeted (roughly one site per ~8 base pairs in the human genome, which is ample for most purposes but not universal). Second, Cas9's mode of action — creating a DSB — introduces the possibility of unwanted DNA damage at off-target locations, an issue that became central to the safety assessment of clinical applications and that Days 4 and 5 of this series will address in detail.

**From E. coli to the cancer ward in eleven years**

The speed of translation from the 2012 Science paper to the first regulatory approvals in 2023 is itself noteworthy. Biologics typically take 15–20 years from discovery to approval; CRISPR-based therapies took 11. Several factors contributed. The underlying therapeutic logic was unusually clear and mechanistically tractable (switching on fetal hemoglobin by disabling BCL11A, as Day 3 of this series describes). The regulatory pathway leveraged the Breakthrough Therapy designation system. And the clinical-grade editing efficiency achievable in human hematopoietic stem cells proved higher than the field had expected at the outset. That said, the approved therapies are not "simple CRISPR" — they incorporate years of optimisation in delivery, editing conditions, and cell processing. The story is one of rapid but iterative progress, not a single eureka moment followed by immediate clinical application.

## Questions to think about

1. CRISPR was discovered through basic curiosity-driven research in bacterial biology with no apparent clinical application — the Barrangou 2007 paper was about understanding cheese-industry starter cultures, not medicine. What does this suggest about how research funding and priority-setting should balance "use-inspired" and "curiosity-driven" science?

2. CRISPR replaced ZFNs and TALENs not because they were fundamentally inferior — ZFN and TALEN-based therapies still work and some are in clinical trials — but because CRISPR was radically easier to design and use. How should we think about the relationship between a technology's "ease of use" and its "safety of use" in biology? Is democratising powerful tools always a net positive?

3. The 2012 Jinek et al. paper demonstrated CRISPR-Cas9 editing in a test tube; several other groups demonstrated editing in human cells in January 2013. In the months between, multiple academic and commercial groups were racing to establish priority. What aspects of that competition — and the subsequent patent dispute between the Broad Institute and the University of California — reveal about how academic incentive structures shape the development of public-good technologies?

---

## This week's theme

**Theme: CRISPR and genome editing therapies** (ISO Week 2026-W27)

CRISPR-Cas9 has transformed molecular biology from a research curiosity into a clinical reality in under a decade. The 2020 Nobel Prize in Chemistry recognized Jennifer Doudna and Emmanuelle Charpentier for a discovery that now underpins dozens of active clinical trials and, as of 2023–2024, the first approved gene-editing medicines for sickle-cell disease and beta-thalassemia. Understanding how CRISPR works — and where it still struggles — is essential for anyone following modern medicine, biotechnology policy, or bioethics. Beyond treating disease, the same tools raise profound questions about germline editing, equitable access, and the long-term governance of human biology.

The week's seven days cover: Day 1 (today) — the discovery arc and comparison with earlier tools; Day 2 — the Cas9 molecular mechanism and DNA repair pathways; Day 3 — the first approved therapies and the clinical pipeline; Day 4 — next-generation tools (base editing, prime editing); Day 5 — off-target effects and safety; Day 6 — ethics, governance, and germline editing; Day 7 — synthesis and open questions.

**Upcoming themes in the backlog** (you can reorder or validate these by editing `themes/backlog.md` on GitHub):

- [proposé] Urban heat islands and climate adaptation of cities — physics, health impacts, and design solutions
- [proposé] The behavioral economics of poverty — how scarcity shapes decision-making
- [proposé] The neuroscience of pain — why pain is a construction of the brain and what this means for treatment
- [proposé] Quantum computing for the non-physicist — what qubits actually are, where the technology stands, and realistic near-term applications
- [proposé] Antibiotic resistance — mechanisms, global surveillance, and the pipeline crisis
- [proposé] The deep ocean — what we know about Earth's least-explored biome and why it matters for climate and biodiversity
