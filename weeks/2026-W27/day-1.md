# CRISPR and Genome Editing Therapies — Day 1/7: The Panorama

## Context

We are living through an extraordinary moment in the history of medicine. In 2012, biochemists Jennifer Doudna and Emmanuelle Charpentier demonstrated that a bacterial immune system — CRISPR-Cas9 — could be reprogrammed to cut any sequence of DNA in any organism with unprecedented precision. Eight years later, they shared the Nobel Prize in Chemistry. Three years after that, the first CRISPR-based therapy received FDA approval. The speed from Nobel lecture to approved drug is almost without precedent in biomedical history.

This week we will explore CRISPR from multiple angles: today's panorama sets the stage (what it is, where it came from, how it works at a high level); Day 2 goes into the molecular mechanism in depth; Day 3 covers the road from laboratory to clinic; Day 4 surveys the approved therapies and the clinical pipeline; Day 5 examines safety and off-target concerns; Day 6 unpacks the ethical and governance debates; and Day 7 ties everything together.

What makes CRISPR different from all the gene-editing tools that came before it? The answer lies in programmability, simplicity, and cost. Earlier methods — zinc-finger nucleases (ZFNs) and TALENs — required designing new proteins for every new genomic target: expensive, slow, and technically demanding. CRISPR needs only a short RNA molecule, the guide RNA, to be redesigned. This democratized genome editing: labs worldwide can now edit any gene in any organism, and the cost of editing a single gene dropped from tens of thousands of dollars to a few hundred. The ripple effects — across basic research, drug development, agriculture, and diagnostics — are still accelerating.

## Today's readings (~20 min total)

**CRISPR gene editing: Moving closer to home** (Knowable Magazine / Annual Reviews, 2024) — [https://knowablemagazine.org/content/article/living-world/2024/crispr-gene-editing-therapy-systems-eukaryotic-cells](https://knowablemagazine.org/content/article/living-world/2024/crispr-gene-editing-therapy-systems-eukaryotic-cells) — ~12 min — A richly accessible overview of where CRISPR stands as approved therapies arrive and newer editing systems (base editors, prime editors) mature. Knowable Magazine is the research-outreach arm of Annual Reviews and publishes articles written by active researchers, making it an ideal bridge between the peer-reviewed literature and a non-specialist reader. This piece covers the BCL11A mechanism behind the FDA-approved Casgevy, plus an update on CRISPR trials for diabetes, amyloidosis, HIV, and cancer.

**What are genome editing and CRISPR-Cas9?** (NIH MedlinePlus Genetics — U.S. National Library of Medicine) — [https://medlineplus.gov/genetics/understanding/genomicresearch/genomeediting/](https://medlineplus.gov/genetics/understanding/genomicresearch/genomeediting/) — ~5 min — A concise authoritative primer from the NIH explaining the core vocabulary: what genome editing is, how CRISPR-Cas9 works mechanistically, and the critical distinction between somatic editing (affecting only the treated individual) and germline editing (heritable changes). An excellent reference to anchor the week's terminology.

**Revolutionary breakthrough: FDA approves CASGEVY, the first CRISPR/Cas9 gene therapy for sickle cell disease** (PMC / NCBI, 2024) — [https://pmc.ncbi.nlm.nih.gov/articles/PMC11305803/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305803/) — ~8 min — A peer-reviewed commentary published in PubMed Central detailing the mechanism of action, clinical trial results, and historical significance of Casgevy's December 2023 FDA approval. It situates this milestone in the broader arc of CRISPR's clinical trajectory and briefly flags the access and cost challenges ahead.

## Guided summary (~8 min)

**Where CRISPR comes from**

CRISPR — Clustered Regularly Interspaced Short Palindromic Repeats — is not a human invention. It is a bacterial immune system that has existed for billions of years. Bacteria encounter viruses (bacteriophages) constantly, and CRISPR is how many species remember and fight previous infections: snippets of viral DNA are stored between the repetitive sequences in the bacterial genome, then transcribed into RNA molecules that guide Cas proteins to find and destroy matching viral DNA on re-infection. It is, essentially, an adaptive immune memory encoded in DNA.

In 2012, Jennifer Doudna (UC Berkeley) and Emmanuelle Charpentier (then at Umeå University) demonstrated that this bacterial machinery could be simplified into two components — a single guide RNA and the Cas9 protein — and reprogrammed to cut any desired DNA sequence. Their landmark paper in *Science* (Jinek et al., 2012) showed the system could be directed to specific targets in a test tube; within months, multiple groups demonstrated it worked in human cells. The 2020 Nobel Prize in Chemistry recognized these "genetic scissors" that had, by then, already begun reshaping biology and biotechnology.

**How CRISPR-Cas9 works**

The system has two components: (1) a **single guide RNA (sgRNA)** — roughly 100 nucleotides long, whose first ~20 bases are designed to match the target DNA sequence — and (2) the **Cas9 protein**, an endonuclease (DNA-cutting enzyme) that does the cutting. The Cas9-sgRNA complex scans along the DNA, pausing at short sequences called PAMs (Protospacer Adjacent Motifs; for the most widely used Cas9, this is the three-base sequence NGG). When both the PAM and the adjacent sequence match the guide RNA, Cas9 changes shape and cuts both strands of the DNA helix, creating a **double-strand break (DSB)**.

The cell then attempts to repair this break through one of two main pathways. **Non-Homologous End Joining (NHEJ)** is fast but imprecise: the cell stitches the broken ends back together but often introduces small insertions or deletions (indels) that disrupt the gene — useful when the goal is to knock out a gene. **Homology-Directed Repair (HDR)** can use a supplied DNA template to insert a specific correction or replacement sequence — far more precise, but also far less efficient, and largely restricted to dividing cells. Much of the CRISPR engineering effort of the last decade has focused on bending these repair pathways to therapeutic will.

**An expanding toolkit**

The original Cas9-based system has spawned a family of related technologies that address different scenarios:

- **Base editors** (developed by David Liu's lab at the Broad Institute, 2016) use a modified Cas9 that nicks rather than fully cuts the DNA, fused to a chemical enzyme that directly converts one DNA base to another (C→T or A→G) without creating a DSB. This reduces the risk of unintended rearrangements and is highly precise for single-nucleotide mutations. In January 2024, Beam Therapeutics dosed the first patient in a clinical trial of a base editor (BEAM-101) for sickle cell disease.
- **Prime editors** (Liu lab, 2019) use a Cas9 nickase fused to a reverse transcriptase and a specialized "prime editing guide RNA" that carries a DNA template. Prime editing can install any of the 12 possible base-pair changes, plus small insertions or deletions — without DSBs or a separate DNA template. In April 2024, Prime Medicine reported the first-ever prime-editing clinical data, showing restored immune function in a patient with chronic granulomatous disease.
- **CRISPRi and CRISPRa** use a catalytically dead Cas9 (dCas9), which cannot cut, fused to gene-silencing (i) or gene-activating (a) domains. These tools modulate gene expression rather than the DNA sequence itself, useful for diseases where permanent deletion would be too drastic.

**The first approved therapy**

In December 2023, the FDA approved **Casgevy** (exagamglogene autotemcel, or exa-cel) — developed by Vertex Pharmaceuticals and CRISPR Therapeutics — for sickle cell disease (SCD), and again in January 2024 for transfusion-dependent β-thalassemia. Both are autosomal recessive blood disorders caused by mutations in the genes encoding adult hemoglobin.

Casgevy is an **ex vivo** therapy: a patient's own hematopoietic stem cells are collected from the blood, edited in the laboratory, and infused back after conditioning chemotherapy. The edit disrupts **BCL11A**, a transcription factor that normally suppresses fetal hemoglobin (HbF) in adults. Knocking out BCL11A in erythroid cells allows HbF to be re-expressed, compensating for the defective adult hemoglobin that causes the disease. In pivotal clinical trials, 94% of SCD patients were free from severe vaso-occlusive crises for at least one year — a transformative result for patients who previously faced a lifetime of pain crises, organ damage, and transfusions.

**The challenges ahead in brief**

Three interrelated challenges will structure the rest of this week:

1. **Delivery**: getting the editing machinery into the right cells in a living body is the central bottleneck for most diseases. Ex vivo editing works for blood stem cells, but most organs cannot be extracted and replaced. Lipid nanoparticles (LNPs, used for the approved COVID vaccines) and adeno-associated viruses (AAVs) are the leading in vivo delivery vehicles, each with trade-offs in cargo size, tissue targeting, and immune response.

2. **Precision and safety**: off-target edits — Cas9 cutting at unintended sites with partial sequence matches — remain a concern. Newer high-fidelity Cas9 variants, base editors, and prime editors have substantially reduced this risk, but long-term safety monitoring in treated patients is still accumulating.

3. **Ethics and equity**: Casgevy costs approximately $2 million per patient, a price that makes it inaccessible to the vast majority of the global patients who need it. Meanwhile, germline editing — changes that would be inherited by future generations — remains largely prohibited following the 2018 scandal in which researcher He Jiankui edited human embryos, producing the world's first gene-edited babies without adequate oversight or consent. These questions of access, consent, and the boundaries of human intervention in the genome are not peripheral to CRISPR — they are central to it.

## Questions to think about

1. Casgevy costs roughly $2 million per patient and targets diseases like sickle cell disease, which disproportionately affects people of African descent — many of whom live in lower-income countries with no realistic path to this therapy. What does it mean for a "cure" to exist but be inaccessible to most who need it? Does this change how you think about the value of the scientific achievement?

2. The NHEJ repair pathway is fast but imprecise; HDR is precise but inefficient. Base editors and prime editors were developed in part to avoid the limitations of both. As you read about the molecular mechanisms tomorrow, think about what trade-offs each approach accepts — and what types of mutations each can address.

3. CRISPR was discovered in bacteria as an adaptive immune memory encoded in DNA. Can you think of other examples of mechanisms evolved in microbes or other organisms that humans have repurposed into powerful biotechnology tools? (Hint: PCR, restriction enzymes…)

---

## This week's theme

**CRISPR and genome editing therapies — from molecular mechanism to approved treatments and ethical debates**

CRISPR-Cas9 represents the most significant leap in our ability to rewrite the genetic code since the discovery of the double helix. Unlike earlier tools (zinc-finger nucleases, TALENs), CRISPR is cheap, fast, and programmable — making it accessible to labs worldwide and accelerating medicine at a pace that has outpaced ethical and regulatory frameworks. The technology went from Nobel Prize (2020) to FDA-approved therapy (2023) in just three years, a remarkable timeline. Understanding how it works — and where it's headed — touches questions at the heart of medicine, equity, and what it means to be human. Tens of millions of people live with genetic diseases for which CRISPR now offers, for the first time, a realistic prospect of cure.

**Tentative 7-day outline** *(a guide, adjusted each day based on what we find)*:
- Day 1 (today): Panorama — what CRISPR is, where it came from, how it works, and why this is a pivotal moment
- Day 2: Molecular mechanism in depth — Cas protein variants, guide RNA design, PAM requirements, DNA repair pathways, base and prime editing
- Day 3: From bench to bedside — ex vivo vs. in vivo strategies, delivery systems (AAVs, lipid nanoparticles), clinical trial design for gene therapies
- Day 4: The clinical pipeline — Casgevy and beyond: TTR amyloidosis, CAR-T oncology programs, in vivo liver-targeting therapies, phase III trials
- Day 5: Off-target effects and safety — detection methods, high-fidelity Cas9 variants, immune responses, and what long-term data is showing
- Day 6: Ethics and governance — He Jiankui and germline editing, WHO frameworks, the access and equity question
- Day 7: Synthesis — what is settled vs. open, 3–5 big open questions, curated resources for going deeper

---

**Upcoming themes** *(backlog as of 2026-W27 — you can reorder or add themes by editing [`themes/backlog.md`](https://github.com/Kamaya22/recherche-hebdo/blob/main/themes/backlog.md) directly on GitHub)*:

- Urban heat islands and climate adaptation of cities — physics, health impacts, and design solutions
- The behavioral economics of poverty — how scarcity shapes decision-making
- The neuroscience of pain — why pain is a construction of the brain and what this means for treatment
- Quantum computing for the non-physicist — what qubits actually are, where the technology stands, and realistic near-term applications
- Antibiotic resistance — mechanisms, global surveillance, and the pipeline crisis
- The deep ocean — what we know about Earth's least-explored biome and why it matters for climate and biodiversity
